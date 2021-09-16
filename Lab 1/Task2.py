name = input("What's your name?")
numCookies = int(input("How many cookies?"))

if numCookies < 10:
    print("Sure it's enough?")
elif numCookies < 20:
    print("Cookies er delic")
elif numCookies < 51:
    print("Careful!")
else:
    print("something is wrong, here take 10 cookies")
    numCookies = 10


print(f"Hi {name} here are your cookies:", "cookie " * numCookies)
