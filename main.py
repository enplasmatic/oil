import pygame
import os
import subprocess
import random
import time
import pyperclip
import funcs
import ast
from pygame.mixer import *
from applescript import tell
from std.oil import OILVARS


globalpath = funcs.open_file_dialog()
if globalpath == None:
        globalpath = "script.oil"

# Initialize Pygame
pygame.init()

full_res = False
# Screen dimensions
if not full_res:
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
else:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1400, 750
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("OilScript")
pygame.display.set_icon(pygame.image.load("fonts/oil-icon2.png").convert_alpha())

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (160, 160, 160)
BLUE = (100, 100, 255)
RED = (255, 0, 0)
GREEN = (0, 128, 0)
ORANGE = (255, 140, 0)
PINK = (255, 0, 255)

#  VS CODE DEFAULT COLORS
# LINE_NUMBER_BG = (50,50,50)
# BG_COLOR = (30, 30, 30)
# STRING_COLOR = "#ce9178"
# FUNCTION_COLOR = "#4ec2aa"
# CLASS_COLOR = "#e82c3b"
# KEYWORD_COLOR = "#c586c0"
# MOD_COLOR = "#dcdcaa"
# OBJECT_COLOR = "#FFA453"
# BLUE_COLOR = "#dcdcaa" #"#9cdcfe"
# TYPE_COLOR = "#f92572"
# BOOL_COLOR = "#559dd6"
# COMMENT_COLOR = "#787878"
# PRE_COLOR = "#7ee687"
# DEFAULT_COLOR = "#97d2f3"
# BUTTON_DIV_COLOR = (45,45,45)
# BUTTON_COLOR = (55,55,55)

# SLEEK COLORS
LINE_NUMBER_BG = (33,32,40)
BG_COLOR = (33,32,40)
BUTTON_DIV_COLOR = (23,22,30)
BUTTON_COLOR = (43,42,50)
STRING_COLOR = "#c46f70"
TYPE_COLOR = "#9fdaf0"
BOOL_COLOR = "#f8eca2"
BLUE_COLOR = "#6cb0cc"
MOD_COLOR = "#f8eca2"
OBJECT_COLOR = "#9fdaf0"
CLASS_COLOR = "#6cb0cc"
KEYWORD_COLOR = "#d25f98"
FUNCTION_COLOR = "#68588e"
COMMENT_COLOR = "#787878"
PRE_COLOR = "#7ee687"
DEFAULT_COLOR = "#c3b1dd"



# Fonts
space = 25
# FONT = pygame.font.SysFont("Consolas", space-1)
# FONT = pygame.font.Font("fonts/FSEX300.ttf", space-1)
FONT = pygame.font.Font("fonts/ttf/JetBrainsMono-Regular.ttf", int(space*0.75))
# FONT = pygame.font.Font("fonts/1.ttf", space-1)

# Text editor content
text_lines = [""]
cursor_pos = [0, 0]  # [line, column]
scroll_offset = 0  # Vertical scrolling offset

# Cursor settings
cursor_visible = True
cursor_blink_time = 0.5
last_cursor_toggle = time.time()

typing = False

# Key repeat settings
MAX_HOLD_KEY = 130
HOLD_KEY = MAX_HOLD_KEY  # Time before a key starts repeating
KEY_REPEAT_RATE = 0.05  # Time between repeated key inputs
last_key_time = 0
last_key_event = None

# Syntax highlighting keywords
OBJECTS = set(funcs._PURPLE.keys())
KEYWORDS = set(funcs._BLUE.keys())
FUNCTIONS = set(funcs._FUNCS.keys())
MODS = set(funcs._MODS.keys())
ONLYBLUE = set(funcs._ONLYBLUE.keys())
TYPECACHE = set(funcs._STATICS.keys())
CLASSES = set(funcs._CLASSES.keys())
PREPROCESSORS = set(funcs._PREPROCESSOR.keys())

