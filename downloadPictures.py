import Image, cStringIO, os,re, urllib

def request(context, flow):
  if( re.match(".*(\.gif|\.png|\.jpe?g)", flow.request.path,flags=re.IGNORECASE)):
    	  #f = open('/home/carlos/borrar_log_mitmproxy.txt', 'wa')
	  mydir="/".join(flow.request.path.split("/")[:-1])
	  destdir=flow.request.host+mydir
	  os.system("mkdir -p "+destdir)
	  filename=flow.request.path.split("/")[-1]
	  downloadfile=(destdir+"/"+filename).split("?")[0]
	  downloadurl=downloadfile
	  if(not downloadurl.startswith("http")):
		downloadurl="http://"+downloadurl
	  #f.write("downloading "+downloadfile)
	  urllib.urlretrieve( downloadurl,downloadfile )
