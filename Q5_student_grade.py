print("--  the program to calculate student grades  --")
students = {
    "Ali": 85,
    "Ayesha": 92,
    "Ahmed": 76,
    "Sara": 68,
    "Usman": 55
}

for name, marks in students.items(): #yaha hum ne dictionary ka use kiya hai jisme hum ne student ka name aur marks store kiya hai our for loop ka use karke hum ne name aur marks ko print kar diya hai
# students.items() ka matlab hai k hum ne dictionary ke items ko access kiya hai jisme hum ne name aur marks ko access kiya hai our for loop ka use karke hum ne name aur marks ko print kar diya hai
    if marks >= 90:
        grade = "A"
    elif marks >= 80:
        grade = "B"
    elif marks >= 70:
        grade = "C"
    else:
        grade = "F"

    print(name, "- Marks:", marks, "- Grade:", grade)# name, "- Marks:", marks, "- Grade:", grade // yaha name ka kam hai k hum ne student ka name print kar diya hai our marks ka kam hai k hum ne student ka marks print kar diya hai our grade ka kam hai k hum ne student ka grade print kar diya hai

print("-- The program End --")