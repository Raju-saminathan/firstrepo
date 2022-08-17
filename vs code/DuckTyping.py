class WhatsApp:
    def execute(self):
        print('Texting feature is working fine \n calling also working fine')

class Myapp(WhatsApp):
    def execute(self):
        print('My app have texting feature \n video calling feature \n audio calling feature')
        

class Laptop:
    def code(self,app):
        app.execute()

ap=Myapp()
lap=Laptop()
lap.code(ap)

# ap=WhatsApp()
# lap.code(ap)

