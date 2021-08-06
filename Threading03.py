from threading import *
def check():
    num=int(input("enter num:"))
    if(num%2==0):
        print(num,"is even")
    else:
        print(num," is odd")


def copy_paste():
    import shutil
    shutil.copy("d:/msg.txt","msg.txt")

t1=Thread(target=check, name="Thread_01")
t2=Thread(target=copy_paste, name="Thread_02")
t1.start()
t2.start()
