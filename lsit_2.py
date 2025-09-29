sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
sandwich_orders.remove("Pastrami sandwich")
finished_sandwiches =[]
for item in sandwich_orders :
    finished_sandwiches.append(item)
    sandwich_orders.remove(item)
    print(f"I made your {item}")