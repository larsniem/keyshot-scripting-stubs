from __future__ import annotations
from typing import Any, List, Tuple, Dict, Callable, Union
from .. import lux
from .. import luxmath
class RenderOptions():
    """
    RenderOptions encapsulates render options in a clear and concise way. The options can be persisted as a dictionary using getDict() and fed to RenderOptions(dict=your_dict) when employing it.
    
    The rendering mode can be found by the "render_mode" key of the dictionary. It can have three values: lux.RENDER_MODE_ADVANCED, lux.RENDER_MODE_TIME, or lux.RENDER_MODE_SAMPLES.
    
    Get an instance of the current render options using ||lux.getRenderOptions()||.
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

    def getDict(self) -> Dict:
        """
        Get specified options as a dictionary. This can be useful to persist options and then supply to a lux.RenderOptions() constructor when needed to render something. Be wary of the version specified in the dictionary, key values will be converted to the latest version automatically.
        """
        pass

    def setAddToQueue(self, add: bool) :
        """
        Instead of rendering immediately then it will be added to the internal KeyShot queue, waiting for processing. Note that a copy of the scene will be saved to disk each time. Call ||lux.processQueue()|| to process the queue and render what has been added to it.
        add = Whether to add to queue or not. *
        """
        pass

    def setAdvancedRendering(self, samples: int) :
        """
        Render in advanced mode with specified samples.
        samples = The number of samples. *
        """
        pass

    def setAntiAliasing(self, level: int) :
        """
        Set anti aliasing level.
        level = Value from 1 to 8. *
        """
        pass

    def setBackgroundRendering(self, ext: bool) :
        """
        Render in external background process. Note that a background window will open and the call-site will return immediately!
        ext = Whether to render in background or not. *
        """
        pass

    def setCausticsQuality(self, quality: int) :
        """
        Set caustics quality.
        quality = Value from 0 to 10 (0 will disable it). *
        """
        pass

    def setDofQuality(self, quality: int) :
        """
        Set depth-of-field quality.
        quality = Value from 1 to 10. *
        """
        pass

    def setGlobalIllumination(self, quality: int) :
        """
        Set global illumination quality.
        quality = Quality from 0 to 5 (0 will disable it). *
        """
        pass

    def setGlobalIlluminationCache(self, enable: bool) :
        """
        Set whether or not to use global illumination cache.
        enable = Use cache. *
        """
        pass

    def setIndirectBounces(self, bounces: int) :
        """
        Set the number of indirect bounces.
        bounces = The number of indirect bounces. *
        """
        pass

    def setMaxSamplesRendering(self, samples: int) :
        """
        Render until max samples is reached.
        samples = Maximum samples. *
        """
        pass

    def setMaxTimeRendering(self, time: float) :
        """
        Render the amount of time specified.
        time = Time in seconds (floating-point number). *
        """
        pass

    def setOutputAlphaChannel(self, enable: bool) :
        """
        Set whether to have alpha channel in output image.
        enable = Use alpha channel or not. *
        """
        pass

    def setOutputAmbientOcclusionPass(self, enable: bool) :
        """
        Output ambient occlusion pass separate to the result.
        enable = Output ambient occlusion pass. *
        """
        pass

    def setOutputCausticsPass(self, enable: bool) :
        """
        Output caustics pass separate to the result.
        enable = Output caustics pass. *
        """
        pass

    def setOutputClownPass(self, enable: bool) :
        """
        Output clown pass separate to the result.
        enable = Output clown pass. *
        """
        pass

    def setOutputDepthPass(self, enable: bool) :
        """
        Output depth pass separate to the result.
        enable = Output depth pass. *
        """
        pass

    def setOutputDiffusePass(self, enable: bool) :
        """
        Output diffuse pass separate to the result.
        enable = Output diffuse pass. *
        """
        pass

    def setOutputDirectLightingPass(self, enable: bool) :
        """
        Output direct lighting pass separate to the result.
        enable = Output direct lighting pass. *
        """
        pass

    def setOutputIndirectLightingPass(self, enable: bool) :
        """
        Output indirect lighting pass separate to the result.
        enable = Output indirect lighting pass. *
        """
        pass

    def setOutputNormalsPass(self, enable: bool) :
        """
        Output normals pass separate to the result.
        enable = Output normals pass. *
        """
        pass

    def setOutputReflectionPass(self, enable: bool) :
        """
        Output reflection pass separate to the result.
        enable = Output reflection pass. *
        """
        pass

    def setOutputRefractionPass(self, enable: bool) :
        """
        Output refraction pass separate to the result.
        enable = Output refraction pass. *
        """
        pass

    def setOutputRenderLayers(self, enable: bool) :
        """
        Output render layers separate to the result
        enable = Output render layers. *
        """
        pass

    def setOutputShadowPass(self, enable: bool) :
        """
        Output shadow pass separate to the result.
        enable = Output shadow pass. *
        """
        pass

    def setPixelBlur(self, blur: float) :
        """
        Set pixel blur.
        blur = Value from 1 to 3. *
        """
        pass

    def setRayBounces(self, bounces: int) :
        """
        Set the number of ray bounces.
        bounces = The number of ray bounces. *
        """
        pass

    def setRegion(self, region: Tuple[float, float, float, float]) :
        """
        Set render region to get subset of image.
        region = Tuple/list of (start x-axis, start y-axis, end x-axis, end y-axis). Use None to unset a region. *
        """
        pass

    def setSendToNetwork(self, send: bool) :
        """
        Instead of rendering locally it can be done using KeyShot Network Rendering.
        send = Whether to send to network or not. *
        """
        pass

    def setShadowQuality(self, quality: int) :
        """
        Set shadow quality.
        quality = Value from 1 to 10. *
        """
        pass

    def setSharpShadows(self, enable: bool) :
        """
        Set whether to have sharp shadows or not.
        enable = Output sharp shadows. *
        """
        pass

    def setSharperTextureFiltering(self, enable: bool) :
        """
        Set whether or not to preserve detail in textures when viewed at grazing angles.
        enable = Output sharper texture filtering. *
        """
        pass

    def setThreads(self, threads: int) :
        """
        Set the number of rendering threads. Zero threads means one thread per core.
        threads = The number of threads. *
        """
        pass
