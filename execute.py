import sys, funcs, time, os, subprocess, repla, re
from termcolor import colored

stdo = print
straightCompile = True

def get_space(word):
    pointer = 0
    while word[pointer] == " ":
        pointer += 1
    return " "*pointer
# Function to check if a word is inside quotes
def is_word_in_quotes(text, word):
    # Regex pattern to match text inside single or double quotes
    pattern = r"[\"']([^\"']*?" + re.escape(word) + r"[^\"']*?)[\"']"
    return re.search(pattern, text) is not None

stdo(colored(" rig compiler for oil* ", "black", "on_light_red", ["bold"]))

INITMSG = "oil"

def compiletopy(filename):
    stdo(colored("rig++", "blue") + colored(" run ", "yellow") + "to:  " + colored(" []", "green") + colored("<oilscript.oil>", "light_red"))

    if filename.split('.')[1] == "oil":
        stdo(colored("    Connected", "light_green", None, ["bold"]) + f" | rig (riff v2.1.12)")

        tags = {}
        modetags = []

        s = ""
        master = funcs.Keywords
        with open(filename) as f:
            stdo(colored("      Opening", "light_green", None, ["bold"]) + f" | ({filename})")

            glob = {}
            v = f.read()
            # lines = v.split("\n")
            # for i in funcs.Clears:
            #     for index, line in enumerate(lines):
            #         # Check if line contains no single or double quotes OR if it has a hashtag before it
            #         if ("'" not in line and '"' not in line) or "#" in line:
            #             lines[index] = line.replace(i, funcs.Clears[i])
            # v = "\n".join(lines)

            lines = v.split("\n")

            # for i in funcs.Clears:
            #     for index, line in enumerate(lines):
            #         # Check if line contains no single or double quotes OR if it has a hashtag before it
            #         if ("'" not in line and '"' not in line) or "#" in line:
            #             words = line.split(" ")
            #             for word_index, word in enumerate(words):
            #                 # Check if the word matches `i` with the tight criteria:
            #                 # 1. It's the first word, or there is a space before it.
            #                 # 2. It's the last word, or there is a space after it.
            #                 if word == i or (
            #                     (word.startswith(i) and word[len(i):].strip() == "") or
            #                     (word.endswith(i) and word[:len(i)].strip() == "")
            #                 ):
            #                     words[word_index] = funcs.Clears[i]
            #             # Join the modified words back into the line
            #             lines[index] = " ".join(words)
            # v = "\n".join(lines)

            stdo(colored("      Running", "light_green", None, ["bold"]) + f" | rig run")

            if not v.startswith(f"{INITMSG}"):
                stdo("OilError: oil not initialized.")
                return 0
            else:
                v = v.replace(f"{INITMSG}", "header std.oil")
            w = v
            r = v.split("\n")
            v = ""
            
            ERR__ACCESS = "\n\nCompilation halted: Possible unsafe memory access detected in safe code"
            ERR__UNSAFE = "\n\nProgram may not remain in unsafe mode at end of code"

            stdo(colored("    Compiling", "light_green", None, ["bold"]) + f" | oil -> ({filename})")

            unsafe = False
            needs_build = False

            preprocess = 1

            while preprocess:
                needs_build = False
                for a, i in enumerate(r):
                    if not unsafe:
                        for circumstance in ["header os", "grab os", "etr os"]:
                            if circumstance in i:
                                raise MemoryError(ERR__ACCESS)

                    g = i.strip()
                    if g.startswith("<??>"):
                        d = g.split(" ")
                        s1 = d[2]
                        s2 = d[1]
                        master[s1] = master[s2]
                        del master[s2]
                        v += f"# Defined {s2} as {s1} (Keyword)" + "\n"
                    elif g.startswith("<def>"):
                        d = g.split(" ")
                        s1 = d[2] + "("
                        s2 = d[1] + "("
                        master[s1] = master[s2]
                        del master[s2]
                        v += f"# Defined {s2} as {s1} (Function)" + "\n"
                    elif g.startswith("precompile"):
                        k = i.replace("precompile ", "")
                        v += "# Precompile Instructions" + "\n"
                        if k.startswith("~~main()"):
                            tags["No Main Function"] = 1
                        elif k.startswith("<std/python.oil>"):
                            tags["Compile to Python"] = 1
                        elif k.startswith("domain wrapper!"):
                            v = w.replace("precompile domain wrapper!", "# Wrapped Domain")
                            break
                    # elif g.startswith("quotient"):
                    #     k = i.replace("quotient ", "")
                    #     v += "# Precompile Instructions" + "\n"
                    #     h = g.split()
                    #     condition = h[1]
                    #     exec(f"""def {h[0]}(val1,val2):\n    return val1.{condition}==val2.{condition}""")
                    elif g.startswith("include"):
                        d = g.split(" ")
                        pth = os.getcwd()+"/"+"".join(d[1:len(d)])
                        try:
                            f = open(f"{pth}", "r")
                        except: raise FileNotFoundError("improper filename given to include in program")
                        content = f.read()
                        if content.startswith(INITMSG):
                            content = list(content)
                            for i in range(len(INITMSG)):
                                content[i] = ""
                            content = "".join(content)
                        needs_build = True
                        v += f"# File {pth} begins \n" + content + "\n" + f"# File {pth} ends \n" 

                    elif g.startswith("alias"):
                        k = i.replace("alias ", "")
                        h = g.split()
                        v += f"{get_space(i)}{h[0]} = {h[1]}\n"
                    elif g.startswith("turn"):
                        k = i.replace("turn ", "")
                        h = k.split()
                        v += f"{get_space(i)}{h[0]} = not {h[0]}\n"

                    elif g.startswith("header"):
                        k = i.replace("header ", "")
                        h = k.split()
                        v += f"{get_space(i)}etr {h[0]} grab *\n"

                    elif g.startswith("defined"):
                        if (i.strip())[-1] == ":":
                            k = i.replace("defined ", "")
                            k = k.strip(":")
                            h = k.split()
                            v += f"{get_space(i)}if '{h[0]}' in vars():\n"
                        else: 
                            raise SyntaxError(f'<Line {a+1}> defined precompile operation missing conditional endl operator (missing colon)')
                        
                    elif g.startswith("ifpublic"):
                        if (i.strip())[-1] == ":":
                            k = i.replace("ifpublic ", "")
                            k = k.strip(":")
                            h = k.split()
                            v += f"{get_space(i)}if '{h[0]}' in globals():\n"
                        else: 
                            raise SyntaxError(f'<Line {a+1}> defined precompile operation missing conditional endl operator (missing colon)')
                        
                    elif g.startswith("mode"):
                            k = i.replace("mode ", "")
                            h = k.split()
                            modetags.append(h[0])
                            v += f"# Added a hidden mode\n"
                    
                    elif g.startswith("rmode"):
                            k = i.replace("rmode ", "")
                            h = k.split()
                            if h[0] in modetags:
                                modetags.remove(h[0])
                            else:
                                NameError(f"<Line {a+1}> mode {h[0]} does not exist")
                            v += f"# Removed a hidden mode\n"

                    elif g.startswith("unsafe"):
                        unsafe = True
                        v += f"# Program has become unsafe"+"\n"

                    elif g.startswith("safe"):
                        unsafe = False
                        v += f"# Program has become safe"+"\n"
                        
                    elif g.startswith("ifmod"):
                        if (i.strip())[-1] == ":":
                            k = i.replace("ifmod ", "")
                            k = k.strip(":")
                            h = k.split()
                            v += f"{get_space(i)}if {h[0] in modetags}:\n"
                        else: 
                            raise SyntaxError(f'<Line {a+1}> ifmode precompile operation missing conditional endl operator (missing colon)')
                        
                    elif g.startswith("ifnmod"):
                        if (i.strip())[-1] == ":":
                            k = i.replace("ifnmod ", "")
                            k = k.strip(":")
                            h = k.split()
                            v += f"{get_space(i)}if not {h[0] in modetags}:\n"
                        else: 
                            raise SyntaxError(f'<Line {a+1}> ifnmod precompile operation missing conditional endl operator (missing colon)')

                    elif g.startswith("imm"):
                        if i[0] == " ":
                            raise SyntaxError("-> ImmutableError: \n\nImmutable objects in the form (imm x) must be defined at the base level, not inside a function.\n")
                        k = i.replace("imm ", "")
                        h = k.split("=")
                        name = h[0].strip()
                        val = h[1].strip()
                        if val[-1] in [";", ':']:
                            val = val[0:len(val)-1]
                        v += f"{get_space(i)}statich['{name}'] = {val}; {name}={val}" + "\n"

                    elif g.startswith("memoize"):
                        k = i.replace("memoize ", "")
                        h = k.split(" ")
                        v += f"{get_space(i)}@lru_cache(maxsize = {h[0]}) " + "\n"
                        
                    
                    # elif i.startswith


                    elif i == "lock!":
                        l = len(lines)
                        v += '# Wrapper Locked' +  "\n"
                        v += "\n".join(lines[a+1:l]) + "\n"
                        break
                    else:
                        v += i + "\n"

                if needs_build:
                    r = v.split("\n")
                    v = ""
                    preprocess = 1
                else:
                    preprocess = 0

                    # # SEMICOLONS
                    # j = i.replace(" ", "")
                    # j = j.replace("\r", "")
                    # if len(j) > 1:
                    #         if j[-1] not in [":", ";"]:
                    #             stdo(f"stderr.err TermError: Unterminated line {a+1}: No endl operator. (Forgot semicolon?)")

          
            if unsafe:
                raise MemoryError(ERR__UNSAFE)
            
            v = repla.runsc(v, funcs.Clears)
            v = repla.runsc(v, master)


            s += v


            if "Compile to Python" in tags:
                stdo(s)
            if "No Main Function" not in tags:
                if "Domain Wrapper" in tags:
                    s += "\r\n" + "main()"
                    # s += "\r\n" + "if wrapper_condition:" + "\r\n" + "   main()"
                else:
                    # if "def main()" not in s:
                    #     stdo("\nstderr.err mainError: code missing pilot function main()\n\n")
                    #     return 0
                    # else:
                    s += "\r\n" + "main()" + "\n"

            # s += "\r\n" + "from additions import *"
            
            s += """for i in statich:\n  if id(statich[i]) != id(vars()[i]):\n   raise SyntaxError(f"WARNING: Attempted to change an immutable static variable:\\n             {i} --> {vars()[i]}")"""
            file = "script[Compiled]"
            print(s, 12322)
            if straightCompile: cmp = compile(s, f"{file}.oil", 'exec')
            stdo("rig: " + colored("Established successfully!", "light_green"))
            
            stdo('\n\n')
            start = time.time()
            
            
            f = open("/Users/aaravs/Documents/Python/ideOil/build/script.py", "w")
            f.write(s)
            f.close()
            if straightCompile:
                exec(cmp, glob)
            else:
                subprocess.run(["osascript", "-e", f'tell application "Terminal" to do script "python3 script.py"'])

            end = time.time()

            
        

        # with open("documents/python/coneide/additions.py") as f:
        #     exec("from additions import *")
        # exec("main()")

        

        stdo("\n\nrig: " + colored("Ended successfully!", "light_green"))
        stdo(f"({filename} executed in {round(end-start, 5)} seconds)\n")



if __name__ == "__main__":
    compiletopy("/Users/aaravs/Documents/Python/ideOil/script.oil")

