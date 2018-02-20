# create a game the guesses users secret number using bisection search

input("Please think of a number between 0 and 100!")
low = 0
high = 100
solved = False
while not solved:
  guess = (high+low)//2
  print('Is your secret number ' + str(guess) + '?')
  response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly." )
  if response == 'c':
    solved = True
  elif response == 'l':
    low = guess
  elif response == 'h':
    high = guess
  else:
    print('Sorry, I did not understand your input.')

print('Game over. Your secret number was: ' + str(guess))