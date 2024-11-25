#This is the shopping cart program

foods = []

prices = []

total = 0

while True:
    food = input("Enter food to buy (q to quit) ")
    if food.lower() == "q":
        break
    else:
        price = int(input(f"Enter price of {food} :$"))
        foods.append(food)
        prices.append(price)

print("-----------------------  Your cart -----------------------")


for food in foods:
    print(food, end="  ")


for price in prices:
    total+=price

print()

print(f"Your total is :$ {total}")

print("-----------------------  Your cart -----------------------")
