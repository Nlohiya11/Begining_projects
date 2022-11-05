print("welcome to our rollercoster")
bill = 0
height = int(input("what is your height?\n "))
if height > 120:
    print("you can ride the rollercoster")
    age = int(input("What is your age?\n"))
    if age <= 12:
        bill += 3
    elif 12 < age <= 18:
        bill += 5
    else:
        bill += 8
    photography = input("Do You want to have a photoshoot? y/n.\n ")
    if photography == "y":
        bill += 3
    else:
        bill += 0
    print(f"your total bill is ${bill}")
else:
    print("You are to small t0 take a ride")
