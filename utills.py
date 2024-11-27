import os

from langchain.chains import ConversationChain
from langchain_openai import ChatOpenAI
from openai import base_url

from langchain.memory import ConversationBufferMemory

def get_chat_response(prompt,memory,openai_api_key):
    model = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_api_key,openai_api_base="https://api.aigc369.com/v1")
    chain = ConversationChain(llm=model,memory=memory)

    response = chain.invoke({"input": prompt})
    return response["response"]

memory = ConversationBufferMemory(return_messages=True)
# print(get_chat_response("爱因斯坦提出的最著名的定理有哪些？",memory,os.getenv("COURSE_API_KEY")))
# print(get_chat_response("我上一个问题问的是什么？",memory,os.getenv("COURSE_API_KEY")))

