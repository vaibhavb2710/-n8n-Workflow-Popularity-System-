import requests, os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")
BASE_URL = "https://www.googleapis.com/youtube/v3/search"

def fetch_youtube_workflows(query="n8n workflow", max_results=10):
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "maxResults": max_results,
        "key": API_KEY
    }

    search_res = requests.get(BASE_URL, params=params).json()
    video_ids = [item["id"]["videoId"] for item in search_res.get("items", [])]

    stats_url = "https://www.googleapis.com/youtube/v3/videos"
    stats_params = {
        "part": "statistics",
        "id": ",".join(video_ids),
        "key": API_KEY
    }

    stats_res = requests.get(stats_url, params=stats_params).json()
    return stats_res.get("items", [])
