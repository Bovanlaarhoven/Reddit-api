import requests
import json

link = "https://reddit.com"

def get_subreddit(subreddit="memes", limit=10, sort="hot", type="json", comments=False, username=False, post_link=False, upvotes=True):
    url = f"{link}/r/{subreddit}/{sort}.json?limit={limit}"
    response = requests.get(url, headers={"User-agent": "RedAPI"})
    
    post_data_list = []

    if response.status_code == 200:
        children_data = response.json()["data"]["children"]

        for child in children_data:
            data = child["data"]
            post_link = f"{link}{data['permalink']}"
            post_info = {}
            
            if comments:
                comments_url = f"{link}{data['permalink']}.json"
                comments_response = requests.get(comments_url, headers={"User-agent": "RedAPI"})
                if comments_response.status_code == 200:
                    comments_data = comments_response.json()[1]["data"]["children"]
                    comments_list = [{"body": comment["data"]["body"], "author": comment["data"]["author"], "score": comment["data"]["score"]} for comment in comments_data]
                    post_info["comments"] = json.dumps(comments_list)

            if post_link:
                post_info["post_link"] = post_link
            if username:
                post_info["username"] = data["author"]
            if upvotes:
                post_info["upvotes"] = data["ups"]
            if type.lower() == "json":
                post_info["data"] = response.json()
            elif type.lower() == "text":
                post_info["data"] = response.text
            elif type.lower() == "title":
                post_info["title"] = data["title"]
            
            post_data_list.append(post_info)

    result_json = json.dumps(post_data_list, indent=2)

    return result_json