# TYPECACHE = set(["static("])

NUMBERS = "0123456789"

REPLACABLES = {
    pygame.K_TAB: "    "
}

OLD_FUNCTIONS = FUNCTIONS.copy()


keyboardsfx = []
for i in range(12):
    keyboardsfx.append(Sound(f"sfx/{i}.wav"))

# Button dimensions
BUTTON_WIDTH, BUTTON_HEIGHT = 100, 30
buttons = {
    "Save": pygame.Rect(10, 10, BUTTON_WIDTH, BUTTON_HEIGHT),
    "Load": pygame.Rect(120, 10, BUTTON_WIDTH, BUTTON_HEIGHT),
    "Run": pygame.Rect(230, 10, BUTTON_WIDTH, BUTTON_HEIGHT),
    "CopyAll": pygame.Rect(340, 10, BUTTON_WIDTH, BUTTON_HEIGHT),
    "Copy": pygame.Rect(500, 10, BUTTON_WIDTH, BUTTON_HEIGHT),
    "Paste": pygame.Rect(610, 10, BUTTON_WIDTH, BUTTON_HEIGHT),
}

# Utility functions
def render_highlighted_text():
    """Render text with syntax highlighting and line numbers."""
    y_offset = 50 - scroll_offset
    line_number_width = 40
    for i, line in enumerate(text_lines):
        if y_offset > SCREEN_HEIGHT:  # Skip lines below visible screen
            break
        if y_offset + space >= 50:  # Skip lines above visible screen
            # Draw line number background
            pygame.draw.rect(screen, LINE_NUMBER_BG, (0, y_offset, line_number_width, space))

            # Render line number
            line_number_surface = FONT.render(str(i + 1), True, GRAY)
            screen.blit(line_number_surface, (5, y_offset))

            # Render syntax-highlighted code
            x_offset = line_number_width + 10
            tokens = tokenize_line(line)
            for token, color in tokens:
                text_surface = FONT.render(token, True, color)
                screen.blit(text_surface, (x_offset, y_offset))
                x_offset += text_surface.get_width()
        y_offset += space

def flatten(xss):
    return [x for xs in xss for x in xs]

def tokenize_line(line):
    """Tokenize a line of text for syntax highlighting."""
    tokens = []
    current_token = ""
    current_color = WHITE
    in_string = False
    string_char = ""
    in_comment = False
    i = 0

    while i < len(line):
        char = line[i]
        if in_string:
            current_token += char
            if char == string_char and (i == 0 or line[i - 1] != "\\"):  # End of string
                tokens.append((current_token, STRING_COLOR))
                current_token = ""
                in_string = False
            i += 1
            continue
        elif in_comment:
            current_token += char
            if char == comment_char and (i == 0 or line[i - 1] != "\\"):  # End of string
                tokens.append((current_token, COMMENT_COLOR))
                current_token = ""
                in_comment = False
            i += 1
            continue

        elif char in {"#"}:
            if current_token:
                tokens.append((current_token, current_color))
            current_token = char
            current_color = COMMENT_COLOR
            in_comment = True
            comment_char = char

        
        elif char in {"'", '"'}:
            if current_token:
                tokens.append((current_token, current_color))
            current_token = char
            current_color = STRING_COLOR
            in_string = True
            string_char = char
        # elif char == "#":
        #     if current_token:
        #         tokens.append((current_token, current_color))
        #     current_token = line[i:]
        #     tokens.append((current_token, DARK_GRAY))
        #     break
        elif char.isalpha() or char in funcs.FUNC_INCLUDE:
            if current_token and current_token[0] in NUMBERS:
                tokens.append((current_token, current_color))
                current_token = ""
            current_token += char
            # FILEINQ = set([item for item in dir(build.script) if not item.startswith("__")])

            if current_token in ["True", "False", "null"]:
                current_color = BOOL_COLOR
            elif current_token in PREPROCESSORS:
                current_color = PRE_COLOR
            elif current_token in KEYWORDS:
                current_color = KEYWORD_COLOR
            elif current_token in FUNCTIONS:
                current_color = FUNCTION_COLOR  
            elif current_token in CLASSES:
                current_color = CLASS_COLOR
            elif current_token in OBJECTS:
                current_color = OBJECT_COLOR 
            elif current_token in TYPECACHE:
                current_color = TYPE_COLOR
            elif current_token in MODS:
                current_color = MOD_COLOR 
            elif current_token in ONLYBLUE:
                current_color = BLUE_COLOR
            elif current_token in OILVARS:
                current_color = BLUE_COLOR
            else: 
                current_color = DEFAULT_COLOR
        # elif char in NUMBERS:
        #     if current_token and not current_token[0] in NUMBERS:
        #         tokens.append((current_token, current_color))
        #         current_token = ""
        #     current_token += char
        #     current_color = ORANGE
        else:
            if current_token:
                tokens.append((current_token, current_color))
                current_token = ""
            tokens.append((char, WHITE))
        i += 1

    if current_token:
        tokens.append((current_token, current_color))
    return tokens

