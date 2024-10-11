# import time
# timestamp=time.strftime('%H:%M:%S')
# print(timestamp)
# hours=time.strftime('%H')
# print(hours)
# timestamp=time.strftime('%M')
# print(timestamp)
# timestamp=time.strftime('%S')
# print(timestamp)
# if(hours>0 and hours<12):
#     print("good morning sir")
# elif(hours>12 and hours<17):
#     print("good afternoon sir")
# elif(hours>17 and hours<0):
#     print("good night sir")
import time
t=time.strftime('%H:%M:%S')
h=int(time.strftime('%H'))
print(h)
if(h>=0 and h<12):
    print("good morning sir")
elif(h>=12 and h<17):
    print("good afternoon sir")
if(h>=17 and h<24):
    print("good night sir")

                        