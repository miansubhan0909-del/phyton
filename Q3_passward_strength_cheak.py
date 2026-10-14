# the program to cheak the streanth the of the passward
print("--  the program to cheak the streanth the of the passward --")
password = input("Enter the passward")
if len(password) >= 8 and password.isupper() == False and password.islower() == False and any(char.isdigit() for char in password):
    print("Strong Password")
elif len(password) >= 6:
    print("Password is medium type")
else:
    print(" Password is weak")
print("-- The prpgram End --")