def play_sfx():
    keyboardsfx[random.randint(0, 11)].play()

def handle_text_input(event):
    """Handle text input from the user."""
    global cursor_pos, scroll_offset, typing
    typing = True
    line, col = cursor_pos
    if event.key == pygame.K_RETURN:
        text_lines.insert(line + 1, text_lines[line][col:])
        text_lines[line] = text_lines[line][:col]
        cursor_pos = [line + 1, 0]
        play_sfx()
    elif event.key == pygame.K_BACKSPACE:
        if col > 0:
            text_lines[line] = text_lines[line][:col - 1] + text_lines[line][col:]
            cursor_pos[1] -= 1
            play_sfx()
        elif line > 0:
            cursor_pos = [line - 1, len(text_lines[line - 1])]
            text_lines[line - 1] += text_lines.pop(line)
            play_sfx()
    elif event.key == pygame.K_LEFT and col > 0:
        play_sfx()
        cursor_pos[1] -= 1
    elif event.key == pygame.K_RIGHT and col < len(text_lines[line]):
        play_sfx()
        cursor_pos[1] += 1
    elif event.key == pygame.K_UP and line > 0:
        play_sfx()
        cursor_pos[0] -= 1
        cursor_pos[1] = min(len(text_lines[line - 1]), col)
    elif event.key == pygame.K_DOWN and line < len(text_lines) - 1:
        play_sfx()
        cursor_pos[0] += 1
        cursor_pos[1] = min(len(text_lines[line + 1]), col)
    elif event.key >= pygame.K_SPACE and event.key <= pygame.K_z:
        txt = event.unicode
        merges = {"(": ")", "[": "]", "{": "}", '"': '"'}
        if event.unicode in merges:
            txt += merges[event.unicode]
        play_sfx()
        text_lines[line] = text_lines[line][:col] + txt + text_lines[line][col:]
        cursor_pos[1] += 1
    elif event.key in REPLACABLES:
        play_sfx()
        text_lines[line] = text_lines[line][:col] + REPLACABLES[event.key] + text_lines[line][col:]
        cursor_pos[1] += len(REPLACABLES[event.key])

    # # Adjust scrolling if cursor goes out of view
    # if cursor_pos[0] * space < scroll_offset:
    #     scroll_offset = max(0, cursor_pos[0] * space)
    # elif (cursor_pos[0] + 1) * space > scroll_offset + SCREEN_HEIGHT - 50:
    #     scroll_offset += space


