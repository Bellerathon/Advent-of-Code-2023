file = open('input.txt', 'r')
input = file.readlines()
file.close()

total = 0
for line in input:
  normal = 0
  reverse = 0
  for num in line:
    if num.isdigit():
      normal = num
      break
  line = line[::-1]
  for num in line:
    if num.isdigit():
      reverse = num
      break

  total += int(normal + reverse)

print(total)