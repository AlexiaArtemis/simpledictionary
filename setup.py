import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="simple-dictionary",
    version="0.1.3",
    description="Read the definition of a word",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/AlexiaArtemis/simpledictionary",
    author="Alexia Artemis Baikas",
    author_email="alexiabaikas4@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=["dictionary"],
    include_package_data=True,
    entry_points='''
    [console_scripts]
    dictionary=dictionary.__main__:main
    '''
)
