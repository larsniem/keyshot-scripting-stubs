from __future__ import annotations
from keyshot_stubs import luxmath
from keyshot_stubs import luxmath
from keyshot_stubs import luxmath
from keyshot_stubs import luxmath
from keyshot_stubs import luxmath
from typing import Any, List, Tuple, Dict, Callable, Union

from .. import luxmath

from .Env import Env as Env
from .ImageStyle import ImageStyle as ImageStyle
from .MultiMaterial import MultiMaterial as MultiMaterial
from .RenderOptions import RenderOptions as RenderOptions
from .SceneNode import SceneNode as SceneNode

DIALOG_CHECK = 4
DIALOG_DOUBLE = 2
DIALOG_FILE = 5
DIALOG_FOLDER = 6
DIALOG_INTEGER = 1
DIALOG_ITEM = 3
DIALOG_LABEL = 7
DIALOG_TEXT = 0
EXPORT_FBX = 1
EXPORT_GLTF = 2
EXPORT_OBJ = 0
EXPORT_SINGLE_COLOR = 0
EXPORT_STL = 4
EXPORT_SUB_DIV_ADAPTIVE = 2
EXPORT_SUB_DIV_EDGE_LENGTH = 1
EXPORT_SUB_DIV_NORMAL = 1
EXPORT_SUB_DIV_POLYCOUNT = 0
EXPORT_TEXS_PROCS_LABELS = 3
EXPORT_TEXTURE_MAPS_ONLY = 2
EXPORT_VERTEX_COLOR = 1
EXPORT_ZPR = 3
IMAGE_STYLE_BASIC = 0
IMAGE_STYLE_PHOTOGRAPHIC = 1
MESSAGE_BOX_CRITICAL = 3
MESSAGE_BOX_INFO = 1
MESSAGE_BOX_WARNING = 2
META_DATA_SIMPLE = 1
META_DATA_XMP = 0
NODE_TYPE_ANIMATION = 3
NODE_TYPE_GROUP = 1
NODE_TYPE_MODEL = 5
NODE_TYPE_MODEL_SET = 4
NODE_TYPE_OBJECT = 2
RENDER_ENGINE_INTERIOR = 1
RENDER_ENGINE_INTERIOR_GPU = 4
RENDER_ENGINE_PRODUCT = 0
RENDER_ENGINE_PRODUCT_GPU = 3
RENDER_MODE_ADVANCED = 0
RENDER_MODE_SAMPLES = 2
RENDER_MODE_TIME = 1
RENDER_OUTPUT_EXR = 2
RENDER_OUTPUT_JPEG = 0
RENDER_OUTPUT_PNG = 5
RENDER_OUTPUT_PSD16 = 8
RENDER_OUTPUT_PSD32 = 7
RENDER_OUTPUT_PSD8 = 6
RENDER_OUTPUT_TIFF32 = 3
RENDER_OUTPUT_TIFF8 = 1
UNIT_CM = 1
UNIT_FT = 3
UNIT_IN = 2
UNIT_M = 4
UNIT_MM = 0
VIEW_BACK = 2
VIEW_BOTTOM = 6
VIEW_FRONT = 1
VIEW_ISOMETRIC = 7
VIEW_LEFT = 3
VIEW_RIGHT = 4
VIEW_TOP = 5
XR_CENTER_CAMERA = 4
XR_CENTER_CAMERA_PIVOT = 5
XR_CENTER_ENVIRONMENT = 1
XR_CENTER_OBJECT = 2
XR_TYPE_CUSTOM = 5
XR_TYPE_HEMISPHERICAL = 3
XR_TYPE_SPHERICAL = 2
XR_TYPE_TUMBLE = 4
XR_TYPE_TURNTABLE = 1

def applyMaterialMapping(dict: Dict[int,str]) :
    """
    Applies a material mapping.
    dict = Dictionary of object IDs to material names. *
    """
    pass

def clearGeometry(ask: bool = False) :
    """
    Clears all geometry in the scene.
    ask = Whether to ask to clear or not (default = false).
    """
    pass

def createMultiMaterial(name: str, mat: luxmath.Matrix) -> MultiMaterial:
    """
    Create a multi-material based on an existing material.
    name = Name of new multi-material. *
    mat = Name of existing material to clone from. Can be a string or list of strings (first item of the list will be used to clone from). *
    """
    pass

def deleteMaterial(name: str) :
    """
    Deletes material from KeyShot context.
    name = Name of material to delete. *
    """
    pass

