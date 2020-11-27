from __future__ import annotations
from typing import Any, List, Tuple, Dict, Callable, Union
from .. import lux
from .. import luxmath
class Env():
    """
    Env encapsulates environment settings in a clear and consise way. Get an instance of the active environment using ||lux.getActiveEnvironment()||.
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


    def getBackgroundColor(self) -> Tuple[int, int, int]:
        """
        Get background color as an RGB tuple.
        """
        pass

    def getBackplateImage(self) -> str:
        """
        Get backplate image, if set.
        """
        pass

    def getBrightness(self) -> float:
        """
        Get environment brightness in the form of a float value.
        """
        pass

    def getFlattenGround(self) -> bool:
        """
        Returns whether flattening of the ground is enabled or disabled.
        """
        pass

    def getGroundReflections(self) -> bool:
        """
        Returns whether ground reflections are enabled or disabled.
        """
        pass

    def getGroundShadows(self) -> bool:
        """
        Returns whether ground shadows are enabled or disabled.
        """
        pass

    def getGroundShadowsColor(self) -> Tuple[int,int,int]:
        """
        Get ground shadows color as an RGB tuple.
        """
        pass

    def getGroundSize(self) -> float:
        """
        Get environment ground size.
        """
        pass

    def getHeight(self) -> float:
        """
        Get environment height.
        """
        pass

    def getLightingEnvironment(self) -> str:
        """
        Get the environment image.
        """
        pass

    def getName(self) -> str:
        """
        Get environment name.
        """
        pass

    def getOcclusionGroundShadows(self) -> bool:
        """
        Returns whether occlusion ground shadows are enabled or disabled.
        """
        pass

    def getRotation(self) -> float:
        """
        Get environment rotation.
        """
        pass

    def getSize(self) -> float:
        """
        Get environment size.
        """
        pass

    def setBackgroundColor(self, color: Tuple [int,int,int]) :
        """
        Apply RGB color as the background color.
        color = RGB color tuple. *
        """
        pass

    def setBackplateImage(self, path: str) :
        """
        Applies backplate image to the scene.
        path = Path to the backplate image. *
        """
        pass

    def setBrightness(self, value: float) :
        """
        Set environment brightness.
        value = Brightness value to set in the form of a float. *
        """
        pass

    def setFlattenGround(self, enable: bool) :
        """
        Enable or disable flattening of the ground.
        enable = Boolean value for enabling or disabling flattening of the ground. *
        """
        pass

    def setGroundReflections(self, enable: bool) :
        """
        Enable or disable ground reflections.
        enable = Boolean value for enabling or disabling ground reflections. *
        """
        pass

    def setGroundShadows(self, enable: bool) :
        """
        Enable or disable ground shadows.
        enable = Boolean value for enabling or disabling ground shadows. *
        """
        pass

    def setGroundShadowsColor(self, color: Tuple [int,int,int]) :
        """
        Apply RGB color as the ground shadows color.
        color = RGB color tuple. *
        """
        pass

    def setGroundSize(self, size: float) :
        """
        Set environment ground size.
        size = Environment ground size in the form of a number larger than zero (in meters). *
        """
        pass

    def setHeight(self, height: float) :
        """
        Set environment height.
        height = Environment height in the form of a float value in [-0.5, 0.5]. *
        """
        pass

    def setLightingEnvironment(self, path: str) :
        """
        Applies an image as the scene's lighting environment. When no path is specified then current lighting environment is used, which is useful when switching from backplate or color background to lighitng environment.
        path = Path to the environment image to apply. *
        """
        pass

    def setOcclusionGroundShadows(self, enable: bool) :
        """
        Enable or disable occlusion ground shadows. It is only possible when ground shadows are enabled.
        enable = Boolean value for enabling or disabling occlusion ground shadows. *
        """
        pass

    def setRotation(self, rotation: float) :
        """
        Set environment rotation.
        rotation = Environment rotation in the form of a float value in [0, 360[. *
        """
        pass

    def setSize(self, size: float) :
        """
        Set environment size.
        size = Environment size in the form of a number value in meters. *
        """
        pass
