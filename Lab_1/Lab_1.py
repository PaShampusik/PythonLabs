import random



print("Hello World")

signs = ["+", "-", "/", "*"]

def calc(a, b, operation):
    if operation == "-":
        return a - b
    elif operation == "+":
        return a + b
    elif operation == "/":
        return a / b
    else:
        return a * b
    
while True:
    try:
        a = float(str(input("Enter the first argument: ")))

        try:                 
            b = float(str(input("Enter second argument: ")))
            operation = input("Enter operation(+, -, /, *): ")

            if operation in signs:
                print(calc(float(a), int(b), operation))
            else:
                print("Wrong input!")
                continue

            answer = input("Wanna calculate more(Y/n)?")
            
            if answer == "Y":
                continue
            else:
                break
        except ValueError:
            print("Wrong input!")
            continue 
    except ValueError:
        print("Wrong input!")
        continue

nums = []

for _ in range(20):
    nums.append(random.randint(0, 100))

print("Not processed list of numbers:", nums)

print("Processed list of nums:", list(filter(lambda num : num % 2 == 0, nums)))

print("Program ended.")
