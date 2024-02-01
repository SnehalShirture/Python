is_male = False
is_tall = True

if is_male or is_tall:
    print("Your are Male or tall or  both ")
else:
    print("Your are neither Male nor tall")

if is_male and is_tall:
    print("Your are Male or tall or  both ")
elif is_male and not (is_tall):
    print("You are a short male")

elif not (is_male) and  is_tall:
    print("You are a not a male but are tall ")

else:
    print("Your are either not Male or not a tall or both")