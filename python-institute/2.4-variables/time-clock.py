hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

new_hour = (hour + (mins+dura)//60) % 24
new_mins = (mins+dura)%60

print("new_hour:",new_hour)
print("new_mins:",new_mins)