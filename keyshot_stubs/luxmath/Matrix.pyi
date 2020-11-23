from __future__ import annotations
from typing import Any, List, Tuple, Dict, Callable, Union
from .. import lux
from .. import luxmath
class Matrix():
    """
    Matrix enables mathematical operations of matrices and vectors.
    
    Its constructor takes either a number or a tuple/list of size 16.
    Examples:
      Matrix(3) # -> (3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3)
      Matrix((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)) # -> (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
    """

    def __init__(self, *values) -> None:
        """
        The constructor takes either a number or a tuple/list of size 16.
        Examples:
        Matrix(3) # -> (3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3, 0, 0, 0, 0, 3)
        Matrix((1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)) # -> (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        """
        pass

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

    def add(self, mat: Matrix) -> Matrix:
        """
        Add Matrix to a copy of this Matrix and return the result.
        mat = Matrix to add. *
        """
        pass

    def det(self) -> float:
        """
        Computes the determinant of the Matrix.
        """
        pass

    def dump(self) -> str:
        """
        Returns a string representation of the Matrix.
        """
        pass

    def getTransformation(self) -> Tuple[luxmath.Vector, luxmath.Vector, luxmath.Vector]:
        """
        Get scale, rotate and translate vectors from Matrix.
        """
        pass

    def invert(self)  -> Matrix:
        """
        Inverts the Matrix.
        """
        pass

    def isDeforming(self) -> bool:
        """
        Checks if the Matrix is deforming.
        """
        pass

    def isEqual(self, mat: Matrix) -> bool:
        """
        Checks if the Matrix is equal to the other Matrix.
        mat = Matrix to check equality against. *
        """
        pass

    def isIdentity(self) -> bool:
        """
        Checks if the Matrix is the identity Matrix.
        """
        pass

    def isTranslation(self) -> bool:
        """
        Checks if the Matrix is a translation.
        """
        pass

    def mul(self, mat: Matrix) -> Matrix:
        """
        Multipy Matrix by a copy of this Matrix and return the result.
        mat = Matrix to multiply by. *
        """
        pass

    def normalize(self) -> Matrix:
        """
        Normalizes a copy of the Matrix and return the result.
        """
        pass

    def rotate(self, vec: luxmath.Vector, left: bool = False) -> Matrix:
        """
        Rotate a copy of the Matrix by a Vector and return the result.
        vec = Vector to rotate by. *
        left = Boolean for rotating left (default = False).
        """
        pass

    def rotateAroundAxis(self, axis: luxmath.Vector, angle: float) -> Matrix:
        """
        Rotate a copy of the Matrix around an axis by an angle in degrees and return the result.
        axis = The axis as a Vector. *
        angle = The angle in degrees to rotate by. *
        """
        pass

    def scale(self, val: Union[float, luxmath.Vector]) -> Matrix:
        """
        Scale a copy of the Matrix by a Vector or number and return the result.
        val = Vector or number to scale with. *
        """
        pass

    def scale4(self, num: float) -> Matrix:
        """
        Scale a copy of the Matrix by a number (all entries) and return the result.
        num = Number to scale with. *
        """
        pass

    def scalePos(self, num: float) -> Matrix:
        """
        Scale a copy of the Matrix "position" part by a number and return the result.
        num = Number to scale with. *
        """
        pass

    def setTransformation(self, scale: luxmath.Vector, rotate: luxmath.Vector, trans: luxmath.Vector) :
        """
        Set scale, rotate and translate parts of the Matrix.
        scale = Scale Vector. *
        rotate = Rotate Vector. *
        trans = Translate Vector. *
        """
        pass

    def sub(self, mat: Matrix) -> Matrix:
        """
        Subtract Matrix from a copy of this Matrix and return the result.
        mat = Matrix to subtract. *
        """
        pass

    def translate(self, vec: luxmath.Vector) -> Matrix:
        """
        Translate a copy of the Matrix by a Vector and return the result.
        vec = Vector to translate by. *
        """
        pass

    def transpose(self) -> Matrix:
        """
        Transposes a copy of the Matrix and return the result.
        """
        pass

    def val(self) :
        """
        Returns the data of the Matrix.
        """
        pass
