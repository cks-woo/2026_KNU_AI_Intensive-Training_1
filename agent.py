from tools import get_current_weather, analyze_body_and_save, save_coordi_result
from langchain.agents import create_agent

def get_fashion_coordinator_agent(model):
    # 새로운 도구인 get_current_weather를 추가합니다.
    tools = [get_current_weather, analyze_body_and_save, save_coordi_result]

    system_prompt = """
    당신은 스마트 패션 스타일리스트입니다. 
    사용자의 '거주 지역, 키, 몸무게, 체형'을 바탕으로 최적의 코디를 제안합니다.

    - 작동 프로세스:
    1. 사용자가 지역(도시명)을 말하면, 먼저 `get_current_weather`를 호출하여 실시간 기온을 확인하세요.
    2. 확인된 기온과 사용자의 체형(역삼각형, 원통형 등)을 결합하여 분석합니다.
    3. `analyze_body_and_save`로 신체 정보를 기록하세요.
    4. 분석 결과를 바탕으로 구체적인 코디와 스타일링 팁을 작성한 후, 
       `save_coordi_result`로 최종 저장하세요.

    - 코디 가이드:
    - 5°C 이하: 패딩, 코트, 히트텍 등 방한 위주
    - 10°C ~ 16°C: 자켓, 가디건, 셔츠 레이어링
    - 20°C 이상: 가벼운 반팔, 면바지 등 통기성 위주
    """

    return create_agent(model=model, tools=tools, system_prompt=system_prompt)
