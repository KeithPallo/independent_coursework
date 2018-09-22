# Given the following classes called location and Campus, shown below

class Location(object):
    # Given class that contains classical 2 dimensional cartesian operations as class methods
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'

class Campus(object):
    # Given class that sets a 0 location for 2 dimensional cartesian coordinate operations
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)

# --------------------------------------------------------------------------------------

class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """

    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """
        self.center_loc = center_loc
        self.tent_loc = tent_loc
        self.list_of_tests = [tent_loc]


    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """

        # Initialize check variable
        sum_check = 0

        # Check that the new tent is the appropriate distance from all current tents
        for i in range(len(self.list_of_tests)):
            if self.list_of_tests[i].dist_from(new_tent_loc) >= 0.5:
                sum_check += 1

        # If it is, then add the tent and return True. Otherwise return False.
        if sum_check == len(self.list_of_tests):
            self.list_of_tests.append(new_tent_loc)
            return True
        else:
            return False

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        try:
            self.list_of_tests.remove(tent_loc)
        except:
            raise ValueError

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """

        # Initialize an empty set
        self.final = []

        # Using the lambda operator, sort the current list of tents by x location
        self.sorted_list = sorted(self.list_of_tests, key=lambda Location: Location.x)

        # Append each tent in order to the new final list and return the list to the user
        for i in range(len(self.sorted_list)):
            self.final.append(str(self.sorted_list[i]))

        return self.final


# ------------------------------------------------------------------------------------------------------------

# Example testing script

c = MITCampus(Location(1,2))

c.add_tent(Location(2,3))
c.add_tent(Location(1,2))
c.add_tent(Location(0,0))
c.add_tent(Location(2,3))

print(c.get_tents())



