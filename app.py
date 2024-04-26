import streamlit as st
from rag_manager import get_response
import logging

# title
st.title('Healthcare ChatBot')

# user input
user_input = st.text_input("Type your message here:")
submit_button = st.button("Submit")

# user button
if submit_button:
    if user_input:
        try:
            result = get_response(user_input)
            ans = result["answer"]

            source_set = set([doc.metadata["source"] for doc in result["context"]])

            source_text = ""
            for source in source_set:
                source_text += source + "\n"

            response = f"{ans}\n\nSource:\n{source_text}"

            st.text_area("LLM ChatBot says:", value=response, height=600)
        except Exception as e:
            logging.error(f"Error in generating response: {str(e)}")
    else:
        st.warning("Please enter a question before submitting.")

# $ nohup streamlit run app.py