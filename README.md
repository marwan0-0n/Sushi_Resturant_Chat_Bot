# 🍣 Sushi Restaurant Chatbot

A simple chatbot built with **Streamlit** and **LangChain** that simulates a friendly sushi chef.
It uses OpenRouter API with `ChatOpenAI` to handle conversations.

---

## 📦 Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/sushi-restaurant-chatbot.git
cd sushi-restaurant-chatbot
```

2. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Linux / Mac
venv\Scripts\activate      # On Windows
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## ⚙️ Environment Variables

Create a .env file in the root of the project and add your keys:

```env
LANGSMITH_TRACING=true
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=your_project_name_here
OPENAI_API_KEY=your_openai_api_key_here
```

👉 Note: Never share your real API keys publicly.

👉 If you share this repo, include a .env.example file instead.

## ▶️ Run the Project

Start the Streamlit app:

```bash
streamlit run sushi_resturant.py
```

The chatbot will open in your browser at http://localhost:8501

## 🔄 Changing the Model

```python
model="deepseek/deepseek-chat-v3-0324:free"
```

If your API key does not support this model, you can change it to another supported model (for example "gpt-4o-mini") inside the code:

```python
llm = ChatOpenAI(
    model="gpt-4o-mini",
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.3,
)
```

## Screenshot of the App

![alt text](<Screenshot from 2025-08-27 17-05-28.png>)

## 📝 License

This project is for learning purposes.