def dumpTree() -> str:
    """
    Dumps the scene tree as a JSON string.
    """
    pass

def enablePerformanceMode(enable: bool = True) :
    """
    Enable or disable performance rendering mode.
    enable = Whether to enable or not. (default = true)
    """
    pass

def encodeVideo(folder: str, frameFiles: str, videoName: str, fps: int, firstFrame: int, lastFrame: int, keepFrames: int = True, opts: Any = None) :
    """
    Encodes a video from frames of a folder.
    folder = Folder to encode video frames from. *
    frameFiles = Name of the frame files. The extension dictates the image format (can be jpg/jpeg, png, exr, or tif/tiff). *
    videoName = Name of the video file, if any. The extension dictates the video format (can be mp4, mov, avi, or flv). *
    fps = Frames per second. Relates to the number of frames available! *
    firstFrame = Frame to start encoding from (defaults to scene settings).
    lastFrame = Frame to end encoding at (defaults to scene settings).
    keepFrames = Whether to keep the frames after encoding (default = true)
    opts = Options specified as a lux.RenderOptions object (see ||lux.getRenderOptions()||).
    """
    pass

def exportFile(path: str, format: Any, mode: Dict) :
    """
    Export scene to a file of specified format.
    path = Path to export file to. *
    format = Export format can be one of the following values: lux.EXPORT_OBJ, lux.EXPORT_FBX, lux.EXPORT_GLTF (will be saved as GLB if the file extension is '.glb'), lux.EXPORT_ZPR, lux.EXPORT_STL. *
    mode = Optional texture mode dictionary to provide additional information. The dictionary has the following form:
      {"mode": mode}
    where mode can be one of the following values: lux.EXPORT_SINGLE_COLOR (STL + ZPR), lux.EXPORT_VERTEX_COLOR (STL + ZPR), lux.EXPORT_TEXTURE_MAPS_ONLY (ZPR), lux.EXPORT_TEXS_PROCS_LABELS (ZPR). The second and last modes can take additional options:
      {"mode": lux.EXPORT_VERTEX_COLOR,
       "sub_div": sub_div,
       "stop_criteria": stop_criteria,
       "poly_count": poly_count,
       "edge_length": edge_length}
    where sub_div can be either lux.EXPORT_SUB_DIV_NORMAL or lux.EXPORT_SUB_DIV_ADAPTIVE, and stop_criteria can be lux.EXPORT_SUB_DIV_POLYCOUNT or lux.EXPORT_SUB_DIV_EDGE_LENGTH.
      {"mode": lux.EXPORT_TEXS_PROCS_LABELS,
       "texture_size": texture_size}
    where texture_size is a positive integer for the texture size.
    """
    pass

def getActiveConfiguration() -> Dict:
    """
    Returns a dict of the current active configuration.
    """
    pass

def getActiveEnvironment() -> Env:
    """
    Get active environment instance for manipulating and retrieving information.
    """
    pass

def getActiveImageStyle() -> ImageStyle:
    """
    Get active image style instance for manipulating and retrieving information.
    """
    pass

def getActiveStudio() -> str:
    """
    Get active studio name of the scene.
    """
    pass

def getAnimationFrame() -> int:
    """
    Returns the current animation frame.
    """
    pass

def getAnimationInfo() -> Tuple[float, int]:
    """
    Returns information about the animation; the duration in seconds, and the amount of frames.
    """
    pass

def getAnimationTime() -> float:
    """
    Returns the current animation time in seconds.
    """
    pass
# TODO: Not fully tested, result Type, init Type?
def getBrowserDialog(url: str = None, html: str = None, result: Callable[[Dict],None] = None, init: Dict = None) :
    """
    Show browser dialog. Specify either URL or HTML contents.
    url = URL to load inside browser dialog (use 'file:///' to load local files).
    html = HTML contents to load inside browser dialog.
    result = Lambda expression or function to evaluate when "lux.yieldResult(..)" is called in JavaScript on the page inside the browser dialog. It will be invoked with the result dictionary (JS Object) as parameter. Note that the earliest time to use the function in JS is when the page is loaded, i.e. the 'load' event, and up to 500ms later. The functionality is automatically loaded onto the page. (default = None)
    init = Dictionary of data to initialize the "lux.initData" with in JavaScript of the browser dialog. (default = None)
    """
    pass

def getCamera() -> str:
    """
    Retrieves the currently active camera of the scene.
    """
    pass

def getCameraDirection() -> List[float]:
    """
    Gets the direction of the active camera of the scene.
    """
    pass

