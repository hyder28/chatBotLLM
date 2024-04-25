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
            source_metadatas = {doc.metadata["source"] for doc in result["context"]}
            source_metadatas = ";".join(str(source) for source in source_metadatas)
            response = f"{ans}\n\nRefer to:\n{source_metadatas}"
            st.text_area("LLM ChatBot says:", value=response, height=600)
        except Exception as e:
            logging.error(f"Error in generating response: {str(e)}")
    else:
        st.warning("Please enter a question before submitting.")

# $ nohup streamlit run app.py