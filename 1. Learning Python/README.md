# 1. Learning Python

A great resource for learning Python can be found [here](https://docs.python.org/2/tutorial/index.html).

There are two ways you can execute Python code:
1. You can type instructions, line by line, into a Python console (such as the one in Spyder).
2. If you have more lines of code you want to execute, you can type them into a file that you give a `.py` extension.

## Using python as a calculator
The easiest thing you can do is use python as a calculator. We will start by running this code directly from the Spyder Console window.

Launch Spyder through Anacodna. The lower right section of the Spyder window is the Console. Click on the console, and you are ready to type commands.

You can for example write `2+2` or `2+10-5*10/2` and hit return on your keyboard to make Python compute the result. This is how my screen looks after having executed these commands:

![](Images/spyder_console.png)

Possible points to discuss:
- Order of operations
- Inequalities
- Modulo operator
- Exponentiation

## Assigning variables
You can define variables by setting them equal to something:
```python
a = 1
b = 2
a+b # will now be equivalent to saying 1+2
```

You can update the value a variable contains by setting it equal to something else:
```python
a = 1
a = 2
a # will now be equal to 2, not 1
```

## Equality
If you want to check if two variables have the same value, you can do this using the `==` operator.
```python
a = 2
b = 4
a == b # False
a+a == b # True
```

Similarly, you can check for inequalities by using
- `a < b`, a less than b
- `a > b`, a greater than b
- `a <= b`, a less than or equal to b
- `a >= b`, a greater than or equal to b

## Strings
You can also set variables to be equal to text. For this to work, you need to surround the text with quotation marks:
```python
a = "this is a string"
b = ' and this is another'
a+b #  "this is a string and this is another"
```

You can use both double quotes and single quotes to surround strings, it makes no difference.

### Indexing
To get parts of a string, you can use indexing. Python uses zero indexing, meaning that the first character is located at index zero. See the example for more details on how it works:

```python
a = "banana"
a[0]    # first character of a
a[1]    # second character
a[-1]   # last character
a[1:3]  # the second and third character
a[1:-1] # all characters except the first and the last
a[1:]   # all characters except the first
```

## Lists
In the same way that you can collect characters in a string, you can other types of data (such as numbers) in a list. Lists are very powerful if you need to store large amounts of data.

If you know what values you want to store in your list, you can initialize a new list by surrounding your numbers with square brackets, and separating them by commas:

```python
numbers = [1, 2, 3, 40, 500]
```

As with strings, you can access individual elements in the list by saying
```python
numbers[0]   # returns the first element in the list
numbers[3:4] # returns the fourth and fifth element in the list as a list
```

If you want to add a number to your list, you can use the `append()` method:
```python
numbers.append(2)
numbers # print all values in numbers
```

You can find the length of a list or the sum of a list by doing
```python
len(numbers) # works for any list
sum(numbers) # works only if the data-types stored in the list supports addition
```

Thus, you can compute the mean of your list by
```python
mean = sum(numbers) / len(numbers)
```

These are just a few things that you can do with numbers and lists. For more information, you can for example search the web for "python lists". You will find lots of great information, such as [this article from Google for Education](https://developers.google.com/edu/python/lists).

## Writing code in a file
If you want to make more complicated programs with commands that span across multiple lines, it is easier to have the code in a file rather than typing it into the terminal. You can do this as follows:
1. Type your code into the Python code editor in Spyder, which is located on the left side of the screen.
2. Click the green play button on the top of the screen.
3. Your program is executed, and its output is printed to the console.

Note: to make what you compute show up in the terminal, you must place it inside the parenthesis of `print()` as seen in the image below.

![](Images/spyder_editor.png)


## Comments
The Python interpreter will skip anything that comes after `#` on a line. You can use this to write notes about what you are doing in your code, which can be useful for humans to understand what is going on. For example
```python
2**6 # is the python notation for exponentiation, ie. 2^6
```

If you want your comment to span multiple lines, you can use a multiline comment:
```python
"""
This is a multiline comment.
It can be useful for writing longer comments!
"""
```

As you have noticed, the Spyder editor already populated your python file with a comment. It is good practice to start code-files with a comment saying what the code does and who made it, so feel free to change the comment generated by Spyder to what you think appropriate.


## `If` statements
It is possible to have parts of code execute only when you want it to. It works like this:

```python
a = 5

if False:
    a = 2

print(a) # will print 5, as the if block has not been executed

if True:
    a = 2

print(a) # will print 2, as the if block has been executed
```

The expression you place after `if` is evaluated by the Python interpreter to determine if it is `True` or `False`. If you go back to the section on equality, you will find that these are very useful in conjunction with `if` statements! You can for example say

```python
a = 5

if a == 5: # evaluates to True, as a is set to 5
    a = 2  # this assignment is therefore executed

print(a)   # the value of a has changed to 2

if a == 5: # evaluates to False
    a = 3  # not executed

print(a)   # a is still 2
```

Python is a special language in that how you indent your lines (how many spaces you have before the first character on a line) matters. Therefore, the code below is different from the code above.

```python
a = 5
if a == 5:
    a = 2
    print(a)
```

## Loops
If you want to execute the same lines of code many times in a row, loops are very useful.

### `While` loops
The `while` loop works a bit like the `if` statement, with the one difference that the `while` loop will continue to execute the while block until the condition becomes `False`.

In the following code for example, we print the numbers from 0 to 5.

```python
a = 0
while a < 5:
    a = a+1
    print(a)
```

### `For` loops
Another common type of loop is the `for` loop. It is very useful for looping through lists.

```python
list = [0, 5, 8, 4, 6]
for item in list:
    print(item * 2)
```

## Functions
In order to make code more readable and easy to reuse, programmers use functions. This a very powerful concept that enables the programmer to do very powerful things by calling a function in one line of code, without needing to know the exact details of how the function works. You have used multiple functions already. `Print()` is a function in Python that prints what you pass to it (what is inside the parenthesis) to the console. `len()` and `sum()` are other functions.

There are a few rules to defining Python functions:
- Function blocks begin with the keyword `def` followed by the function name, parentheses and a colon.
- Variables can be passed to the function by placing them inside the parenthesis. They are called function arguments or parameters.
- The code block within every function is indented.
- The statement `return` exits a function. If you want, you can add a return argument that will be passed back to the caller of the function. A return statement with no arguments is the same as return `None`.

In summary, a function looks like this:
```python
def functionName(argument1, argument2):

  # code

  return returnArgument
```

And you can call it by saying
```python
value = functionName(a, b)
```

Inside the function, you will be able to access _a_ as _argument1_ and _b_ as _argument2_. After the function has completed executing, _value_ will have the same value as the variable _returnArgument_ that you returned in the function.

Let us take a look at a practical example:

```python
def magnitude(x, y):
  m = (x**2 + y**2)**0.5
  return m

print(magnitude(3,4)) # prints 5
```

One of the great benefits of Python is that so many people use it and write code for it. There are thousands of libraries made by organizations and by the Python community, that you can download. These libraries contain functions that you can call, so that you do not have to implement core pieces of functionality yourself. This can speed your development up significantly!


### A few useful functions
Below you will find a small list of some very useful functions in Python.
#### `range()`
You can declare a list of all numbers from zero to N by saying `range(N)`. This is very useful when executing loops for example:

```python
list = [0, 5, 8, 4, 6]
for index in range(100):
  # code
```

## Exercises
- Write a program that computes the sum of the 100 first natural numbers (1,2,3,4..100).
- Declare `string = "UBC Physics and Astronomy"`. Make a program that counts the number of 's' characters in this string.
- Make a function that takes one string as an argument, and returns the number of 's' characters in it. Can you make the character to search for be a parameter as well?
- Print all prime numbers smaller than 100.
- Write a function to compute the mode (the number that appears the most frequently) in a list of numbers.


Next: [Module 2: Arduino for Data Collection](/2.%20Arduino%20for%20Data%20Collection/)
