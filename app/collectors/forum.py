import requests

BASE_URL = "https://community.n8n.io/latest.json"

def fetch_forum_workflows():
    res = requests.get(BASE_URL).json()
    topics = res["topic_list"]["topics"]

    workflows = []
    for t in topics:
        workflows.append({
            "name": t["title"],
            "replies": t["reply_count"],
            "likes": t["like_count"],
            "views": t["views"]
        })
    return workflows
