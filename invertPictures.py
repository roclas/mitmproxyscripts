import Image, cStringIO, os

def response(context, flow):
    if flow.response.headers["content-type"] == ["image/png"] or flow.response.headers["content-type"] == ["image/jpeg"]:
        s = cStringIO.StringIO(flow.response.content)
	s.replace('<body', '<body dir="ltr"')
        img = Image.open(s).rotate(180)
        s2 = cStringIO.StringIO()
        img.save(s2, "png")
        flow.response.content = s2.getvalue()

def request(context, flow):
	f = open('/home/carlos/borrar_log_mitmproxy.txt', 'wa')
    	f.write ("hola "+str(flow.request.host)+"  "+str(flow.request.path))
    	#f.write ("hola "+str(dir(flow.request.path)))
	
	
