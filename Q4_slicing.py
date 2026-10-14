# this is the the code for slicing
print("--  the program to slice the name  --")
name = input("Enter your complete name : ")
name_part = name.split(" ")# is ka matlab hai k yahaan pe hum ne name ko space k hisaab se split kar diya hai
print("Your name is : ", name_part[0])# yahaan print ho ga k user ka fist ka name kya hai ya is wajah se hum ne name ko split kar diya hai aur us ka first part print kar diya hai our 0 yaha per represent karta hai k hum ne first part ko print kiya hai
print("Your last name is : ", name_part[-1])# yahaan print ho ga k user ka last name kya hai is ka matlab hai k hum ne name ko split kar diya hai aur us ka last part print kar diya hai our -1 yaha per represent karta hai k hum ne last part ko print kiya hai

print("initials of your name is : ", name_part[0].upper()+ "." + name_part[0].upper())# ab 0 upper ka matlab hai k hum ne first part ko upper case me convert kar diya hai our . ka matlab hai k hum ne first part ke baad dot laga diya hai our last part ko upper case me convert kar diya hai
print("Uppercase name:", name.upper())# yahaan print ho ga k user ka name upper case me kya hai
print("Reversed name:", name[::-1])# yahaan print ho ga k user ka name reverse me kya hai our :: ka use tab hota hai jab hum ne name ko reverse kar diya hai our -1 ka matlab hai k hum ne name ko reverse kar diya hai
print("-- The program End --")