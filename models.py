from pydantic import BaseModel, Field
from typing import List

class UserStyleProfile(BaseModel):
    height: int = Field(description="사용자의 키 (cm)")
    weight: int = Field(description="사용자의 몸무게 (kg)")
    body_shape: str = Field(description="사용자의 체형 (예: 모래시계형, 역삼각형, 원통형 등)")
    gender: str = Field(description="성별 (male | female)")
    bmi: float = Field(description="신체질량지수")

class CoordiRecommendation(BaseModel):
    weather_condition: str = Field(description="현재 날씨 및 기온 정보")
    style_concept: str = Field(description="추천 스타일 컨셉 (예: 캐주얼, 비즈니스 캐주얼)")
    items: List[str] = Field(description="추천 의류 아이템 리스트")
    styling_tips: str = Field(description="체형 보완을 위한 스타일링 팁")
