def show():
    while(True):
        print("this is show")

def disp():
    while(True):
        print("this is disp")


t1=Thread(target=show)
t2=Thread(target=disp)
t1.start()
t2.start()
