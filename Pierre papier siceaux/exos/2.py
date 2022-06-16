import time

#while x=0:
times=int(input("Timer : "))
while times:
    sec=times%60
    min=times//60
    hour=min//60
    

    leformat='{:02d}:{:02d}:{:02d}'.format(hour,min,sec)
    print(leformat,end="\r")
    time.sleep(1)
    times-=1

print("Au revoir")