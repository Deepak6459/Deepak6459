from threading import *
class mythread(Thread):
    def run(self):
        print("a")
        print("b")
        print("c")
        print("d")


class ourthread(Thread):
    def run(self):
        print("1")
        print("2")
        print("3")
        print("4")

t1=mythread()
t2=ourthread()
t1.start()
t2.start()
