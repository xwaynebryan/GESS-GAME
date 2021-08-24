#my guessing game

def main():
    secret_word = "Bryan"
    guess = ""
    count_limit = 3
    guess_count = 0
    out_of_guesses = False
    while guess != secret_word and not out_of_guesses:
        if guess_count < count_limit:
            guess = input("Enter a guess: ")
            guess_count += 1
        else:
            out_of_guesses = True
    if out_of_guesses:
        print("Out of guesses, YOU LOOSE!")

        print("Would you like to try again? ")
        answer = input("yes/no: ")
        if answer == "yes":
            main()
        else:
            print("GOODBYE!")
    else:
        print("YOU WIN!")
        print("Would you like to try again? ")
        answer = input("yes/no: ")
        if answer == "yes":
            main()
        else:
            print("GOODBYE!")
main()







































































































