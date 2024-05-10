# WORDS

[![GitHub license](https://img.shields.io/github/license/daniel-alvarenga/words)](vitorcarvalho67/Boot/blob/master/LICENSE)
![GitHub languages top](https://img.shields.io/github/languages/top/daniel-alvarenga/Words)
[![GitHub contributors](https://img.shields.io/github/contributors/daniel-alvarenga/Words)](https://github.com/daniel-alvarenga/Words/graphs/contributors)
![GitHub stars](https://img.shields.io/github/stars/daniel-alvarenga/Words)

Simple offline terminal game inspired by the classic [Termo](https://term.ooo), brazilian version of [Wordle](https://www.nytimes.com/games/wordle/).

The game consists of getting a five-letter word correct in 7 attempts. For each word entered, the letters are classified as existing in the correct place, in green, existing in the wrong place in orange, and non-existent letters, which form the clues to guess the secret word. Words not listed in the game base or already entered are not accepted. There are around 1500 different games.

## Languages and Libs

[Python](https://python.org)
[Unidecode](https://pypi.org/project/Unidecode/)
[Pyinstaller](https://pyinstaller.org/en/stable/)


## How to Play

> [!Note]
> Depending on the terminal used, colors may not be displayed correctly due to the lack of support for ANSI escape codes. It is recommended to test the program on different terminals to ensure the best possible user experience.

You can download and execute the [release](https://github.com/Daniel-Alvarenga/Words/releases/tag/game) or:

Clone the repository
```bash
git clone https://github.com/Daniel-Alvarenga/Words
```

Create and activate virtual envinroment (venv)
```bash
python -m venv venv
./venv/Scripts/activate
```
Install dependencies
```bash
pip install -r requirements.py
```

Run game.py
```bash
python game.py
```

## Contributing
Contributions to this project are welcome. 

>[!tip]
>It would be interesting to contribute a version containing a duet and quartet

Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes
4. Commit your changes.
5. Push to the branch.
5. Submit a pull request.

> [!IMPORTANT]  
> To build a new .exe with pyinstaller the file to edit must be gen/words.py
