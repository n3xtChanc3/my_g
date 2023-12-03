import secrets

def generate_secret_number(min_value, max_value):
	return secrets.randbelow(max_value - min_value + 1) + min_value

def get_user_input(min_value, max_value):
	return int(input(f"Enter a number between {min_value} and {max_value} : "))

def evaluate_guess(secret, guess, attempt):
	if guess > secret:
		print("It should be smaller. Try to guess again!")
	elif guess < secret:
		print("it should be bigger. Try to guess again!")
	else:
		print(f"Bingo! {attempt} attempt(s)")

def play_guessing_game():
	MIN = 0
	MAX = 100

	secret_number = generate_secret_number(MIN, MAX)
	attempt = 0

	input_number = get_user_input(MIN, MAX)
	attempt += 1

	evaluate_guess(secret_number, input_number, attempt)

	while input_number != secret_number:
		input_number = get_user_input(MIN, MAX)
		attempt += 1
		evaluate_guess(secret_number, input_number, attempt)


# Call the function to start the game
play_guessing_game()
