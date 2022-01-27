import logging 
class List:
    """Consists of all the list functions"""

    # append()	: Adds an element at the end of the list
    # clear()	: Removes all the elements from the list
    # copy()	: Returns a copy of the list
    # count()	: Returns the number of elements with the specified value
    # extend()	: Add the elements of a list (or any iterable), to the end of the current list
    # index()	: Returns the index of the first element with the specified value
    # insert()	: Adds an element at the specified position
    # pop()	    : Removes the element at the specified position
    # remove()	: Removes the first item with the specified value
    # reverse()	: Reverses the order of the list
    # sort()	: Sorts the list
 
    def __init__(self,l):

        if(type(l) == list):
             self.l = l
        else:
            raise Exception("Input is not a list")

        
    logging.basicConfig(filename = "list.log", level = logging.INFO, 
                    format = '%(asctime)s %(levelname)s %(message)s')
        
     
    def append(self,value):
        """Adds an element at the end of the list"""
        try:
            self.l = self.l + [value]
            logging.info("Appended %s to the existing list", str(value))
            
        except Exception as e:
            logging.error("Append function failed " + str(e))
            
        else:
            return 
        
   
    def clear(self):
            """Removes all the elements from the list"""
            try:
                self.l = []
                logging.info("Cleared existing list successfully")
                return self.l
            
            except Exception as e:
                    logging.error("Clear function failed " + str(e))
            
        
   
    def copy(self):
            """Returns a copy of the list"""
            try:
                logging.info("Copy function successful")
                return self.l
            
            except Exception as e:
                logging.error("Copy function failed " + str(e))
            
    
    def extend(self,value):
            """Add the elements of a list (or any iterable), to the end of the current list"""
            try:
                for i in value:
                    self.l = self.l + i
                logging.info("Extend function successful")
                return self.l
            
            except Exception as e:
                logging.error("Extend function failed " + str(e))
            
      
    def count(self,value):
            """Returns the number of elements with the specified value"""
            try:
                count = 0
                for i in self.l:
                    if(i == value):
                        count+=1
                logging.info("Count function successful")
                return count
                
            except Exception as e:
                logging.error("Count function failed " + str(e))
        
    
    def index(self,value):
        """Returns the index of the first element with the specified value"""
        try:
                for i in range(len(self.l)):
                    if(self.l[i] == value):
                        break    
                logging.info("Index function successful")
                return i
                
        except Exception as e:
                logging.error("Index function failed " + str(e))
        
        
    def insert(self,value,position):
        """Adds an element at the specified position"""
        try:
                m = self.l[0:position]+ value + self.l[position::]
                logging.info("Inserted %s to the existing list", value)
                return m
            
        except Exception as e:
                logging.error("Insert function failed " + str(e))
        
        
        
    def pop(self, *args):
        """Removes the element at the specified position"""
        try:
                if(args == None):
                    position = len(self.l)-1
                else:
                    position = args[0]
                m = self.l[0:position-1] + self.l[position::]
                n = self.l[position-1]
                self.l = m 
                logging.info("Popped from the %s position of the existing list", str(position))
                return n
            
        except Exception as e:
                logging.error("Pop function failed " + str(e))
        
       
        
    def reverse(self):
        """Reverses the order of the list"""
        try:
                m = self.l[::-1]
                logging.info("Reversing list successful")
                return m
            
        except Exception as e:
                logging.error("Reverse function failed " + str(e))
        
       
      
    def remove(self,value):
        """Removes the first item with the specified value"""
        try:
                for i in range(len(self.l)):
                    if(self.l[i] == value):
                        break
                m = self.l[0:i] 
                n = self.l[i+1:len(self.l)]
                p = m + n
                logging.info("Removed %s from the existing list", str(value))
                return p
            
        except Exception as e:
                logging.error("Remove function failed " + str(e))
        
       
        
    def sort(self):
        """Sorts the list"""
        try:
                for i in range(0,len(self.l)-1):
                    for j in range(0,len(self.l)-1-i):
                        t = self.l[j]
                        self.l[j] = self.l[j+1]
                        self.l[j+1] = t 
                logging.info("Sorting list successful")
                return self.l
                    
        except Exception as e:
                logging.error("Sort function failed " + str(e))
        


    a = [1,2,3,"and,True"]
    a.self.append(45)

 