def handle_mouse_click(pos):
    global globalpath
    """Handle mouse clicks for buttons and text."""
    global cursor_pos, scroll_offset
    for name, rect in buttons.items():
        if rect.collidepoint(pos):
            if name == "Save":
                save_file()
            elif name == "Load":
                # globalpath = funcs.open_file_dialog()
                load_file()
                
            elif name == "Run":
                run_code()
            elif name == "CopyAll":
                copy_all()
            elif name == "Copy":
                copy_selected_text()
            elif name == "Paste":
                paste_text()
            # elif name == "Paste":
            #     paste_all()
            return

    # Handle text click
    x, y = pos
    if y >= 50:  # Clicked inside the text area
        relative_y = y + scroll_offset - 50
        line_index = relative_y // space
        if line_index < len(text_lines):
            line = text_lines[line_index]
            char_index = (x - 50) // FONT.size(" ")[0]  # Approximation using font size
            cursor_pos[0] = line_index
            cursor_pos[1] = min(len(line), max(0, char_index))

def copy_selected_text():
    """Copy the selected text to the clipboard."""
    global cursor_pos, text_lines
    line, col = cursor_pos
    selected_text = ""
    if line < len(text_lines):
        selected_text = text_lines[line][:col]
    pyperclip.copy(selected_text)

def paste_text():
    """Paste text from the clipboard into the editor."""
    global cursor_pos, text_lines
    line, col = cursor_pos
    clipboard_text = pyperclip.paste()
    text_lines[line] = text_lines[line][:col] + clipboard_text + text_lines[line][col:]
    cursor_pos[1] += len(clipboard_text)
 
def copy_all():
    pyperclip.copy("\n".join(text_lines))
    # send_msg("Text yanked into clipboard.")


def save_file():
    """Save the editor content to a file."""
    with open(f"{globalpath}", "w") as f:
        f.write("\n".join(text_lines))
    
    update_syntax()


def update_syntax():
    def get_function_names(file_path):
        with open(file_path, 'r') as file:
            tree = ast.parse(file.read(), filename=file_path)
        function_names = set([node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)])
        return function_names
    # Recolors all the new functions imported
    global FUNCTIONS
    FUNCTIONS = OLD_FUNCTIONS
    for f in os.listdir("std"):
        if f[-2:] == "py":
            my_dict2 = {y: x for x, y in funcs._BLUE.items()}
            colt = "\n".join(text_lines)
            if (f"{my_dict2["from"]} std.{f[:-3]}" in colt) or (f"header std.{f[:-3]}" in colt):
                FUNCTIONS = FUNCTIONS.union(get_function_names("std/" + f))
            elif f == "oil.py":
                FUNCTIONS = FUNCTIONS.union(get_function_names("std/" + f))

    def get_classes_and_functions(file_path):
        with open(file_path, "r") as file:
            tree = ast.parse(file.read(), filename=file_path)

        classes = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                # Get all function names within the class
                functions = [
                    n.name for n in node.body if isinstance(n, ast.FunctionDef)
                ]
                classes[node.name] = functions
        return classes

    # Recolors all the new functions imported
    global CLASSES
    for f in os.listdir("std"):
        if f[-2:] == "py":
            my_dict2 = {y: x for x, y in funcs._BLUE.items()}
            if f"{my_dict2["from"]} std.{f[:-3]}" in "\n".join(text_lines) or (f"header std.{f[:-3]}" in colt):
                CLASSES = CLASSES.union(get_classes_and_functions("std/" + f).keys())
            elif f == "oil.py":
                CLASSES = CLASSES.union(get_classes_and_functions("std/" + f).keys())

    global MODS
    for f in os.listdir("std"):
        if f[-2:] == "py":
            my_dict2 = {y: x for x, y in funcs._BLUE.items()}
            if f"{my_dict2["from"]} std.{f[:-3]}" in "\n".join(text_lines) or (f"header std.{f[:-3]}" in colt):
                r = (flatten(get_classes_and_functions("std/" + f).values()))
                for a, i in enumerate(r):
                    r[a] = "." + i
                MODS = MODS.union(r)
            elif f == "oil.py":
                r = (flatten(get_classes_and_functions("std/" + f).values()))
                for a, i in enumerate(r):
                    r[a] = "." + i
                MODS = MODS.union(r)

