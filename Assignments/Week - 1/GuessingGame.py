# Guessing game by Balaji Natarajan
import random

def main():
	# getting a single digit random value
    answer = random.randint(0,9)
    num_of_guess = 0
    print('Answer', answer)
	# Repeat until correct
    while True:
        guess = int(input("Guess the digit: "))
		# correct guess
        if guess == answer:
            print('Your answer is PERFECT!! Congratulations!!')
            num_of_guess += 1
            break
		# low guess value
        elif guess < answer:
            print('Your answer is lower than required')
		# high guess value
        elif guess > answer:
            print('Your answer is higher than required')
        num_of_guess += 1
    print('Number of guesses taken:', num_of_guess)

if __name__ == '__main__':
    main()