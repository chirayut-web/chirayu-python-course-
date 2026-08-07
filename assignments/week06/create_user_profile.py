def create_user_profile(username, age, premium = False):

    user_type = "standard_user"

    if premium == True:
        user_type = "premium_user"

    user_profile = (f"[{username}] (age: [{age}]) - [{user_type}]")
    return user_profile



print(create_user_profile("Bonchoo",41))
print(create_user_profile("Yang",19))
print(create_user_profile("Poom",22,True))