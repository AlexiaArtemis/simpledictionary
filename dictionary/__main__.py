import sys

from dictionary import app


def main():
    input_word = sys.argv

    try:
        if len(sys.argv[1:]) > 1:
            word = ""
            for i in (1, len(sys.argv[1:])):
                word = word + str(input_word[i]) + " "
            word = word[:-1]
        else:
            word = str(input_word[1])

        app.translate(word)

    except:
        print("Please enter the word that you want to search for.")


if __name__ == "__main__":
    main()
