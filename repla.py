
import funcs
NUMBERS = '0123456789'
def all_quotes(code):
        global starts, ends
        starts, ends = set(), set()
        quotes = [["", {}]]
        insidequote = False
        mainquote = "'"
        for i, char in enumerate(code):
            if insidequote:
                condition = ((char == mainquote and code[i-1] != "\\"))
                if mainquote == "#":
                    condition = ((char == "\n"))
                if condition:
                    insidequote = False
                    quotes[-1][1]["end"] = (i)
                    ends.add(i)
                    quotes.append(["", {}])
                else:
                    quotes[-1][0] += char
                
            else:
                if char in ['"', "'", "#"]:
                    insidequote = True
                    mainquote = char
                    quotes[-1][1]["start"] = i
                    starts.add(i)
        if quotes[-1][0] == "":
            del quotes[-1]
        # we never use this but hey, why not return it
        return quotes

def runsc(code, master):
    # Step 1: Get a list of all the words in quotes.
    all_quotes(code)


    # Step 2: Iterate thru all of the keywords, slowly checking and parsing for quotes...
    token = ""
    start = -1
    indiv = list(code)
    skipmode = False
    for i, char in enumerate(indiv):
        if i in starts:
            skipmode = True
        elif i in ends:
            skipmode = False

        if skipmode:
            token = ""
            start = i
            continue
        
        if "".join(indiv[i-1:i+1]) == "++":
            indiv[i-1] = "+=1"
            indiv[i] = ""
        if "".join(indiv[i-1:i+1]) == "--":
            indiv[i-1] = "-=1"
            indiv[i] = ""

        if char.isalpha() or char in (funcs.FUNC_INCLUDE):
            token += char
        elif char == ".":
            # range(x,y) expression
            if indiv[i-1]+char == "..":
                leftp = i-2
                rightp = i+1
                num1 = ""
                num2 = ""
                while indiv[leftp] in NUMBERS:
                    num1 = indiv[leftp] + num1
                    leftp -= 1
                    if leftp < 0:
                        raise SyntaxError("improper from-loop expression")
                while indiv[rightp] in NUMBERS:
                    num2 += indiv[rightp]
                    rightp += 1
                for a in range(leftp+2, rightp):
                    indiv[a] = ""
                indiv[leftp+1] = f"range({num1}, {int(num2)+1})"
            else:
                token = ""
                start = i
        else:
            token = ""
            start = i
        print(2, token)
        if token in master:
            indiv[start+1] = master[token]
            for i in range(start+2,i+1):
                indiv[i] = ""
    code = "".join(indiv)
    return code