import os
import requests
from typing import List
from langchain_core.tools import tool
from models import UserStyleProfile, CoordiRecommendation
from mock_db import get_store

@tool
def get_current_weather(location: str) -> str:
    """
    입력된 지역의 현재 날씨와 기온 정보를 가져옵니다.
    """
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    if not api_key:
        return "날씨 API 키가 설정되지 않았습니다."

    # 1. 안전한 HTTPS 사용
    # 2. quote() 함수로 '천안' 같은 한글 지역명을 URL 안전 문자로 변환
    encoded_location = quote(location)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={encoded_location}&appid={api_key}&units=metric&lang=kr"
    
    try:
        response = requests.get(url)
        # API 응답 상태를 먼저 확인하는 것이 좋습니다 (상태 코드 200 체크)
        response.raise_for_status() 
        
        data = response.json()
        weather_desc = data['weather'][0]['description']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        
        return f"{location}의 현재 날씨는 '{weather_desc}'이며, 기온은 {temp}°C (체감 {feels_like}°C)입니다."
    except requests.exceptions.HTTPError as e:
        return f"날씨 API 호출 에러: {e.response.status_code} - {e.response.text}"
    except Exception as e:
        return f"날씨 조회 중 예상치 못한 오류 발생: {str(e)}"

@tool
def analyze_body_and_save(height: int, weight: int, body_shape: str, gender: str) -> UserStyleProfile:
    """사용자의 신체 정보를 바탕으로 BMI를 계산하고 프로필을 저장합니다."""
    bmi = round(weight / (height / 100) ** 2, 1)
    
    profile = UserStyleProfile(
        height=height,
        weight=weight,
        body_shape=body_shape,
        gender=gender,
        bmi=bmi
    )
    
    store = get_store()
    store["profile"].append(profile)
    return profile

@tool
def save_coordi_result(weather: str, style: str, items: List[str], tips: str) -> CoordiRecommendation:
    """최종 결정된 코디와 스타일링 팁을 데이터베이스에 저장합니다."""
    recommendation = CoordiRecommendation(
        weather_condition=weather,
        style_concept=style,
        items=items,
        styling_tips=tips
    )
    
    store = get_store()
    store["saved_plans"].append(recommendation)
    return recommendation
