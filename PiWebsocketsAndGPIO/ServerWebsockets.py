import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
from PiGPIO import InsAndOuts

PORT=XXXX

class WSHandler(tornado.websocket.WebSocketHandler):

    def open(self):
        self.write_message("Socket Is Open")
        print("Socket is Open")

    def on_message(self, message):
        if "LOW" in message:
            InsAndOuts.resetOutput(23)
            self.write_message("I turned off the light")
            print(message)
        if "HIGH" in message:
            InsAndOuts.setOutput(23)
            self.write_message("I turned on the light")
            print(message)

    def on_close(self):
        print("Socket Is Closed")
        InsAndOuts.resetOutput(23)
        print("I turned off the light")


application = tornado.web.Application([
    (r'/', WSHandler),
])

if __name__ == "__main__":
    InsAndOuts.setupOutputs()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(PORT)
    print("Attempting to open socket")
    tornado.ioloop.IOLoop.instance().start()