def getCameraDistance() -> float:
    """
    Get distance from active camera to pivot/look-at point.
    """
    pass

def getCameraLookAt() -> List[float]:
    """
    Gets the lool-at point of the active camera of the scene.
    """
    pass

def getCameraPosition() -> List[float]:
    """
    Gets the position of the active camera of the scene.
    """
    pass

def getCameraUp() -> List[float]:
    """
    Gets the up vector of the active camera of the scene.
    """
    pass

def getCameras() -> List[str]:
    """
    Retrieves the cameras of the scene.
    """
    pass

def getEnvironments() -> List[str]:
    """
    Get list of environents of the scene.
    """
    pass
# TODO: Return Type?
def getExternalFiles() -> List[str]:
    """
    Returns a list of all external files needed by the current scene.
    """
    pass

def getImageStyles() -> List[ImageStyle]:
    """
    Get list of image styles of the scene.
    """
    pass
# TODO: includion_options Type?
def getImportOptions(selected_model_set_ids: List[int], ext: bool, getDefaults: bool = False, inclusion_options: bytes = b"31") -> Dict:
    """
    Returns import options in a dictionary:
     accurate_tessellation: Use alternative tessellation method when available.
     adjust_camera_look_at: Adjust active camera to look at the imported geometry.
     adjust_environment: Adjust environment sphere to fit the imported geometry.
     camera_import: Import cameras if able.
     center_geometry: Center newly added geometry in the scene.
     snap_to_ground: Snap newly imported geometry to the ground plane.
     compute_normals: Compute normals during import, if the format allows.
     geometry_units: The unit of the imported scene, if not automatically detected. Supply as conversion factor from meters, e.g. cm = 100, feet = 3.2808399, etc.
     include_nurbs: Include NURBS data.
     update_mode: If true: Update the active geometry if able. If false: Add the imported model to the root.
     merge_groups: Apply some post import merging to identically named groups.
     merge_objects: Apply some post import merging to identically named objects.
     retain_materials: Apply material changes to the active model to the imported model.
     separate_materials: Ensure that materials are not linked across parts.
     separate_parts: Prevent objects from being merged during import. Certain formats only.
     tessellation_quality: Tessellation quality from 0.0 to 1.0. Higher values should yield more triangles.
     up_vector: Up vector of the source program. x = 0, y = 1, z = 2, -x = 3, -y = 4, -z = 5
     frame: Import a specific animation frame, if able.
     mayaForceVersion: Maya file import depends on a local Maya installation. This option forces the importer to use a specific version. Should be a string representing the year release, e.g. "2013".
     group_by: For importers with multiple grouping options. Group by Layer = 0, Group by Shader = 1, Group by Object = 2.
     model_set_import_to: Which model set to import to. All = 0, Active = 1, Selected = 2, New = 3
    selected_model_set_ids = List of ids of model sets to import to when model_set_import == 2. Get model set id with GetId() on a lux.SceneNode.
    ext = File extension to get specific options.
    getDefaults = Whether to get KeyShot defaults or user settings from a previous import (default = false).
    inclusion_options = A bitwise collection of flags determining which features to import. Set to 31 for all features.
    """
    pass

