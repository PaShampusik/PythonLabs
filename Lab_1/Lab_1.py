import random


#first part of the program

print("Hello World")

signs = { "*" : ["multy", "mul", "*", "m"], "/" : ["div", "divide", "d", "/"], "+" : ["addition", "add", "+", "a"], "-" : ["sub", "substraction", "-", "s"]}

#second part of the program

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
            operation = input("Enter odoperation(+, -, /, *): ")

            done = False
            for key, value in signs.items():
                if operation in value:
                    print(calc(float(a), int(b), key))
                    done = True
            if done == False:
                print("Wrong input!")
                

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


#third part of the program

nums = []

for _ in range(20):
    nums.append(random.randint(0, 100))

print("Not processed list of numbers:", nums)

print("Processed list of nums:", list(filter(lambda num : num % 2 == 0, nums)))

print("Program ended.")
