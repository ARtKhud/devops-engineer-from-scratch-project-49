# Brain games
This repository contains simple command-line games written in Python as part of the "DevOps Engineer from Scratch" educational project. Each game greets the user and asks a question such as whether a number is even.
## Badges

[![GitHub Actions Status](https://github.com/hexlet-boilerplates/python-package/workflows/Python%20CI/badge.svg)](https://github.com/hexlet-boilerplates/python-package/actions)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=hexlet-boilerplates_python-package&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=hexlet-boilerplates_python-package)


## Games

- **brain-games**: Greets the user and asks for their name.
- **brain-even**: Asks the user whether a randomly generated number is even.
- **brain-clac**: Asks the user to calculate the expression and write the right answer

More games may be added as the project evolves.

## 🎮 Launch and demonstration of the game
## Launch the brain games:
```bash
brain-games
```
### Demonstration of different outcomes:

### 1. Successful completion of the game:
```
Welcome to the Brain Games!
May I have your name? John
Hello, John!
```

## Launch the even game:
```bash
brain-even
```
### Demonstration of different outcomes:

### 1. Successful completion of the game:
```
Welcome to the Brain Games!
May I have your name? Alice
Hello, Alice!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: no
Correct!
Question: 24
Your answer: yes  
Correct!
Question: 7
Your answer: no
Correct!
Congratulations, Alice!
```

### 2. Wrong answer:
```
Welcome to the Brain Games!
May I have your name? Bob
Hello, Bob!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Bob!
```

## Launch the calc game:
```bash
brain-calc
```
### Demonstration of different outcomes:

### 1. Successful completion of the game:
```
Welcome to the Brain Games!
May I have your name? Tom
Hello, Tom!
What is the result of the expression?
Question: 4 + 10
Your answer: 14
Correct!
Question: 25 - 11
Your answer: 14
Correct!
Question: 25 * 7
Your answer: 175
Correct!
Congratulations, Tom!
```

### 2. Wrong answer:
```
Welcome to the Brain Games!
May I have your name? Bob
Hello, Bob!
What is the result of the expression?
Question: 25 * 7
Your answer: 145
'145' is wrong answer ;(. Correct answer was '175'.
Let's try again, Bob!
```