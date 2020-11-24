from __future__ import annotations
from typing import Any, List, Tuple, Dict, Callable, Union
from .. import lux
from .. import luxmath
class ImageStyle():
    """
    ImageStyle encapsulates image style settings in a clear and consise way. Get an instance of the active image style using ||lux.getActiveImageStyle()||.
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

    def getBloom(self) -> bool:
        """
        Returns whether bloom is enabled or disabled for the image style.
        """
        pass

    def getChromaticAberration(self) -> bool:
        """
        Returns whether chromatic aberration is enabled or disabled for the image style.
        """
        pass

    def getColor(self) -> bool:
        """
        Returns whether color is enabled or disabled for the photographic image style.
        """
        pass

    def getCurve(self) -> bool:
        """
        Returns whether curve is enabled or disabled for the photographic image style.
        """
        pass

    def getDenoise(self) -> bool:
        """
        Returns whether denoise is enabled or disabled for the image style.
        """
        pass

    def getKind(self) -> int:
        """
        Get image style kind. Returns ||lux.IMAGE_STYLE_BASIC|| or ||lux.IMAGE_STYLE_PHOTOGRAPHIC||
        """
        pass

    def getName(self) -> str:
        """
        Get image style name.
        """
        pass

    def getVignette(self) -> bool:
        """
        Returns whether vignette is enabled or disabled for the image style.
        """
        pass

    def setBloom(self, enable: bool) :
        """
        Enable or disable bloom.
        enable = Boolean value for enabling or disabling bloom. *
        """
        pass

    def setChromaticAberration(self, enable: bool) :
        """
        Enable or disable chromatic aberration.
        enable = Boolean value for enabling or disabling chromatic aberration. *
        """
        pass

    def setColor(self, enable: bool) :
        """
        Enable or disable color for the photographic image style.
        enable = Boolean value for enabling or disabling color. *
        """
        pass

    def setCurve(self, enable: bool) :
        """
        Enable or disable curve for the photographic image style.
        enable = Boolean value for enabling or disabling curve. *
        """
        pass

    def setDenoise(self, enable: bool) :
        """
        Enable or disable denoise.
        enable = Boolean value for enabling or disabling denoise. *
        """
        pass

    def setKind(self, kind: Any) :
        """
        Set image style kind.
        kind = Kind of image style: ||lux.IMAGE_STYLE_BASIC|| or ||lux.IMAGE_STYLE_PHOTOGRAPHIC||. *
        """
        pass

    def setVignette(self, enable: bool) :
        """
        Enable or disable vignette.
        enable = Boolean value for enabling or disabling vignette. *
        """
        pass
