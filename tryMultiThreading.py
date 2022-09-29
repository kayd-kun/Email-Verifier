import threading
import time

class NoMulti:

    def doSth(self):
        time.sleep(2)
        print('Did Somthing')
    
    def __init__(self):
        self.doSth()

class YesMulti:

    def doSth(self):
        time.sleep(2)
        print('Did Somethign')
        
    
    def __init__(self):
        t = threading.Thread(target=self.doSth)
        t.start()


NoMulti()
NoMulti()
NoMulti()
NoMulti()

YesMulti()
YesMulti()
YesMulti()
YesMulti()



