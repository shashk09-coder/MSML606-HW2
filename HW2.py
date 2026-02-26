import csv
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class HomeWork2:

    # Problem 1: Construct an expression tree (Binary Tree) from a postfix expression
    # input -> list of strings (e.g., [3,4,+,2,*])
    # this is parsed from p1_construct_tree.csv (check it out for clarification)

    # there are no duplicate numeric values in the input
    # support basic operators: +, -, *, /

    # output -> the root node of the expression tree. Here: [*,+,2,3,4,None,None]
    # Tree Node with * as root node, the tree should be as follows
    #         *
    #        / \
    #       +   2
    #      / \
    #     3   4

    def constructBinaryTree(self, input) -> TreeNode:
      
        operators = {"+", "-", "*", "/"}   # set of valid operators
        stack = [] # stack to hold tree nodes during construction

        for token in input:
            token = token.strip() # removes any  whitespace

            
            if token in operators:   # to check if the token is an operator
                
                if len(stack) < 2:   #  we need at least two operands
                    raise ValueError("Invalid postfix expression: insufficient operands.")

                right = stack.pop()  # right operand is the top of the stack
                left = stack.pop()   # left operand is the next element in the stack

                new_node = TreeNode(token, left, right)
                stack.append(new_node)

            # checking if its a number
            else:
                try:
                    int(token)  # validate that the token is an integer
                except ValueError:
                    raise ValueError(f"Invalid token found: {token}")

                stack.append(TreeNode(token))

        
        if len(stack) != 1:    # at the end we must have exactly one element (the root)
            raise ValueError("Invalid postfix expression: leftover operands.")

        return stack[0]



    # Problem 2.1: Use pre-order traversal (root, left, right) to generate prefix notation
    # return an array of elements of a prefix expression
    # expected output for the tree from problem 1 is [*,+,3,4,2]
    # you can see the examples in p2_traversals.csv

    def prefixNotationPrint(self, head: TreeNode) -> list:
        if head is None:   # if the node is null it returns an empty list
            return []

        result = [head.val]   # add the current nodes value to the result list
        result += self.prefixNotationPrint(head.left)  # recursively traverse the left subtree and add its result to the result list
        result += self.prefixNotationPrint(head.right) # recursively traverse the right subtree and add its result to the result list
        return result
        

    # Problem 2.2: Use in-order traversal (left, root, right) for infix notation with appropriate parentheses.
    # return an array of elements of an infix expression
    # expected output for the tree from problem 1 is [(,(,3,+,4,),*,2,)]
    # you can see the examples in p2_traversals.csv

    # don't forget to add parentheses to maintain correct sequence
    # even the outermost expression should be wrapped
    # treat parentheses as individual elements in the returned list (see output)

    def infixNotationPrint(self, head: TreeNode) -> list:
        if head is None:   # if the node is null it returns an empty list
            return []

        # leaf node
        if head.left is None and head.right is None:  #  if the node is a leaf node return a list containing its value
            return [head.val]

        result = ["("]  # add an opening parenthesis before processing the left subtree
        result += self.infixNotationPrint(head.left) # traverse the left subtree and add its result to the result list
        result.append(head.val)  # add the current node's value to the result list after the left subtree
        result += self.infixNotationPrint(head.right)  # traverse the right subtree and add its result to the result list
        result.append(")")
        return result
        


    # Problem 2.3: Use post-order traversal (left, right, root) to generate postfix notation.
    # return an array of elements of a postfix expression
    # expected output for the tree from problem 1 is [3,4,+,2,*]
    # you can see the examples in p2_traversals.csv

    def postfixNotationPrint(self, head: TreeNode) -> list:
        if head is None:   # if the node is null it returns an empty list
            return []

        result = []
        result += self.postfixNotationPrint(head.left)  # traverse the left subtree and add its result to the result list
        result += self.postfixNotationPrint(head.right) # traverse the right subtree and add its result to the result list
        result.append(head.val)  # add the current node's value to the result list after processing both subtrees
        return result
        

                            
