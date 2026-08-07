def create_user_profile(username, age, premium):
    user_profile = (f"[{username}] (age: [{age}]) - [{premium}]")
    return user_profile



print(create_user_profile("Bonchoo",41,"premium User"))
print(create_user_profile("Yang",19,"Standard User"))
print(create_user_profile("Poom",22,"Standard User"))