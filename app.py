import streamlit as st
from olive import classify_message, generate_response

st.set_page_config(page_title="Olive – AI Help Assistant")

st.title("🫒 Olive – Your Friendly Support Assistant")

message = st.text_area("Paste a customer message here:")

if st.button("Generate AI Response") and message:
    try:
        intent = classify_message(message)
        reply = generate_response(message, intent)

        st.subheader("Detected Intent")
        st.success(intent)

        st.subheader("Suggested Reply")
        st.info(reply)
    except Exception as e:
        st.error(f"Oops! Something went wrong: {e}")
