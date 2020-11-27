from __future__ import annotations
from typing import Any, List, Tuple, Dict, Callable, Union
from .. import lux
from .. import luxmath
class MultiMaterial():
    """
    MultiMaterial encapsulates access and modification in a clear and consise way. Create a new multi-material using ||lux.createMultiMaterial()|| by giving a name of an existing material to base it off of. Or retrieve a multi-material instance via ||lux.getMultiMaterial()||. A multi-material can be applied to scene nodes by using its name, just like normal materials.
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

    def getActiveMaterial(self) -> MultiMaterial:
        """
        Gets the active sub material of the multi-material.
        """
        pass

    def getName(self) -> str:
        """
        Gets the name of the multi-material.
        """
        pass

    def getSubMaterials(self) -> List[MultiMaterial]:
        """
        Gets the list of sub materials of the multi-material. The order matters.
        """
        pass

    def setActiveMaterial(self, name: str) :
        """
        Set active sub material of multi-material.
        name = Name of sub material to activate. Must be one of the associated sub materia names! *
        """
        pass

    def setName(self, name: str) :
        """
        Set multi-material name.
        name = Name of multi-material. *
        """
        pass

    def setSubMaterials(self, mats: List[str]) :
        """
        Sets the list of sub materials of the multi-material. The order matters.
        mats = The list of materials. *
        """
        pass
