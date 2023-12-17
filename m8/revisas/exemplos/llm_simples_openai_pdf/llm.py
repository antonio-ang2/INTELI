from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnablePassthrough
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv



load_dotenv()

loader = PyPDFLoader("./data/Profile.pdf")
pages = loader.load_and_split()

pages[0]

text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=0
)


vectorstore = FAISS.from_documents(pages, OpenAIEmbeddings())


retriever = vectorstore.as_retriever()



template = """Answer the question based only on the following context:
{context}

Question: {question}


"""

prompt = ChatPromptTemplate.from_template(template)

model = ChatOpenAI(model="gpt-3.5-turbo")

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | model
)