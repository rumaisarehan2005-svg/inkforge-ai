# ✍️ InkForge AI

> **Turn ideas into polished articles.**

InkForge AI is a simple AI-powered article generator built while learning **LangChain** and exploring how LLMs can be integrated into real-world web applications.

Enter a topic, and InkForge AI generates a structured, readable article without refreshing the page.

## ✨ Features

* 🤖 AI-powered article generation
* 🔗 LangChain prompt workflow
* 🐍 Flask backend
* ⚡ Asynchronous generation using Vanilla JavaScript
* 📋 Copy generated articles with one click
* 🎨 Modern glassmorphism UI
* 📱 Responsive design
* 🔐 API keys stored securely using environment variables
* 🧩 Simple and beginner-friendly architecture

## 🛠️ Tech Stack

| Technology                        | Purpose                         |
| --------------------------------- | ------------------------------- |
| 🐍 Python                         | Backend programming             |
| 🌶️ Flask                         | Web framework                   |
| 🔗 LangChain                      | LLM & prompt orchestration      |
| 🤖 Gemini / OpenAI-compatible API | Article generation              |
| 🔐 python-dotenv                  | Environment variable management |
| 🌐 HTML5                          | Page structure                  |
| 🎨 CSS3                           | UI & styling                    |
| ⚡ Vanilla JavaScript              | Frontend interactions           |

## 🔄 How It Works

```text
💡 User enters a topic
        ↓
⚡ JavaScript sends request
        ↓
🌶️ Flask /generate route
        ↓
🔗 LangChain prompt workflow
        ↓
🤖 AI Model
        ↓
📝 Generated article
        ↓
✨ Article displayed in browser
```

## 📁 Project Structure

```text
inkforge-ai/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

> 🔐 The `.env` file is intentionally excluded from GitHub because it contains the API configuration/secrets.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/inkforge-ai.git
cd inkforge-ai
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=your_base_url_here
OPENAI_MODEL=your_model_here
```

Never commit your `.env` file to GitHub.

### 5. Run the application

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

## 🎯 Why I Built This

I built InkForge AI while learning **LangChain** to move beyond tutorials and understand how LLM workflows can be connected to a real web application.

This project helped me practice:

* Flask routes
* POST requests
* Fetch API
* Prompt templates
* LangChain Runnables
* LLM integration
* Environment variables
* Frontend/backend communication

## 📸 Demo

🎥 **Video Demo:** Add your video link here

🌐 **Live Demo:** Add your deployment link here

## 🔮 Future Improvements

Some features that could be added later:

* 📄 Export articles as PDF
* ✨ Multiple writing styles
* 🌍 Multiple languages
* 📝 Article history
* 🎯 SEO-focused article generation

## 👩‍💻 Built By

**Rumaisa**

Built with curiosity, LangChain, and a lot of learning. ✨

---

⭐ If you found this project interesting, feel free to explore the code!
