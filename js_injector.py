# Usage: mitmdump -s "js_injector.py"
# (this script works best with --anticache)
from bs4 import BeautifulSoup
from libmproxy.protocol.http import decoded

def response(context, flow):
    #if flow.request.host in context.src_url:
        #return # Make sure JS isn't injected to itself
    with decoded(flow.response):  # Remove content encoding (gzip, ...)
        html = BeautifulSoup(flow.response.content,fromEncoding='latin-1')
        #html = BeautifulSoup(flow.response.content)
        if html.body:
            script = html.new_tag( "script", type='application/javascript')
	    script.string="alert(2);"
            html.body.insert(0, script)
            flow.response.content = str(html.prettify('latin-1'))
            context.log("Script injected.")
