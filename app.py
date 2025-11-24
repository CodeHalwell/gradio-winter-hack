"""
Gradio Winter Hack - Multi-tab Code Editor with Multimodal AI Assistant
This application provides:
1. A code editor with HTML, CSS, and JavaScript tabs
2. Live preview using Playwright for screenshots
3. Multimodal AI interface using Gemini API (vision, speech-to-text)
4. MCP server integration for AI logic
"""

import os
import gradio as gr
from playwright.sync_api import sync_playwright
import google.generativeai as genai
from dotenv import load_dotenv
import tempfile
import base64
from PIL import Image
import io

# Load environment variables
load_dotenv()

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Initialize models
vision_model = None
text_model = None

if GEMINI_API_KEY:
    try:
        vision_model = genai.GenerativeModel('gemini-1.5-flash')
        text_model = genai.GenerativeModel('gemini-1.5-flash')
    except Exception as e:
        print(f"Warning: Could not initialize Gemini models: {e}")


# Default code templates
DEFAULT_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Live Preview</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Welcome to the Code Editor!</h1>
    <p>Edit the HTML, CSS, and JavaScript to see live changes.</p>
    <button id="btn">Click me!</button>
    <script src="script.js"></script>
</body>
</html>"""

DEFAULT_CSS = """body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    background: linear-gradient(to right, #667eea 0%, #764ba2 100%);
    color: white;
}

h1 {
    color: #fff;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
}

button {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #fff;
    color: #667eea;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: transform 0.2s;
}

button:hover {
    transform: scale(1.05);
}"""

DEFAULT_JS = """document.addEventListener('DOMContentLoaded', function() {
    const btn = document.getElementById('btn');
    let clickCount = 0;
    
    btn.addEventListener('click', function() {
        clickCount++;
        btn.textContent = `Clicked ${clickCount} times!`;
    });
});"""


def create_preview_html(html_code, css_code, js_code):
    """Combine HTML, CSS, and JS into a single HTML file for preview."""
    # Inject CSS and JS into HTML
    if "<style>" not in html_code and css_code:
        html_code = html_code.replace("</head>", f"<style>{css_code}</style></head>")
    if "<script>" not in html_code and js_code:
        html_code = html_code.replace("</body>", f"<script>{js_code}</script></body>")
    return html_code


def generate_preview(html_code, css_code, js_code):
    """Generate a screenshot preview of the combined HTML, CSS, and JS code."""
    try:
        # Create combined HTML
        full_html = create_preview_html(html_code, css_code, js_code)
        
        # Create temporary HTML file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8') as f:
            f.write(full_html)
            temp_html_path = f.name
        
        # Create screenshot using Playwright
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={'width': 800, 'height': 600})
            page.goto(f'file://{temp_html_path}')
            page.wait_for_timeout(1000)  # Wait for JS to execute
            
            # Take screenshot
            screenshot_bytes = page.screenshot()
            browser.close()
        
        # Clean up temp file
        os.unlink(temp_html_path)
        
        # Convert bytes to PIL Image
        image = Image.open(io.BytesIO(screenshot_bytes))
        
        return image, "Preview generated successfully!"
    
    except Exception as e:
        return None, f"Error generating preview: {str(e)}"


def analyze_image_with_gemini(image, text_prompt):
    """Analyze an uploaded image using Gemini Vision API."""
    if not GEMINI_API_KEY or not vision_model:
        return "Please set GEMINI_API_KEY in .env file to use AI features."
    
    try:
        # Convert PIL Image to bytes if needed
        if isinstance(image, str):
            # If it's a file path
            with open(image, 'rb') as f:
                image_data = f.read()
        else:
            # If it's already a PIL Image
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            image_data = img_byte_arr.getvalue()
        
        # Create prompt
        prompt = text_prompt if text_prompt else "Analyze this image and provide code suggestions for recreating it with HTML, CSS, and JavaScript."
        
        # Generate response
        response = vision_model.generate_content([prompt, {"mime_type": "image/png", "data": image_data}])
        
        return response.text
    
    except Exception as e:
        return f"Error analyzing image: {str(e)}"


def process_audio_input(audio_file):
    """Process audio input and convert to text using Gemini."""
    if not GEMINI_API_KEY or not vision_model:
        return "Please set GEMINI_API_KEY in .env file to use AI features."
    
    try:
        if audio_file is None:
            return "No audio file provided."
        
        # Read audio file
        with open(audio_file, 'rb') as f:
            audio_data = f.read()
        
        # Use Gemini to transcribe and understand audio
        prompt = "Transcribe this audio and if it contains code-related requests, provide HTML/CSS/JavaScript code suggestions."
        response = vision_model.generate_content([
            prompt,
            {"mime_type": "audio/wav", "data": audio_data}
        ])
        
        return response.text
    
    except Exception as e:
        return f"Error processing audio: {str(e)}"


def generate_code_from_text(text_prompt):
    """Generate code suggestions from text prompt using Gemini."""
    if not GEMINI_API_KEY or not text_model:
        return "", "", "", "Please set GEMINI_API_KEY in .env file to use AI features."
    
    try:
        prompt = f"""Based on this request: "{text_prompt}"
        
