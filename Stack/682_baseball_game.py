"""
You are given a list of strings operations, 
where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
"""

# Input: ops = ["5","2","C","D","+"]
# Output: 30

ops = ["5","2","C","D","+"]

def getScore(ops: list[str])-> int:
    stack = []
    # Rules
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'D':
            stack.append(2 * stack[-1])
        elif op == 'C':
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)
sol = getScore(ops)
print(sol)