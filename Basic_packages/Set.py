import logging
import random
class Set:
    """Consists of all the set functions"""
    # add()	                 : Adds an element to the set
    # clear()	             : Removes all the elements from the set
    # copy()	             : Returns a copy of the set
    # difference()	         : Returns a set containing the difference between two or more sets
    # difference_update()	 : Removes the items in this set that are also included in another, specified set
    # discard()	             : Remove the specified item
    # intersection()	     : Returns a set, that is the intersection of two or more sets
    # intersection_update()	 : Removes the items in this set that are not present in other, specified set(s)
    # isdisjoint()	         : Returns whether two sets have a intersection or not
    # issubset()	         : Returns whether another set contains this set or not
    # issuperset()	         : Returns whether this set contains another set or not
    # pop()	                 : Removes an element from the set
    # remove()	             : Removes the specified element
    # symmetric_difference() : Returns a set with the symmetric differences of two sets
    # symmetric_difference_update()	: Inserts the symmetric differences from this set and another
    # union()	             : Returns a set containing the union of sets
    # update()	             : Update the set with another set, or any other iterable
    
    def __init__(self,s):

        if(type(s) == set):
             self.s = s
        else:
            raise Exception("Input is not a Set")

        
    logging.basicConfig(filename = "set.log", level = logging.INFO, 
                    format = '%(asctime)s %(levelname)s %(message)s')

    def add(self,value):
        """Adds an element in the set"""
        try:
            self.s = self.s.add(value)
            logging.info("Added %s to the existing set", str(value))
            
        except Exception as e:
            logging.error("Add function failed " + str(e))
            
        else:
            return self.l
        

    def copy(self):
            """Returns a copy of the set"""
            try:
                logging.info("Copy function successful")
                return self.s
            
            except Exception as e:
                logging.error("Copy function failed " + str(e))


    def clear(self):
            """Removes all the elements from the set"""
            try:
                self.l = []
                logging.info("Cleared existing set successfully")
                return self.l
            
            except Exception as e:
                    logging.error("Clear function failed " + str(e))

    
    def difference(self,temp):
        """Returns a set containing the difference between two sets"""
        try:
            diff_set = {}
            if type(temp) == set:
                 for i in self.s:
                     if i not in temp:
                             diff_set.add(i)
                 logging.info("difference function successful")
                 return(diff_set)
            else:
                raise Exception("Please enter a set")

        except Exception as e:
            logging.error("difference function failed " + str(e))


    def difference_update(self,temp):
        """Removes the items which are same in two sets"""
        try:
            diff_set = self.difference(temp)
            self.s = diff_set
            logging.info("difference_update function successful")
            return 

        except Exception as e:
            logging.error("difference_update function failed " + str(e))


    def discard(self,value):
        """Removes the specified item"""
        try:
             s1 = set()
             if value in self.s:
                for i in self.s:
                    if i == value:
                         continue
                    else:
                         s1.add(i)
             logging.info("Discard function successful")
             return s1

        except Exception as e:
            logging.error("Discard function failed " + str(e))
    
    def intersection(self,temp):
        """Returns a set containing the intersection of two sets"""
        try:
            int_set = {}
            if type(temp) == set:
                 for i in self.s:
                     if i in temp:
                             int_set.add(i)
                 logging.info("intersection function successful")
                 return int_set
            else:
                raise Exception("Please enter a set")

        except Exception as e:
            logging.error("intersection function failed " + str(e))


    def intersection_update(self,temp):
        """Removes the items which are non-intersecting of two or more sets"""
        try:
            int_set = self.difference(temp)
            self.s = int_set
            logging.info("intersection_update function successful")
            return

        except Exception as e:
            logging.error("intersection_update function failed " + str(e))


    def symmetric_difference(self,temp):
        """Returns a set with the symmetric differences of two sets"""
        try:
            int_set = {}
            if type(temp) == set:
                 for i in self.s:
                     if i not in temp:
                             int_set.add(i)
                 for i in temp:
                     if i not in self.s:
                             int_set.add(i)
                 logging.info("symmetric_difference function successful")
                 return int_set
            else:
                raise Exception("Please enter a set")

        except Exception as e:
            logging.error("symmetric_difference function failed " + str(e))


    def symmetric_difference_update(self,temp):
        """Remove the items that are present in both sets, AND insert the items that is not present in both sets"""
        try:
            int_set = self.symmetric_difference(temp)
            self.s = int_set
            logging.info("symmetric_difference_update function successful")
            return

        except Exception as e:
            logging.error("symmetric_difference_update function failed " + str(e))


    def isdisjoint(self,temp):
        """Returns whether two sets have a intersection or not"""
        try:
            a = self.intersection(temp)
            if a is not None:
                ans = True
            else:
                ans = False

            logging.info("isdisjoint function successful")
            return ans

        except Exception as e:
            logging.error("isdisjoint function failed " + str(e))


    def issubset(self,temp):
        """Returns whether another set contains this set or not"""
        try:
            flag = 0
            if type(temp) == set:
                 for i in self.s:
                     if i not in temp:
                             flag = 1
                 if flag == 1:
                     ans = False
                 else:
                     ans = True
                 logging.info("issubset function successful")
                 return ans
            else:
                raise Exception("Please enter a set")

        except Exception as e:
            logging.error("issubset function failed " + str(e))


    def issuperset(self,temp):
        """Returns whether this set contains another set or not"""
        try:
            flag = 0
            if type(temp) == set:
                 for i in temp:
                     if i not in self.s:
                             flag = 1
                 if flag == 1:
                     ans = False
                 else:
                     ans = True
                 logging.info("issuperset function successful")
                 return ans
            else:
                raise Exception("Please enter a set")

        except Exception as e:
            logging.error("issuperset function failed " + str(e))


    def pop(self):
        """	Removes a random element from the set"""
        try:
            s1 = list(self.s)
            r = random.choice(s1)
            s2 = set()
            for i in self.s:
                     if (i != r):
                         s2.add(i)
            self.s = s2
            logging.info("Pop function successful")
            return(r)

        except Exception as e:
            logging.error("Pop function failed " + str(e))


    def remove(self,value):
        """Removes the specified element"""
        try:
            s1 = set()
            if value in self.s:
                for i in self.s:
                     if (i != value):
                         s1.add(i)

            logging.info("Element removed successfully")
            return s1

        except Exception as e:
            logging.error("Remove function failed " + str(e))


    def union(self,*args):
        """Returns a set containing the union of sets"""
        try:
            s1 = self.s
            for i in args:
                try:
                     iter(i)
                     s1.add(i) 
                except TypeError:
                     logging.error("Non iterable input") 
                     raise TypeError("{} is not iterable".format(i))
            
            logging.info("Union function successful")
            return s1

        except Exception as e:
            logging.error("Union function failed " + str(e))


    def update(self,value):
        """Updates the set with another set, or any other iterable"""
        try:
            for i in value:
                    self.s.add(i)
            logging.info("Set updated successfully")
            return self.s

        except Exception as e:
            logging.error("Update function failed " + str(e))
