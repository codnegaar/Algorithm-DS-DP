'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:
        Input
            ["MinStack","push","push","push","getMin","pop","top","getMin"]
            [[],[-2],[0],[-3],[],[],[],[]]

        Output
              [null,null,null,null,-3,null,0,-2]

        Explanation
                  MinStack minStack = new MinStack();
                  minStack.push(-2);
                  minStack.push(0);
                  minStack.push(-3);
                  minStack.getMin(); // return -3
                  minStack.pop();
                  minStack.top();    // return 0
                  minStack.getMin(); // return -2

Constraints:
          -231 <= val <= 231 - 1
          Methods pop, top and getMin operations will always be called on non-empty stacks.
          At most 3 * 104 calls will be made to push, pop, top, and getMin.

'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.minValue = None

        
    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(value)
            self.minValue = value
        else:
            if self.minValue <= value:
                self.stack.append(value)
            else:
                self.stack.append(2 * value - self.minValue)
                self.minValue = value
        return None

    
    def pop(self) -> None:
        if len(self.stack) != 0:
            if self.stack[-1] >= self.minValue:
                self.stack.pop()
            else:
                self.minValue = 2 * self.minValue - self.stack[-1]
                self.stack.pop()
        return None

    
    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            if self.stack[-1] >= self.minValue:
                return self.stack[-1]
            else:
                return self.minValue

            
    def getMin(self) -> int:
        return self.minValue

# Second solution
class MinStack:

    def __init__(self):
        """
        Initialize the MinStack.
        The stack will hold tuples of (value, current_min).
        """
        self.stack = []

    def push(self, val: int) -> None:
        """
        Push a new value onto the stack, along with the current minimum.
        
        Parameters:
        - val (int): The value to be pushed onto the stack.
        """
        # If the stack is empty, the new minimum is the pushed value itself.
        if not self.stack:
            self.stack.append((val, val))
        else:
            # Otherwise, push the value and the new minimum.
            current_min = min(val, self.stack[-1][1])
            self.stack.append((val, current_min))

    def pop(self) -> None:
        """
        Pop the top value from the stack.
        """
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        """
        Get the top value of the stack.
        
        Returns:
        - The value at the top of the stack.
        """
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self) -> int:
        """
        Retrieve the minimum value in the stack.
        
        Returns:
        - The minimum value in the stack.
        """
        if self.stack:
            return self.stack[-1][1]
        return None

