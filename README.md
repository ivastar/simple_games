### Basics to Cover

- How to control what Python does when executing a script from the command line
- How does Python take input from user
    - Parameters
    - Flags
    - Interactive input
    
- Example: Rock, Paper, Scissors
    - Breaking program into functions
    - Commenting
    
- Algorithm: Game Play

- Templates
    - Number Guessing
    - Mad Libs
    - Game Of Life
  


#### Simple Function

```
def hello():
    """Greeting function."""

    print("Hello!")

if __name__ == '__main__':
    hello()
```

Test by running in the terminal:

```
> python hello.py
```

#### Setting parameters

Python comes with a couple of tools that you can use to write command-line interfaces for your programs and apps. If you need to quickly create a minimal CLI for a small program, then you can use the `argv` attribute from the `sys` module. This attribute automatically stores the arguments that you pass to a given program at the command line.

```
import sys

def hello():
    """Greeting function."""

    print("Hello!")

if __name__ == '__main__':
    hello()
    print(sys.argv)
    
```

Test how `sys` captures the variables via:

```
> python hello.py 1 2 3 4 John Hugh
```

#### Using input inside code

```
import sys

def hello(name):
    """Greeting function."""

    print(f"Hello {name}!")

if __name__ == '__main__':
    name = sys.argv[1]
    hello(name)
```

Test by running in the terminal:

```
> python hello.py John
```

#### Or something a bit more complex

```
import sys

def hello(name):
    """Greeting function."""

    print(f"Hello {name}!")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide a name.')
    else:
        name = sys.argv[1]
        hello(name)
```

Test by running in the terminal:

```
> python hello.py 
Please provide a name.
> python hello.py 
Hello John!
```

Even though your program works okay, parsing command-line arguments manually using the `sys.argv` attribute isn’t a scalable solution for more complex CLI apps. If your app needs to take many more arguments and options, then parsing `sys.argv` will be a complex and error-prone task. You need something better, and you get it in Python’s `argparse` module.

#### Flags

Python’s `argparse` module allows you to:

- Parse command-line arguments and options
- Take a variable number of parameters in a single option
- Provide subcommands in your CLIs

To use Python’s argparse, you’ll need to follow four straightforward steps:

- Import `argparse`.
- Create an argument parser by instantiating `ArgumentParser`.
- Add arguments and options to the parser using the `.add_argument()` method.
- Call `.parse_args()` on the parser to get the Namespace of arguments.

Example:

```
import argparse

def hello(name):
    """Greeting function."""

    print(f"Hello {name}!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("name")

    args = parser.parse_args()

    name = args.name
    hello(name)
```

Test by running in the terminal:

```
> python hello.py John
```
* More here: https://realpython.com/command-line-interfaces-python-argparse/


#### Options modify the behavior of the program

```
import argparse

def hello(name, long=False):
    """Greeting function."""

    if long:
        print(f"Hello {name}! How are you doing today?")
    else:
        print(f"Hello {name}!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("name")
    parser.add_argument("-l","--long",action="store_true")

    args = parser.parse_args()

    name = args.name
    hello(name, long=args.long)
```

Test by running in the terminal:

```
> python hello.py John -l
```

#### Another option:

```
import argparse

def hello(name, greeting = '', long=False):
    """Greeting function."""

    if not greeting:
        greeting = 'Hello'

    if long:
        print(f"{greeting} {name}! How are you doing today?")
    else:
        print(f"{greeting} {name}!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("name")
    parser.add_argument("-l","--long",action="store_true", required=False)
    parser.add_argument("-g","--greeting", dest='greeting', required=False) 
    args = parser.parse_args()

    name = args.name
    hello(name, greeting = args.greeting, long=args.long)
```

Test by running in the terminal:

```
> python hello.py John -l -g Howdy
```

#### Finally, interactive outputs

```
import argparse

def hello(name, greeting = '', long=False):
    """Greeting function."""

    if not greeting:
        greeting = 'Hello'

    if long:
        print(f"{greeting} {name}!")
        mood = input("How are you doing today? ")
        print(f'I see, you are feeling {mood} today.')
    else:
        print(f"{greeting} {name}!")

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("name")
    parser.add_argument("-l","--long",action="store_true", required=False)
    parser.add_argument("-g","--greeting", dest='greeting', required=False) 
    args = parser.parse_args()

    name = args.name
    hello(name, greeting = args.greeting, long=args.long)

```

Test by running in the terminal:

```
> python hello.py John -l -g Howdy
```

### Resources:

- Advent of Code: https://adventofcode.com/2022/events
- Pytudes: https://github.com/norvig/pytudes
- Geeks for geeks: https://www.geeksforgeeks.org/
- Python projects for beginners: https://www.dataquest.io/blog/python-projects-for-beginners/
- Pygame: https://www.pygame.org/news
