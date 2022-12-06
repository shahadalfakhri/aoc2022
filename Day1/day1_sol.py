print('Day 1')

f = open('input.txt', 'r')
elfNumber = 1
calorieSum = 0
caloriesPerElf = []
allCalloriesPerElf = []

for line in f:
    y = line.split()
    if y == []:
        print(f'elfNumber: {elfNumber}')
        print(caloriesPerElf)
        for x in caloriesPerElf:
            calorieSum = calorieSum + x
        print(f'calorieSum: {calorieSum}')
        allCalloriesPerElf.append(calorieSum)
        print('empty line')
        elfNumber += 1
        calorieSum = 0
        caloriesPerElf = []
    else:
        caloriesPerElf.append(int(y[0]))

print(f'Final list of calories: {allCalloriesPerElf}')
max_value = max(allCalloriesPerElf)
elfIndex = allCalloriesPerElf.index(max_value)
elfNumber = elfIndex + 1
print(f'Elf number {elfNumber} with index {elfIndex} has the most calories with a total of {max_value} calories.')

allCalloriesPerElf.sort(reverse=True)
print(f'sorted: {allCalloriesPerElf}')

x = allCalloriesPerElf
sumOfTopThree = x[0] + x[1] + x[2]
print(f'sum of top three: {sumOfTopThree}')