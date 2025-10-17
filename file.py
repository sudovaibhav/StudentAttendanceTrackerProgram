class_held = int(input("Enter number of classes held: "))
class_attended = int(input("Enter number of classes attended: "))
percentage_attendence = ((class_held/class_attended) * 100)
print(f"Classes Held = {class_held} \nClasses attended = {class_attended}\n Percentage of classes attended = {percentage_attendence}%")

if (percentage_attendence >= 75):
    print("Student is eligible to write exam.")
else: 
    print("Student is not eligible to write exam.")