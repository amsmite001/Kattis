# Simon Says (simon)
* https://open.kattis.com/problems/simon
* 2.2 Difficulty

## Input
The first line of the input consists of a single integer, *__T__*, the number of test cases.
Each test case consists of a single line of text – Simon’s command.
* 1≤ *__T__* ≤20
* Each line consists of only the letters a-z and spaces
* Each word will be separated by exactly one space
* Lines will not have leading or trailing spaces
* Each line will have between 1 and 1000 characters

## Output
For each test case, repeat the command if the first two words were “simon says”. Do not repeat the initial “simon says”. Otherwise output a blank line.

## Running the file
For the base kattis problem,
```
python3 simonsays.py
```

The input is looking for a number of iterations, hit enter, then enter a phrase per each line you told the program you would.
* There will be extra spaces after each output if there is a line without 'simon says' per the problem.

For the test cases:
```
python3 simonsays.py test
```