# Testing if the user is 18 or older and allowed entry into a party

# ASKING FOR THE USER TO ENTER HIS/HER YEAR OF BIRTH
age = int(input( "Enter the year of your birth :"))
print(age)

current_year = 2023

# TOOK THE CURRENT YEAR MINUS IT WITH AGE 
users_age = current_year - age  
print(users_age )

# USED IF,ELSE,ELIF STAEMENTS 
if users_age >= 18:
    print("You old Enough!")
elif users_age > 16 < 18:
    print("Almost there")
else:
    print("You're just too young!")