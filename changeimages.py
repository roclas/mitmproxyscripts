#mitmproxy -p 8000 -s changeimages.py --view-filter "~s .*.png$"
def response(flow):
    if flow.response.headers.get("content-type", "").startswith("image"):
        img = open("gavin.jpeg", "rb").read()
        flow.response.content = img
        flow.response.headers["content-type"] = "image/jpeg"
