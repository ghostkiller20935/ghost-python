secter_word="kec"     #rec koja treba da se pogodi
guess= ""           #prazan string za kucanje
guess_count = 0 #limit
guess_limit= 3 #max
out_of_guesses = False

while guess != secter_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess= input("enter guess:")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
        print("out of guesses")
else:
        print("u win")