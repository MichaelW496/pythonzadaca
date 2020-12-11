print("Hello! This program converts kilometers into miles.")


while True:
    Km = int(input("Enter the number of kilometers: "))
    Miles = (Km * 1.6)
    print(str(Km) + " kilometers is " + str(Miles) + " miles")
    additional = input("Would you like another query (y/n): ")
    if additional != "y":
        break
