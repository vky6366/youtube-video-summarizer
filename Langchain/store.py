from Utils.yt_transcription import transcription
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

class vector_store():
    def __init__(self,url):
        self.url = url
        self.chunks = transcription.transcript(self.url)



    def my_invoke(self,question):
        self.question = question
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        vector_store = FAISS.from_documents(self.chunks, embeddings)

        retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

        llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

        prompt = PromptTemplate(
            template="""
                You are a helpful assistant.
                Answer ONLY using the provided transcript context, as if you are explaining to a beginner in the field.
                Respond in bullet points.
                If the context is insufficient, say "I don't know based on the given context."

                Context:
                {context}

                Question:
                {question}
            """,
            input_variables=['context', 'question']
        ) 
        retrieved_docs = retriever.invoke(self.question)
        def format_docs(retrieved_docs):
            context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
            return context_text


        context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
        parallel_chain = RunnableParallel({
            'context': retriever | RunnableLambda(format_docs),
            'question': RunnablePassthrough()
        })

        parser = StrOutputParser()
        main_chain = parallel_chain | prompt | llm | parser

        result = main_chain.invoke('Can you summarize the video')
                