def getInputDialog(values: List[Tuple], opts: Any, title: str, desc: str = None, id: int = None, apply: Callable[..., Dict] = None) :
    """
    Show dialog according to the arguments provided and return the results. It returns None if cancelled.
    
    For example, to show a dialog asking a string, an integer between 10 and 50 that has default value 42, and an item of [1, 2, 3]:
        values = [("string", lux.DIALOG_TEXT, "Input string:", "hello"),
                  ("int", lux.DIALOG_INTEGER, "Input int:", 42, (10, 50)),
                  (lux.DIALOG_LABEL, "Freestanding label text."),
                  ("item", lux.DIALOG_ITEM, "Select item:", 2, [1, 2, 3])]
        opts = lux.getInputDialog(title = "This is the title", values = values)
    The returned options, with default values, would be:
        {"string": "hello", "int": 42, "item": [1, "2"]}
    
    Another trick is using a lambda when clicking "Apply" so the dialog does not need to close every time, and it gets a more interactive feel.
        values = [("string", lux.DIALOG_TEXT, "Text:", "test")]
        lux.getInputDialog(title = "Testing Apply", values = values,
                           apply = lambda res: print(res))
    In this case it means that whenever "Apply" is clicked the result will be printed to console.
    
    title = Title of the dialog. *
    
    desc = Description of dialog. (default = None) 
    
    values = The values of the dialog to build and show. It expects a list of tuples, one tuple for each control. The tuple must contain four or five values depending on the type: key, type, label, and default value, with the additional constraints value in some cases. The key is a string, the label is a string, the type can be one of the following values: lux.DIALOG_TEXT, lux.DIALOG_INTEGER, lux.DIALOG_DOUBLE, lux.DIALOG_ITEM, lux.DIALOG_CHECK, lux.DIALOG_FILE, lux.DIALOG_FOLDER, or lux.DIALOG_LABEL. If the type is lux.DIALOG_INTEGER or lux.DIALOG_DOUBLE then the extra constraints value must be present in the tuple, which is a tuple of minimum and maximum value, and if the type is lux.DIALOG_ITEM then the extra argument must be a list of items to select from. As a special case, if the type is lux.DIALOG_LABEL then the tuple size must be two and the second value must be a string (if the string contains only dashes then it becomes a horizontal divider). * 
    
    id = Special ID to enable persisting values and when reopening. If given then clicking OK will remember the values so that if the ID is used again then the values will be the default values. Make sure that the ID is unique enough so other scripts won't use it by accident. (default = None)
    
    apply = Lambda expression or function to evaluate when "Apply" is clicked in the dialog. It will be invoked with the result dictionary as parameter. The dialog will not close when "Apply" is clicked. (default = None)
    """
    pass

def getInputDouble(title: str, label: str, value: float = 0, min: int = -2147483647, max: int = 2147483647, decimal: int = 1) -> float:
    """
    Show dialog to input a double.
    title = Title of the dialog (default = "Enter double").
    label = Label of the dialog (default = "Enter double:").
    value = Initial value (default = 0).
    min = Minimum value (default = -2147483647).
    max = Maximum value (default = 2147483647).
    decimal = Maximum number of decimal places (default = 1).
    """
    pass

def getInputFile(multiple: Any = False, title: str = "", folder: str = None, filter: str = None) -> str:
    """
    Show dialog to select file(s) from the file system.
    multiple = If multiple files can be selected (default = false).
    title = Title of the dialog (default = "Select file(s)").
    folder = The folder to show initially (default = home folder).
    filter = Filter of files to allow selection from (default = none). An example could be "*.obj *.bip" for all OBJs and BIPs.
    """
    pass

def getInputFolder(title: str, folder: str = None) -> str:
    """
    Show dialog to select a folder from the file system.
    title = Title of the dialog (default = "Select folder").
    folder = The folder to show initially (default = home folder).
    """
    pass

def getInputInt(title: str, label: str, value: float = 0, min: int = -2147483647, max: int = 2147483647, step: float = 1) -> int:
    """
    Show dialog to input an integer.
    title = Title of the dialog (default = "Enter integer").
    label = Label of the dialog (default = "Enter integer:").
    value = Initial value (default = 0).
    min = Minimum value (default = -2147483647).
    max = Maximum value (default = 2147483647).
    step = Stepping amount (default = 1).
    """
    pass

def getInputItem(items: Union[List, Tuple], title: str, label: str, current: int = 0, editable: bool = True) -> int:
    """
    Show dialog to select an item from a list/tuple of items.
    items = List/tuple of items to choose from. *
    title = Title of the dialog (default = "Select item").
    label = Label of the dialog (default = "Select item:").
    current = Index of initial item (default = 0).
    editable = If editable or not (default = true).
    """
    pass

def getInputText(title: str, label: str, value: str = None) -> str:
    """
    Show dialog to input a string.
    title = Title of the dialog (default = "Enter text").
    label = Label of the dialog (default = "Enter text:").
    value = Initial value (default = empty string).
    """
    pass

def getKeyShotVersion() -> Tuple[int, int, int, str]:
    """
    Returns the KeyShot version as (major, minor, build, arch) tuple, where arch is either "32 bit" or "64 bit".
    """
    pass

def getLibraryBackplates(filter: str) -> List[str]:
    """
    Gets all backplates of the library.
    filter = Filter by relative path in library, e.g. 'Backplates/Outdoor'.
    """
    pass

def getLibraryEnvironments(filter: str) -> List[str]:
    """
    Gets all environments of the library.
    filter = Filter by relative path in library, e.g. 'Environments/Studio/Basic'.
    """
    pass

def getLibraryMaterials(filter: str) -> List[str]:
    """
    Gets all materials of the library.
    filter = Filter by relative path in library, e.g. 'Materials/Metal/Titanium'.
    """
    pass

