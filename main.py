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