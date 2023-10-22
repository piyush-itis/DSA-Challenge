time=input("Enter time in HHMM format: ")
s=input("Enter AM/PM: ")
f_time=int(time)+1200
time_str2=str(f_time)
if (s=="AM" or s=='am'):
    print(f"Time is {time[0:2]}:{time[2:4]} hrs")
elif (s=="PM" or s=="pm"):
    print(f"Time is {time_str2[0:2]}:{time_str2[2:4]} hrs")
else:
    print("Invalid input")