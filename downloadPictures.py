#mitmproxy -p 8000 -s logimages.py --view-filter "~s .*.png$"
import os,re, urllib
import urllib.request
f= open("/tmp/pngs.txt","w+")

def downloadfile(url,path):
    myfile = open(path, 'wb')
    response = urllib.request.urlopen(url)
    myfile.write(response.read())
    myfile.close()

def response(flow):
    if flow.response.headers.get("content-type", "").startswith("image"):
        mydir="/tmp/proxied_files/".join(flow.request.path.split("/")[:-1])
        destdir=mydir+flow.request.host
        os.system("mkdir -p "+destdir)
        filename=flow.request.path.split("/")[-1]
        path=(destdir+"/"+filename).split("?")[0]
        downloadurl=flow.request.url
        if(not downloadurl.startswith("http")):
            downloadurl="http:/"+downloadurl
        f.write("%s -> %s\n"%(downloadurl,path))
        downloadfile( downloadurl,path)
