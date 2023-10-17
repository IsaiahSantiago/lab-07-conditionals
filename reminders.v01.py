time = float(input("What is the current hour (in military time)"))

if 0 <= time < 5:
    answer = ("It's early. You should be sleeping!")
elif 5 <= time < 7:
   answer = "Wake up, brew that coffee, get that mile run in, and get that breakfast…"
elif 7 <= time < 9:
    answer = "Time to go to work"
elif 9 <= time < 12:
   answer = "You should be working!"
elif 12 <= time < 13:
    answer = "Take your lunch break!"
elif 13 <= time < 17:
   answer = "Do you feel that afternoon lull?"
elif 17 <= time < 19:
    answer = "Time to hit the gym…"
elif 19 <= time < 21:
   answer = "Gotta eat that dinner."
elif 21 <= time < 23:
    answer = "Get that SLEEP. And rePEAT!"
elif 23 <= time < 100:
   answer = "You didn't type an acceptable value! (0-23)"

print(answer)