class Stack:   #  stack implementation to be used for initializing the stack for problem 3

    # Implement your stack using either an array or a list
    # (i.e., implement the functions based on the Stack ADT we covered in class)
    # You may use Python's list structure as the underlying storage.
    # While you can use .append() to add elements, please ensure the implementation strictly follows the logic we discussed in class
    # (e.g., manually managing the "top" of the stack
    
    # Use your own stack implementation to solve problem 3

    def __init__(self):     # initialize the stack with an empty list and set the top index to -1
        self.data = []
        self.top = -1    
    
    def isEmpty(self):     # check if the stack is empty by comparing the top index to -1
        return self.top == -1
    
    def push(self, value):   # add a value to the top of the stack by appending it to the list and incrementing the top index
        self.data.append(value)
        self.top += 1
    
    def pop(self):           # remove and return the value at the top of the stack by popping it from the list and decrementing the top index
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        
        value = self.data[self.top]  # get the value at the top of the stack
        self.data.pop()
        self.top -= 1
        return value
    
    def peek(self):                # return the value at the top of the stack without removing it by accessing it from the list using the top index
        if self.isEmpty():
            raise IndexError("peek from empty stack")
        
        return self.data[self.top]




    # Problem 3: Write code to evaluate a postfix expression using stack and return the integer value
    # Use stack which you implemented above for this problem

    # input -> a postfix expression string. E.g.: "5 1 2 + 4 * + 3 -"
    # see the examples of test entries in p3_eval_postfix.csv
    # output -> integer value after evaluating the string. Here: 14

    # integers are positive and negative
    # support basic operators: +, -, *, /
    # handle division by zero appropriately

    # DO NOT USE EVAL function for evaluating the expression

    def evaluatePostfix(self, expression: str) -> int:  # 
        operators = {"+", "-", "*", "/"}  # set of valid operators

        tokens = expression.split()   # split the input string into tokens(whitespace)

        for token in tokens:
            if token in operators:
                if self.top < 1:    # checks if there are at least two operands on the stack before performing an operation
                    raise ValueError(" insufficient operands")   #it raises a value error if there are not enough operands to perform the operation
                right = self.pop()
                left = self.pop()  # it pops the top two operands from the stack, with the right operand being the one that was most recently added to the stack and the left operand being the one that was added before that

                if token == "+":    # it checks the operators below as (+,-,*,/) and performs the corresponding operation on the left & right operands, and pushes it back onto the stack
                    self.push(left + right)
                elif token == "-":   
                    self.push(left - right)
                elif token == "*":
                    self.push(left * right)
                elif token == "/":  # If the right operand is zero, it raises a ZeroDivisionError.
                    if right == 0:   
                        raise ZeroDivisionError("division by zero")   
                    self.push(int(left / right))   # it performs integer division and pushes the result back onto the stack and 
                                                  #the int() function is used to ensure that the result is an integer, which is important for cases where the division might result in a float.
            else:
                try:
                    self.push(int(token))     # if the token is not an operator it just tries to convert it to an integer and push it back onto the stack else raises a value error.
                except ValueError:
                    raise ValueError(f"Invalid token: {token}")
        if self.top != 0:      # just a small check at the end to make sure that there is exactly one element left on the stack, ff there are more or fewer elements, it raises a ValueError indicating that the postfix expression is invalid.
            raise ValueError("Invalid postfix expression")
        return self.pop()
# Main Function. Do not edit the code below
if __name__ == "__main__":
    homework2 = HomeWork2()

    print("\nRUNNING TEST CASES FOR PROBLEM 1")
    testcases = []
    try:
        with open('p1_construct_tree.csv', 'r') as f:
            testcases = list(csv.reader(f))
    except FileNotFoundError:
        print("p1_construct_tree.csv not found")

    for i, (postfix_input,) in enumerate(testcases, 1):
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)
        output = homework2.postfixNotationPrint(root)

        assert output == postfix, f"P1 Test {i} failed: tree structure incorrect"
        print(f"P1 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 2")
    testcases = []
    with open('p2_traversals.csv', 'r') as f:
        testcases = list(csv.reader(f))

    for i, row in enumerate(testcases, 1):
        postfix_input, exp_pre, exp_in, exp_post = row
        postfix = postfix_input.split(",")

        root = homework2.constructBinaryTree(postfix)

        assert homework2.prefixNotationPrint(root) == exp_pre.split(","), f"P2-{i} prefix failed"
        assert homework2.infixNotationPrint(root) == exp_in.split(","), f"P2-{i} infix failed"
        assert homework2.postfixNotationPrint(root) == exp_post.split(","), f"P2-{i} postfix failed"

        print(f"P2 Test {i} passed")

    print("\nRUNNING TEST CASES FOR PROBLEM 3")
    testcases = []
    try:
        with open('p3_eval_postfix.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                testcases.append(row)
    except FileNotFoundError:
        print("p3_eval_postfix.csv not found")

    for idx, row in enumerate(testcases, start=1):
        expr, expected = row

        try:
            s = Stack()
            result = s.evaluatePostfix(expr)
            if expected == "DIVZERO":
                print(f"Test {idx} failed (expected division by zero)")
            else:
                expected = int(expected)
                assert result == expected, f"Test {idx} failed: {result} != {expected}"
                print(f"Test case {idx} passed")

        except ZeroDivisionError:
            assert expected == "DIVZERO", f"Test {idx} unexpected division by zero"
            print(f"Test case {idx} passed (division by zero handled)")