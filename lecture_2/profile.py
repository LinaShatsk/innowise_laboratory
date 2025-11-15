def generate_profile(age):
    life_stage = ''
    if 0 <= age <= 12:
        life_stage = 'Child'
    elif 13 <= age <= 19:
        life_stage = 'Teenager'
    elif age >= 20:
        life_stage = 'Adult'

    return life_stage


user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = 2025-birth_year
stage = generate_profile(current_age)


hobbies = []
while (True):
    key = input("Enter a favorite hobby or type 'stop' to finish: ")
    if key == "stop":
        break
    else:
        hobbies.append(key)


user_profile = {
    'user_name': user_name,
    'current_age': current_age,
    'stage': stage,
    'hobbies': hobbies,
}

print("\n---\nProfile Summary:")
print(f"Name: {user_profile['user_name']}")
print(f"Age: {user_profile['current_age']}")
print(f"Life Stage: {user_profile['stage']}")

if user_profile['hobbies']:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}): ")
    for user_hobby in user_profile['hobbies']:
        print(f"- {user_hobby}")
else:
    print("You didn't mention any hobbies")
