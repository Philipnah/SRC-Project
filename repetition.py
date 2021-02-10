from typing import collections


message = input("message: ")

ready2Transmit = []

for i in message:
     n = 0
     while n < 3:
          ready2Transmit.append(i)
          n += 1

i = 0
while i < 3:
     ready2Transmit.append(">")
     i += 1

# ---- ready2Transmit now is 4 times repeated


reconstructed = []


i = 0
n = 0

letter = []
while i < len(ready2Transmit):

     if n < 3:
          letter.append(ready2Transmit[i])
          n += 1

     else:
          reconstructed.append(letter)
          letter = []
          n = 0
          i -= 1

     i += 1

print(reconstructed)

#reconstructed = [['h', 'h', 'h'], ['e', 'e', 'e'], ['j', 'j', 'j'], [' ', ' ', ' '], ['m', 'm', 'm'], ['e', 'e', 'e'], ['d', 'd', 'd'], [' ', ' ', ' '], ['d', 'd', 'd'], ['i', 'i', 'i'], ['g', 'g', 'g']]
i = 0
print("\nReceived message:\n")
while i < len(reconstructed):
     print(collections.Counter(reconstructed[i]).most_common(1)[0][0], end="")
     i += 1

