import yfinance as yf
import pandas as pd
import datetime

# 시가총액 상위 10개 기업 (티커 기준, 2025년 기준 예상)
tickers = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Saudi Aramco': '2222.SR',
    'Alphabet': 'GOOGL',
    'Amazon': 'AMZN',
    'Nvidia': 'NVDA',
    'Berkshire Hathaway': 'BRK-B',
    'Meta': 'META',
    'TSMC': 'TSM',
    'Tesla': 'TSLA'
}

# 데이터 가져올 기간: 최근 3년
end_date = datetime.datetime.today()
start_date = end_date - datetime.timedelta(days=3*365)

# 빈 데이터프레임 생성
market_caps = pd.DataFrame()

for name, ticker in tickers.items():
    stock = yf.Ticker(ticker)
    # 주가 정보 (주 1회로 간단화)
    hist = stock.history(start=start_date, end=end_date, interval='1wk')
    
    # 발행 주식 수 (Shares Outstanding) - 최신값 기준
    shares_outstanding = stock.info.get("sharesOutstanding", None)
    
    if shares_outstanding is None:
        print(f"{name} ({ticker}) - 발행주식 수 정보 없음")
        continue

    # 시가총액 계산: 주가 * 주식 수
    hist['Market Cap'] = hist['Close'] * shares_outstanding
    market_caps[name] = hist['Market Cap']

# 결과 확인
print(market_caps.tail())

# 그래프 그리기 (선택)
import matplotlib.pyplot as plt

market_caps.plot(figsize=(15, 7), title="Top 10 기업 시가총액 (3년 간 추이)")
plt.ylabel("Market Cap (USD)")
plt.xlabel("Date")
plt.grid(True)
plt.tight_layout()
plt.show()