def getLibraryTextures(filter: str) -> List[str]:
    """
    Gets all textures of the library.
    filter = Filter by relative path in library, e.g. 'Textures/Wood'.
    """
    pass

def getLightingPreset() -> str:
    """
    Get currently used lighting preset.
    """
    pass

def getLightingPresets() -> List[str]:
    """
    Get list of lighting presets, both default and custom ones.
    """
    pass

def getMaterialMapping() -> Dict[int, str]:
    """
    Gets material mapping: object ID -> material name.
    """
    pass

def getMaterialTemplates() -> List[str]:
    """
    Gets material template names.
    """
    pass

def getMessageBox(msg: str, title: str, type: Any = MESSAGE_BOX_INFO) :
    """
    Show message box.
    msg = Descriptive text of message box. *
    title = Title of message box. Note that it doesn't show on macOS. (default is empty).
    type = Type of message box: lux.MESSAGE_BOX_INFO, lux.MESSAGE_BOX_WARNING, lux.MESSAGE_BOX_CRITICAL (default = lux.MESSAGE_BOX_INFO).
    """
    pass

def getMetaData(format: Any = META_DATA_XMP) :
    """
    Get meta data of scene.
    format = Format of meta data can be lux.META_DATA_SIMPLE (simple format .meta) or lux.META_DATA_XMP (XML). (default = XMP)
    """
    pass

def getModelSets() -> List[str]:
    """
    Returns the list of active model sets.
    """
    pass

def getMultiMaterial(name: str) -> MultiMaterial:
    """
    Get multi-material instanced from material name.
    name = Name of multi-material. *
    """
    pass

def getOS() -> str:
    """
    Returns the OS version string.
    """
    pass
# TODO: Only takes int, and the returns None??? Exception on list of ints'
def getObjectMaterial(obj: Any) -> List[str]:
    """
    Gets the material applied to the object(s).
    obj = list of IDs. *
    obj = Object ID or list of IDs. *
    """
    pass

def getObjects() -> List[int]:
    """
    Gets the object IDs of the scene.
    """
    pass

def getRenderEngine() -> str:
    """
    Get render engine currently in use.
    """
    pass

def getRenderLayers() -> List[str]:
    """
    Returns a list of render layers in the current scene.
    """
    pass

def getRenderOptions(defaults: bool = False) -> RenderOptions:
    """
    Returns render options as a lux.RenderOptions object. If defaults is set then it will return the internal defaults, otherwise it's the values as they appear in the render dialog.
    defaults = Return defaults or not (default = false).
    """
    pass

def getSceneInfo() -> Dict:
    """
    Returns information about the scene in a dict: name, file name, unit/meter scale and number of triangles, objects, nurbs, curves, scene width/height, and rendering width/height.
    """
    pass

def getSceneMaterials() -> List[str]:
    """
    Gets currently used materials of the scene.
    """
    pass

def getSceneTree() -> SceneNode:
    """
    Get lux.SceneNode object representing the root of the scene tree.
    """
    pass

def getSphericalCamera() -> List[float]:
    """
    Get spherical information in degrees of active camera as a list: azimuth, inclination, and
    twist.
    """
    pass

def getStudios() -> List[str]:
    """
    Get studio names of the scene.
    """
    pass

def hasContents() -> bool:
    """
    Determine if there is any content in the scene.
    """
    pass

def importFile(path: str, showOpts: bool = False, dontAsk: bool = True, opts: Dict = {}) :
    """
    Imports a file.
    path = File path to import. *
    showOpts = Show options dialog (default = false).
    dontAsk = Whether or not to suppress blocking dialogs while script is running, e.g. save scene (default = true).
    opts = Options specified as a dictionary (see ||lux.getImportOptions()||).
    """
    pass

def importMaterials(file: str, folder: str) :
    """
    Imports materials from MTL file into material library.
    file = MTL File path to import materials from. *
    folder = The existing sub material library folder to add the materials to, i.e. 'Glass/Basic' (default = '.', which is the root materials folder).
    """
    pass

def isCameraUnsaved() -> bool:
    """
    Checks if current camera has unsaved changes.
    """
    pass

def isHeadless() -> bool:
    """
    Returns whether KeyShot is running in headless or GUI mode.
    """
    pass

def isPaused() -> bool:
    """
    Checks if renderer is paused.
    """
    pass

def isPerformanceModeEnabled() -> bool:
    """
    Checks if performance rendering mode is enabled.
    """
    pass

