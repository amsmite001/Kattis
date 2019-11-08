# Above Average
* https://open.kattis.com/problems/aboveaverage
* 2.0 Difficulty

It is said that 90% of frosh expect to be above average in their class. You are to provide a reality check.
## Input
The first line of standard input contains an integer 1≤ *__C__* ≤50, the number of test cases. *__C__* data sets follow. 
 
 Each data set begins with an integer, *__N__*, the number of people in the class (1≤ *__N__* ≤1000). *__N__* integers follow, separated by spaces or newlines, each giving the final grade (an integer between 0 and 100) of a student in the class.

## Output
For each case you are to output a line giving the percentage of students whose grade is above average, rounded to exactly 3 decimal places.

## Running the file
For the base kattis problem,
```
python3 aboveavg.py
```
The input is looking for, something like so:
```
2
5 50 50 70 80 100
7 100 95 90 80 70 60 50
```
For running the test cases,
```
python3 aboveavg.py test
```
