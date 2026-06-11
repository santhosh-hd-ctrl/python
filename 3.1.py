boy_name = input("boy name: ")
boy_age = int(input("boy age: "))
girl_name = input("girl name: ")
girl_age = int(input("girl age: "))



age_diff = boy_age - girl_age

print("boy = " + boy_name)
print("girl = " + girl_name)
print(boy_name + " loves " + girl_name  + ". Age difference is " + str(age_diff)+" years")
print(f"{boy_name} loves {girl_name}. Age difference is {age_diff} years")