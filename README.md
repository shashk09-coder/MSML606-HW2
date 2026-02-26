# MSML606-HW2

### Overview

In this assignment, I worked with two main data structures: stacks and binary trees.

The goal was to:

  * Build an expression tree from a postfix expression

  * Print prefix, infix, and postfix expressions using tree traversals

  * Evaluate a postfix expression using my own stack implementation

All parts of this assignment were implemented, tested, and debugged using VS Code.

### **Commands used to push code from VS Code to GitHub**

```python
git log

git branch

git remote add origin https://github.com/shashk09-coder/MSML606-HW2.git

git add .gitignore
git add HW2.py
git add csv_files
git add .

git commit -m "statement"

git pull origin main --allow-unrelated-histories

git push -u origin master
```

### Test Case Outputs

```python
python HW2.py
```


**Problem 1**  
<img src="https://github.com/user-attachments/assets/c3e14303-ee06-4961-87fc-ed0e9eb44e33" width="450"/>

**Problem 2**  
<img src="https://github.com/user-attachments/assets/b4638150-7f78-40d0-a991-16b7b227d179" width="450"/>

**Problem 3**  
<img src="https://github.com/user-attachments/assets/41fe7e39-1074-4a93-b38f-3e148718711b" width="450"/>



# Problem 4

Edge cases are handled by performing validation checks before executing operations. I verify that the stack contains enough operands before applying operators, ensure that tokens are valid integers or supported operators, and explicitly check for division by zero before performing division. If any condition fails, I raise appropriate exceptions such as ValueError or ZeroDivisionError to prevent incorrect results.

While implementing **Problems 1, 2, and 3**, I encountered several edge cases that required careful handling to make sure the program behaved correctly and did not crash unexpectedly.


### Empty Postfix Expressions

If the input is empty, there is nothing to build or evaluate.

Edge cases faced when constructing the expression tree in problem 1, printing traversals of a tree in problem 2 and evaluating postfix expression using stack in problem 3

Suppose in Problem 1 if the input list is empty, the stack never gets any nodes. At the end of construction, I check:

```python
if len(stack) != 1:
    raise ValueError("Invalid postfix expression: leftover operands.")
```
If the input is empty:
  * If the input is empty:
    * len(stack) will be 0
    * So it raises ValueError

***In problem 2*** 

```python
if head is None:
    return []
```

This ensures:
  * The function does not crash
  * It satisfies the assignment requirement to handle empty trees

***In problem 3***

If the expression string is empty:

```python
tokens = expression.split()
```

Which produces an empty list.

and at the end of evaluation I check:

```python
if self.top != 0:
    raise ValueError("Invalid postfix expression")
```

So empty input correctly raises an error instead of returning garbage.


### Malformed Postfix Expressions (insufficient operands, too many operands)

This was mainly faced in Problem 1 and Problem 3.

***A) Insufficient Operands***

Example: "3 +"

In both tree construction and evaluation, when I encounter an operator, I check:

**Problem 1:**

```python
if len(stack) < 2:
    raise ValueError("Invalid postfix expression: insufficient operands.")
```

**Problem 3**

```python
if self.top < 1:
    raise ValueError("Invalid postfix expression")
```

this makes sure :
  * An operator cannot be applied unless there are at least two operands available.
  * Prevents runtime crashes from popping empty stack.

***B) Too Many Operands***

Example: "3 4 5 +"

After processing all tokens, I verify:

```python
if len(stack) != 1:
    raise ValueError("Invalid postfix expression: leftover operands.")
```

which :
  * A valid postfix expression must reduce to exactly one result.
  * Extra operands indicate malformed input.


### Division by Zero

What can go wrong

Example: 5 / 0
Division by zero should not return a number.

Particularly in Problem 3

When handling division:

```python
elif token == "/":
    if right == 0:
        raise ZeroDivisionError("Division by zero")
    self.push(int(left / right))
```

I explicitly check if the right operand is zero before dividing.


### Invalid Tokens

Faced in both Problem 1 and Problem 3.

If a token is not one of + - * /, I attempt to convert it to an integer by using the (int fucntion) convert it to an integer and push it back onto the stack:

```python
try:
    int(token)
except ValueError:
    raise ValueError(f"Invalid token found: {token}")
```
This ensures:
  * Only valid integers are allowed
  * Unsupported symbols like ^ or letters like a are rejected
  * Prevents silent logical errors


### Very Large Numbers or Results

Expressions might include large integers, or repeated multiplications.

Python integers automatically expand in size


### Negative Numbers in the Expression

Negative numbers cause problems in tree construction and evaluation

A very easy way to handle is this is by :

```python
    int(token)
```
No extra special logic was needed because int() handles signed integers.

To make sure my program works correctly in all situations, I created a small function called ***run_edge_case_tests()*** in HW2.py. In this function, I manually tested different inputs that could cause errors, such as empty expressions, missing operands, invalid tokens, division by zero, negative numbers, and very large numbers.

<img src="https://github.com/user-attachments/assets/6aea2063-851e-4869-8a3e-f06b4b399f16" width="450"/>

The output shows that all edge case tests were handled correctly. For invalid inputs such as empty expressions, insufficient operands, leftover operands, invalid tokens, and division by zero, the program correctly raised exceptions and printed “PASS,” meaning the error was properly detected. It also shows that valid edge cases like negative numbers and very large numbers were evaluated correctly, confirming that the stack logic works reliably even in extreme situations.


