
numbers = int(input("How many numbers?"))
sum = 0
for i in range(1, numbers+1):
    currentNumber = int(input(f"What is the {i}. number? "))
    sum += int(currentNumber)

print(f"The average is: {round((sum/numbers),2)}")
