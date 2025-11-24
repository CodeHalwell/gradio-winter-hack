# 🎨 Gradio Winter Hack - Code Editor + AI Assistant

A powerful multimodal code editor with AI assistance powered by Gradio 6, Playwright, and Gemini API.

## Features

### 1. **Code Editor App (Gradio)**
- Multi-tab interface for HTML, CSS, and JavaScript editing
- Syntax highlighting and code formatting
- Live preview generation using Playwright
- Real-time screenshot capture of rendered code

### 2. **MCP Server (Gradio)**
- Gradio-based MCP server for AI logic
- Integration with Gemini API for intelligent code generation
- Vision and speech-to-text capabilities
- RESTful API endpoints for programmatic access

### 3. **Multimodal Interface**
- **Text Input**: Natural language prompts for code generation
- **Audio Input**: Voice commands and speech-to-code conversion
- **Image Upload**: Design analysis and code suggestions from screenshots
- **Multiple Output Formats**: Text feedback, audio responses, and code suggestions

## Tech Stack

- **Gradio 6**: UI framework for creating the web interface
- **Playwright**: Browser automation for screenshot capture and rendering
- **Gemini API**: Google's multimodal AI for vision and speech-to-text
- **Python 3.8+**: Core programming language

## Installation

1. Clone the repository:
```bash
git clone https://github.com/CodeHalwell/gradio-winter-hack.git
cd gradio-winter-hack
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install chromium
```

5. Configure environment variables:
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

## Usage

### Running the Application

Start the Gradio application:
```bash
python app.py
```

The application will be available at `http://localhost:7860`

### Using the Code Editor

1. Navigate to the "Code Editor" tab
2. Edit HTML, CSS, and JavaScript in the respective code editors
3. Click "Generate Preview" to see a live screenshot of your code
4. The preview updates with your latest changes

### Using the AI Assistant

1. Navigate to the "AI Assistant" tab
2. Choose your input method:
   - **Text**: Type a natural language description of what you want to create
   - **Audio**: Record or upload a voice command
   - **Image**: Upload a design screenshot for code suggestions
3. Click "Generate Code" to get AI-powered code suggestions
4. Copy the generated code to the Code Editor tab

### MCP Server Integration

The application functions as an MCP server providing:

- `generate_code(prompt: str)` - Generate HTML/CSS/JavaScript from text
- `analyze_image(image: bytes, prompt: str)` - Analyze designs and suggest code
- `transcribe_audio(audio: bytes)` - Convert speech to code
- `preview_code(html: str, css: str, js: str)` - Generate preview screenshots

## Examples

### Example 1: Text-based Code Generation
```
Prompt: "Create a responsive card with a gradient background, image, title, and button"
Result: Complete HTML, CSS, and JavaScript code for a responsive card component
```

### Example 2: Image Analysis
```
Upload: Screenshot of a website design
Result: HTML/CSS code suggestions to recreate the design
```

### Example 3: Voice Commands
```
Audio: "Create a navigation bar with dropdown menus"
Result: Transcribed text and generated navigation bar code
```

## Project Structure

```
gradio-winter-hack/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env.example          # Example environment variables
├── .gitignore            # Git ignore patterns
└── README.md             # This file
```

## Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

To get a Gemini API key:
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Add it to your `.env` file

## Development

### Adding New Features

The application is structured with clear separation of concerns:

- **Code Editor**: Handles code editing and preview generation
- **AI Assistant**: Manages multimodal inputs and AI processing
- **MCP Server**: Provides API endpoints and integration capabilities

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Troubleshooting

### Playwright Installation Issues
```bash
# Install Playwright browsers manually
playwright install chromium
```

### Gemini API Errors
- Ensure your API key is valid and properly set in `.env`
- Check API quota and rate limits
- Verify internet connectivity

### Port Already in Use
```bash
# Change the port in app.py
demo.launch(server_port=7861)  # Use a different port
```

## License

MIT License - feel free to use this project for your own purposes.

## Acknowledgments

- Built for the Gradio Winter Hack MCP Hackathon
- Powered by Gradio, Playwright, and Google Gemini API
- Special thanks to the Gradio and Google AI teams
