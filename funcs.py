import tkinter as tk
import execute
from tkinter import filedialog

def open_file_dialog():
    return "script.oil"


_PURPLE = {
    "new": "def",
    "body": "class",
    "container": "def",
    "domain": "lambda",
    "object": "class",
    "struct": "class",

    f"{execute.INITMSG}": f"{execute.INITMSG}",
}

_BLUE = {
    "grab": "import",
    "using": "with",
    "void": "pass",
    "attempt": "try",
    "eif": "elif",
    "if": "if",
    "else": "else",
    "then": "finally",
    "this": "self",
    "for": "for",
    "while": "while",
    "serve": "yield",
    "<<": "in",
    "and": "and",
    "or": "or",
    "!!": "not",
    "||": "or",
    "&&": "and",
    "ensure": "if",
    "named": "as",
    "testerr": "assert",
    "send": "async",
    "pause": "await",
    "public": "global",
    "private": "nonlocal",
    "return": "return",
    "err": "raise",
    "pointsto": "is",
    "catch": "except",
    "etr": "from",
    "break": "break",
    "kill": "del",
    "skip": "continue",
    "type": "type",
    "lookup": "match",
    "search": "case",
    "otherwise": "case _",

    "null": "None",
    "false": "False",
    "true": "True",

    # Other
    "turn": "turn",
    "header": "header",
    "forget": "except: pass",
    "imm": "imm",
    "memoize": "memoize",

    #Numerical
    "++": "+=1",
    "--": "-=1",
    

    
}

import keyword
for i in keyword.kwlist:
    if i not in _BLUE.values() and i not in _PURPLE.values():
        print(i)

_PREPROCESSOR = {
    # Rename and Precompile Operations
    "<??>": "<??>",
    "<def>": "<def>",
    "precompile": "precompile",
    "alias": "alias",
    

    # If / mode
    "defined": "defined",
    "ifpublic": "ifpublic",
    "mode": "mode",
    "rmode": "rmode",
    "ifmod": "ifmod",
    "ifnmod": "ifnmod",

    "unsafe": "unsafe",
    "safe": "safe",
    
    "include": "include",


}


_REPLACE_ONLY = {

}

_STATICS = {
    "static": "__init__",
    "@complement": "@staticmethod",
    "@included": "@classmethod",
    "compile>>Python{to=stdterminal}": "compile>>Python{to=stdterminal}"
}

_FUNCS = {
    #I/O

    # "ln": "ln",
    # "lin": "lin",

    #FILE OPERATIONS
    "Filei": "open",
    "Fileo": "close",

    #INTEGERS AND FLOATS
    "longint": "int",
    "shortint": "int",
    "intd": "int",
    "intx": "int",
    "longerint": "int",
    "infint": "float('inf')",
    "bigf": "float",
    "normf": "float",
    "double": "double",

    #LOOP OPERATIONS
    "max": "max",
    "min": "min",
    "+-": "max",
    "-+": "min",
    "clamp": "clamp",
    "from": "range",
    "r++": "reversed",
    "sort": "sorted",
    "long": "len",


    #DATA OPERATIONS
    "get": "zip",
    "vector": "list",
    "each": "map",
    "rep": "format",
    "assign": "enumerate",
    "unmut": "frozenset",
    

    #MATHEMATICAL OPERATIONS
    "|": "abs",
    "abs": "abs",
    "summed": "sum",
    "complexJ": "complex",
    "longdiv": "divmod",
    "pow": "pow",
    "round": "round",
    

    #ITERABLES
    "any": "any",
    "all": "all",
    "asyncit": "aiter",
    "asyncnext": "anext",
    "iterable": "iter",
    "getnext": "next",
    "erad": "filter",

    #TYPES
    "dict": "dict",
    "float": "float",
    "array": "list",
    "str": "str",
    "group": "tuple",
    "bool": "bool",
    "set": "set",
    "type": "type",

    #BASE OPERATIONS
    "ascii": "ascii",
    "b2": "bin",
    "toch": "chr",
    "toint": "ord",
    "b16": "hex",
    "b8": "oct",
    
    #COMPUTABLE OPERATIONS
    "attach": "breakpoint",
    "bytesome": "bytearray",
    "byteone": "bytes",
    "mem": "id",

    #FOLDER, CLASS, AND FUNCTION OPERATIONS
    "isfn": "callable",
    "compile": "compile",
    "scope": "dir",
    "isof": "isinstance",
    "subof": "issubclass",
    "parent": "super",
    "encomp": "hasattr",
    "raw": "repr",
    "structset": "setattr",
    "structget": "getattr",
    "structdel": "delattr",


    
    #VARIABLE OPERATIONS
    "PublicVars": "globals",
    "Hashed": "hash",
    "Variables": "vars",
    "PrivateVars": "locals",
    "Literal": "eval",
    "ExecutePython": "exec",

    #MISC
    "blank": "object",
    "only": "slice",
    "complement": "staticmethod",
    "included": "classmethod",
    "memoryh": "memoryview",
    "prop": "property",

}


_MODS = {
    "chop": "split",
    "add": "append",
}

_SIMPLES = {
    '[]"': 'f"',
    "[]'": "f'",
}

_CLASSES = {
    "wrapper!": "wrapper!",
    "main": "main",
    "lock!": "lock!",
}

_IDECOLOR = [
    "+=", "<<", "-=", "&&", " *", "||", "!!",
]


