
# What Type means in Python

# we already established that all values are objects in python , and every object has a type.
# we established that a name can have any type and a type belongs to the value instead.


# you can check the value type in python by using type which ie an equivalent of typeof

"""
so in python we'll use this function to see if we are working with the correct function.

The builtin typee Map

int , float, complex, bool , str, bytes , list, tuple, dict, set, frozenset, NoneType,ect
we have more types that you will know bit by bit.

there are more like paths, queues , fractions,dates,decimals,etc

Numeric Types

Integers, floating Pont numbers, and complex numbers
"""

quantity = 5
price = 29.99
impedance = 4 + 3j

print(type(quantity))
print(type(price))
print(type(impedance))

"""
Remember that bool behave like an int in python like in C , so if you sum your true and false , you get, 2

print(True + True)
print(isinstance(True ,int))

String and Bytes

A string can be written with both quotes double or single.
"""

customer = "Aisha"
product =  'Wireless Mouse'

print(type(customer))
print(len(product))

# string in python are immutable so you can't simply change them , they are immutable in java as well.
# all the operation functions that we use on strings simply written a new string, in other words thy are part of that
# class and then return a defensive copy of the string.

product = "Wireless Mouse"
# product[0] = "w"

# in this case we'll get a new error

"""
the byte type is used mostly for file contents , network packets and image bytes.
we uss a b prefix for it, maybe hex use x , oct used 0 here as well

"""

order_data = "Wireless Mouse"
print(type(order_data))

"""
working with integers is unique because , it return a numeric value instead of 1 character byte object, lets see how.
"""

order_data1 = b"order_id=12345"
print(type(order_data1))
print(order_data1[0]) # return 111  a value instead of a 1 character byte object (not an array of 1s and 0s)


# Sequence : List and Tuple
# these sequences are specialised , like those of binaries and strings.

"""
In python the are two type of General Purpose sequences :
List for mutable types and tuples of immutable types

"""

cart = ["apple", "bread", "milk"]
cart.append("eggs")
print(cart)
print(type(cart))

# tuples use parenthesis or none since the commas do the  real work (this was new to me saw this the other day )

order_position = (37.7749, -122.4194)
customer_info = "Thembi", "Thembi@gmail.com", 28 # I should mention that a tuple like a list it can hold kinds of things.

print(type(order_position))
print(type(customer_info))

# the tuple cannot be changed ,they are used for coordinates ,order's (id,status,total) or as keys in dictionary

# Mappings: Dict

"""
Dictionaries uses keys that are hashable , its the equivalent of a hashmap in java 
"""

customer3 = {
    "name" : "Thembi",
    "email" : "Thembi@gmail.com",
    "orders" : 7
}


print(customer["name"])
print(type(customer))

# you can add and update entries of a dictionary which makes it mutable.
# the order of the dictionary is preserved.
customer3["email"] = "rato@gmail.com"
del custome["orders"] # you can del one on  the data structure values using del
print(customer3)


"""
Sets and Frozensets

A set is an unordered collection of unique (suspicously sets only hold the same type so i don't know what they mean here)

"""

favourite_cat = {"electronics", "books","kitchen"}
favourite_cat.add("electronic")

## this should remove the duplicate

# like in java using contains functions for some of the structures we we have in python we use the overloaded operator
# 'in' to do our check

# the frozen set is the immutable version of the set
# you can use it as a dictionary key.
# sets in python makes it easier to support things like union , intersection, and difference


# None and NoneType






