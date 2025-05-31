import streamlit as st
import folium
from streamlit_folium import st_folium

# 제주도 핫한 관광지 데이터 (간단 예시, 실제 좌표 기준)
jeju_hot_places = [
    {"name": "성산일출봉 🌅", "desc": "제주의 일출 명소! 푸른 바다 위로 솟은 거대한 오름!", "lat": 33.458, "lon": 126.942},
    {"name": "한라산 국립공원 🏞️", "desc": "한국에서 가장 높은 산! 사계절 다른 매력을 느낄 수 있어요!", "lat": 33.3617, "lon": 126.5292},
    {"name": "만장굴 동굴 🌋", "desc": "신비로운 용암 동굴! 세계자연유산으로 지정된 곳이에요.", "lat": 33.5203, "lon": 126.7708},
    {"name": "협재 해수욕장 🏖️", "desc": "하얀 모래와 에메랄드빛 바다가 아름다운 해변!", "lat": 33.3931, "lon": 126.2397},
    {"name": "우도 🐚", "desc": "작고 아름다운 섬! 자전거 타고 한 바퀴 돌기 최고예요!", "lat": 33.5064, "lon": 126.9517},
    {"name": "카멜리아힐 🌺", "desc": "동백꽃이 아름다운 정원! 사진 찍기 좋은 명소예요!", "lat": 33.2483, "lon": 126.4211},
    {"name": "이호테우 해변 🐴", "desc": "말 모양 조형물이 유명한 포토존! 노을 맛집이에요.", "lat": 33.5141, "lon": 126.4632},
    {"name": "제주 돌문화공원 🪨", "desc": "제주의 돌 문화를 체험할 수 있는 독특한 공간!", "lat": 33.4268, "lon": 126.7203},
    {"name": "용머리해안 🐉", "desc": "용이 머리를 내민 듯한 지형! 바다와 절벽의 조화가 아름다워요.", "lat": 33.2373, "lon": 126.3139},
    {"name": "서귀포 칠십리 🌊", "desc": "절경의 해안 산책로! 자연과 함께 걷는 힐링 코스!", "lat": 33.2524, "lon": 126.5617},
]

# Streamlit 페이지 설정
st.set_page_config(page_title="🌟 제주도 핫플 투어", layout="wide")

st.title("🏝️ 제주도 핫한 관광지 TOP 10!")
st.markdown("안녕하세요! 🌞 제주의 매력을 듬뿍 느낄 수 있는 🔥핫한 명소 10곳을 소개할게요! 지도와 함께 확인해보세요 👇")

# Folium 지도 생성
m = folium.Map(location=[33.38, 126.55], zoom_start=10, tiles="CartoDB positron")

# 명소 마커 추가
for place in jeju_hot_places:
    folium.Marker(
        location=[place["lat"], place["lon"]],
        popup=f"<b>{place['name']}</b><br>{place['desc']}",
        tooltip=place["name"],
        icon=folium.Icon(color="orange", icon="info-sign")
    ).add_to(m)

# Streamlit에 지도 표시
st_data = st_folium(m, width=1000, height=600)

# 하단에 리스트 형태로 보기
st.subheader("📍 명소 정보 한눈에 보기")
for place in jeju_hot_places:
    st.markdown(f"### {place['name']}")
    st.markdown(f"📝 {place['desc']}")
    st.markdown("---")
