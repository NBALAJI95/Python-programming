import random

def main():
    answer = random.randint(0,9)
    num_of_guess = 0
    print('Answer', answer)
    while True:
        guess = int(input("Guess the digit: "))
        if guess == answer:
            print('Your answer is PERFECT!! Congratulations!!')
            num_of_guess += 1
            break
        elif guess < answer:
            print('Your answer is lower than required')
        elif guess > answer:
            print('Your answer is higher than required')
        num_of_guess += 1
    print('Number of guesses taken:', num_of_guess)

if __name__ == '__main__':
    main()