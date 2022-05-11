from random import randint


def guess_processor(actual_number, guess_number):
    if actual_number == guess_number:
        return "Correct"
    elif actual_number > guess_number:
        return "Higher"
    else:
        return "Lower"


def create_number():
    return randint(1, 100)


def make_guess():
    guess = input("Enter a number from 1 to 100: ")
    return int(guess)


if __name__ == "__main__":
    result = None
    number = create_number()
    attempts = 0
    while attempts < 10:
        attempts += 1
        guess = make_guess()
        result = guess_processor(number, guess)
        print(result)
        if result == "Correct":
            break
    if result == "Correct":
        print("You won")

    print("Computer number:", number)
    print("Your last guess:", guess)
