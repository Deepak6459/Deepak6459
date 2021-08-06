
def check():
    num=int(input("enter num:"))
    if(num%2==0):
        print(num,"is even")
    else:
        print(num," is odd")


def copy_paste():
    import shutil
    shutil.copy("d:/msg.txt","msg.txt")

check()
copy_paste()
    
