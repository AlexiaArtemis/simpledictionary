# Simple Dictionary

---

This Simple Dictionary is a dictionary in which the user can search for the definition of a word.

It uses a data file that contais a vocabluary. This data file is from the Udemy course ["The Python Mega Course"](https://www.udemy.com/course/the-python-mega-course/) by ["Ardit Sulce"](https://www.udemy.com/user/adiune/).

## Installation

---

You can install the Simple Dictionary from [PyPI](https://pypi.org/project/simple-dictionary/)

```
pip install simple-dictionary
```

The dictionary is supported on Python 3.5 and above.

## How to use

---

The Simple Dictionary is a command line application, named `dictionary`. To see the definition of a word, for example _acid rain_, simple call the program:

```
$ dictionary acid rain
acid rain  means:
1. definition: Rain having a pH less than 5.6.
```

If there is a typo in the name, the program will find a similar word and ask you if you want to use this similar word. For yes press `y` and for no press `n`.

```
$ dictionary acid rainn
Did you mean acid rain ? y
acid rain  means:
1. definition: Rain having a pH less than 5.6.
```
