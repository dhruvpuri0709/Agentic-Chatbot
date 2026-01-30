# 🤖 Agentic AI News Summarizer

> **The future of AI is not just responding—it's *thinking, searching, and acting* autonomously.**

Agentic AI represents a paradigm shift in how we interact with artificial intelligence. Rather than simple request-response patterns, agents can plan, use tools, and execute complex workflows. This chatbot harnesses that power through LangGraph and Groq, creating an intelligent system that doesn't just answer—it *reasons*.

---

## ✨ Features

### 💬 **Basic Chatbot**
Clean, direct conversations powered by LLM API calls. Perfect for quick queries and casual interactions.

### 🌐 **Web-Enhanced Chatbot**
Built on ReAct architecture with integrated tool nodes:
- 🔍 **Tavily Web Search** - Real-time internet knowledge
- 📚 **Wikipedia** - Comprehensive encyclopedia access  
- 📄 **ArXiv** - Latest research papers and scientific content

### 📰 **AI News Summarizer**
Stay ahead of the curve with curated AI news:
- 📅 **Daily** briefings
- 📊 **Weekly** roundups
- 📈 **Monthly** trends
- 🌍 Coverage of USA and global AI developments

---

## 🏗️ Architecture

```
Agentic_AI_Chatbot/
├── 📄 app.py                    # Streamlit entry point
└── 📁 src/
    └── 📁 AgenticAI/
        ├── 📄 main.py           # Core application logic
        ├── 📁 Graph/            # LangGraph workflow definitions
        ├── 📁 LLMs/             # Language model configurations
        ├── 📁 Nodes/            # Agent nodes and logic
        ├── 📁 State/            # State management
        ├── 📁 Tools/            # External tool integrations
        └── 📁 UI/               # Streamlit interface components
```

**Modular by design.** Each component is isolated, making the system maintainable, testable, and extensible.

---

## 🚀 Quick Start

```bash
streamlit run app.py
```

That's it. Your agentic AI chatbot is live.

---

## 🛠️ Tech Stack

- **🧠 LangGraph** - Agent orchestration and workflow management
- **⚡ Groq** - Lightning-fast LLM inference
- **🎨 Streamlit** - Beautiful, responsive UI
- **🔧 Modular Python** - Clean, maintainable codebase

---

## 💡 Why Agentic AI?

Traditional chatbots are limited to what they know. **Agentic AI breaks free:**

- 🧭 **Autonomous decision-making** - Agents choose when and how to use tools
- 🔄 **Multi-step reasoning** - Complex problems get broken down and solved systematically  
- 🌐 **Real-world grounding** - Up-to-date information through web search and APIs
- 🎯 **Goal-oriented behavior** - Focus on outcomes, not just responses

---

Built with 💙 for the future of human-AI collaboration
