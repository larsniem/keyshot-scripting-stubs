from __future__ import annotations
from typing import Any, List, Tuple, Dict, Callable, Union
from .. import luxmath
class Vector():
    """
    Vector enables mathematical operations of vectors.
    
    Its constructor takes either a tuple/list of three values (x, y, z), a single number as (x, x, x) or three numbers as (x, y, z).
    Examples:
      Vector((1, 2, 3)) # -> (1, 2, 3)
      Vector(1)         # -> (1, 1, 1)
      Vector(1, 2, 3)   # -> (1, 2, 3)
    
    Additionally, whenever a Vector is accepted it is also allowed to give a tuple/list of size 3 or a number.
    Examples:
      Vector(1).add(1)         # -> (2, 2, 2)
      Vector(1).add((1, 2, 3)) # -> (2, 3, 4)
    """
    def __dir__(self) :
        """
        Default dir() implementation.
        """
        pass

    def __format__(self) :
        """
        Default object formatter.
        """
        pass

    def __reduce__(self) :
        """
        Helper for pickle.
        """
        pass

    def __reduce_ex__(self) :
        """
        Helper for pickle.
        """
        pass

    def __sizeof__(self) :
        """
        Size of object in memory, in bytes.
        """
        pass

    def add(self, vec: Vector) -> Vector:
        """
        Adds the Vector to a copy of this Vector and returns the result.
        vec = Vector to add. *
        """
        pass

    def cross(self, vec1: Vector, vec2: Vector) -> Vector:
        """
        Calculates the cross product and returns the result.
        vec1 = Vector one. *
        vec2 = Vector two. *
        """
        pass

    def div(self, num: float) -> Vector:
        """
        Divides a copy of this Vector with a number and returns the result.
        num = Number to divide with. *
        """
        pass

    def getOrthogonalBasis(self) -> Vector:
        """
        Gets the orthogonal basis as two Vectors.
        """
        pass

    def len(self) -> int:
        """
        Returns the length of the Vector.
        """
        pass

    def mul(self, val: Union[float, Vector]) -> Vector:
        """
        Multiplies the Vector or number to a copy of this Vector and returns the result.
        val = Vector or number to multiply with.
        """
        pass

    def normalize(self) -> Vector:
        """
        Normalizes a copy of the Vector and returns the result.
        """
        pass

    def set(self, tup: Tuple) -> Vector:
        """
        Set (x, y, z) values.
        tup = Tuple of size 3 to assign. *
        """
        pass

    def setOrthogonal(self, vec: Vector) -> Vector:
        """
        Sets orthogonal to input Vector.
        vec = Vector make orthogonal to. *
        """
        pass

    def sub(self, vec: Vector) -> Vector:
        """
        Subtracts the Vector from a copy of this Vector and returns the result.
        vec = Vector to subtract. *
        """
        pass

    def val(self) -> Tuple[float,float,float]:
        """
        Returns the values in a tuple (x, y, z).
        """
        pass
