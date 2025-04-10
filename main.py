import random
print("Task 1")
money = int(input("Enter start money "))
perc = int(input("Enter percentage "))
fin = int(input("Enter final money "))
years = 0
while money < fin:
    money=money+(money*(perc/100))
    years+=1
    print(years,money)
print("It takes",years,"years to get", fin)
print("----------------------------------")
print("Task 2")
numb = random.randint(1,100)
for i in range(7):
    guess = int(input("Your guess: "))
    if guess == numb:
        print("You guessed after",i+1,"attempts")
        break
    if guess > numb:
        print("Smaller")
    else:
        print("Bigger")
if guess!=numb:
    print("Correct number was:",numb)
print("----------------------------------")
print("Task 3")
lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
for num in range(lower, upper + 1):
    if num > 1:
        x = True
        for i in range(2, num):
            if num % i == 0:
                x = False
                break
        if x:
            print(num)
print("----------------------------------")
print("Task 4")
while True:
    try:
        numb = int(input("Enter a number "))
        if numb < 0:
            raise ValueError
        break
    except ValueError:
        print("Don`t enter negative numbers or letters")
fact = 1
numb = int(numb)
while numb > 1:
    fact*=numb
    numb-=1
print(fact)
