#1. Given a list of numbers, write code to iterate through the list
#and calculate the sum of all even numbers. Print the resulting sum.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sumOeven = 0

for num in numbers:
    if num % 2 == 0:
        sumOeven += num

print("Sum of even numbers:", sumOeven)

#2. With a list of strings provided, write code that counts how many
#times the word "Olympic" appears in the list, and then print the count.
strings = ["Olympic", "Olympia", "Olympic College", "Bremerton", "Olympic", "Olympus"]
OLcount = 0

for word in strings:
    if word == "Olympic":
        OLcount += 1

print("Count of 'Olympic':", OLcount)

#3. Given a list of strings, write code to create a new list that includes
#only the strings longer than three characters. Print the resulting filtered list.
strings = ["Cavin", "dog", "Patrick", "rat", "bat", "Krenik"]
filtered_strings = []

for s in strings:
    if len(s) > 3:
        filtered_strings.append(s)

print("Filtered list:", filtered_strings)

#4. For a list of integers, write code that counts how many numbers
#are positive and how many are negative, then print both counts.
numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1

print("Positive count:", positive)
print("Negative count:", negative)

#5. For a list of integers, use a loop to build a new list where each element is the
#square of the corresponding element in the original list. Print the new list.
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num ** 2)

print("Squared list:", squared_numbers)

