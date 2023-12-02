file = open('input.txt', 'r')
input = file.readlines()
file.close()

records = []
sum = 0
for line in input:
  line = line.rstrip()
  id = line.split(":")[0].split("Game ")[1]
  game = line.split(": ")[1].split(";")

  red = 0
  blue = 0
  green = 0
  for i, round in enumerate(game):
    round = round.strip()
    split = round.split(", ")
  
    for dice in split:
      num = dice.split(" ")[0]
      colour = dice.split(" ")[1]
      if colour == "red":
        if int(num) > red:
          red = int(num)
      elif colour == "blue":
        if int(num) > blue:
          blue = int(num)
      elif colour == "green":
        if int(num) > green:
          green = int(num)

  sum += int(red*blue*green)

print(sum)