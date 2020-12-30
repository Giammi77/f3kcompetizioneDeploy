import time

def countDown(timeCountDown):

    while timeCountDown[0] != 0:
        now=time.time() 
        future=now+1    
        while now<future:
            now=time.time() 
        
        timeCountDown[0]=timeCountDown[0]-1
        
# timeCountDown=[10]
# x = threading.Thread(target=countDown, args=(timeCountDown,))
# x.start()
# while timeCountDown[0]!=0:
#     print(timeCountDown)
# x.join()
# print(timeCountDown)
