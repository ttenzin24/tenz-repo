x = input("Enter your age:")
print(x)

y = input("Are you a student? (yes/no):")
print(y)

if x <= "12" :
    print("You are eligible for a discount on the movie ticket!")

elif x >= "13"and x <= "18" and y == "yes" :
    print("You are eligible for a discount on movie ticket!")

else:
    print("You are not eligible for a discount on movie ticket!")




