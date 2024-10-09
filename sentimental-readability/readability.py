from cs50 import get_string


def main():

    text = get_string("Text: ")
    g = grade(text)

    if g < 1:
        print("Before Grade 1\n")
    elif g >= 1 and g < 16:
        print(f"Grade {g}")
    elif g >= 16:
        print("Grade 16+\n")


def grade(s):

    letter = 0
    space = 0
    punctuation = 0

    for i in range(len(s)):

        if s[i].isalpha():
            letter += 1
        elif s[i] == " ":
            space += 1
        elif s[i] in [".", "!", "?"]:
            punctuation += 1

    words = space + 1
    L = (letter / words) * 100
    S = (punctuation / words) * 100
    index = 0.0588 * L - 0.296 * S - 15.8
    g = round(index)
    return g


main()
