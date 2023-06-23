# Найти среднее арифметическое
# среди всех элементов массива
# [2, 5, 13, 7, 6, 4]

numbers = [2, 5, 13, 7, 6, 4]
size = len(numbers)
i = 0
avg = 0
sum = 0

while i < size:
    sum = sum + numbers[i]
    i+= 1
avg = sum/size
print(avg)
