print("Welcome to FizzBuzz!")

game = input("Please enter a number (1-100): ")
game = int(game)

for num in range(1, game+1):
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
