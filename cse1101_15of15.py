#OMAR FARUK KHAN
#ID-0182210012101167

time = input("What time is it? ")
h,m = [float(i) for i in time.split(":")]

dtime = h + (m/60)

def next_time(a):
    h1=int(a)
    m1=int((a-int(a))*60)
    return(f"{h1}:{m1}")
    
if dtime>24 or dtime<0:
    print("Sorry!! invalid time. ")
elif  0<dtime<7:
    a = 7-dtime
    print(f"Break fast in {next_time(a)} hours")
elif 8>=dtime>=7:
    print("Breakfast time ")
elif 8<dtime<12:
    a = 12-dtime
    print(f"Lunch time in {next_time(a)} hours ")
elif 13>=dtime>=12:
    print("Lunch time ")
elif 13<dtime<18:
    a = 18-dtime
    print(f"Dinner time in {next_time(a)} hours ")
elif 19>=dtime>=18:
    print("Dinner time ")
elif 19<dtime<=24:
    a = (24-dtime)+7
    print(f"Breakfast in {next_time(a)} hours ")

