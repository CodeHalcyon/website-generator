# AI Website Generator 🚀

An intelligent website generator that creates premium, responsive websites using natural language descriptions. Powered by Google's Gemini AI and built with modern web technologies.

## ✨ Features

- **AI-Powered Generation**: Describe your vision and get a complete website
- **Premium Design**: Award-winning aesthetic with editorial layouts
- **Modern Tech Stack**: TailwindCSS + GSAP animations
- **Responsive Design**: Mobile-first approach with dark mode toggle
- **Real Content**: No placeholders - uses actual images and copy
- **Interactive Updates**: Iteratively improve your website with follow-up requests
- **Instant Preview**: Automatically opens generated websites in your browser

## 🛠️ Tech Stack

- **AI Model**: GPT oss (or) Google Gemini 2.5 Flash
- **Framework**: LangChain with Pydantic validation
- **Frontend**: HTML5, TailwindCSS, GSAP
- **Languages**: Python 3.8+

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package installer)
- A modern web browser
- Google AI Studio API key

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/CodeHalcyon/website-generator
cd website-generator
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
# Copy the example file
cp .env.example .env
```

Add your Google AI API key to the `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key_here
```

### 5. Get Your Google AI API Key

1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key to your `.env` file

HuggingFace API Token:

Go to HuggingFace Settings
Sign in or create an account
Click "New token"
Choose "Read" access type
Copy the token to your .env file

### 6. Run the Generator

```bash
python main.py
```

## 📦 Dependencies

Your `requirements.txt` file should contain:

```txt
python-dotenv
pydantic
langchain-core
langchain-google-genai
langchain-huggingface
langchain
grandalf
```

## 🎯 Usage

1. **Start the Generator**: Run `python main.py`
2. **Describe Your Website**: Enter a detailed description of what you want
3. **Wait for Generation**: The AI will create your complete website
4. **View Results**: The website opens automatically in your browser
5. **Iterate**: Make improvements by describing changes you want

### Example Prompts

```
"Create a modern portfolio website for a minimalist photographer specializing in nature photography"

"Build a landing page for a sustainable fashion brand targeting eco-conscious millennials"

"Design a dashboard for a fitness tracking app with dark theme and data visualizations"
```

## 📁 Project Structure

```
ai-website-generator/
├── main.py                 # Main application file
├── .env                   # Environment variables (create this)
├── .env.example          # Environment template
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── index.html           # Generated website (auto-created)
├── styles.css           # Generated styles (auto-created)
├── script.js            # Generated scripts (auto-created)
└── raw_model_output.txt # AI response log (auto-created)
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | Your Google AI Studio API key | ✅ Yes |
| `HUGGINGFACEHUB_API_TOKEN` | Your HUGGINGFACEHUB API TOKEN | ✅ Yes |

### Model Settings

You can modify the AI model parameters in `main.py`:

```python
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",  # Model version
    temperature=0.3            # Creativity level (0-1)
)
```

## 🎨 Generated Website Features

Each generated website includes:

- **Responsive Design**: Works on all devices
- **TailwindCSS Styling**: Modern, utility-first CSS
- **GSAP Animations**: Smooth, performant animations
- **Dark Mode Toggle**: Seamless theme switching
- **Accessibility**: Semantic HTML and ARIA labels
- **Real Content**: Actual images from Unsplash/Pexels
- **Performance Optimized**: Hardware acceleration and lazy loading

## 🐛 Troubleshooting

### Common Issues

**❌ "No module named 'langchain_google_genai'"**
```bash
pip install langchain-google-genai
```

**❌ "GOOGLE_API_KEY not found"**
- Ensure `.env` file exists in root directory
- Check that your API key is correctly formatted
- Verify the key is active in Google AI Studio

**❌ "Could not extract valid JSON"**
- This usually indicates an API issue
- Check your internet connection
- Verify your API key hasn't expired

**❌ Files not generating**
- Check folder permissions
- Ensure you have write access to the directory
- Try running with administrator privileges

### Debug Mode

To see detailed error information, check the `raw_model_output.txt` file that's created after each generation.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request


**Happy Building! 🎉**

*Transform your ideas into stunning websites with the power of AI.*
