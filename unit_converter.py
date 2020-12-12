print("Hello! This program converts kilometers into miles.")

while True:
    Km = int(input("Enter the number of kilometers: "))
    Miles = (Km * 1.6)
    print(str(Km) + " kilometers is " + str(Miles) + " miles.")
    additional = input("Would you like to do another conversion? ")
    if additional.lower() != "y" and additional.lower() != "yes":
        print("Thank you for using this converter.")
        break
