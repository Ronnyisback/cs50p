import sys
import random
from pyfiglet import Figlet
figlet=Figlet()
fl=figlet.getFonts()
if not len(sys.argv)==3 and not len(sys.argv)==1:
    sys.exit("Invalid usage")
if len(sys.argv)==3:
    if not sys.argv[1]=="-f" and not sys.argv[1]=="--font":
        sys.exit("Invalid usage")
    font_name=sys.argv[2]
    if not font_name in figlet.getFonts():
            sys.exit("Invalid usage")
elif len(sys.argv)==1:
     font_name=random.choice(fl)
usr_input=input("Input: ")
figlet.setFont(font=font_name)
print(f"Output: {figlet.renderText(usr_input)}")
