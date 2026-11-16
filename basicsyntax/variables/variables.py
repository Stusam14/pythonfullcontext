# this is for my personal studying , so the might be some mistakes.


# name point to objects in python and assignment rebinds the name, but how.
# names in python are pointers that can point to same object, which begs the question where are these objects
# the reason why python does not have clear types it's because it uses objects for its work.

# e.g
price = 19.99

# python creates the float object with the value 19.99, then goes on to bind the object to the pointer price ,which is not a container for its
# value like in other languages.

# if we reassign the value the old object is simply garbage collected.

print(price)

# doing a reset to the value like this
price = 23.3
# just lives the old object without a label and the garbage collector does its thing.

print(price)

# so the is no actual container(in memory yes ,but the label is a reference or id ) that is holding the value just a label
# i would say the label is a reference since python check to see if the is such a label, and it points to the memory.

print(id(price))

# logic sticks to data types as well

cart = ["apple", "cake", "soup"]
items = cart # these are two variable pointing to the same object.

print(id(items)) # this should give you the objects reference to this object.
print(cart is items) # this return true.

# the is operator check the reference of the names if the are the same if so , its like a function called by one object
# and takes in another then does the check like in C++
# this simply mean a change you do in one object happens to the other.

# so far we have seen that assignment does not copy but shares, like pointers in C
# so to copy we must be very explicit about it , so we use functions like cart.copy -> this one is from object or list(cart) -> this one must be built in

# Rebinding v.s Mutating

items = ["new","list"] # now this no longer points to the original list, whatever you do affects just it.

items = items + [cart] # this creates a new list, the plus again like in C++ is overloaded operator the returned list
                        # is returned from a defensive copy i assume which it's reference is stored in the name.


# Multiple Assignment

name, email, age = "Sarah", "sarah@gmail.com", 60
print(name)
print(email)
print(age)

# this is called tuple unpacking and the number of variable must be the same as the tuple on the right which is evaluated first
# or else we get a value error.

# chaining several names for not mutable object gives us separate object created for each
a = b = c = 0 , # they do not share the same object they are different

# but for mutable object we can have the same one
aa = bb = []
aa.append("same as bb")
# bb gets the same value because they point to the same object

# this should help us get independent empty list
lista, listb = [],[]

# Swapping Values

item1 = "something"
item2 = "something2"

item1,item2 = item2,item1

# you can use this for data types with their elements

# Augmented Assignment
# this is called so many things in different languages so i will just say it's a plus equal operator

# does a quick bind by changing the original value with a new one , so as you might imagine for mutable object this behaves
# differently
total = 0
total += 2
total += 3.5 # this involves implicit conversion and we will talk about that.

# In C the conversion moves from one type to the next dependending on the size, or whether it's a float or int.

# the augmented assignment is for all arithmetic operations we have += , -= , *= , /= ,//= **= ,%=
# like i said for mutable object the is always a rebind to a new object , so keep that in mind cause it makes alot of different.
# but not when you use these operations and that is why python is crazy.

cart1 = ["apple"]
items1 = cart1
items1 += ["pear"]

print(item1)
print(cart1)

# Dynamic Typing

# this means the same name can be used for another object, and the is no size defined container.

order_id = 12345
print(type(order_id))

order_id = "ORD_12345"
print(type(order_id))

order_id = None
print(type(order_id))

# you can have optional type to make the code more verbose e.g quantity: int = 5

# Identifier Rules
# we can start with A-Za-z and (_) underscore.

# deleting a Name with a del

# will remove it from the stack and it won't be available to be used,  but if there are other references to the object
# that points to that name , it will exist because we did not delete it but its name.

price6 = 19.8
print(price6)

del price6
# print(price6) it will give an error

# you won't have to use this alot , maybe for removing item in the list
























