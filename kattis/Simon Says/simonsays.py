#!/usr/bin/env python3
import sys
def problem(inp):
    if 'simon says' in inp:
        return inp[11:]
    else:
        return '\n'

def regular():
    l = [] #I'm really lazy with variable names....
    iterations = int(input())
    for i in range(iterations):
        inp = input()
        l.append(problem(inp))
    for t in l:
        print(t)
def test():
    assert(problem('simon says hello')) == 'hello'
    assert(problem('hello')) == '\n'
    assert(problem('simon says  do the thing')) == ' do the thing'
    print('All test cases passed')
if __name__ == '__main__':
  if len(sys.argv) > 1 and sys.argv[1] == 'test':
      test()
  else:
      regular()
