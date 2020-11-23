from __future__ import annotations
# -*- coding: utf-8 -*-
# AUTHOR Anyone
# VERSION 1.0.0
# Hello World for debugging with PyCharm (2019.2.6)

################################################################################################
# Preprare debugging
################################################################################################
import sys
import os
import pydevd

root = os.path.dirname(__file__)
sys.path.append(root)
os.chdir(root)
# Fix unmappable file/s issue
pydevd.mapping_patches = {"<string>": os.path.basename(__file__)}
print(*sys.path, sep="\n")
################################################################################################
pydevd.settrace('localhost', port=15678, stdoutToServer=True, stderrToServer=True, suspend=True)
from os import path, makedirs
import inspect
import re
from typing import Dict, List
import json

root = os.path.dirname(__file__)
out_dir = os.path.join(root, "keyshot_stubs_raw")
extension = ".pyi"

indent = 4*" "

modules_to_import = [
    "lux",
    "luxmath"
]

default_imports = [
    "from __future__ import annotations",
    "from typing import Any, List, Tuple, Dict, Callable, Union",
]

default_imports_class = default_imports + [
    "from .. import lux",
    "from .. import luxmath",
]

with open(os.path.join(root, "known_parameters.json"), "r", encoding="utf-8") as f:
    known_parameters = json.loads(f.read())
new_parameters = {}


def format_doc(doc: str, indent: str = 4*" "):
    doc = ("\n"+indent).join(doc.splitlines())
    return doc

class Module_:
    def __init__(self):
        self.name: str
        self.functions: List[Method_] = []
        self.classes: List[Class_] = []

class Class_:
    def __init__(self) -> None:
        self.name: str
        self.doc: str
        self.imports: List[str] = []
        self.base_classe: List[str] = []
        self.members: List[Member_]
        
    def render(self):
        text = [
            f"class {self.name}():",
            indent+'"""',
            indent + self.doc,
            indent+'"""'
            ""
        ]

        for member in self.members:
            text += member.render()
            text += [""]
        return text

class Member_:
    def __init__(self) -> None:
        self.name: str
        self.member_type: str
        self.doc: str
        self.cls: Class_ = None
        self.static: bool = False

class Method_(Member_):
    def __init__(self) -> None:
        self.member_type: str = "Method"
        self.params: Dict[str, str] = {}
        self.returns: str = None

    def render(self, indention=indent):
        parameters = []
        for param in self.params.keys():
            p_str = param + ("" if self.params[param] is None else ": " + self.params[param])
            parameters.append(p_str)
        rtype = "" if self.returns is None else (" -> " + self.returns)
        boundparameter = ""
        if self.cls and self.static:
            boundparameter = "cls"
        elif self.cls:
            boundparameter = "self"
        text = [
            indention+f"def {self.name}({boundparameter}{', ' if parameters and self.cls else ''}{', '.join(parameters)}){rtype} :",
            indention+indent+'"""',
            indention+indent+self.doc,
            indention+indent+'"""',
            indention+indent+"pass",
        ]
        return text

class Data_(Member_):
    def __init__(self) -> None:
        super().__init__()
        self.value: object

    def render(self):
        return [f"{self.name} = {self.value}"]

def generate_members(_class, module="", cls=""):
    members = []
    for _,member in inspect.getmembers(_class):
        if(str(member).startswith("<method")):
            members.append(generate_method(member, module, _class))
        # elif(str(member).startswith("<bound method")):
        #     members.append(generate_method(member, module, _class, True))
        else:
            print(f"Member: {member}")
    return members

parameters_regex = re.compile(r'^ {4,8}(\w+) = (.*?)((?:default = (\w+))|$)', flags=re.MULTILINE)
def generate_method(method, module, cls, static=False):
    m = Method_()
    m.name = method.__name__
    doc_indent = 8*" " if cls else 4*" "
    m.doc = format_doc(method.__doc__, doc_indent)
    m.static = static
    m.cls = cls
    m.returns = None
    
    parameters = []
    for parameter in parameters_regex.findall(m.doc):
        if not parameter[0] in known_parameters:
            new_parameters[parameter[0]] = parameter[1]
            m.params[parameter[0]] = ""
        else:
            m.params[parameter[0]] = known_parameters[parameter[0]]
            if parameter[3]:
                default_value = parameter[3]
                if default_value== "false":
                    default_value = "False"
                if default_value == "true":
                    default_value = "True"
                m.params[parameter[0]] = m.params[parameter[0]] + " = " + default_value

    return m

def generate_class(cls, module=""):
    doc = cls.__doc__ if cls.__doc__ else ""
    doc = format_doc(doc, 4*" ")
    c = Class_()
    c.name = cls.__name__
    c.doc = doc
    c.members = generate_members(cls, module, c.name)
    for m in c.members:
        m.cls = c
    return c

def generate_constant(descriptor, module):
    data = Data_()
    data.name = descriptor[0]
    data.value = descriptor[1]
    return data

try:
    for module in modules_to_import:
        print(f"Creating: {module}")
        module_path = path.join(out_dir, os.sep.join(module.split(".")))
        if not path.exists(module_path):
            makedirs(module_path)

        py_module = sys.modules[module]
        init_imports = []
        in_builds = []

        # for name, obj in inspect.getmembers(py_module):
        #     print(f"{name}: {obj}: {type(obj)}: isint? {obj is int}")

        for name, obj in filter(lambda x: type(x[1]) is int, inspect.getmembers(py_module)):
            d = generate_constant((name, obj), module)
            in_builds += d.render()

        for name, obj in inspect.getmembers(py_module, predicate=inspect.isbuiltin):
            f = generate_method(obj, module, None)
            in_builds += f.render("")

        for name, obj in inspect.getmembers(py_module, predicate=inspect.isclass):
            print(obj.__name__)
            c = generate_class(obj, module)
            text = default_imports_class + c.render()
            with open(path.join(module_path, obj.__name__+extension), "w+", encoding="utf-8") as f:
                f.write("\n".join(text))

        with open(path.join(module_path, "__init__"+extension), "w+", encoding="utf-8") as f:
            f.write("\n".join(default_imports + in_builds))

    if new_parameters:
        with open(path.join(out_dir, "new_parameters.json"), "w+", encoding="utf-8") as f:
            f.write(json.dumps(new_parameters, indent="  "))
except Exception as e:
    print(e)
finally:
    pydevd.stoptrace()
