

"""

List data type has some more important methods

list.append(x)
Add an item to the end of the list. Equivalent to a[len(a):] = [x].

list.extend(iterable)
Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.

list.insert(i, x)
Insert an item at a given position. The first argument is the index of the element before which to insert, so a.insert(0, x) inserts at the front of the list, and a.insert(len(a), x) is equivalent to a.append(x).

list.remove(x)
Remove the first item from the list whose value is x. It is an error if there is no such item.

list.pop([i])
Remove the item at the given position in the list, and return it. If no index is specified, a.pop() removes and returns the last item in the list. (The square brackets around the i in the method signature denote that the parameter is optional, not that you should type square brackets at that position. You will see this notation frequently in the Python Library Reference.)

list.clear()
Remove all items from the list. Equivalent to del a[:].

list.index(x[, start[, end]])
Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.

The optional arguments start and end are interpreted as in the slice notation and are used to limit the search to a particular subsequence of the list. The returned index is computed relative to the beginning of the full sequence rather than the start argument.

list.count(x)
Return the number of times x appears in the list.

list.sort(key=None, reverse=False)
Sort the items of the list in place (the arguments can be used for sort customization, see sorted() for their explanation).

list.reverse()
Reverse the elements of the list in place.

list.copy()
Return a shallow copy of the list. Equivalent to a[:].

"""

fruits = ['apple', 'banana', 'blueberry', 'cherry', 'kiwi', 'orange', 'grapes', 'pear', 'apple', 'watermelon']
print(fruits)


appleCount = fruits.count('apple')
print(appleCount)

bananaIndex = fruits.index('banana')
print(bananaIndex)

tangoCount = fruits.count('tango')
print(tangoCount)

fruits.reverse()
print(fruits)

fruits.reverse()
print(fruits)

fruits.append('resberry')
print(fruits)

fruits.sort()
print(fruits)


fruits.pop()
print(fruits)

fruits.append('watermelon')
print(fruits)


fruits.pop(3)
print(fruits)


fruits.insert(3, 'blueberry')
print(fruits)


"""
5.1.3. List Comprehensions
List comprehensions provide a concise way to create lists.
Common applications are to make new lists where each element
is the result of some operations applied to each member of another
sequence or iterable, or to create a subsequence of those elements
that satisfy a certain condition.
For example, assume we want to create a list of squares, like:
"""

squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)


squares1 = list(map(lambda x: x * 2, range(100)))
print(squares1)

# OR

squares2 = [x * 2 for x in range(10)]
print(squares2)
