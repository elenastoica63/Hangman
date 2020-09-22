word = list("Romania")
hidden = []
for character in word:
    hidden.append("_")

attempts = 0
max_attempts = 5

isGameOver = False
while not isGameOver:
    print(f'You have {attempts} attempts remaining')
    break