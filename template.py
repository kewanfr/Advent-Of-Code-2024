import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "/input.txt"
file_input = open(file_path, "r").read().strip()
file_lines = file_input.split("\n")
answer = 0

for line in file_lines:
  
  answer += 1

print(answer)