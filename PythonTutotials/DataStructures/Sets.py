"""
Python also includes a data type for sets. A set is an unordered collection
with no duplicate elements. Basic uses include membership testing and eliminating
duplicate entries. Set objects also support mathematical operations like union,
intersection, difference, and symmetric difference.Curly braces or the set()
function can be used to create sets. Note: to create an empty set you have to
use set(), not {}; the latter creates an empty dictionary, a data structure
that we discuss in the next section.

"""

basket = {"apple", "banana", "apple", "pear", "oranges", "watermellon", "cherries", "blueberries", "coconut", "pear"}
print(basket) # show that duplicates have been removed
print("banana" in basket) # fast membership testing
print("pineapple" in basket) # fast membership testing

a = set('asasasaaswwewqwqklioasdhadsuadhaio')
b = set('alacazam')
print(a) # unique letters in a
print(b) # unique letters in b
print(a - b) # letters in a but not in b
print(a | b) # letters in a or b or both
print(a & b) # letters in both a and b
print(a ^ b) # letters in a or b but not both
