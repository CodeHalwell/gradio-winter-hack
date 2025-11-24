# Usage Guide

This guide provides detailed instructions on how to use the Gradio Winter Hack Code Editor + AI Assistant application.

## Table of Contents

1. [Getting Started](#getting-started)
2. [Code Editor](#code-editor)
3. [AI Assistant](#ai-assistant)
4. [MCP Server](#mcp-server)
5. [Examples](#examples)

## Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/CodeHalwell/gradio-winter-hack.git
cd gradio-winter-hack

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium

# Configure environment (optional, for AI features)
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

### Running the Application

```bash
python app.py
```

The application will start at `http://localhost:7860`

## Code Editor

The Code Editor tab provides a multi-tab interface for editing HTML, CSS, and JavaScript code with live preview functionality.

### Features

- **Syntax Highlighting**: Automatic syntax highlighting for HTML, CSS, and JavaScript
- **Line Numbers**: Easy reference with line numbers
- **Copy/Download**: Copy code to clipboard or download as files
- **Live Preview**: Generate real-time screenshots of your code

### How to Use

1. Navigate to the **Code Editor** tab
2. Edit your code in the HTML, CSS, and JavaScript editors
3. Click **🔄 Generate Preview** to see a live screenshot of your code
4. The preview shows exactly how your code will render in a browser
5. The status field confirms when the preview is ready

### Default Template

The application comes with a beautiful default template featuring:
- Responsive HTML structure
- Gradient background (purple to blue)
- Interactive button with click counter
- Smooth hover animations

### Tips

- Make sure your HTML includes proper `<head>` and `<body>` tags
- CSS is automatically injected into the HTML for preview
- JavaScript is automatically injected and executed for interactive elements
- The preview viewport is 800x600 pixels

## AI Assistant

The AI Assistant tab provides multimodal AI capabilities powered by Google's Gemini API for intelligent code generation.

### Features

- **Text-based Code Generation**: Describe what you want, get the code
- **Voice Commands**: Use audio input for hands-free coding
- **Image Analysis**: Upload design screenshots for code suggestions
- **Multi-language Output**: Get HTML, CSS, and JavaScript code

### Prerequisites

To use AI features, you need a Gemini API key:

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

### How to Use

#### Text Input

1. Navigate to the **AI Assistant** tab
2. Type your request in the "Text Prompt" field
3. Example prompts:
   - "Create a responsive navigation bar with dropdown menu"
   - "Build a card component with image, title, description, and button"
   - "Make a contact form with validation"
4. Click **✨ Generate Code**
5. The AI will generate HTML, CSS, and JavaScript code
6. Copy the code to the Code Editor tab to preview

#### Audio Input

1. Click the **Record** button or **Upload file**
2. Record or upload your voice command
3. Speak clearly, for example: "Create a hero section with background image"
4. Click **✨ Generate Code**
5. The AI will transcribe your audio and generate code

#### Image Input

1. Click **Drop Image Here** or **Upload file**
2. Upload a screenshot of a design you want to recreate
3. Optionally, add a text prompt to guide the AI
4. Click **✨ Generate Code**
5. The AI will analyze the image and suggest code to recreate it

### Tips

- Be specific in your prompts for better results
- You can combine text, audio, and image inputs
- The AI Response field shows the full explanation
- Generated code appears in separate HTML, CSS, and JavaScript sections

## MCP Server

The MCP (Model Context Protocol) Server tab provides information about the application's API capabilities.

### API Endpoints

When running as an MCP server, the application provides these endpoints:

#### `generate_code(prompt: str)`
Generate HTML/CSS/JavaScript code from a text description.

**Parameters:**
- `prompt`: Natural language description of what to create

**Returns:** Generated HTML, CSS, and JavaScript code

#### `analyze_image(image: bytes, prompt: str)`
Analyze a design image and suggest code to recreate it.

**Parameters:**
- `image`: Image file as bytes
- `prompt`: Optional guidance for code generation

**Returns:** Code suggestions based on image analysis

#### `transcribe_audio(audio: bytes)`
Convert speech to code suggestions.

**Parameters:**
- `audio`: Audio file as bytes (WAV, MP3, OGG, WebM)

**Returns:** Transcribed text and code suggestions

#### `preview_code(html: str, css: str, js: str)`
Generate a preview screenshot of code.

**Parameters:**
- `html`: HTML code
- `css`: CSS code
- `js`: JavaScript code

**Returns:** Screenshot image of rendered code

## Examples

### Example 1: Creating a Landing Page

**Input (Text Prompt):**
```
Create a modern landing page with a hero section, features grid, and call-to-action button
```

**Result:**
The AI will generate:
- HTML with semantic structure
- CSS with modern styling
- JavaScript for any interactive elements

### Example 2: Voice Command

**Input (Audio):**
Say: "Make a pricing table with three tiers: basic, professional, and enterprise"

**Result:**
The AI transcribes your speech and generates a complete pricing table with appropriate styling.

### Example 3: Image-to-Code

**Input:**
1. Upload a screenshot of a card design from Dribbble or Behance
2. Add prompt: "Create a responsive version of this card"

**Result:**
The AI analyzes the design and generates code to recreate it with responsive behavior.

### Example 4: Combining Inputs

**Input:**
1. Text: "Create a dashboard"
2. Image: Upload a dashboard screenshot
3. Audio: "Make it responsive and add dark mode"

**Result:**
The AI combines all inputs to generate a comprehensive dashboard with all requested features.

## Troubleshooting

### Playwright Installation Issues

```bash
# Manually install Playwright browsers
playwright install chromium
```

### Gemini API Errors

- Verify your API key is correct in `.env`
- Check your API quota at [Google AI Studio](https://makersuite.google.com/)
- Ensure you have internet connectivity

### Port Already in Use

Edit `app.py` and change the port:
```python
demo.launch(server_port=7861)  # Use a different port
```

### Preview Not Generating

- Check that Playwright is installed correctly
- Verify your HTML has proper structure
- Check the console for error messages

## Best Practices

1. **Start Simple**: Begin with basic components and build up
2. **Be Specific**: Detailed prompts yield better results
3. **Iterate**: Use the AI to generate base code, then refine in the editor
4. **Test Often**: Generate previews frequently to catch issues early
5. **Combine Tools**: Use AI for scaffolding, editor for fine-tuning

## Support

For issues or questions:
- Create an issue on [GitHub](https://github.com/CodeHalwell/gradio-winter-hack/issues)
- Check the README.md for additional documentation
- Review the MCP Server Info tab for API details

## License

MIT License - See LICENSE file for details
