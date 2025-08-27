import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import dotenv

dotenv.load_dotenv()

system_template = """you are a chef in a sushi resturant
you only dedicated to this kind of resturants
you cant answer nonrelated topics
only give short answers for greetings you cant give tips or any recommendations before user asks his question
give short and briefly answers
be kind
you can sometimes say some japanese common words in english letters
if user asks any unrelated question say (sorry but i'am just a sushi chef) """

st.title("Sushi Resturant")


if "history" not in st.session_state:
    st.session_state.history = [SystemMessage(system_template)]

for msg in st.session_state.history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)


prompt = st.chat_input("Enter your message")


if prompt:
    llm = ChatOpenAI(
        model="deepseek/deepseek-chat-v3-0324:free",
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0.3,
    )
    st.session_state.history.append(HumanMessage(prompt))
    st.chat_message("user").write(prompt)
    generator = llm.stream(st.session_state.history)
    response = st.chat_message("assistant").write_stream(generator)
    st.session_state.history.append(AIMessage(response))
