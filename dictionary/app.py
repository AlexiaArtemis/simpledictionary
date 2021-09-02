import json
import difflib
import importlib.resources

with importlib.resources.open_text("dictionary", "data.json") as file:
    data = json.load(file)


def pretty(word, definition):
    print(word, " means:")
    for i in range(len(definition)):
        print(f"{i+1}. definition: {definition[i]} \n")


def translate(word):

    if word.lower() in data:
        return pretty(word.lower(), data[word.lower()])

    elif word.title() in data:
        return pretty(word.title(), data[word.title()])

    elif word.upper() in data:
        return pretty(word.upper(), data[word.upper()])

    elif difflib.get_close_matches(word, data.keys(), cutoff=0.8) and (
        difflib.get_close_matches(word, data.keys(), cutoff=0.8)[0] in data.keys()
    ):

        new_word = difflib.get_close_matches(word, data.keys(), cutoff=0.8)

        answer = input(f"Did you mean {new_word[0]}? ") == "y"
        print()

        if answer:
            return pretty(new_word[0], data[new_word[0]])
        else:
            return print("Sorry, your word is not in the dictionary. \n")

    else:
        return print("Sorry, your word is not in the dictionary. \n")
