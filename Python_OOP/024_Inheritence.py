"""
In this, we shall talk about Inheritence
"""

#Inheritence is about branching of classes and inheriting the main class
# properties by the sub-classes

class Person:

    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    def Name(self):
        return (self.firstname + " " + self.lastname)

class Employee(Person):
    #it is a class that uses the methods of Person class and do much more
    #it is a subclass of class Person

    # we could also use::::
    #  super().__init__(first, last)
    #instead of  Person.__init__(self,...)
    
    def __init__(self, first, last, staffnum):
        Person.__init__(self, first, last)
        self.staffnumber = staffnum

    def GetEmployee(self):
        return self.Name() + ", " +  self.staffnumber

x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(x.Name())
print(y.GetEmployee())

#######################################
""" there is a catch, when we defined
    class Employee(Person):

        The Employee class automatically inherits the __init__ method of Person
        Class by default as it is a subclass, but we can override the method
        by defining __init__ method of the Employee class own

"""

# we can generalize the concept of inheritence
#    class SubclassName(BaseClass1, BaseClass2,....BaseClassn):

#we construct a clock class, a calender class, then combine then into another class

class Clock(object):
    """The class Clock is used to simulate a clock."""
    def __init__(self, hours, minutes, seconds):
        self.set_Clock(hours, minutes, seconds)

    def set_Clock(self, hours, minutes, seconds):
        if type(hours) == int and 0 <= hours and hours < 24:
            self._hours = hours
        else:
            raise TypeError("Hours have to be integers between 0 and 23!")
        if type(minutes) == int and 0 <= minutes and minutes < 60:
            self.__minutes = minutes 
        else:
            raise TypeError("Minutes have to be integers between 0 and 59!")
        if type(seconds) == int and 0 <= seconds and seconds < 60:
            self.__seconds = seconds
        else:
            raise TypeError("Seconds have to be integers between 0 and 59!")

    def __str__(self):
        return "{0:02d}:{1:02d}:{2:02d}".format(self._hours, self.__minutes, self.__seconds)

    def tick(self):
        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self._hours == 23:
                    self._hours = 0
                else:
                    self._hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1


class Calendar(object):
    """The class calender implements a calender"""
    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    date_style = "British"

    @staticmethod
    def leapyear(year):
        if not year % 4 == 0:
            return False
        elif not year % 100 == 0:
            return True
        elif not year % 400 == 0:
            return False
        else:
            return True

    def __init__(self, d, m, y):
        self.set_Calendar(d,m,y)

    def set_Calendar(self, d, m, y):
        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__months = m
            self.__years = y
        else:
            raise TypeError("d, m, y have to be integers!")


    def __str__(self):
        if Calendar.date_style == "British":
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__days, self.__months, self.__years)
        else:
            return "{0:02d}/{1:02d}/{2:4d}".format(self.__months, self.__days, self.__years)

    def advance(self):
        max_days = Calendar.months[self.__months-1]
        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days= 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1

            
class CalendarClock(Clock, Calendar):
    def __init__(self,day, month, year, hour, minute, second):
        Clock.__init__(self,hour, minute, second)
        Calendar.__init__(self,day, month, year)

    def tick(self):
        previous_hour = self._hours
        Clock.tick(self)
        if (self._hours < previous_hour): 
            self.advance()

    def __str__(self):
        return Calendar.__str__(self) + ", " + Clock.__str__(self)


x = CalendarClock(31,12,2013,23,59,59)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)

x = CalendarClock(28,2,1900,23,59,59)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)

x = CalendarClock(28,2,2000,23,59,59)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)

x = CalendarClock(7,2,2013,13,55,40)
print("One tick from ",x, end=" ")
x.tick()
print("to ", x)
























