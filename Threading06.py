from threading import *
#import time
def platform():
    n=current_thread().getName()
    print(f"{n} is arriving on platform")
    print(f"{n} is on platform")
    print(f"{n} is going to leave platform")
    print(f"{n} has left")


t1=Thread(target=platform,name="rajdhani")
t2=Thread(target=platform,name="shatabdi")
t1.start()
t2.start()
          
