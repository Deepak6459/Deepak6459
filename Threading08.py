from threading import *
import time
lk=Lock()
def platform():
    lk.acquire()
    n=current_thread().getName()
    print(f"{n} is arriving on platform")
    print(f"{n} is on platform")
    time.sleep(2)
    print(f"{n} is going to leave platform")
    print(f"{n} has left")
    lk.release()


t1=Thread(target=platform,name="rajdhani")
t2=Thread(target=platform,name="shatabdi")
t1.start()
t2.start()
          
