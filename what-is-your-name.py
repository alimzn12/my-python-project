# Ask the user for their name
user_name = input("Enter your name: ").strip().lower()

# Set your name here
my_name = "ali"

# Compare names
if user_name == my_name:
    print("Hey! That's my name too!")
else:
    print("Nice to meet you,", user_name)
