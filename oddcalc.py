firstnumb = input("Give me a number...")
secondnumb = input("Give me a another number...")
operation = input("And what operation do you want? (mul/div/mod)")

if (operation == "mul"):
    answer = (float(firstnumb) * float(secondnumb)) 
    print(answer)
elif ( operation == "div"):
    answer = (float(firstnumb) / float(secondnumb))
    print(answer)
elif ( operation == "mod"):
    answer = (float(firstnumb) % float(secondnumb))
    print(answer)
else:
    print("INVALID OPERATION")

