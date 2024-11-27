import streamlit as st
import os

from langchain.memory import ConversationSummaryBufferMemory

from utills import get_chat_response
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=os.getenv("COURSE_API_KEY"),openai_api_base="https://api.aigc369.com/v1")

st.title("AI聊天助手")


if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationSummaryBufferMemory(llm=model,return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的AI助手，请问有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    # if not openai_api_key:
    #     st.info("请输入你的Openai API Key")
    #     st.stop()
    st.session_state["messages"].append({"role": "human","content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("AI正在思考中，请稍等..."):
        response = get_chat_response(prompt,st.session_state["memory"],os.getenv("COURSE_API_KEY"))
    msg = {"role": "ai","content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)


clear = st.button("清除所有对话")
if clear:
    st.session_state["messages"] = []
    st.session_state["memory"] = ConversationSummaryBufferMemory(llm=model,return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是你的AI助手，请问有什么可以帮你的吗？"}]
    st.info("已清除全部对话")