Generate HTML, CSS, and JavaScript code. Format your response as:

HTML:
```html
[HTML code here]
```

CSS:
```css
[CSS code here]
```

JavaScript:
```javascript
[JavaScript code here]
```
"""
        
        response = text_model.generate_content(prompt)
        response_text = response.text
        
        # Parse the response to extract HTML, CSS, and JS
        html_code = ""
        css_code = ""
        js_code = ""
        
        # Extract HTML
        if "```html" in response_text:
            html_start = response_text.find("```html") + 7
            html_end = response_text.find("```", html_start)
            html_code = response_text[html_start:html_end].strip()
        
        # Extract CSS
        if "```css" in response_text:
            css_start = response_text.find("```css") + 6
            css_end = response_text.find("```", css_start)
            css_code = response_text[css_start:css_end].strip()
        
        # Extract JavaScript
        if "```javascript" in response_text or "```js" in response_text:
            js_marker = "```javascript" if "```javascript" in response_text else "```js"
            js_start = response_text.find(js_marker) + len(js_marker)
            js_end = response_text.find("```", js_start)
            js_code = response_text[js_start:js_end].strip()
        
        return html_code, css_code, js_code, response_text
    
    except Exception as e:
        return "", "", "", f"Error generating code: {str(e)}"


def multimodal_assistant(text_input, audio_input, image_input):
    """Process multimodal inputs and provide comprehensive feedback."""
    responses = []
    html_suggestions = ""
    css_suggestions = ""
    js_suggestions = ""
    
    # Process text input
    if text_input and text_input.strip():
        html, css, js, text_response = generate_code_from_text(text_input)
        responses.append(f"**Text Input Response:**\n{text_response}")
        if html:
            html_suggestions = html
        if css:
            css_suggestions = css
        if js:
            js_suggestions = js
    
    # Process audio input
    if audio_input:
        audio_response = process_audio_input(audio_input)
        responses.append(f"**Audio Input Response:**\n{audio_response}")
    
    # Process image input
    if image_input is not None:
        image_response = analyze_image_with_gemini(image_input, "Analyze this image and suggest HTML/CSS/JavaScript code to recreate or represent it.")
        responses.append(f"**Image Analysis Response:**\n{image_response}")
    
    if not responses:
        responses.append("Please provide at least one input (text, audio, or image).")
    
    combined_response = "\n\n".join(responses)
    
    return combined_response, html_suggestions, css_suggestions, js_suggestions


# Create Gradio Interface
with gr.Blocks(title="Gradio Winter Hack - Code Editor + AI Assistant") as demo:
    gr.Markdown(
        """
        # 🎨 Gradio Winter Hack - Code Editor + AI Assistant
        
        A powerful multimodal code editor with AI assistance powered by Gemini API.
        
        ### Features:
        - 📝 Multi-tab code editor (HTML, CSS, JavaScript)
        - 👁️ Live preview with Playwright
        - 🎤 Audio input for voice commands
        - 🖼️ Image analysis for design inspiration
        - 💬 Text-based code generation
        - 🤖 AI-powered code suggestions
        """
    )
    
    with gr.Tabs():
        # Tab 1: Code Editor
        with gr.Tab("📝 Code Editor"):
            gr.Markdown("### Edit your HTML, CSS, and JavaScript code below:")
            
            with gr.Row():
                with gr.Column(scale=1):
                    html_input = gr.Code(
                        value=DEFAULT_HTML,
                        language="html",
                        label="HTML",
                        lines=15
                    )
                    css_input = gr.Code(
                        value=DEFAULT_CSS,
                        language="css",
                        label="CSS",
                        lines=15
                    )
                    js_input = gr.Code(
                        value=DEFAULT_JS,
                        language="javascript",
                        label="JavaScript",
                        lines=15
                    )
                    
                    preview_btn = gr.Button("🔄 Generate Preview", variant="primary")
                
                with gr.Column(scale=1):
                    preview_output = gr.Image(label="Live Preview", type="pil")
                    preview_status = gr.Textbox(label="Status", interactive=False)
            
            preview_btn.click(
                fn=generate_preview,
                inputs=[html_input, css_input, js_input],
                outputs=[preview_output, preview_status]
            )
        
        # Tab 2: Multimodal AI Assistant
        with gr.Tab("🤖 AI Assistant"):
            gr.Markdown(
                """
                ### Multimodal AI Assistant
                
                Use text, audio, or images to get code suggestions powered by Gemini AI.
                
                **Note:** Requires GEMINI_API_KEY in .env file
                """
            )
            
            with gr.Row():
                with gr.Column():
                    text_prompt = gr.Textbox(
                        label="Text Prompt",
                        placeholder="E.g., 'Create a responsive navigation bar with dropdown menu'",
                        lines=3
                    )
                    audio_prompt = gr.Audio(
                        label="Audio Input (Voice Command)",
                        sources=["microphone", "upload"],
                        type="filepath"
                    )
                    image_prompt = gr.Image(
                        label="Image Input (Design Reference)",
                        type="pil"
                    )
                    
                    submit_btn = gr.Button("✨ Generate Code", variant="primary")
                
                with gr.Column():
                    ai_response = gr.Textbox(
                        label="AI Response",
                        lines=10,
                        interactive=False
                    )
                    
                    gr.Markdown("### Generated Code:")
                    html_output = gr.Code(label="HTML", language="html", lines=5)
                    css_output = gr.Code(label="CSS", language="css", lines=5)
                    js_output = gr.Code(label="JavaScript", language="javascript", lines=5)
            
            submit_btn.click(
                fn=multimodal_assistant,
                inputs=[text_prompt, audio_prompt, image_prompt],
                outputs=[ai_response, html_output, css_output, js_output]
            )
        
        # Tab 3: MCP Server Info
        with gr.Tab("ℹ️ MCP Server Info"):
            gr.Markdown(
                """
                ### MCP Server Integration
                
                This application serves as a Gradio-based MCP (Model Context Protocol) server that provides:
                
                1. **Code Generation Service**: Transform natural language into HTML/CSS/JavaScript
                2. **Vision Analysis**: Analyze designs and generate corresponding code
                3. **Speech-to-Code**: Convert voice commands into code
                4. **Live Preview**: Real-time rendering using Playwright
                
                #### API Endpoints (when running as MCP server):
                
                - `generate_code(prompt: str)` - Generate code from text
                - `analyze_image(image: bytes, prompt: str)` - Analyze image and suggest code
                - `transcribe_audio(audio: bytes)` - Convert speech to code suggestions
                - `preview_code(html: str, css: str, js: str)` - Generate preview screenshot
                
                #### Configuration:
                
                Create a `.env` file with your Gemini API key:
                ```
                GEMINI_API_KEY=your_api_key_here
                ```
                
                #### Technologies:
                - **Gradio 6**: UI Framework
                - **Playwright**: Screenshot capture and rendering
                - **Gemini API**: Vision and speech-to-text capabilities
                """
            )
            
            if GEMINI_API_KEY:
                gr.Markdown("✅ **Status:** Gemini API configured")
            else:
                gr.Markdown("⚠️ **Status:** Gemini API key not configured. Set GEMINI_API_KEY in .env file.")


if __name__ == "__main__":
    demo.launch(share=False, server_name="0.0.0.0", server_port=7860)
