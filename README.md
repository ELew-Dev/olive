# 🫒 Olive – Friendly AI Support Assistant

Olive is an AI-powered helper designed to make support teams faster, calmer, and more efficient. It classifies customer messages and drafts smart, friendly replies in real time.

Built with:  
- 🧠 OpenAI GPT  
- 🖼️ Streamlit interface  
- 💬 Clean UX for support agents  

---

## 🚀 Getting Started

1. Clone the repo:  
   ```bash
   git clone https://github.com/your-username/olive.git
   cd olive
```

2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Install requirements:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with your OpenAI API key:

   ```ini
   OPENAI_API_KEY=sk-...
   ```

5. Run the app:

   ```bash
   streamlit run app.py
   ```

---

## 🧠 What Olive Does

* ✅ Classifies customer message intent (Cancel, Reschedule, Complaint, Compliment, General Question)
* ✨ Generates a thoughtful, natural reply based on the detected intent
* 🔁 Easily extendable for tagging, routing, automation, or real-time support

---

## 📂 Project Structure

```bash
olive/
 ├── app.py               # Streamlit UI for user input and output
 ├── olive.py             # Core AI logic: intent classification & response generation
 ├── .env                 # Environment variables (e.g., OpenAI API key)
 ├── .gitignore           # Git ignore rules
 ├── requirements.txt     # Python dependencies
 ├── README.md            # This file
 └── examples/
     └── sample_inputs.md # Example customer messages for testing
```

---

## 🧱 Development Outline

1. **Project Setup (15–20 min)**
   Create folder, virtual environment, install packages (openai, streamlit, python-dotenv)
   Create files: `app.py`, `olive.py`, `.env`
   Add `.gitignore` with entries for `__pycache__/`, `.env`, and `venv/`
   Create `requirements.txt`

2. **AI Logic (30 min)**
   Write `classify_message()` to detect intent using OpenAI ChatCompletion
   Write `generate_response()` to produce friendly replies based on intent

3. **Streamlit UI (30–40 min)**
   Build UI in `app.py` to input messages and display intent and AI-generated reply

4. **Example Inputs (10–15 min)**
   Add example messages and expected outputs in `examples/sample_inputs.md`

5. **README polish (20 min)**
   Document the project goals, usage, and structure

6. **Final Polish + GitHub Upload (15–20 min)**
   Initialize git repo, commit, push to GitHub

---

## 🙌 Why "Olive"?

Because this AI bot is simple, warm, and always ready to help — just like a good olive oil drizzle. 🍽️