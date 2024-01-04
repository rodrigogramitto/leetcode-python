
def is_valid(s):
  stack = list()

  for char in s:
    if char == '(' or char == '{' or char == '[':
      stack.append(char)

    if char == ')' and stack[len(stack) - 1] == '(':
      stack.pop()
    elif char == '}' and stack[len(stack) - 1] == '{':
      stack.pop()
    elif char == ']' and stack[len(stack) - 1] == '[':
      stack.pop()


  return len(stack) == 0



my_vals = "()[]{)"

actual = is_valid(my_vals)

print(actual)