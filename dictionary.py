#dictionary is a collection of key-value pairs. Each key is unique, and it is used to access the corresponding value. Dictionaries are defined using curly braces {}.

student = {
    "name": "Subhan",
    "age": 20,
    "course": "BSIT"
}

print(student["name"])# is sa yahaan print ho ga k student ka name kya hai

student["age"] = 21
student["city"] = "Sheikhupura"

print(student)

del student["city"]
print(student)#yaha yahaan print ho ga k student ka city name delete ho
#ok