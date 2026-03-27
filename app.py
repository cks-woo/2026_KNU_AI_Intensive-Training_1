from agent import get_fashion_coordinator_agent
from langchain_openai import ChatOpenAI  # OpenAI 계열 사용 시
from langchain_groq import ChatGroq      # Groq 계열 사용 시
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-5-mini", temperature=0.7)

coach_agent = get_fashion_coordinator_agent(model)

user_input = """
나는 지금 천안에 살고 있어.
내 성별은 남성이고, 키는 180cm, 몸무게는 80kg이야. 
체형은 보통 체형인데, 오늘 학교에 입고 갈 만한 코디 추천해줘.
"""

result = coach_agent.invoke({
    "messages": [{"role": "user", "content": user_input}]
})

print(result['messages'][-1].content)
