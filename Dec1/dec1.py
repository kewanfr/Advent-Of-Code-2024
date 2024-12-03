import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "/input.txt"
file_input = open(file_path, "r").read().strip()
file_lines = file_input.split("\n")
answer = 0

left_part = []
right_part = []

for line in file_lines:
  
  parts = line.split("   ")

  left_part.append(parts[0])
  right_part.append(parts[1])


left_part = sorted(left_part)
right_part = sorted(right_part)


for i in range(len(left_part)):
  if i < len(right_part):
    if right_part[i] > left_part[i]:
      answer += int(right_part[i]) - int(left_part[i])
    else :
      answer += int(left_part[i]) - int(right_part[i])


print(answer)