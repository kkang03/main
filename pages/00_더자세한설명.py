import streamlit as st
import folium
from streamlit_folium import st_folium

# 제주도 핫한 관광지 데이터 (명소, 역사적 의미, 주변 맛집 및 핫플)
jeju_hot_places = [
    {
        "name": "성산일출봉 🌅",
        "desc": "약 5만 년 전에 형성된 화산섬으로, 유네스코 세계자연유산에 등재된 제주도의 대표적인 일출 명소입니다.",
        "lat": 33.458,
        "lon": 126.942,
        "restaurants": ["성산일출봉 근처 해산물 전문 음식점"],
        "hotspots": ["성산일출봉 주변 해변"]
    },
    {
        "name": "한라산 국립공원 🏞️",
        "desc": "제주도의 중심에 위치한 활화산으로, 다양한 식물과 동물들이 서식하고 있어 생태학적으로 중요한 지역입니다.",
        "lat": 33.3617,
        "lon": 126.5292,
        "restaurants": ["한라산 인근 전통 음식점"],
        "hotspots": ["한라산 국립공원 내 다양한 등산 코스"]
    },
    {
        "name": "만장굴 동굴 🌋",
        "desc": "약 20만 년 전에 형성된 용암 동굴로, 세계자연유산에 등재되어 있으며, 동굴 내부에는 다양한 종유석과 석순들이 형성되어 있습니다.",
        "lat": 33.5203,
        "lon": 126.7708,
        "restaurants": ["만장굴 근처 지역 특산물 음식점"],
        "hotspots": ["만장굴 주변 자연 산책로"]
    },
    {
        "name": "협재 해수욕장 🏖️",
        "desc": "맑은 바닷물과 고운 모래사장이 특징인 제주도의 대표적인 해수욕장으로, 여름철에는 많은 관광객들이 방문하여 해수욕을 즐깁니다.",
        "lat": 33.3931,
        "lon": 126.2397,
        "restaurants": ["협재 해수욕장 인근 해산물 요리 전문 음식점"],
        "hotspots": ["협재 해수욕장 주변 카페와 레스토랑"]
    },
    {
        "name": "우도 🐚",
        "desc": "제주도의 동쪽에 위치한 작은 섬으로, 아름다운 자연 경관과 해변으로 유명하며, '우도'라는 이름은 '소의 머리'를 닮았다고 하여 붙여졌습니다.",
        "lat": 33.5064,
        "lon": 126.9517,
        "restaurants": ["우도 특산물인 땅콩 아이스크림과 땅콩국수를 맛볼 수 있는 음식점"],
        "hotspots": ["우도의 해변과 자연 경관을 즐길 수 있는 장소들"]
    },
    {
        "name": "카멜리아힐 🌺",
        "desc": "동백꽃을 테마로 한 정원으로, 다양한 종류의 동백꽃을 감상할 수 있으며, 특히 겨울철에는 동백꽃이 만개하여 아름다운 경관을 제공합니다.",
        "lat": 33.2483,
        "lon": 126.4211,
        "restaurants": ["카멜리아힐 인근 전통 제주 음식을 제공하는 음식점"],
        "hotspots": ["카멜리아힐 주변 자연 경관을 즐길 수 있는 장소들"]
    },
    {
        "name": "이호테우 해변 🐴",
        "desc": "말 모양의 조형물이 특징인 해변으로, 일몰을 감상하기에 좋은 장소로 알려져 있습니다.",
        "lat": 33.5141,
        "lon": 126.4632,
        "restaurants": ["이호테우 해변 인근 해산물 요리 전문 음식점"],
        "hotspots": ["이호테우 해변 주변 카페와 레스토랑"]
    },
    {
        "name": "제주 돌문화공원 🪨",
        "desc": "제주도의 전통적인 돌 문화를 체험할 수 있는 공간으로, 다양한 돌 조형물과 전시물이 있습니다.",
        "lat": 33.4268,
        "lon": 126.7203,
        "restaurants": ["돌문화공원 인근 전통 제주 음식을 제공하는 음식점"],
        "hotspots": ["돌문화공원 주변 자연 경관을 즐길 수 있는 장소들"]
    },
    {
        "name": "용머리해안 🐉",
        "desc": "용이 머리를 내민 듯한 지형으로, 바다와 절벽의 조화가 아름다운 명소입니다.",
        "lat": 33.2373,
        "lon": 126.3139,
        "restaurants": ["용머리해안 인근 해산물 요리 전문 음식점"],
        "hotspots": ["용머리해안 주변 자연 산책로"]
    },
    {
        "name": "서귀포 칠십리 🌊",
        "desc": "절경의 해안 산책로로, 자연과 함께 걷는 힐링 코스로 알려져 있습니다.",
        "lat": 33.2524,
        "lon": 126.5617,
        "restaurants": ["서귀포 칠십리 인근 전통 제주 음식을 제공하는 음식점"],
        "hotspots": ["서귀포 칠십리 주변 자연 경관을 즐길 수 있는 장소들"]
    }
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
        popup=folium.Popup(f"""
            <b>{place["name"]}</b><br>
            <i>{place["desc"]}</i><br><br>
            <b>🍽️ 주변 맛집:</b><br>
            {'<br>'.join(place["restaurants"])}<br><br>
            <b>📸 주변 핫플:</b><br>
            {'<br>'.join(place["hotspots"])}
        """, max_width=300),
        tooltip=place["name"],
        icon=folium.Icon(color="orange", icon="info-sign")
    ).add_to(m)

# 지도 렌더링
st_data = st_folium(m, width=1000, height=600)

# 하단에 리스트 형태로 보기
st.subheader("📍 명소 정보 상세 보기")

for place in jeju_hot_places:
    st.markdown(f"### {place['name']}")
    st.markdown(f"🧭 **역사적 의미:** {place['desc']}")
    st.markdown("🍽️ **추천 맛집:**")
    for restaurant in place["restaurants"]:
        st.markdown(f"- {restaurant}")
    st.markdown("📸 **핫플레이스:**")
    for spot in place["hotspots"]:
        st.markdown(f"- {spot}")
    st.markdown("---")
