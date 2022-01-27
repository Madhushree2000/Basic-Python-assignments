import logging 
class Dict:
    """Consists of all the Dictionary functions"""
    # clear()	    : Removes all the elements from the dictionary
    # copy()	    : Returns a copy of the dictionary
    # fromkeys()	: Returns a dictionary with the specified keys and value
    # get()	        : Returns the value of the specified key
    # items()	    : Returns a list containing a tuple for each key value pair
    # keys()	    : Returns a list containing the dictionary's keys
    # pop()	        :  Removes the element with the specified key
    # popitem()	    : Removes the last inserted key-value pair
    # setdefault()	: Returns the value of the specified key. If the key does not exist,insert the key, with the specified value
    # update()	    : Updates the dictionary with the specified key-value pairs
    # values()	    : Returns a list of all the values in the dictionary
    
    def __init__(self,d):
        if(type(d) == dict):
             self.d = d
        else:
            raise Exception("It is not a dictionary")
        
    logging.basicConfig(filename = "dict.log", level = logging.INFO, 
                    format = '%(asctime)s %(levelname)s %(message)s')

    def clear(self):
            """Removes all the elements from the dictionary"""
            try:
                self.d = {}
                logging.info("Cleared existing dictionary successfully")
                return self.d
            
            except Exception as e:
                    logging.error("Clear function failed " + str(e))

    
    def copy(self):
            """Returns a copy of the list"""
            try:
                logging.info("Copy function successful")
                return self.d
            
            except Exception as e:
                logging.error("Copy function failed " + str(e))


    def get(self,key):
        """Returns the value of the specified key"""
        try:
                x = self.d[key]
                logging.info("Get function successful")
                return x
            
        except Exception as e:
                logging.error("Get function failed " + str(e))

    
    def items(self):
        """Returns a list containing a tuple for each key value pair"""
        try:
            l = []
            for i in self.d:
                 value = self.d[i]
                 tup = (i,value)
                 l.append(tup)
            logging.info("Items function successful")
            return l
            
        except Exception as e:
                logging.error("items function failed " + str(e))


    def keys(self):
        """Returns a list containing the dictionary's keys"""
        try:
            l = []
            for i in self.d:
                l.append(i)
            logging.info("Keys function successful")
            return l
            
        except Exception as e:
                logging.error("Keys function failed " + str(e))


    def pop(self,key):
        """Removes the element with the specified key"""
        try:
             d1 = dict()
             for i in self.d:
                    if (i == key):
                        x = self.d[i]
                        continue
                    else:
                        d1[i] = self.d[i]   
             self.d = d1
             logging.info("Pop function successful")
             return x
                     
        except Exception as e:
                logging.error("Pop function failed " + str(e))

    def popitem(self):
        """Removes the last inserted key-value pair"""
        try:
             d1 = dict()
             keys_list = self.keys()
             key = keys_list[len(keys_list)-1]
             for i in self.d:
                    if (i == key):
                        value = self.d[i]
                        tup = (i,value)
                        continue
                    else:
                        d1[i] = self.d[i]   
             self.d = d1
             logging.info("Popitem function successful")
             return tup
                     
        except Exception as e:
                logging.error("Popitem function failed " + str(e))


    def values(self,key):
        """Returns a list of all the values in the dictionary"""
        try:
             l = []
             for i in self.d:
                    l =  self.d[i] 

             logging.info("Pop function successful")
             return l
                     
        except Exception as e:
                logging.error("Pop function failed " + str(e))


    def update(self,new):
        """Updates the dictionary with the specified key-value pairs"""
        try:
            if type(eval(new)) != dict:
                new = dict(new)
                
            for key in new:
                self.d[key] = new[key]

            logging.info("Update function successful")
            return self.d
                         
        except Exception as e:
                logging.error("Update function failed " + str(e))

    def setdefault(self,key,value = None):
        """Returns the value of the item with the specified key"""
        """If the key does not exist: insert the key, with the specified value"""
        try:
             if key in self.d:
                 ans = self.d[key]
             else:
                 self.d[key] = value

        except Exception as e:
                logging.error("Update function failed " + str(e))
