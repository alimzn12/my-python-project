my_fav_num=[1,2,3,4,5]
print(f' my fav numbers are {my_fav_num}')
#add the two numbers 
my_fav_num.extend([6,7])
# print the list after update
print(f' my fav numbers are after update {my_fav_num}')

# creat my frend's list fav numbers 
friend_fav_numbers=[4,5,6,7,8,9]
print(f" my freind's favorite numbers are {friend_fav_numbers}")
#  CREAT OUR FAV NUMBERS 
OUR_FAV_NUM =list(set(my_fav_num + friend_fav_numbers))
print(f"our fav numbvers are {OUR_FAV_NUM}")
# 2nd methode for combine the two list without repeatation
combined = my_fav_num.copy()
for item in friend_fav_numbers :
    if item not in combined :
        combined.append(item)
print(f"our fav numbvers are {combined}")