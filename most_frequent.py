numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
numbers.sort()
most_frequent= []
x = 0
for x in numbers :
    numberx= numbers.count(x)
    most_frequent.append(numberx)

most_frequent.sort()

print(f"The most frequent number is {numbers[most_frequent[len(most_frequent)-1]]} and it was {most_frequent[len(most_frequent)-1]} times repeated")
