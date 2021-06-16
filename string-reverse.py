str_input = input("Enter a string to reverse: ")
i = len(str_input) - 1
reverse_str = ""
while i >= 0:
  reverse_str += str_input[i]
  i -= 1

print(reverse_str)
