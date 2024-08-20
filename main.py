import streamlit as st

from langchain_openai import ChatOpenAI

#### Streamlit
# streamlit run main.py

#### Env Setting ####
# from dotenv import load_dotenv
# load_dotenv()

#### LLM
model_name = "gpt-4o-mini"
model = ChatOpenAI(model_name=model_name)

#### Streamlit
st.title("AI 시인")
content = st.text_input("시의 주제를 제시해주세요.")
if st.button("시 작성 요청하기"):
    st.write(f"주제\n{content}")
    with st.spinner("시 작성 중..."):
        output = model.invoke(f"{content}에 대한 시를 지어줘")
        st.markdown(output.content)