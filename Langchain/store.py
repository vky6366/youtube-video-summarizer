from Utils.yt_transcription import transcription
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS

class vector_store():
    def __init__(self,url):
        self.url = url
        self.chunks = transcription.transcript(self.url)

    def store(self):
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.vector_store = FAISS.from_documents(self.chunks, embeddings)
        return self.vector_store
    
    def retrieve(self,querry):
        self.querry = querry
        retriever = self.vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
        return retriever.invoke(querry)