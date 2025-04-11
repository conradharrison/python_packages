##############################################################################
# Python API for using ANSI terminal control codes
#
# User interface:
#
#    import colors
#
#    colors.xtext(...)  -> Accepts control strings as input parameters
#    colors.coloroff()  -> Useful for non-interactive outputs
#    colors.coloron()   -> Restore coloroff()
#    colors.examples()  -> Prints some usage examples
# 
# Compound example:
#    print(xtext(fgcolor256(15), bgcolor256(21), strike) + "white on blue strike" + xtext(reset))
#
# Control strings have aliases as shown below. Some complex control 
# strings (e.g., color) have generator functions that accept parameters
# 
#    EFFECT CONTROL
#    ==============
#    reset,normal
#    bold                  boldoff     
#    light                 lightoff    
#    italic                italicoff   
#    underline             underlineoff
#    slowblink,fastblink   blinkoff    
#    reverse               reverseoff  
#    conceal               reveal      
#    strike                strikeoff   
#    frame                 frameoff    
#    circle                circleoff   
#    overline              overlineoff 
#    
#    COLOR CONTROL
#    =============
#    5-bit colors: normal foreground and background by name
#                  black|red|green|yellow|blue|magenta|cyan|white
#    fgcolor4(color-name)
#    bgcolor4(color-name)
#    
#    5-bit colors: bold foreground and background by name
#                  black|red|green|yellow|blue|magenta|cyan|white
#    fgcolorb4(color-name)
#    bgcolorb4(color-name)
#    
#    8-bit colors: foregound and background colors by number (0-255)
#    fgcolor256(color-number)
#    bgcolor256(color-number)
#    
#    RGB colors: foregound and background colors by R,G,B number (0-255)
#    fgcolorRGB(r, g, b)  
#    bgcolorRGB(r, g, b)
#    
#    Reset to default:
#    fgdefault   
#    bgdefault
#
# Reference: https://en.wikipedia.org/wiki/ANSI_escape_code
##############################################################################

# Below are the ANSI escape sequences for terminal control from the above 
# reference
#
# 0	Reset / Normal	all attributes off
# 1	Bold or increased intensity	
# 2	Faint (decreased intensity)	Not widely supported.
# 3	Italic	Not widely supported. Sometimes treated as inverse.
# 4	Underline	
# 5	Slow Blink	less than 150 per minute
# 6	Rapid Blink	MS-DOS ANSI.SYS; 150+ per minute; not widely supported
# 7	[[reverse video]]	swap foreground and background colors
# 8	Conceal	Not widely supported.
# 9	Crossed-out	Characters legible, but marked for deletion. Not widely supported.
# 10	Primary(default) font	
# 11–19	Alternate font	Select alternate font n-10
# 20	Fraktur	hardly ever supported
# 21	Bold off or Double Underline	Bold off not widely supported; double underline hardly ever supported.
# 22	Normal color or intensity	Neither bold nor faint
# 23	Not italic, not Fraktur	
# 24	Underline off	Not singly or doubly underlined
# 25	Blink off	
# 27	Inverse off	
# 28	Reveal	conceal off
# 29	Not crossed out	
# 30–37	Set foreground color	See color table below
# 38	Set foreground color	Next arguments are 5;<n> or 2;<r>;<g>;<b>, see below
# 39	Default foreground color	implementation defined (according to standard)
# 40–47	Set background color	See color table below
# 48	Set background color	Next arguments are 5;<n> or 2;<r>;<g>;<b>, see below
# 49	Default background color	implementation defined (according to standard)
# 51	Framed	
# 52	Encircled	
# 53	Overlined	
# 54	Not framed or encircled	
# 55	Not overlined	
# 60	ideogram underline	hardly ever supported
# 61	ideogram double underline	hardly ever supported
# 62	ideogram overline	hardly ever supported
# 63	ideogram double overline	hardly ever supported
# 64	ideogram stress marking	hardly ever supported
# 65	ideogram attributes off	reset the effects of all of 60-64
# 90–97	Set bright foreground color	aixterm (not in standard)
# 100–107	Set bright background color	aixterm (not in standard)

# Above ANSI control sequences are stored in these symbols, and can be used
# while calling xtext(...)

# default
reset       = "0"
#text effects
bold        = "1"
boldoff     = "21"
light       = "2"
lightoff    = "22"
normal      = "22"
italic      = "3"
italicoff   = "23"
underline   = "4"
underlineoff= "24"
slowblink   = "5"
fastblink   = "6"
blinkoff    = "25"
reverse     = "7"
reverseoff  = "27"
conceal     = "8"
reveal      = "28"
strike      = "9"
strikeoff   = "29"
frame       = "51"
frameoff    = "54"
circle      = "52"
circleoff   = "54"
overline    = "53"
overlineoff = "55"
# colors
color4      = lambda c: {"black":30, "red":31, "green":32, "yellow":33, "blue":34, "magenta":35, "cyan":36, "white":37}[c]
fgcolor4    = lambda c: str(color4(c))
bgcolor4    = lambda c: str(color4(c) + 10)
fgcolorb4   = lambda c: str(color4(c) + 60)
bgcolorb4   = lambda c: str(color4(c) + 10 + 60)
fgcolor256  = lambda c: "38;5;" + str(c)
bgcolor256  = lambda c: "48;5;" + str(c)
fgcolorRGB  = lambda r,g,b: "38;2;" + "{};{};{}".format(r, g, b)
bgcolorRGB  = lambda r,g,b: "48;2;" + "{};{};{}".format(r, g, b)
fgdefault   = "39"
bgdefault   = "49"

# Use coloron() and coloroff() to enable/disable escape sequences
# default: escape sequences are enabled
plain_text = False

def coloroff():
    global plain_text
    plain_text = True

def coloron():
    global plain_text
    plain_text = False

# Use xtext(...) to apply the sequences
# xtext() accepts only the above control names as arguments
def xtext(*args):
    if (plain_text):
        return ""
    else:
        return "\033[" + ";".join(args) + "m"

# Some examples of xtext usage
def examples():
    # Just pass the control name to xtext: underline, and then reset
    print(xtext(underline) + "underlined text" + xtext(reset))
    # Can reset by an empty call to xtext too
    print(xtext(underline) + "underlined text" + xtext() + " no more underlined")
    print("This is " + xtext(bold) + "bold" + xtext(reset) + " no more bold")
    # Can pass more than one control to xtext
    print(xtext(overline, bold) + "overlined bold text" + xtext(overlineoff) + " -> no overline, bold only" + xtext(reset))
    # 16-color usage: Pass color names
    print(xtext(fgcolorb4("green"), italic) + "green italic" + xtext(reset))
    # 256-color usage: Pass a number between 0 and 255
    print(xtext(fgcolor256(15), bgcolor256(21), strike) + "white on blue strike" + xtext(reset))
    # RGB-color usage: Pass red, green and blue values as 8-bit numbers
    print(xtext(fgcolorRGB(250,120,100)) + "some RGB" + xtext(reset))
    # Disable control sequences completely. Useful for non interactive outputs
    coloroff()
    print(xtext(fgcolorRGB(250,120,100)) + "some RGB" + xtext(reset))

if __name__ == "__main__":
    examples()
