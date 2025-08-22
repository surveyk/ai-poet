<<<<<<< HEAD
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

#ChatOpenAI 초기화
llm = init_chat_model("gpt-4o-mini", model_provider="openai")

#프롬프트 템플릿
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "{input}")
])

#문자열 출력 파서
output_parser = StrOutputParser()

chain = prompt | llm | output_parser
result = chain.invoke({"input": "hi"})
print(result)
=======
# test.py
import streamlit as st
#from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
# .env 파일 로드
#load_dotenv()
api_key = os.environ["OPENAI_API_KEY"]

st.set_page_config(
    page_title="n행시 생성기",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ n행시 생성기 (LangChain + GPT-4o-mini)")
st.markdown("아래 입력창에 단어를 넣으면 AI가 재치있는 n행시를 만들어 줍니다!")

# 단어 입력
input_word = st.text_input("단어를 입력하세요:", value="코딩")

# 버튼 클릭 시 n행시 생성
if st.button("n행시 생성"):
    with st.spinner("AI가 생각 중... 잠시만 기다려주세요"):
        try:
            # ChatOpenAI 초기화
            llm = init_chat_model("gpt-4o-mini", model_provider="openai")

            # 프롬프트 템플릿
            prompt = ChatPromptTemplate.from_messages([
                ("system", "You are a helpful assistant."),
                ("user", "{input}")
            ])

            # 출력 파서
            output_parser = StrOutputParser()

            # 체인 구성
            chain = prompt | llm | output_parser

            # n행시 생성
            prompt_input = f"{input_word}에 대한 재치있는 n행시를 써줘"
            result = chain.invoke({"input": prompt_input})

            st.success("완성! 🎉")
            st.text_area("AI n행시:", value=result, height=200)

        except Exception as e:
            st.error(f"오류 발생: {e}")
>>>>>>> ce96c00 (추가)