def isSceneChanged() -> bool:
    """
    Checks if scene has been changed.
    """
    pass

def isUndoEnabled() -> bool:
    """
    Check whether undo/redo stack is enabled.
    """
    pass

def loadMaterials(file: str) :
    """
    Loads materials from MTL file as in-project materials, i.e. they will not show up in the material library visually.
    file = MTL File path to load materials from. *
    """
    pass

def newCamera(name: str, unique: bool = False) -> bool:
    """
    Creates a new camera and makes it active. If not creating unique name and the name exists then it returns false.
    name = The name of the camera to create. *
    unique = Whether to create a unique name using numbers at the end (default = false)
    """
    pass

def newModelSet(name: str) -> bool:
    """
    Create a new model set.
    name = The name of the new model set to create. *
    """
    pass

def newScene(dontAsk: bool = True) :
    """
    Clears the scene.
    dontAsk = Whether or not to suppress blocking dialogs while script is running, e.g. save scene (default = true).
    """
    pass

def openFile(path: str, dontAsk: bool = True) :
    """
    Opens or imports a file.
    path = File path to open. *
    dontAsk = Whether or not to suppress blocking dialogs while script is running, e.g. save scene (default = true).
    """
    pass

def pause() :
    """
    Pauses renderer.
    """
    pass
# TODO: obj Type? Not working on SceneNodes?
def prettyPrint(obj: Any) :
    """
    Returns pretty representation of input object.
    """
    pass

def processQueue() :
    """
    Process render queue.
    """
    pass

def removeCamera(name: str) :
    """
    Removes a camera.
    name = The name of the camera to remove. *
    """
    pass

def removeModelSet(name: str) :
    """
    Remove a model set. If current model set is to be removed then the default model set is chosen.
    name = The name of the new model set to remove. *
    """
    pass

def renderAnimation(folder: str, frameFiles: str, keepFrames: int = True, width: int = 0, height: float = 0, fps: int = 12, videoName: str = None, opts: RenderOptions = None, format: Any = None) :
    """
    Renders frames of the scene to a folder and/or video file.
    folder = Folder to render frames to. *
    frameFiles = Name of the frame files. The extension dictates the image format (can be jpg/jpeg, png, exr, tif/tiff or psd). (default = "frame.%d.jpg")
    keepFrames = Whether to keep the frames after rendering (default = true).
    width = Resolution width in pixels of the frames (default = scene width).
    height = Resolution height in pixels of the frames (default = scene height).
    fps = Frames per second (default = 12).
    videoName = Name of the video file, if any. The extension dictates the video format (can be mp4, mov, avi, or flv). (default = none)
    opts = Options specified as a lux.RenderOptions object (see ||lux.getRenderOptions()||).
    format = Image format. Can be one of the following values: lux.RENDER_OUTPUT_JPEG, lux.RENDER_OUTPUT_PNG, lux.RENDER_OUTPUT_EXR, lux.RENDER_OUTPUT_TIFF8, lux.RENDER_OUTPUT_TIFF32, lux.RENDER_OUTPUT_PSD8, lux.RENDER_OUTPUT_PSD16, lux.RENDER_OUTPUT_PSD32 (requires file extension to match).
    """
    pass

def renderConfiguration(name: str, folder: str, web: bool = False, modelVariations: bool = False, materialVariations: bool = False, studioVariations: bool = False, iBook: bool = False, iBookWidth: int = 0, iBookHeight: int = 0, opts: Any = 0) :
    """
    Renders a configuration of the scene.
    name = Name of configuration. It must contain an image extension: jpg, jpeg, or png. For images mode the name must also contain '%d'. *
    folder = Folder to render files to. *
    web = Whether or not to render web files (default = False).
    modelVariations = Enable model variations for images mode (default = False).
    materialVariations = Enable material variations for images mode (default = False).
    studioVariations = Enable studio variations for images mode (default = False).
    iBook = Whether or not to produce an iBook widget. Only suitable for Web Configurations. (default = False)
    iBookWidth = Resolution width of the iBook frames. Only suitable when iBook is enabled. (Default = scene width)
    iBookHeight = Resolution height of the iBook frames. Only suitable when iBook is enabled. (Default = scene height)
    opts = Options specified as a lux.RenderOptions object (see ||lux.getRenderOptions()||).
    """
    pass

