#!/usr/bin/env python
# Copyright 2009 Facebook
#

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import logging
import sys
import os
import simplejson

class FileUploadService(tornado.web.RequestHandler):
    def set_default_headers(self):
            print "setting headers!!!"
            self.set_header("Access-Control-Allow-Origin", "*")
            self.set_header("Access-Control-Allow-Headers", "x-requested-with")
            self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    def options(self):
        pass

    def get(self):
        self.write('please upload a image url')

    def post(self):
        result = {}
        result['flag'] = 0
        result['msg'] = ''
        try:
            meta = self.request.files['file'][0]
            # suffix = meta['filename'].split('.')[-1]
            filename = meta['filename']
            while os.path.exists(filename):
                logging.info('已经存在文件：' + filename)
            f = open(filename, 'wb')
            f.write(meta['body'])
            f.close()
            result['flag'] = 1
        except Exception, e:
            logging.info('Error: upload image failing,%s' % str(e))
            result['flag'] = 0
            result['msg'] = 'fail in upload image'
            self.write(simplejson.dumps(result))
            return
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(simplejson.dumps(result))


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                        (r"/upload", UploadImageHandler),
                    ]
        tornado.web.Application.__init__(self, handlers)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    port = 8889
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    http_server.listen(port)
    loop = tornado.ioloop.IOLoop.instance()
    logging.info('File Server running on http://127.0.0.1:%d' % port)
    loop.start()
