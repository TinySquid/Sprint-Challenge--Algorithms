"""
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
"""


def count_th(word, i=0):
    repititions = 0

    # Base case when we have run out of letters to check for patterns
    if i > len(word) - 2:
        return 0

    # If we find occurrence of "th", inc repititions
    if word[i] + word[i + 1] == "th":
        repititions += 1

    # Return our result of THIS call, and then recursively continue until we hit end of the word
    return repititions + count_th(word, i + 1)


# print(count_th("that is the way of the worm"))
