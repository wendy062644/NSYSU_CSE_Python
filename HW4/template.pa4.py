# Python Programming Assignment #4
#
# The code below is a template for you assignment. Fill in the empty portions,
# according to the indicated instructions.
#
# Rename your file as <studentID>.pa4.py, and submit to the cyber university
# website by Friday, June 14th at 11:59pm. 
#
#Note: I don't care about efficiency; instead, try to keep the code simple.
#
#Note: You can discuss the assignment requirements with your classmates. But
#      you cannot discuss your solutions with your classmates. Don't copy other
#      student's work.


from sys import exc_info
class Point(object):
    """
Point is a class for a 2-dimensional point in cartesian coordinates. 

Defined relational operations are: ==, !=, <, <=, >, and >=
  These operations are a partial order. 
  For example:
      P < Q   if and only if:  P.x()<Q.x()  AND  P.y()<Q.y()

  There are also mathematical operations: +, -, *, /, +=, -=, *=, and /=.
  The meaning of "+" is vector addition (and subtraction, for -). In other 
  words:  P+=Q  means that" P.x+=Q.x()  AND  P.y+=Q.y()
  The meaning of "*" is vector extension (compression, for /). The 2nd operand
  is a scalar extension factor. Eg:  P*=2  ->  P.x*=2  AND  P.y*=2

  The remaining externally-accessed functions are: __init__(), __str__(),
  copy(), len(), repr(), __getitem__ and __setitem.
    """

# Looking at __init__, we see that the point is stored in the attribute, P
# This P is a 2-element tuple. X is the first element and y is the second.
# The heart of the __init__ function is the call to the ConvertTo() function
# that you will have to implement, farther down in this program...
    def __init__(self,a,*b):
        self.P = self.ConvertTo(a,*b)

# Complete the __str__ function. It should print the point's position, in the
# standard format of "(x, y)". Notice the parentheses -- these are universally
# used for printing coordinates, so we have to include them.
    def __str__(self):
        return f"({self.P[0]}, {self.P[1]})" #1

# Complete the __repr__ function.
    def __repr__(self):
        return f"Point({self.P[0]}, {self.P[1]})" #2
    
# For getitem, the index can be 0 or 1 or 'x' or 'y'. Anything else is error.
    def __getitem__(self, i): #3
        if i == 0 or i == 'x':
            return self.P[0]
        elif i == 1 or i == 'y':
            return self.P[1]
        else:
            raise ValueError(f"{i} is not a valid dimension.")

# For setitem, index is as with getitem. But also, the value must be a number.
    def __setitem__(self, i, v): #4
        if not isinstance(v, (int, float)):
            raise ValueError(f"\n  Value Error:{v} is not a number.\n")
        if i == 0 or i == 'x':
            self.P = (v, self.P[1])
        elif i == 1 or i == 'y':
            self.P = (self.P[0], v)
        else:
            raise ValueError(f"\n  Value Error:{i} is not a valid dimension.\n")

# Use math.hypot.  Also round to the nearest integer, because len return ints.
    def __len__(self): #5
        return round((self.P[0] ** 2 + self.P[1] ** 2) ** 0.5)

# Complete all of the mathematical functions below:
    def __eq__(self, *a): #6
        return self.P == a[0].P
    def __ne__(self, *a): #7
        return self.P != a[0].P
    def __lt__(self, *a): #8
        return self.P[0] < a[0].P[0] and self.P[1] < a[0].P[1]
    def __le__(self, *a): #9
        return self.__lt__(*a) or self.__eq__(*a)
    def __gt__(self, *a): #10
        return self.P[0] > a[0].P[0] and self.P[1] > a[0].P[1]
    def __ge__(self, *a): #11
        return self.__gt__(*a) or self.__eq__(*a)

# For +,- you need to create a new Point. I'll do it for you, just in case its
# not clear. But the rest is up to you. Remember that tuples are immutable...
# and remeber to return a value...
    def __add__(self, *a):
        point = Point(*a)
        return Point(self.P[0] + point.P[0], self.P[1] + point.P[1])
    def __sub__(self, *a):
        point = Point(*a)
        return Point(self.P[0] - point.P[0], self.P[1] - point.P[1])

