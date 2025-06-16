# 🫒 Olive – Friendly AI Support Assistant

Olive is an AI-powered helper designed to make support teams faster, calmer, and more efficient. It classifies customer messages and drafts smart, friendly replies in real time.

**Built with:**

  * **🧠 OpenAI GPT:** The powerful language model behind Olive's intelligence.
  * **🖼️ Streamlit interface:** For a clean, interactive web application.
  * **💬 Clean UX:** Designed for support agents to easily input messages and get responses.

-----

## 🚀 Getting Started

Follow these steps to get Olive up and running on your local machine.

### 1\. Clone the Repository & Navigate

First, get a copy of the project and move into its directory:

```bash
git clone https://github.com/your-username/olive.git
cd olive
```

### 2\. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage project dependencies.

```bash
python3 -m venv venv
source venv/bin/activate   # On macOS/Linux
# venv\Scripts\activate    # On Windows
```

### 3\. Install Requirements

Install all necessary Python packages within your activated virtual environment:

```bash
pip install -r requirements.txt
```

### 4\. OpenAI API Key Configuration

Olive requires an OpenAI API key to access its language models.

  * **Obtain Your API Key:**

    1.  Go to the OpenAI API Keys page: [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)
    2.  Log in to your OpenAI account.
    3.  Click **"Create new secret key"**. Give it a descriptive name (e.g., "Olive App Key").
    4.  **Immediately copy the *entire* key\!** It will only be shown once. It will start with `sk-` or `sk-proj-`.

  * **Create or Update `.env` File:**

    1.  In the root of your `olive` project directory, create a new file named **`.env`** (note the leading dot, this makes it a hidden file).

    2.  Add the following line to your `.env` file, replacing `<YOUR_OPENAI_API_KEY>` with the key you just copied:

        ```dotenv
        OPENAI_API_KEY=sk-your_brand_new_secret_key_here
        ```

          * **Important:** Ensure there are no spaces around the `=` sign or at the end of the key.

  * **Verify `.env` Loading (Optional but Recommended):**
    You can use the `check_env.py` script to confirm your `.env` file is being read correctly:

    ```bash
    (venv) your_username@your_machine olive % python3 check_env.py
    ```

    Expected Output: `API key loaded: sk-xxxxx***********************xxxx`

### 5\. Run the Application

With your virtual environment active and `.env` configured, you can launch the Streamlit app:

```bash
streamlit run app.py
```

This will open the Olive AI Assistant in your web browser.

-----

## 🧠 What Olive Does

  * **✅ Classifies Customer Message Intent:** Olive can detect the core purpose of a customer message (e.g., Cancel, Reschedule, Complaint, Compliment, General Question).
  * **✨ Generates Thoughtful Replies:** Based on the detected intent and the original message, Olive crafts a friendly and natural language response.
  * **🔁 Easily Extendable:** The core logic is designed to be easily extended for more advanced features like automated tagging, intelligent message routing, or integration into real-time support systems.

-----

## 📂 Project Structure

```
olive/
 ├── app.py               # Streamlit UI for user input and output
 ├── olive.py             # Core AI logic: intent classification & response generation
 ├── .env                 # Environment variables (e.g., OpenAI API key - crucial for security!)
 ├── .gitignore           # Git ignore rules (prevents sensitive files like .env from being committed)
 ├── requirements.txt     # Python dependencies
 ├── README.md            # This file
 ├── check_env.py         # Utility script to verify .env file loading (useful for debugging)
 └── examples/
     └── sample_inputs.md # Example customer messages for testing
```

-----

## 🛠️ Troubleshooting Common Issues

Encountering problems? Here are solutions to the most common issues:

### Error: `401 - Incorrect API key provided`

**Problem:** The OpenAI API is rejecting the API key being sent. This means the key is invalid, expired, revoked, or incorrectly formatted/loaded. Even if `check_env.py` shows it loaded, the API itself isn't accepting it.

**Solution:**

1.  **Generate a NEW API Key:** Go back to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) and create a brand new secret key. Copy it immediately.
2.  **Update `.env`:** Open your `.env` file and *replace* the existing `OPENAI_API_KEY` value with this **new, freshly copied key**. Save the file.
3.  **Full Restart:**
      * Stop the Streamlit app (`Ctrl + C` in your terminal).
      * Deactivate your virtual environment (`deactivate`).
      * Reactivate your virtual environment (`source venv/bin/activate`).
      * Run `streamlit run app.py` again.
4.  **Verify `olive.py`:** Ensure `load_dotenv()` is called at the very top of `olive.py` and that the OpenAI client is initialized like `client = openai.OpenAI(api_key=api_key)`.

### Error: `429 - You exceeded your current quota`

**Problem:** Your API key is valid and connected to OpenAI, but your account has run out of free credits or has reached its spending limit. This is a billing-related issue.

**Solution:**

1.  **Check OpenAI Usage/Billing:** Visit [https://platform.openai.com/usage](https://platform.openai.com/usage) and review your current usage and available credit.
2.  **Add Payment Information/Credits:** If necessary, add a payment method or purchase more credits directly on the OpenAI platform to continue using the API.

-----

## 🙌 Why "Olive"?

Because this AI bot is simple, warm, and always ready to help — just like a good olive oil drizzle. 🍽️