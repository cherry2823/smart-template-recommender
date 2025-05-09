# 🎨 Smart Template Recommender

An AI-powered template recommendation tool inspired by Canva's design style.  
Given a user keyword (e.g. "travel", "fitness", "startup"), it suggests relevant design templates using semantic embeddings.

---

## ✨ Features

- 🔍 Keyword-based search with semantic matching  
- 🧠 Uses OpenAI’s `text-embedding-ada-002` to represent user intent and template metadata  
- ⚡ Vector similarity via cosine distance  
- 🖥 Clean Streamlit interface for interactive exploration  

---

## 📦 Tech Stack

| Component       | Description                                 |
|----------------|---------------------------------------------|
| `openai`        | For generating text embeddings              |
| `streamlit`     | For building the web UI                     |
| `numpy`         | For similarity computation                  |
| `dotenv`        | For securely loading API keys               |

---

## 🚀 Quickstart

### 1. Clone this repo

```bash
git clone https://github.com/cherry2823/smart-template-recommender.git
cd smart-template-recommender
```

### 2. Create virtual environment (recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` file

```bash
cp .env.example .env
```

Replace the placeholder with your real OpenAI API key:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```
smart-template-recommender/
├── app.py                  # Streamlit frontend
├── recommender.py          # Embedding & recommendation logic
├── templates.json          # Simulated template dataset
├── .env.example            # API key template (do not commit .env)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ✅ Why this project?

This project was built as a showcase for a Machine Learning internship at Canva.  
It demonstrates:

- Embedding-based recommendation logic  
- Prompt design and OpenAI API usage  
- Frontend prototyping with Streamlit  
- Git/GitHub best practices for clean, collaborative code  

---

## 🔐 Notes

- `.env` is excluded from Git for security  
- Embedding model used: `text-embedding-ada-002`  
- Token usage may apply when testing

---

## 🙋‍♀️ Author

Made with ❤️ by [cherry2823](https://github.com/cherry2823)  
Feel free to fork, explore, or connect!
