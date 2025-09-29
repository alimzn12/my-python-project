basket = ["Banana", "Apples", "Oranges", "Blueberries"]# first version of our list 
basket.remove("Banana")
basket.remove("Blueberries")
# after rm some elemnts
print(f" list after update {basket}")
basket.append("Kiwi")
basket.append("Apples")
# After add some items
print(f" list after update {basket}")
# how many items do we have in the list 
lenth = len(basket)
print(f"the lenth of our lsit is {lenth}" )
basket.clear
print(f"basket : {basket}")