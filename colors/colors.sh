##############################################################################
# This is the bash version of colors.py
#
# See colors.py for documentation
#
# User interface is identical to colors.py except for python vs. bash syntax
#
# Examples:
#    b=$(xtext $bold $(fgcolor4 "red") $(bgcolorb4 "yellow"))
#    c=$(xtext $(fgcolorRGB 0 10 150) $(bgcolorb4 "green"))
#    r=$(xtext $reset)
#    echo -e "${b}bold red${r}, not bold red"
#    echo -e "${c}colorful${r}, not colorful"
##############################################################################

# default
reset="0"
#text effects
bold="1"
boldoff="21"
light="2"
lightoff="22"
normal="22"
italic="3"
italicoff="23"
underline="4"
underlineoff="24"
slowblink="5"
fastblink="6"
blinkoff="25"
reverse="7"
reverseoff="27"
conceal="8"
reveal="28"
strike="9"
strikeoff="29"
frame="51"
frameoff="54"
circle="52"
circleoff="54"
overline="53"
overlineoff="55"
# colors
declare -A color4_names=(["black"]=30 ["red"]=31 ["green"]=32 ["yellow"]=33 ["blue"]=34 ["magenta"]=35 ["cyan"]=36 ["white"]=37)
color4() { echo "${color4_names[$1]}"; }
fgcolor4() { echo "${color4_names[$1]}"; }
bgcolor4() { echo $(("${color4_names[$1]}" + 10)); }
fgcolorb4() { echo $(("${color4_names[$1]}" + 60)); }
bgcolorb4() { echo $(("${color4_names[$1]}" + 10 + 60)); }
fgcolor256() { echo "38;5;$1"; }
bgcolor256() { echo "48;5;$1"; }
fgcolorRGB() { echo "38;2;$1;$2;$3"; }
bgcolorRGB() { echo "48;2;$1;$2;$3"; }

join_with_sep () {
    local IFS="$1"
    shift
    echo "$*"
}

xtext () {
    s="\033[$(join_with_sep \; $*)m"
    echo $s
}

examples() {
    b=$(xtext $bold $(fgcolor4 "red") $(bgcolorb4 "yellow"))
    r=$(xtext $reset)
    c=$(xtext $(fgcolorRGB 0 10 150) $(bgcolorb4 "green"))
    echo -e "${b}bold red${r}, not bold red"
    echo -e "${c}colorful${r}, not colorful"
}
