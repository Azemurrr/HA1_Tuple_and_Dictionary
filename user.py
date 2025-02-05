user_info = {}
user_info["name"] = input("What is the user's name? ")
user_info["age"] = int(input("What is the user's age? "))
user_info["country_of_birth"] = input("What is the user's country of birth? ")
user_info["known_for"] = input("What is the user known for? ")

print(f'"{user_info["name"]}"')
print(f'"{user_info["age"]}"')
print(f'"{user_info["country_of_birth"]}"')
print(f'"{user_info["known_for"]}"')
