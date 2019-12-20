#mitmproxy -p 8000 -s logimages.py --view-filter "~s .*.png$"
f= open("/tmp/pngs.txt","w+")
def response(flow):
    if flow.response.headers.get("content-type", "").startswith("image"):
        f.write(flow.request.url+"\n")
        #img = open("gavin.jpeg", "rb").read()
        #flow.response.content = img
        #flow.response.headers["content-type"] = "image/jpeg"