_ONLYBLUE = {}
for i in _IDECOLOR:
    _ONLYBLUE[i] = i

_VUNCS = _FUNCS.copy()
# for f in _VUNCS.copy():
#     _VUNCS[f+"("] = _VUNCS[f] + "("
#     del _VUNCS[f]

_VODS = _MODS.copy()
# for f in _VODS.copy():
#     _VODS[f+"("] = _VODS[f] + "("
#     del _VODS[f]

_VSTATICS = _STATICS.copy()
# for f in _VSTATICS.copy():
#     _VSTATICS[f+"("] = _VSTATICS[f] + "("
#     del _VSTATICS[f]

FUNC_INCLUDE = ["_", "{", "}", "?", "<", ">", "|", "!", "+", "=", "-", "&", "@"]

Keywords = {**_VUNCS, **_VODS, **_BLUE, **_PURPLE, **_SIMPLES, **_REPLACE_ONLY, **_VSTATICS, **_CLASSES}

KeywordsInversed = {v: k for k, v in Keywords.items()}

Clears = {}
kk = Keywords.copy()
for i in kk:
    if kk[i] not in Keywords:
        Clears[kk[i]] = "x"+kk[i]

# def _PRINTL(v):
#     print(f'{v}')


# _PURPLE = {
#     "<func>": "def",
#     "<class>": "class",
# }

# _BLUE = {
#     "<pair>": "lambda",
#     "<add>": "import",
#     "<per>": "with",
#     "<?>": "pass",
#     "<attempt>": "try",
#     "<ef>": "elif",
#     "<if>": "if",
#     "<else>": "else",
#     "<but>": "finally",
#     "<for>": "for",
#     "<while>": "while",
#     "<give>": "yield",
#     " << ": " in ",
#     " <&> ": " and ",
#     " <|> ": " or ",
#     " <! ": " not ",
#     "<named>": "as",
#     "<test>": "assert",
#     "<send>": "async",
#     "<pause>": "await",
#     "<globe>": "global",
#     "<!l>": "nonlocal",
#     "<return>": "return",
#     "<err>": "raise",
#     "<aterr>": "except",
#     "<using>": "from",
#     "<end>": "break",
#     "<del>": "del",
#     "<skip>": "continue",
#     " ++ ": " += "

    
# }


# _FUNCS = {
#     #I/O
#     'out': "print",
#     "read": "input",
#     "ln": "sys.stdout.write",
#     "lin": "sys.stdin.readline",

#     #HEADERS & CUSTOM FUNCS
#     "acc:Standard": "__FROM_X_IMPORT_SYS8",
#     "indx": "__FROM_X_RANGELEN",
#     "acc:File": "__FROM_X_IMPORT_FILE2",

#     #FILE OPERATIONS
#     "Filei": "open",
#     "Fileo": "close",
#     "Int64": "int",
#     "Int32": "int",
#     "intd": "int",
#     "intb": "__FROM_X_BINARY",
#     "long Int": "int",

#     #LOOP OPERATIONS
#     "++": "max",
#     "--": "min",
#     "from": "range",
#     "rev": "reversed",
#     "sorted": "sort",
#     "long": "len",


#     #DATA OPERATIONS
#     "get": "zip",
#     "array": "list",
#     "each": "map",
#     "rep": "format",
#     "assign": "enumerate",
    

#     #MATHEMATICAL OPERATIONS
#     "|": "abs",
#     "total": "sum",
#     "complexJ": "complex",
#     "divmod": "remainder",
#     "pow": "pow",
    

#     #ITERABLES
#     "anytrue": "any",
#     "alltrue": "all",
#     "async.it": "aiter",
#     "async.next": "anext",
#     "iterable": "iter",
#     "getNext": "next",
    

#     #TYPES
#     "Dict": "dict",
#     "Float": "float",
#     "List": "list",
#     "Str": "str",
#     "Pair": "tuple",
#     "Field": "set",
#     "Type": "type",

#     #BASE OPERATIONS
#     "ascii": "ascii",
#     "b2": "bin",
#     "toChr": "chr",
#     "toNum": "ord",
#     "b16": "hex",
#     "b8": "oct",
    
#     #COMPUTABLE OPERATIONS
#     "hook": "breakpoint",
#     "bytes.some": "bytearray",
#     "bytes.one": "bytes",

#     #FOLDER, CLASS, AND FUNCTION OPERATIONS
#     "isFunc": "callable",
#     "comp": "compile",
#     "scope": "dir",
#     "eval": "Express",
#     "exec": "Equate",
#     "isOf": "isinstance",
#     "subOf": "issubclass",
#     "parent": "super",
#     "isin": "hasattr",
    
#     #VARIABLE OPERATIONS
#     "Globals": "globals",
#     "ConeHash": "hash",
#     "FieldAttribute": "vars",
#     "Locals": "locals",



# }

# _MODS = {
#     ".chop": ".split",
#     ".add": ".append",
    
# }

# _VUNCS = _FUNCS.copy()
# for f in _VUNCS.copy():
#     _VUNCS[f+"("] = _VUNCS[f] + "("
#     del _VUNCS[f]

# _VODS = _MODS.copy()
# for f in _VODS.copy():
#     _VODS[f+"("] = _VODS[f] + "("
#     del _VODS[f]

# Keywords = {**_VUNCS, **_VODS, **_BLUE, **_PURPLE}

# KeywordsInversed = {v: k for k, v in Keywords.items()}

# # def _PRINTL(v):
# #     print(f'{v}')

