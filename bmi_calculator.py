print("------BMI Calculator------")
user_weight = float(input("Enter your weight in kg:"))

# checking valid weight
if user_weight <=0:
    print("Invalid weight. Please entered correct weight.")
    exit()

print("\nSelect height unit:")
print("1 -> Meter")
print("2 -> Feet")
height_choice = int(input("Enter your choice (1 or 2): "))

if height_choice == 1:
    user_height = float(input("Emter your height in meters: "))

    if user_height <=0:
        print("Invalid height. Please entered correct height.")
        exit()

elif height_choice == 2:
    
    height_feet = float(input("Enter height (feet part): "))
    height_inches = float(input("Enter extra inches: "))
    if height_feet <=0 or height_inches <=0:
            print("Invalid height. Please entered correct height.")
            exit()

    # converting feet and inches into meters
    total_inches = (height_feet * 12) + height_inches
    user_height = total_inches * 0.0254

    print("\nYour height in meters is:", round(user_height, 2), "m")

else:
    print("Invalid choice. try again....")
    exit()

# calculating BMI
print("\nCalculating BMI........")
bmi_value = user_weight / (user_height * user_height)
print("\nYour BMI is: ",round(bmi_value,2))

if bmi_value < 18.5:
    print("You are underweight.")

elif bmi_value >= 18.5 and bmi_value < 24.9:
    print("You are normal weight.")

elif bmi_value >= 25 and bmi_value < 30:
    print("You are overweight.")

else:
    print("High BMI detected.")