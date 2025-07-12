import random

print("The Colatz Game")
print("READ about Rule.txt to know the rules")

step = random.randint(1, 100)
result = step % 2
if result == 0:
    result = step // 2
else:
    result = step * 3 + 1

for i in range(3):
    try:
        answer = int(input(f"I put some Positive Number, and it became {result}. What was it first?"))
        if answer == step:
            print("congratulations! You got it right")
            break
        elif answer < step:
            print("The Correct Answer is bigger than this")
        else:
            print("The Correct Answer is smaller than this.")
    except ValueError:
        print("You should Input Integer. Not Floating or Strings.")

print(f"The Correct Answer was {step}")
