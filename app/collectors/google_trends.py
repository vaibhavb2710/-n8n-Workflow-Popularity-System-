from pytrends.request import TrendReq
from pytrends.exceptions import TooManyRequestsError

def fetch_google_trends(keyword="n8n automation"):
    try:
        pytrends = TrendReq(hl="en-US", tz=360)
        pytrends.build_payload([keyword], timeframe="today 3-m")
        data = pytrends.interest_over_time()

        if data.empty:
            return 0

        return int(data[keyword].mean())

    except TooManyRequestsError:
        # Google rate-limited us
        print("Google Trends rate-limited (429). Skipping this run.")
        return 0

    except Exception as e:
        print(f"Google Trends error: {e}")
        return 0
