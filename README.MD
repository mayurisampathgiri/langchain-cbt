# 🧠 CBT Thought Reframer — Built with LangChain + Streamlit

This is an AI-powered mental wellness app that helps you **reframe negative or unhelpful thoughts** using **Cognitive Behavioral Therapy (CBT)** techniques — guided by the power of Large Language Models (LLMs).

> From concept to code - built with LangChain, OpenAI, FastAPI and Streamlit.

---

### 💡 Why I built this

As part of my journey learning LangChain and FastAPI, I wanted to build something meaningful, interactive, and human-centered. Mental health is close to my heart — and combining CBT with LLMs felt like the perfect way to apply both empathy and engineering.

---

### ✨ Features

- 📬 Input a negative or anxious thought
- 🧠 Reframed using CBT principles (powered by LangChain + OpenAI)
- 🔐 Secure API Key usage via environment variables
- 💬 Clean, interactive Streamlit UI

---

### 🛠️ How it Works

1. You enter a raw, unfiltered thought (e.g., “I’m not good enough”).
2. The app sends this to a LangChain prompt pipeline using `ChatOpenAI`.
3. A custom prompt template reframes the input using CBT techniques.
4. The AI returns a compassionate, structured CBT response.
5. The result is displayed in a calming, single-page Streamlit app.

---

### 🖼️ App Preview (yet to come)


---

### ⚙️ Tech Stack

| Tool                     | Use Case                    |
| ------------------------ | --------------------------- |
| **LangChain**            | Prompt chaining / LLM logic |
| **OpenAI**               | LLMs (gpt-3.5-turbo, gpt-4) |
| **Streamlit**            | Frontend + Deployment       |
| **FastAPI**              | Backend API version   |

---

### 📦 Installation

```bash
git clone https://github.com/mayurisampathgiri/langchain-cbt-clean.git
cd langchain-cbt-clean
pip install -r requirements.txt
```

> Run backend first from the parent directory.

```
uvicorn backend.main:app --reload
```

> Open other terminal to run the frontend (simultaneously)
```
streamlit run frontend/app.py
```

> Make sure to add your OpenAI key in `.env`:

```
OPENAI_API_KEY=your-api-key-here
```

---

### 🚀 Deployment (yet to come)

Deploy in 1-click using **Streamlit Cloud** (free):\
[https://share.streamlit.io/](#)

---

### 🌤️ Example Thought

> “I feel like I'm failing at everything.”

🧘 **AI CBT Reframe:**

> *“Let’s look at this together. It sounds like you’re experiencing all-or-nothing thinking...”*


---

### 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### 💖 Built by

**Mayuri Sampathgiri** — learning AI, building tools with care\
[LinkedIn](https://linkedin.com/in/mayurisampathgiri) • [GitHub](https://github.com/mayurisampathgiri)

