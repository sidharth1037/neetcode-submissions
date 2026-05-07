class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            try:
                stack.append(int(item))
            except ValueError:
                if item == '+':
                    stack.append(stack.pop()+stack.pop())
                elif item == '-':
                    stack.append(-(stack.pop()-stack.pop()))
                elif item == '*':
                    stack.append(stack.pop()*stack.pop())
                else:
                    tmp = stack.pop()
                    stack.append(int(stack.pop()/tmp)) 

        return stack.pop()