def renderFrames(folder: str, frameFiles: str, width: int = 0, height: float = 0, fps: int = 12, opts: Any = 0, format: Any = 0) :
    """
    Renders frames of the scene to a folder.
    folder = Folder to render frames to. *
    frameFiles = Name of the frame files. The extension dictates the image format (can be jpg/jpeg, png, exr, tif/tiff or psd). (default = "frame.%d.jpg")
    width = Resolution width in pixels of the frames (default = scene width).
    height = Resolution height in pixels of the frames (default = scene height).
    fps = Frames per second (default = 12).
    opts = Options specified as a lux.RenderOptions object (see ||lux.getRenderOptions()||).
    format = Image format. Can be one of the following values: lux.RENDER_OUTPUT_JPEG, lux.RENDER_OUTPUT_PNG, lux.RENDER_OUTPUT_EXR, lux.RENDER_OUTPUT_TIFF8, lux.RENDER_OUTPUT_TIFF32, lux.RENDER_OUTPUT_PSD8, lux.RENDER_OUTPUT_PSD16, lux.RENDER_OUTPUT_PSD32 (requires file extension to match).
    """
    pass

def renderImage(path: str, width: int = 0, height: float = 0, opts: Any = 0, format: Any = 0) :
    """
    Renders the scene to an image file.
    path = File path to render to. The extension dictates the image format (can be jpg/jpeg, png, exr, tif/tiff or psd). *
    width = Resolution width in pixels of the output image (default = scene width).
    height = Resolution height in pixels of the output image (default = scene height).
    opts = Options specified as a lux.RenderOptions object (see ||lux.getRenderOptions()||).
    format = Image format. Can be one of the following values: lux.RENDER_OUTPUT_JPEG, lux.RENDER_OUTPUT_PNG, lux.RENDER_OUTPUT_EXR, lux.RENDER_OUTPUT_TIFF8, lux.RENDER_OUTPUT_TIFF32, lux.RENDER_OUTPUT_PSD8, lux.RENDER_OUTPUT_PSD16, lux.RENDER_OUTPUT_PSD32 (requires file extension to match).
    """
    pass

def renderMultiMaterial(name: str, folder: str, opts: Any) :
    """
    Renders a multi-material in the scene.
    name = The name of the material or multi-material to apply. It can also be an instance of ||lux.MultiMaterial||. *
    folder = Folder to render files to. *
    opts = Options specified as a lux.RenderOptions object (see ||lux.getRenderOptions()||).
    """
    pass

def renderXR(folder: str, name: str, type: Any = 0, center: Any = 0, width: int = 0, height: int = 0, vwidth: int = 0, vheight: int = 0, hframes: int = 0, vframes: int = 0, hbegin: int = 0, hend: int = 0, vbegin: int = 0, vend: int = 0, opts: Any = 0) :
    """
    Renders a XR from the scene.
    folder = Folder to put results in. *
    name = Name of the XR. *
    type = XR type. (default = lux.XR_TYPE_TURNTABLE)
    center = XR center type. (default = lux.XR_CENTER_OBJECT)
    width = Resolution width in pixels of the frames (default = scene width).
    height = Resolution height in pixels of the frames (default = scene height).
    vwidth = Viewport width in pixels. Will be the size that is displayed in XR. (default = resolution width).
    vheight = Viewport height in pixels. Will be the size that is displayed in XR. (default = resolution height).
    hframes = Horizontal frames. The XR type plays a role here. (default = 0 = use default)
    vframes = Vertical frames. The XR type plays a role here. (default = 0 = use default)
    hbegin = Horizontal angel begin. (only for lux.XR_TYPE_CUSTOM)
    hend = Horizontal angel end. (only for lux.XR_TYPE_CUSTOM)
    vbegin = Vertical angel begin. (only for lux.XR_TYPE_CUSTOM)
    vend = Vertical angel end. (only for lux.XR_TYPE_CUSTOM)
    opts = Explicit render options specified as a lux.RenderOptions object (see ||lux.getRenderOptions()||). NOTE that some values are overwritten by other options provided to this function and internally to suite the XR rendering.
    """
    pass

def saveCamera() :
    """
    Saves current camera if there are unsaved changes.
    """
    pass

def saveFile(path: str) :
    """
    Saves scene to a file. If no path is given then known path is used or a dialog will ask.
    path = File to save to.
    """
    pass

def savePackage(path: str) :
    """
    Saves scene to a KSP package. If no path is given then known path is used or a dialog will ask.
    path = File to save to.
    """
    pass

def screenshot() -> str:
    """
    Take a screenshot of current realtime window state and return the path to it.
    """
    pass

