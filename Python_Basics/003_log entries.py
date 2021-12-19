import logging
import math
#Logging is a kind of debugging method where you get to know where the error occurs by writing into a log file
#the 5 levels of logger is; NOTSET, DEBUG, INFO, WARNING, ERROR, CRITICAL
#Create and Configure logger
LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s" #saves the formatting structure of log file into a variables
logging.basicConfig(filename = "test.log", level = logging.DEBUG, filemode = 'w')

logger = logging.getLogger()


#the actual code starts from here
def quadratic_formula(a,b,c):
    """Return the solutions to the equation ax^2+bx+c = 0"""
    logger.info("quadratic_formula({0},{1},{2})".format(a,b,c))

    #Compute the discriminant
    logger.debug("# Compute the discriminant")
    disc = b**2 - 4*a*c

    #compuute the two roots
    logger.debug("# Compute the two roots")
    root1 = (-b + math.sqrt(disc))/(2*a)
    root2 = (-b - math.sqrt(disc))/(2*a)

    #return the roots
    logger.debug("#return the roots")
    return (root1, root2)

roots = quadratic_formula(1,0,1)
print(roots)
