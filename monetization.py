import json
with open("config/config.json") as f:
    config = json.load(f)

def get_tools_message():
    links = config["affiliate_links"]
    return f"ChatGPT: {links['chatgpt']}\nCanva: {links['canva']}\nMidjourney: {links['midjourney']}"