def setActiveEnvironment(name: str) :
    """
    Set active environment of the scene. Use ||lux.getEnvironments()|| to get a list of names.
    name = Name of the environment. *
    """
    pass

def setActiveImageStyle(name: str) :
    """
    Set active image style of the scene. Use ||lux.getImageStyles()|| to get a list of names.
    name = Name of the image style. *
    """
    pass

def setActiveStudio(name: str) :
    """
    Set active studio name of the scene.
    name = Name of studio. *
    """
    pass

def setAnimationFrame(frame: int) :
    """
    Set the animation frame.
    frame = The animation frame number. *
    """
    pass

def setAnimationTime(secs: float) :
    """
    Set the animation time in seconds.
    secs = The animation time in seconds as a floating-point number. *
    """
    pass

def setCamera(camera: str) :
    """
    Sets the active camera of the scene.
    camera = The name of the camera to use. *
    """
    pass

def setCameraDirection(dir: Tuple[float,float,float]) :
    """
    Sets the direction of the active camera of the scene.
    dir = Direction of the camera (x, y, z). *
    """
    pass

def setCameraDistance(dist: float) :
    """
    Set distance from active camera to pivot/look-at point.
    dist = The distance. *
    """
    pass

def setCameraLookAt(obj: int, pt: Tuple[float, float, float]) :
    """
    Set camera to look at an object or a point.
    obj = Object ID.
    pt = Point as tuple (x, y, z).
    """
    pass

def setCameraPosition(pos: Tuple[float, float, float]) :
    """
    Sets the position of the active camera of the scene.
    pos = Position of the camera (x, y, z). *
    """
    pass

def setCameraUp(up: Tuple[float, float, float]) :
    """
    Sets the up vector of the active camera of the scene.
    up = Up vector of the camera (x, y, z). *
    """
    pass

def setLightingPreset(name: str) :
    """
    Set lighting preset to be used.
    name = Name of preset. *
    """
    pass

def setMaterialTemplate(name: str, showSel: bool) :
    """
    Applies a material template to part of the scene or all of it if no argument is given.
    name = Name of the material template. *
    showSel = Show part selection dialog.
    """
    pass

def setModelSets(names: List[str]) :
    """
    Set active model sets and deativate all others. It returns true if all names of model sets could be activated, and thus false even if only some were activated.
    names = The list of names of model sets to activate. Using 'Default' will set the default model set. An empty list deactivates all model sets. *
    """
    pass

def setObjectMaterial(mat: str, obj: int) :
    """
    Applies a material to an object in the scene.
    mat = Material name to apply. *
    obj = Object ID to apply to. *
    """
    pass

def setRenderEngine(engine: Any) :
    """
    Set render engine to use for the scene.
    engine = Type of render engine to use: lux.RENDER_ENGINE_PRODUCT, lux.RENDER_ENGINE_INTERIOR, lux.RENDER_ENGINE_PRODUCT_GPU, or lux.RENDER_ENGINE_INTERIOR_GPU. *
    """
    pass

def setSceneUnit(unit: Any, keep: bool = True) :
    """
    Set scene unit and rescale scene if desired.
    unit = The scene unit can be one of the following values: lux.UNIT_MM, lux.UNIT_CM, lux.UNIT_IN, lux.UNIT_FT, lux.UNIT_M. *
    keep = Whether to keep current size or rescale (default = True).
    """
    pass

def setSphericalCamera(azimuth: float, incl: float, twist: float) :
    """
    Set spherical information of active camera: azimuth, inclination, and twist.
    azimuth = The spherical azimuth in degrees [-180, 180]. *
    incl = The spherical inclination in degrees [-90, 90]. *
    twist = The spherical twist degrees [-180, 180]. *
    """
    pass

def setStandardView(view: Any) :
    """
    Set standard view of currently active camera.
    view = Standard view to set. Must be one of the following: lux.VIEW_FRONT, lux.VIEW_BACK, lux.VIEW_LEFT, lux.VIEW_RIGHT, lux.VIEW_TOP, lux.VIEW_BOTTOM, lux.VIEW_ISOMETRIC. *
    """
    pass

def setUndoEnabled(enable: bool = True) :
    """
    Enable or disable the undo/redo stack. When a script context is destroyed then undo is re-enabled if disabled.
    enable = Enable or not (default = true).
    """
    pass

def sync() :
    """
    Synchronize event queue to enforce pending operations.
    """
    pass

def unpause() :
    """
    Unpauses renderer.
    """
    pass