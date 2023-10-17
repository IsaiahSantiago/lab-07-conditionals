import datetime
now = datetime.datetime.now()
print(now.hour)

if 0 <= now.hour < 5:
    answer = ("It's early. You should be sleeping!")
elif 5 <= now.hour < 7:
   answer = "Wake up, brew that coffee, get that mile run in, and get that breakfast…"
elif 7 <= now.hour < 9:
    answer = "Time to go to work"
elif 9 <= now.hour < 12:
   answer = "You should be working!"
elif 12 <= now.hour < 13:
    answer = "Take your lunch break!"
elif 13 <= now.hour < 17:
   answer = "Do you feel that afternoon lull?"
elif 17 <= now.hour < 19:
    answer = "Time to hit the gym…"
elif 19 <= now.hour < 21:
   answer = "Gotta eat that dinner."
elif 21 <= now.hour < 23:
    answer = "Get that SLEEP. And rePEAT!"
elif 23 <= now.hour < 100:
   answer = "You didn't type an acceptable value! (0-23)"

print(answer)
