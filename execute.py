import sys, funcs, time, os, subprocess

def compile(filename):
    if filename.split('.')[1] == "base":
        print("Status: Successfully connected")

        

        s = ""
        master = funcs.Keywords
        with open(filename) as f:
            print("Status: Successfully opened")
            print('\n\n')
            glob = {}
            v = f.read()
            r = v.split("\n")
            v = ""
            for a, i in enumerate(r):
                if i.startswith("<??>"):
                    d = i.split(" ")
                    s1 = "{" + d[2] + "}"
                    s2 = "{" + d[1] + "}"
                    master[s1] = master[s2]
                    del master[s2]
                    v += f"# Defined {s2} as {s1} (Keyword)" + "\n"
                elif i.startswith("<def>"):
                    d = i.split(" ")
                    s1 = d[2] + "("
                    s2 = d[1] + "("
                    master[s1] = master[s2]
                    del master[s2]
                    v += f"# Defined {s2} as {s1} (Function)" + "\n"
                else:
                    v += i + "\n"

                    # SEMICOLONS
                    # j = i.replace(" ", "")
                    # j = j.replace("\r", "")
                    # if len(j) > 1:
                    #     if j[-1] not in [":", ";"]:
                    #         print(f"stderr.err TermError: Unterminated line {a+1}: No endl operator. (Forgot semicolon?)")
                    #         return 0

            for i in master:
                v = v.replace(i, master[i])
            s += v
      
            if "compile>>Python{to=stdterminal}" in v:
                print(s)

            if "def main()" not in s:
                print("\nstderr.err mainError: code missing pilot function main()\n\n")
                return 0

            start = time.time()
            # s += "\r\n" + "from additions import *"
            s += "\r\n" + "if not main(): print('[stderr.err: Process incomplete: main() has not returned True. Manual shutdown.]')"
            end = time.time()

    
            exec(s,glob)

        

        # with open("documents/python/coneide/additions.py") as f:
        #     exec("from additions import *")
        # exec("main()")

        


        print(f"\n\n({filename} executed in {round(end-start, 5)} seconds)")



if __name__ == "__main__":
    compile("/Users/aaravs/Documents/Python/ideBase/script.base")