# For *,/ also remember that the you need to create a new Point and that tuples
# are immutable and that you need to return a value. But also remember that *a
# is a scalar (actually a tuple that contains a scalar). Since *a is not a
# coordinate, you won't use it to make your point. Instead, we'll just make a
# placeholder Point, (0,0). In addition, in the code below, I also indicate
# that you must use the GetOperand() method:
    def __mul__(self, *a):
        scalar = self.GetOperand(*a)
        return Point(self.P[0] * scalar, self.P[1] * scalar)
    def __truediv__(self, *a):
        scalar = self.GetOperand(*a)
        if scalar == 0:
            raise ZeroDivisionError("division by zero")
        return Point(self.P[0] / scalar, self.P[1] / scalar)

# For +=, -=, *=, and /=, the simplest solution (not the most efficient, but I
# don't care) is to make use of the above +, -, *, and / methods. Remember to
# return a value.
    def __iadd__(self, *a):
        return self.__add__(*a)
    def __isub__(self, *a):
        return self.__sub__(*a)
    def __imul__(self, *a):
        return self.__mul__(*a)
    def __itruediv__(self, *a):
        return self.__truediv__(*a)

# Fill in the simple code for copy. Remember to return a value.
    def copy(self):
        return Point(self.P[0], self.P[1])

# The GetOperand method is used by __mul__ and __truediv__. Its purpose is to
# make the class flexible to varied input. We want an input like "([([5],)],)"
# to be understood as the simple scalar number 5.
    def GetOperand(self,*a):
        if len(a) == 1:          # This condition tests that "a" only has 1 element.
            operand = self.Collapse(*a) # This function is defined below.
            if isinstance(operand, (int, float, complex)):      # Test if a scalarwas recieved
                return operand        # Return that scalar
        raise SyntaxError("Expected a scalar value")                # raise a SyntaxError exception, with an argument
                           # string indicating that a scalar was not given.

                           
# This method takes a single argument, but which might be wrapped up in lists,
# tuples and Points. The function will remove all of the wrapping and return
# the value. This is hard to explain, but can be illustrated by examples:
#       >>> print(P1.Collapse((1,)))
#       1
#       >>> print(P1.Collapse((1,2)))
#       (1, 2)                                # Notice this answer is one value
#       >>> print(P1.Collapse([1,2]))
#       [1, 2]                                # Notice this answer is one value
#       >>> print(P1.Collapse((([P1],),),))   # Notice this one: P1 is a Point
#       (1, 2)                                # Notice this answer is one value
#       >>> print(P1.Collapse(([([2],)],),))
#       2
#       >>> print(P1.Collapse([(1+2j)]))
#       (1+2j)                                # Notice this answer is one value

    def Collapse(self,a):
        while isinstance(a, (list, tuple)) and len(a) == 1:
            a = a[0]
        if isinstance(a, Point):
            return a.P
        return a


# This is the most complex function. It is used by __init__ to verify that
# the input is a point. it uses Collapse() to reduce the user's input. After
# collapsing, there are a few situations:
#   1. The user had typed something like Point(1,2). This would put the y value
#      into *b.
#   2. The user had typed something like Point(1+2j). This is acceptable. Both
#      x and y will be inside of the one-element a.
#   3. The user had typed sompething like Point(P1) or Point ([1,2]), etc. The
#      x and y will be inside of the two-element a.
#   4. The user typed something wrong. An excception must be raised.
#
# If the user gave a proper input, this function returns a 2-element tuple for
# that coordinate.

    def ConvertTo(self,a,*b):
        collapsed_a = self.Collapse(a)
        if b:
            b = self.Collapse(b[0])
            if isinstance(collapsed_a, complex) or isinstance(b, complex):
                raise SyntaxError(f"\n  Syntax Error:{a},{b} cannot convert to coordinates.\n")
            return (collapsed_a, b)
        if isinstance(collapsed_a, (int, float)):
            return (collapsed_a, 0)
        if isinstance(collapsed_a, (list, tuple)) and len(collapsed_a) == 2:
            if isinstance(collapsed_a[0], complex) or isinstance(collapsed_a[1], complex):
                raise SyntaxError(f"\n  Syntax Error:{collapsed_a[0]},{collapsed_a[1]} cannot convert to coordinates.\n")
            return (collapsed_a[0], collapsed_a[1])
        if isinstance(collapsed_a, complex):
            return (collapsed_a.real, collapsed_a.imag)
        raise SyntaxError(f"\n  Syntax Error:{a},{b} cannot convert to coordinates.\n")


        