def load_file():
    """Load content from a file into the editor."""
    global text_lines, cursor_pos, scroll_offset
    if os.path.exists(f"{globalpath}"):
        with open(f"{globalpath}", "r") as f:
            text_lines = f.read().splitlines()
            if text_lines == []:
                with open(f"boilerplate/#load.oil", "r") as g:
                    boilerplate = g.read()
                    text_lines = boilerplate.splitlines()
            cursor_pos = [len(text_lines) - 1, len(text_lines[-1]) if text_lines else 0]
            scroll_offset = 0

def run_code():
    """Run the Python script."""
    save_file()
    subprocess.run(["osascript", "-e", f'tell application "Terminal" to do script "python3 documents/python/ideOil/execute.py"'])

def draw_cursor():
    global typing
    """Draw the blinking text cursor."""
    global last_cursor_toggle, cursor_visible
    if time.time() - last_cursor_toggle > cursor_blink_time:
        cursor_visible = not cursor_visible
        last_cursor_toggle = time.time()
    if typing:
        cursor_visible = True

    if cursor_visible:
        line, col = cursor_pos
        x = 50 + col * FONT.size(" ")[0]
        y = 50 + line * space - scroll_offset
        pygame.draw.line(screen, WHITE, (x, y), (x, y + space), 2)

def draw_buttons():
    """Draw the buttons."""
    for name, rect in buttons.items():
        pygame.draw.rect(screen, BUTTON_COLOR, rect)
        text_surface = FONT.render(name, True, WHITE)
        screen.blit(text_surface, (rect.x + 10, rect.y + 5))

# Main loop
def main():
    global last_key_time, last_key_event, scroll_offset, typing, HOLD_KEY, text_lines, cursor_pos
    clock = pygame.time.Clock()
    running = True

    while running:
        screen.fill(BG_COLOR)

        typing = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                handle_text_input(event)
                last_key_time = 0
                last_key_event = event
            elif event.type == pygame.KEYUP:
                HOLD_KEY = MAX_HOLD_KEY
                if last_key_event != None:
                    if event.key == last_key_event.key:
                        last_key_event = None
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    handle_mouse_click(event.pos)
            elif event.type == pygame.MOUSEWHEEL:
                scroll_offset += event.y * -space

        scroll_offset = max(0,scroll_offset)
        last_key_time += 1
        # Handle key repeat
        if (last_key_event) and (last_key_time >= HOLD_KEY):
            handle_text_input(last_key_event)
            last_key_time = 0
            HOLD_KEY = MAX_HOLD_KEY // 14
        

        render_highlighted_text()
        draw_cursor()
        # Draw interface

        pygame.draw.rect(screen, BUTTON_DIV_COLOR, pygame.Rect(0,0,SCREEN_WIDTH,50))
        draw_buttons()

        # Quick commands
        if text_lines[0].startswith("os::"):
            try:
                with open(f"boilerplate/#{text_lines[0].replace("os::", "")}.oil", "r") as g:
                    cursor_pos = [0,0]
                    boilerplate = g.read()
                    text_lines = boilerplate.splitlines()
                    update_syntax()

            except:
                pass
        
        pygame.draw.rect(screen, BUTTON_DIV_COLOR, pygame.Rect(0,SCREEN_HEIGHT-40,SCREEN_WIDTH,40))
        text_surface = FONT.render(f"lines: {len(text_lines)} || bytes: {sum(len(sublist) for sublist in text_lines)}", True, WHITE)
        screen.blit(text_surface, (10, SCREEN_HEIGHT-30))

        if full_res:
            text_surface = FONT.render(f"OilScript Cone IDE", True, WHITE)
            screen.blit(text_surface, (SCREEN_WIDTH-220, 14))

        # Update display
        pygame.display.flip()
        clock.tick(240)

    pygame.quit()


if __name__ == "__main__":
    main()