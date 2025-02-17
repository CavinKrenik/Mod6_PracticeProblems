#1. Given a list of numbers, write code to iterate through the list
#and calculate the sum of all even numbers. Print the resulting sum.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even = sum(num for num in numbers if num % 2 == 0)
print("Sum of even numbers:", sum_even)

#2. With a list of strings provided, write code that counts how many
#times the word "Olympic" appears in the list, and then print the count.

strings = ["Olympic", "Games", "Olympic", "Sports", "Olympic"]
count_olympic = strings.count("Olympic")
print("Count of 'Olympic':", count_olympic)

#3. Given a list of strings, write code to create a new list that includes
#only the strings longer than three characters. Print the resulting filtered list.

strings = ["Cavin", "dog", "Patrick", "rat", "bat", "Krenik", "him"]
filtered_strings = [s for s in strings if len(s) > 3]
print("Filtered list:", filtered_strings)

#4. For a list of integers, write code that counts how many numbers
#are positive and how many are negative, then print both counts.

numbers = [-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]
positive = sum(1 for num in numbers if num > 0)
negative = sum(1 for num in numbers if num < 0)
print("Positive count:", positive)
print("Negative count:", negative)

#5. For a list of integers, use a loop to build a new list where each element is the
#square of the corresponding element in the original list. Print the new list.

numbers = [1, 2, 3, 4, 5]
squared_numbers = [num ** 2 for num in numbers]
print("Squared list:", squared_numbers)