# And that is the end of the homework. I'm also giving you the code below, for
# testing:
if __name__ == "__main__":
    P1 = Point(1,2)
    print(P1.Collapse((1,)))
    print(P1.Collapse((1,2)))
    print(P1.Collapse([1,2]))
    print(P1.Collapse((([P1],),),))
    print(P1.Collapse(([([2],)],),))
    print(P1.Collapse([(1+2j)]))
    print('About to try "P1=Point(1,2);P1":',end='')
    try: P1 = Point(1,2);    print('  It should give "(1, 2)":',P1)
    except: print('  This should not have printed.',exc_info()[1])

    print('About to try "len(P1)":',end='')
    try: l=len(P1);    print('  It should round to "2":',l)
    except: print('  This should not have printed.',exc_info()[1])

    print('About to try "Pz=Point(P1);Pz":',end='')
    try: Pz = Point(P1);    print('  It should give "(1, 2)":',Pz)
    except: print('  This should not have printed.',exc_info()[1])


    print('''About to try "P1['y']":''',end='')
    try: y=P1['y'];    print('  It should give "2":',y)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try "P2=Point((2,1));P2":',end='')
    try: P2 = Point((2,1));  print('  It should give "(2, 1)":',P2)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try "P3=Point([1,1]);P3":',end='')
    try: P3 = Point([1,1]);  print('  It should give "(1, 1)":',P3)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try "P4=Point(([([2],)],),2);P4":',end='')
    try: P4 = Point(([([2],)],),2);  print('  It should give "(2, 2)":',P4)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try "P5=Point(3+4j);P5":',end='')
    try: P5 = Point(3+4j);  print('  It should give "(3.0, 4.0)":',P5)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try "P6=P1+P2;P6":',end='')
    try: P6 = P1+P2;  print('  It should give "(3, 3)":',P6)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try "P7=P1-P2;P7":',end='')
    try: P7 = P1-P2;  print('  It should give "(-1, 1)":',P7)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try "P7 += P6;P7":',end='')
    try: P7 += P6;  print('  It should give "(2, 4)":',P7)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try "P8 = P6*4;P8":',end='')
    try: P8 =P6*4;  print('  It should give "(12, 12)":',P8)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try "P8 *= 5;P8":',end='')
    try: P8 *= 5;  print('  It should give "(60, 60)":',P8)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try "P8/=6;P8":',end='')
    try: P8/=6;  print('  It should give "(10.0, 10.0)":',P8)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to try bad syntax "P9 = (1,2j)":',end='')
    try: P9 = Point(1,2j);  print('  This should not have printed.',P9)
    except: print (" Got the expected error:",exc_info()[1])
    print('About to try bad syntax "P9 = (1+1j,2)":',end='')
    try: P9 = Point(1+1j,2);  print('  This should not have printed.',P9)
    except: print (" Got the expected error:",exc_info()[1])
    print('About to test "P1 == P1":',end='')
    try: T1 = P1==P1;  print('  It should give "True":',T1)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to test "P1 == P2":',end='')
    try: T2 = P1==P2;  print('  It should give "False":',T2)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to test "P1 <= P2":',end='')
    try: T3 = P1<P2;  print('  It should give "False":',T3)
    except: print('  This should not have printed.',exc_info()[1])
    print('About to test individual element accessing:',end="")
    try: P1['x']=0.1;  print(f'  It should give 0.1 2:',P1[0],P1[1])
    except: print('  This should not have printed.',exc_info()[1])
    print('About to test a bad access:',end='')
    try: P1[2]=0.01;  print('  This should not have printed.')
    except: print(' Got expected error:',exc_info()[1])
    print('About to test a bad value assignment:',end='')
    try: P1[0]='No';  print('  This should not have printed.')
    except: print(' Got expected error:',exc_info()[1])
