# Brain games
This repository contains simple command-line games written in Python as part of the "DevOps Engineer from Scratch" educational project. Each game greets the user and asks a question such as whether a number is even.
## Badges

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ARtKhud_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=ARtKhud_devops-engineer-from-scratch-project-49)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=ARtKhud_devops-engineer-from-scratch-project-49&metric=bugs)](https://sonarcloud.io/summary/new_code?id=ARtKhud_devops-engineer-from-scratch-project-49)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=ARtKhud_devops-engineer-from-scratch-project-49&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=ARtKhud_devops-engineer-from-scratch-project-49)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=ARtKhud_devops-engineer-from-scratch-project-49&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=ARtKhud_devops-engineer-from-scratch-project-49)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ARtKhud_devops-engineer-from-scratch-project-49&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=ARtKhud_devops-engineer-from-scratch-project-49)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=ARtKhud_devops-engineer-from-scratch-project-49&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=ARtKhud_devops-engineer-from-scratch-project-49)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ARtKhud_devops-engineer-from-scratch-project-49&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=ARtKhud_devops-engineer-from-scratch-project-49)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=ARtKhud_devops-engineer-from-scratch-project-49&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=ARtKhud_devops-engineer-from-scratch-project-49)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ARtKhud_devops-engineer-from-scratch-project-49&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=ARtKhud_devops-engineer-from-scratch-project-49)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=ARtKhud_devops-engineer-from-scratch-project-49&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=ARtKhud_devops-engineer-from-scratch-project-49)

## Games

- **brain-games**: Greets the user and asks for their name.
- **brain-even**: Asks the user whether a randomly generated number is even.
- **brain-clac**: Asks the user to calculate the expression and write the right answer
- **brain-gcd**: Asks the user to find GCD (greatest common divisor)
- **brain-progression**: Asks the user to find ommited number in the sequence of numbers 

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

## Launch the GCD game:
```bash
brain-gcd
```
### Demonstration of different outcomes:

### 1. Successful completion of the game:
```
Welcome to the Brain Games!
May I have your name? Helen
Hello, Helen!
Find the greatest common divisor of given numbers.
Question: 29 16
Your answer: 1
Correct!
Question: 96 62
Your answer: 2
Correct!
Question: 92 53
Your answer: 1
Correct!
Congratulations Helen
```
### 2. Wrong answer:
```
Welcome to the Brain Games!
May I have your name? Tirion
Hello, Tirion!
Find the greatest common divisor of given numbers.
Question: 66 79
Your answer: 1
Correct!
Question: 2 61
Your answer: 1
Correct!
Question: 51 45
Your answer: 1
'1' is wrong answer ;(. Correct answer was '3'.
Let's try again, Tirion
```

## Launch the progression games:
```bash
brain-progression
```
### Demonstration of different outcomes:

### 1. Successful completion of the game:
```
Welcome to the Brain Games!
May I have your name? Anna
Hello, Anna!
What number is missing in the progression?
Question: 413 418 423 .. 433 438
Your answer: 428
Correct!
Question: 76 81 86 91 96 101 106 111 ..
Your answer: 116
Correct!
Question: 975 982 989 996 1003 1010 .. 1024 1031
Your answer: 1017
Correct!
Congratulations Anna
```
### 2. Wrong answer:
```
Welcome to the Brain Games!
May I have your name? Anna     
Hello, Anna!
What number is missing in the progression?
Question: 409 .. 419 424 429 434 439
Your answer: 414
Correct!
Question: 816 824 832 .. 848 856 864 872 880
Your answer: 838
'838' is wrong answer ;(. Correct answer was '840'.
Let's try again, Anna
```