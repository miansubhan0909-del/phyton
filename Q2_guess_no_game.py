#code to guess the number 
print("--  the program to guess the secreat number  --")
guess_no = 42
attamp=0
while attamp < 5:
    guess = int (input(" guess a number between 1 to 100 : "))
    if guess < 1 or guess > 100:
     print("Invalid NO")
     continue
    attamp = attamp + 1
    if guess == guess_no:
      print("Congratulation you guess the secreat number")
      break
    else:
      print("Sorry you guess the wrong number")
else:
    print("You have used all your attempts. The secreat number was", guess_no)
print("-- The prpgram End --")