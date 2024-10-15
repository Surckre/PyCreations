print("Surckre´s Shop\n")
print("(1) Coca Cola: 1.49")
print("(2) Chocolate: 1.99")
print("(3) USB-Stick: 12.99")

chose = input("\nWhat u want to buy: ")

if chose == '1':
    print("Its 1.49")
elif chose == '2':
    print("Its 1.99")
elif chose == '3':
    print("Its 12.99")
else :
    print(f"The item #{chose} is not valid")

