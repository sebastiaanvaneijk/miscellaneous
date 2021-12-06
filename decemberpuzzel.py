# Gegeven is: KERST + BOMEN = MTEXH
# A. Welke twee figuren komen in botsing als XGEEBYM de uitkomst is?
# B. Wat zijn de originele platen bij de mash-up PFKCTKKPPTVXUGLLVYCHNBXG?

import numpy as np

def guess_word(guess, input_string):
    if len(guess) != len(input_string):
        print('Words not of equal length.')
        return

    input_string = np.array([ord(i)-64 for i in input_string])
    guess = np.array([ord(j)-64 for j in guess])

    output = input_string - guess
    output = np.array([i+26 if i < 0 else i for i in output])
    output = [chr(i+64) for i in list(output)]
    output = "".join(output)

    return output


def find_combinations(input_letter):
    all_letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    combos = []
    for q, i in enumerate(all_letters):
        for p, j in enumerate(all_letters[q+1:]):
            if ord(i)-64 + ord(j)-64 == ord(input_letter)-64 or ord(i)-64 + ord(j)-64 == ord(input_letter)-64+26:
                combos.append([i, j])
    return combos

q0 = "MTEXH"
q1 = "XGEEBYM"
q2 = "PFKCTKKPPTVXUGLLVYCHNBXG"

input_string = q1
guess = ""
answer = guess_word(guess=guess, input_string=input_string)
print(f"{guess} + {answer} = {input_string}")

input_string = q2
guess = "SANTACLAUSISCOMINGTOTOWN"
answer = guess_word(guess=guess, input_string=input_string)
print(f"{guess} + {answer} = {input_string}")

