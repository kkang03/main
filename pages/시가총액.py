import streamlit as st
import yfinance as yf
import plotly.express as px

# 기업 목록과 티커
companies = {
    'Microsoft': 'MSFT',
    'Apple': 'AAPL',
    'Nvidia': 'NVDA',
    'Alphabet (Google)': 'GOOGL',
    'Meta Platforms': 'META'
}

# 기업 시가총액 데이터 (단위: 조 달러)
market_caps = {
    'Microsoft': 2.79,
    'Apple': 3.08,
    'Nvidia': 2.79,
    'Alphabet (Google)': 1.88,
    'Meta Platforms': 1.46
}

# 시가총액을 데이터프레임으로 변환
df = pd.DataFrame(list(market_caps.items()), columns=['Company', 'Market Cap'])

# Plotly로 시각화
fig = px.bar(df, x='Company', y='Market Cap',
             title='Top 5 AI Companies by Market Capitalization (2025)',
             labels={'Market Cap': 'Market Capitalization (Trillions USD)'},
             color='Market Cap',
             color_continuous_scale='Viridis')

# Streamlit 대시보드 설정
st.title('AI 분야 유망 기업 시가총액 시각화')
st.write('2025년 기준으로 AI 분야에서 가장 유망한 기업 5곳의 시가총액을 시각화한 결과입니다.')
st.plotly_chart(fig)
