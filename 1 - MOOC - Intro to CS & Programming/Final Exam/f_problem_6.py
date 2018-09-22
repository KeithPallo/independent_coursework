# Initial class Container is given from the problem. It represents a simple container that can
# hold hashable objects of any type

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """

    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

# ---------------------------------------------------------------------------------------------------------

# First created subclass Bag - can remove, count, or add objects in a container

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of
            times it occurs in self by 1. Otherwise does nothing. """

        # Using built in function try, attempt to remove one occurance of input e
        try:
            self.vals[e] -= 1

        # If an exception is thrown, do nothing and pass
        except:
            pass


    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """

        # Using built in function try, check to see if a value is within the current Bag. If it is, then
        # return the value. If there is an exception raised instead, return 0

        try:
            return self.vals[e]
        except:
            return '0'


    def __add__(self,other):
        # Class method to add two objects of class bag together

        # Create a copy of the current bag
        dict_copy = dict(self.vals)

        # Check to see if there are common keys within each bag. If there are, add their value to the correct
        # key within the copy
        for i in sorted(self.vals.keys()):
            if i in sorted(other.vals.keys()):
                dict_copy[i] = self.vals[i] + other.vals[i]

        # For all other keys that are within bag other, but not within the current bag, add them to the
        # dictionary copy
        for i in sorted(other.vals.keys()):
            if i not in sorted(self.vals.keys()):
                dict_copy[i] = other.vals[i]

        # Resort the dictionary and append all non 0 values to an empty string. Return the string.
        statement = ""
        for i in sorted(dict_copy.keys()):
            if dict_copy[i] != 0:
                statement += str(i)+":"+str(dict_copy[i])+"\n"
        return statement

# ---------------------------------------------------------------------------------------------------------

# Second created subclass ASet - can remove objects from a hashable input, and test to see if a specified
# user input is contained within itself

class ASet(Container):
    def remove(self, e):

        """assumes e is hashable
           removes e from self"""

        # Using built in function try, attempt to remove one occurance of input e
        try:
            del self.vals[e]

        # If an exception is thrown, do nothing and pass
        except:
            pass

    def is_in(self, e):

        # Check to see if input is in the current instance. Return True if it is, otherwise return False
        if e in self.vals.keys():
            return True


        else:
            return False

# ------------------------------------------------------------------------------------------------------------

# Example testing script for Bag

print("Bag Example:")

a = Bag()
a.insert(3)
a.insert(5)
b = Bag()

b.insert(5)
b.insert(5)
b.insert(5)
print(a+b)


# Example testing script for ASet


print("ASet Example:")
d1 = ASet()
d1.insert(4)
d1.insert(4)

d1.remove(2)
print(d1)

d1.remove(4)
print(d1)