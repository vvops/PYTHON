############-----СПИСК----######
strings = ["hello", "world"]
numbers = [1,2,3,4,5]
data = ["hello", 1]

print(data)
print(numbers)
print(strings)

##############################

summa = numbers + data
print(summa)

numbers.append(6)
print(numbers)

first = strings[0]
second = strings[1]
print(first)
print(second)
#print(strings[3]) ####отсутствует 3 элемент списка strings

strings_length = len(strings)
print(strings_length)
s = sum(numbers)
print(s)