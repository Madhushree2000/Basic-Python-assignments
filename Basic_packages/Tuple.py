import logging 
class List:
    """Consists of all the Tuple functions"""
    # count()	: Returns the number of times a specified value occurs in a tuple
    # index()	: Searches the tuple for a specified value and returns the position of where it was found
    
    def __init__(self,t):

        if(type(t) == tuple):
             self.t = t
        else:
            raise Exception("Input is not a Tuple")

        
    logging.basicConfig(filename = "tuple.log", level = logging.INFO, 
                    format = '%(asctime)s %(levelname)s %(message)s')

    def count(self,value):
            """Returns the number of elements with the specified value occurs in a tuple"""
            try:
                count = 0
                for i in self.t:
                    if(i == value):
                        count+=1
                logging.info("Count function successful")
                return count
                
            except Exception as e:
                logging.error("Count function failed " + str(e))
                
    def index(self,value):
        """Returns the index of the first element with the specified value"""
        try:
                for i in range(len(self.d)):
                    if(self.d[i] == value):
                        break    
                logging.info("Index function successful")
                return i
                
        except Exception as e:
                logging.error("Index function failed " + str(e))
        

    
