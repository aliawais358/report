# check if a number is even
is_even = lambda x : x % 2 == 0

print(is_even(4))
print(is_even(9))

#Use a lambda function with the filter() function to return all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8]
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


#Use a lambda function with the map() function to convert a list of temperatures in Celsius [0, 10, 20, 30] to Fahrenheit.
celsius = [0, 10, 20, 30]

fahrenheit = list(map(lambda x : (x * 9/5) + 32, celsius))
print(fahrenheit)

# sorts a list of tuples based on the second value of each tuple
tuples_list = [(1, 2), (4, 1), (2, 3)]

sorted_tuples = sorted(tuples_list, key=lambda x: x[1])

print(sorted_tuples)

#Doubling Each Number in a List Using map
class NumberProcessor:
    def __init__(self, numbers):
        self.numbers = numbers

    def double_numbers(self):
        
        doubled = list(map(lambda x: x * 2, self.numbers))
        return doubled


processor = NumberProcessor([1, 2, 3, 4])


result = processor.double_numbers()

print(f"Doubled numbers: {result}")
