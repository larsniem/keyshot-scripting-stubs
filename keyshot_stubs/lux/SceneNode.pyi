from __future__ import annotations
from keyshot_stubs import luxmath
from typing import Any, List, Tuple, Dict, Callable, Union
from .. import lux
from .. import luxmath

class SceneNode():
    """
    SceneNode encapsulates a node in the scene tree and enables for manipulation, such as hiding/showing, locking/unlocking, setting materials etc., and traversal of the tree. It provides a means for searching and accessing groups, objects and animations for global and local operations. Get an instance of the root of the scene tree using ||lux.getSceneTree()||.
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

    def applyTransform(self, trans: luxmath.Vector, absolute: bool = False) :
        """
        Apply a transformation (luxmath.Matrix) to the node and its children.
        For example, to scale the node to 1/10 of the size:
          T = luxmath.Matrix().makeIdentity().scale(0.1)
          node.applyTransform(T)
        Where 'node' is your lux.SceneNode.
        Or move an object to absolute position (1, 2, 3):
          T = luxmath.Matrix().makeIdentity().translate(luxmath.Vector((1, 2, 3)))
          node.applyTransform(T, absolute = True)
        
        trans = The transformation (luxmath.Matrix) to apply. *
        absolute = Whether to make an absolute transformation instead of a relative one. Must be an object node for absolute transform. (default = False)
        """
        pass

    def centerAndFit(self) :
        """
        Centers and fits the node.
        """
        pass

    def deselect(self) :
        """
        Visually deselects node in the scene.
        """
        pass

    def dump(self) -> str:
        """
        Returns a string representation of the node and its children.
        """
        pass
    #TODO:Returns Scene Node
    def duplicate(self, amount: int = 1, linkMats: bool = False) -> SceneNode:
        """
        Duplicate current node and subtree.
        amount = The amount of duplicates to create (default = 1).
        linkMats = Whether to link materials or not (default = false).
        """
        pass
    #TODO:Returns List or Tuple?
    def find(self, name: str, mat: luxmath.Matrix, all: bool = False, types: Union[int,List,Tuple] = 0, depth: int = -1) -> List[SceneNode]:
        """
        Find nodes in the subtree of this node by searching part names and material names. If no names or materials are given then it will find everything.
        name = Part name to search for (string/tuple/list). 
        mat = Material name to search for (string/tuple/list). 
        all = Match all part names or all material names (default = false).
        types = Filter results to match types (int/tuple/list) which can be the following the values: lux.NODE_TYPE_GROUP, lux.NODE_TYPE_OBJECT, lux.NODE_TYPE_ANIMATION, lux.NODE_TYPE_MODEL_SET, and lux.NODE_TYPE_MODEL default = all types). 
        depth = The amount of levels to go down the tree. A value of 1 means to only match the direct children of this node etc. (default = -1 = all)
        """
        pass

    def getBoundingBox(self, world: bool = False) -> Tuple[luxmath.Vector, luxmath.Vector]:
        """
        Get bounding box of node as a tuple of two vectors: min and max.
        world = Whether to be in world space or not (default = false).
        """
        pass
    #TODO: Return Type?
    def getCenter(self, world: bool = False) -> Tuple[float, float, float]:
        """
        Get the center of this node.
        world = Whether to be in world space or not (default = false).
        """
        pass
    #TODO: Return Type?
    def getChildren(self) -> List[SceneNode]:
        """
        Get children of group.
        """
        pass
    #TODO: Return Type?
    def getID(self) -> int:
        """
        Get node ID.
        """
        pass

    def getKind(self) -> int:
        """
        Get node kind. Can be one of the following values: lux.NODE_TYPE_GROUP, lux.NODE_TYPE_OBJECT, lux.NODE_TYPE_ANIMATION, lux.NODE_TYPE_MODEL_SET, or lux.NODE_TYPE_MODEL.
        """
        pass
    #TODO: Return Type?
    def getMaterial(self) -> lux.MultiMaterial:
        """
        Get material of a node.
        """
        pass

    def getName(self) -> str:
        """
        Get node name.
        """
        pass

    def getParent(self) -> SceneNode:
        """
        Get parent node of this node.
        """
        pass

    def getPath(self, text: bool = False) -> Tuple[SceneNode, ...]:
        """
        Get path from root to this node as a tuple of lux.SceneNode objects.
        text = Whether to return the names instead of lux.SceneNode objects (default = false).
        """
        pass

    def getRenderLayer(self) -> str:
        """
        Get render layer for associated node, if any.
        """
        pass

    def getTransform(self, world: bool = False) -> luxmath.Matrix:
        """
        Get the transformation matrix of this node.
        world = Whether to be in world space or not (default = false).
        """
        pass

    def hide(self) :
        """
        Hide node.
        """
        pass

    def isAnimation(self) -> bool:
        """
        Check if node is an animation.
        """
        pass

    def isDescendantOf(self, group: Any) -> bool:
        """
        Checks if this node is a descendant of the input group node.
        group = Group node to check sub-tree of. *
        """
        pass

    def isGroup(self) -> bool:
        """
        Check if node is a group.
        """
        pass

    def isHidden(self) -> bool:
        """
        Check if node is hidden.
        """
        pass

    def isLocked(self) -> bool:
        """
        Check if node is locked.
        """
        pass

    def isModel(self) -> bool:
        """
        Check if node is a model (direct child of a model set).
        """
        pass

    def isModelSet(self) -> bool:
        """
        Check if node is a model set.
        """
        pass

    def isObject(self) -> bool:
        """
        Check if node is an object.
        """
        pass

    def isSelected(self) -> bool:
        """
        Check if node is selected in the scene.
        """
        pass

    def lock(self) :
        """
        Lock node.
        """
        pass

    def moveToGroup(self, group: SceneNode) :
        """
        Move this node to another group node. Note: This changes the scene tree.
        group = Group node to move this node to. *
        """
        pass

    def select(self) :
        """
        Visually selects node in the scene.
        """
        pass

    def setMaterial(self, mat: luxmath.Matrix) :
        """
        Set material of a node. If applying to a group then it will apply to all sub nodes.
        mat = The name of the material or multi-material to apply. It can also be an instance of ||lux.MultiMaterial||. *
        """
        pass

    def setName(self, name: str) :
        """
        Set name of node.
        name = New name of node. *
        """
        pass

    def setRenderLayer(self, name: str) :
        """
        Associate node with render layer, creating it if name is non-existent. Current render layer will be unset if name is unspecified or empty.
        name = Render layer name. (See available ones with lux.getRenderLayers())
        """
        pass

    def show(self) :
        """
        Show node if hidden.
        """
        pass

    def snapToGround(self) :
        """
        Snaps node to ground plane.
        """
        pass

    def unlock(self) :
        """
        Unlock node.
        """
        pass
