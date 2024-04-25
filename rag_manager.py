from langchain_core.documents.base import Document
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
import pandas as pd

from config import load_config
import logging
load_config()

# retrieve parsed pdf and htmls docs from df pkl
try:
    docs_df = pd.read_pickle("./data/docs_13_pdf_htmls_df.pkl")
    docs = [Document(page_content=row["text"], metadata=row["metadata"]) for index, row in docs_df.iterrows()]
except Exception as e:
    logging.error(f"Failed to load documents: {str(e)}")

# setup chroma vector store
try:
    vectorstore = Chroma.from_documents(documents=docs, embedding=OpenAIEmbeddings(model="text-embedding-ada-002"))
    retriever = vectorstore.as_retriever()
except Exception as e:
    logging.error(f"Failed to setup vector store and retriever: {str(e)}")

# setup llm prompting
try:
    prompt_template = """You are an healthcare assistant...
    Question: {question}
    Context: {context}
    Answer:"""
    prompt = ChatPromptTemplate.from_template(prompt_template)

    llm = ChatOpenAI(model="gpt-3.5-turbo")
except Exception as e:
    logging.error(f"Failed to setup OpenAI LLM: {str(e)}")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# setup rag
try:
    rag_chain_from_docs = (
        RunnablePassthrough.assign(context=(lambda x: format_docs(x["context"])))
        | prompt
        | llm
        | StrOutputParser()
    )
    rag_chain_with_source = RunnableParallel({"context": retriever, "question": RunnablePassthrough()}).assign(answer=rag_chain_from_docs)
except Exception as e:
    logging.error(f"Failed to setup rag: {str(e)}")
def get_response(user_input):
    result = rag_chain_with_source.invoke(user_input)
    return result