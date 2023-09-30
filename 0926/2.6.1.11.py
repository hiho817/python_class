hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

time = hour*60+mins+dura
hour = time // 60
mins = time % 60
hour = hour-24 if hour > 24 else hour

print(hour, ':', mins, sep="")
