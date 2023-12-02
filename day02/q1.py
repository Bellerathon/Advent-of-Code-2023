file = open('input.txt', 'r')
input = file.readlines()
file.close()

records = []
sum = 0
for line in input:
  line = line.rstrip()
  id = line.split(":")[0].split("Game ")[1]
  game = line.split(": ")[1].split(";")
  count = 0
  for i, round in enumerate(game):
    round = round.strip()
    split = round.split(", ")
    for dice in split:
      red = 0
      blue = 0
      green = 0
      num = dice.split(" ")[0]
      colour = dice.split(" ")[1]

      if colour == "red":
        red += int(num)
      elif colour == "blue":
        blue += int(num)
      elif colour == "green":
        green += int(num)
      if (red > 12 or green > 13 or blue > 14) or ((red + green + blue) > 39):
        count += 1

  if count == 0:
    sum += int(id)

print(sum)



















  
  # for i, round in enumerate(game):
  #   gg = []
  #   round = round.strip()
  #   rounds = round.split(", ")
  #   print(round)
  #   red = 0
  #   blue = 0
  #   green = 0
  #   num = round.split(" ")[0]
  #   colour = round.split(" ")[1]
  #   if colour == "red":
  #     red += int(num)
  #   elif colour == "blue":
  #     blue += int(num)
  #   elif colour == "green":
  #     green += int(num)

  #   record = {
  #     "id": int(i),
  #     "red": red,
  #     "blue": blue,
  #     "green": green,
  #     "total": int(red + green + blue),
  #   }
  #   gg.append(record)
    
  # records.append(gg)

# max = 39
# total = 0
# for record in records:
#   if record["total"] < max:
#     if record["red"] <= 12 and record["green"] <= 13 and record["blue"] <= 14:
#       print(record["id"])
#       total += record["id"]
  
# print(records)