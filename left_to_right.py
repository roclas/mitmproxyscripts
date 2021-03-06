#!/usr/bin/env python
"""
    Zap encoding in requests and inject iframe after body tag in html responses.
    Usage:
        iframe_injector http://someurl/somefile.html
"""
from libmproxy import controller, proxy
import os
import sys


class InjectingMaster(controller.Master):
    def __init__(self, server, iframe_url):
        controller.Master.__init__(self, server)
        self._iframe_url = iframe_url

    def run(self):
        try:
            return controller.Master.run(self)
        except KeyboardInterrupt:
            self.shutdown()

    def handle_request(self, msg):
        if 'Accept-Encoding' in msg.headers:
            msg.headers["Accept-Encoding"] = 'none'
        msg.reply()

    def handle_response(self, msg):
        if msg.content:
            c = msg.replace('<body', '<body dir="ltr"')
            if c > 0:
                print 'Iframe injected!'
        msg.reply()


def main(argv):
    if len(argv) != 2:
        print "Usage: %s IFRAME_URL" % argv[0]
        sys.exit(1)
    iframe_url = argv[1]
    config = proxy.ProxyConfig(
        cacert = os.path.expanduser("~/.mitmproxy/mitmproxy-ca.pem")
    )
    server = proxy.ProxyServer(config, 8080)
    print 'Starting proxy...'
    m = InjectingMaster(server, iframe_url)
    m.run()

if __name__ == '__main__':
    main(sys.argv)
