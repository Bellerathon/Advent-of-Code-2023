file = open('input.txt', 'r')
input = file.readlines()
file.close()

num_words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
nums_word_dict = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9",
}

total = 0
for line in input:
  # The below two arrays are synced such that the indexes are related, the first element in nums_index is the index of the value of the first element in nums_actual
  # I can now search for the lowest index (which represents the first number in the string) in nums_index, say it's 6, so i know the value of that index by looking at nums_actual[6], same for highest
  nums_index = []
  nums_actual = []
  # Find all instances of a word-number and save the words index in the line, continuosly search starting from just past that index to find any more instances 
  for word in num_words:
    # First instance
    index = line.find(word)
    if index != -1:
      nums_index.append(index)
      nums_actual.append(nums_word_dict[word])
      # Every other instance
      while index != -1:
        index = line.find(word, index + 1)
        if index != -1:
          nums_index.append(index)
          nums_actual.append(nums_word_dict[word])
  # Find all digits in the line
  for i, num in enumerate(line):
    if num.isdigit():
      nums_index.append(i)
      nums_actual.append(num)
  
  # Find lowest and highest index to find first and last number
  index_copy = sorted(nums_index)
  lowest = index_copy[0]
  highest = index_copy[len(index_copy) - 1]

  # The first number in the string is the index in nums_actual of the lowest index in nums_index (remember they are synced and not neccesarily sorted), same for last
  num1 = nums_actual[nums_index.index(lowest)]
  num2 = nums_actual[nums_index.index(highest)]

  # Combine two strings into a number
  total += int(num1 + num2)

print(total)