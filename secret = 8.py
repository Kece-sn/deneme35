secret = 8
input_number = int(input("Guess the secret number: "))
if input_number == secret:
    print("Congratulations! You guessed the secret number.")
elif input_number < secret:
    print("Sorry, that's not the secret number. Try a higher number.")
else:
    print("Sorry, that's not the secret number. Try a lower number.")