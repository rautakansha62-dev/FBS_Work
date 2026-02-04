#Convert the time entered in hh,min and sec into seconds.
hr=int(input("Enter hours:"))
min=int(input("Enter minutes:"))
sec=int(input("Enter seconds:"))
#hr=1
#print(id(hr))
#min=30
#print(id(min))
#sec=45
#print(id(sec))
#print(id(sec))
total_sec=(hr*3600)+min*60+sec
print(f'total time in sec={total_sec}')