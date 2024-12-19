import tkinter as tk
from tkinter import filedialog

def open_file_dialog():
    return "script.base"
# def open_file_dialog():
#     root = tk.Tk()
#     root.withdraw()  # Hide the main window

#     file_path = filedialog.askopenfilename(
#         title="Select a file",
#         # filetypes=(("Text files", "*.base"), ("All files", "*.*"))
#     )

#     print("whate")
#     root.destroy()
#     return file_path

_PURPLE = {
    "{new}": "def",
    "{body}": "class",
    "{container}": "def",
    "{domain}": "lambda",
}

_BLUE = {
    "{grab}": "import",
    "{using}": "with",
    "{void}": "pass",
    "{attempt}": "try",
    "{elseIf}": "elif",
    "{if}": "if",
    "{else}": "else",
    "{then}": "finally",
    "{for}": "for",
    "{while}": "while",
    "{serve}": "yield",
    " << ": " in ",
    "{and}": "and",
    "{or}": "or",
    "{!}": " not ",
    "{named}": "as",
    "{testerr}": "assert",
    "{send}": "async",
    "{pause}": "await",
    "{public}": "global",
    "{private}": "nonlocal",
    "{return}": "return",
    "{err}": "raise",
    "{catch}": "except",
    "{etr}": "from",
    "{break}": "break",
    "{kill}": "del",
    "{skip}": "continue",
    "{type}": "type",
    "{lookup}": "match",
    "{search}": "case",
    "{otherwise}": "case _",

    # Rename Operations
    "<??>": "<??>",
    "<def>": "<def>",

    
}


_REPLACE_ONLY = {
    "print(": "puts (",
    "input(": "inputs (",
}

_STATICS = {
    "static": "__init__",
    "compile>>Python{to=stdterminal}": "compile>>Python{to=stdterminal}"
}
_FUNCS = {
    #I/O

    # "ln": "ln",
    # "lin": "lin",

    #FILE OPERATIONS
    "Filei": "open",
    "Fileo": "close",
    "longint": "int",
    "shortint": "int",
    "intd": "int",
    "longerint": "int",
    "infint": "float('inf')",

    #LOOP OPERATIONS
    "max": "max",
    "min": "min",
    "++": "max",
    "--": "min",
    "+-": "clamp",
    "from": "range",
    "r++": "reversed",
    "sort": "sorted",
    "long": "len",


    #DATA OPERATIONS
    "get": "zip",
    "array": "list",
    "each": "map",
    "rep": "format",
    "assign": "enumerate",
    

    #MATHEMATICAL OPERATIONS
    "|": "abs",
    "summed": "sum",
    "complexJ": "complex",
    "longdiv": "divmod",
    "pow": "pow",
    

    #ITERABLES
    "any": "any",
    "every": "all",
    "asyncit": "aiter",
    "asyncnext": "anext",
    "iterable": "iter",
    "getNext": "next",
    "erad": "filter",

    #TYPES
    "Dict": "dict",
    "Float": "float",
    "Array": "list",
    "Str": "str",
    "Vector": "tuple",
    "Ring": "set",
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

    #FOLDER, CLASS, AND FUNCTION OPERATIONS
    "isfn": "callable",
    "compile": "compile",
    "scope": "dir",
    "base>>Literal": "eval",
    "base>>py": "exec",
    "isOf": "isinstance",
    "subOf": "issubclass",
    "parent": "super",
    "encomp": "hasattr",
    
    #VARIABLE OPERATIONS
    "base>>Globals": "globals",
    "base>>Hash": "hash",
    "base>>FieldAttrs": "vars",
    "base>>Locals": "locals",



}

_MODS = {
    "chop": "split",
    "add": "append",
}

_SIMPLES = {
    '[]"': 'f"',
    "[]'": "f'",
}

_IDECOLOR = [
    "+=", "<<", "-=", "&&", " *", 
]

_ONLYBLUE = {}
for i in _IDECOLOR:
    _ONLYBLUE[i] = i

_VUNCS = _FUNCS.copy()
for f in _VUNCS.copy():
    _VUNCS[f+"("] = _VUNCS[f] + "("
    del _VUNCS[f]

_VODS = _MODS.copy()
for f in _VODS.copy():
    _VODS[f+"("] = _VODS[f] + "("
    del _VODS[f]

_VSTATICS = _STATICS.copy()
for f in _VSTATICS.copy():
    _VSTATICS[f+"("] = _VSTATICS[f] + "("
    del _VSTATICS[f]

Keywords = {**_VUNCS, **_VODS, **_BLUE, **_PURPLE, **_SIMPLES, **_ONLYBLUE, **_REPLACE_ONLY, **_VSTATICS}

KeywordsInversed = {v: k for k, v in Keywords.items()}



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


