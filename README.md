# Healthcare Streamlit ChatBot 
By: Hyder Ali

### 1. Problem Statement
A local healthcare company published multiple articles containing healthcare facts,
information, and tips. It wishes to create a conversational chatbot that can address readers’
concerns in natural language using information from the trusted articles and in the
healthcare context.
### 2. Streamlit ChatBot
The conversational chatbot should answer readers' queries using only the information from
the published articles. Where appropriate, it should adopt an empathetic and understanding
tone.

_i.e., What is gestational diabetes
and how is it diagnosed?_
![Alt Text](/Results/Healthcare ChatBot.png)
#### Installation Guide
- Python
- Run pip install to install dependencies listed in `./requirements.txt` and establish a virtual environment `./env`.
- Ensure connectivity to OpenAI environment by placing OpenAI API Key into `./conf.ini`.
i.e. `OPEN_API_KEY=<OpenAI API Key>`
#### Start Usage
Run the following commands to start the Streamlit application.
```
$ source env/bin/activate/python
$ pip install -r requirements.txt
$ nohup streamlit run app.py
```
The Streamlit application will launch on your local server and open in your web browser.
### 3. Methodology
Build a Streamlit ChatBot application using Retrieval Augmented Generation (RAG) pipeline. RAG is the process of improving large language models (LLMs) by integrating additional information from external knowledge sources. This allows the LLMs to produce more precise and context-aware responses, while also mitigating hallucinations. Find the complete codes in the notebooks located in the `./notebook` folder.
#### a) Retrieve text and tabular content from PDFs and HTMLs
Retrieve text and table content from PDFs and HTMLs using the methods outlined in `[01_Data_Extraction_Synapxe_Assignment_Hyder.ipynb]`.
- Fetch PDFs and HTMLs from the specified URLs 
- Use Unstructured framework to extract text and tables, summarizing table contents for later inclusion. Employ rule-based semantic chunking to construct text chunks incorporating table information to be added.

Tools: Unstructured framework
#### b) Construct Retrieval Augmented Generation pipeline (RAG)
Construct RAG pipeline using the methods outlined in `[02_Q&A_RAG_Pipeline_Synapxe_Assignment_Hyder.ipynb]`. The text and table data extracted from PDFs and HTMLs are saved in .`/data/docs_13_pdf_htmls_df.pkl.`
- Establish a RAG pipeline utilizing the Chroma vector store, LangChain, and OpenAI LLM. The RAG setup involves employing a multiquery retriever with Chroma, incorporating prompt engineering, and stateful management of chat history to retain previous conversations in an emphathetic manner.

Tools: OpenAI, Chroma vector store, LangChain 
#### c) LLM Evaluation
Assess the performance of the RAG pipeline by examining its Faithfulness, Answer relevance, and Context relevancy utilizing Ragas, as detailed in `[02_Q&A_RAG_Pipeline_Synapxe_Assignment_Hyder.ipynb]`.

Tools: Ragas