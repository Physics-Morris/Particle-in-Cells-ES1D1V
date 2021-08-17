M = """
M   M
MM MM
M M M
M   M
M   M
""";
O = """
OOOOO
O   O
O   O
O   O
OOOOO
""";
R = """
RRRRR
R    
R    
R    
R    
""";
I = """
IIIII
  I  
  I  
  I  
IIIII
""";
S = """
SSSSS
S    
SSSSS
    S
SSSSS
""";
v = """
     
     
v   v
 v v 
  V  
""";
a = """
       
   A   
  A A  
 AAAAA 
A     A
""";
N = """
     
N   N 
NN  N 
N NNN 
N   N 
""";
D = """
     
DDDD  
D   D 
D   D 
DDDD  
""";
Y = """
     
 Y   Y  
  Y Y 
   Y  
   Y  
""";
space = """
     
     
     
     
     
""";

dot = """
     
     
     
     
.    
""";
d2 = """
#### 
    #
   # 
 ##  
#####
""";
s2 = """
     
222  
   2 
 2   
2222 
""";

d0 = """
 ### 
#   #
#   #
#   #
 ### 
""";
s0 = """
     
 000 
0   0
0   0
 000 
""";

d1 = """
  #  
 ##  
  #  
  #  
 ### 
""";
s1 = """
     
  1  
 11  
  1  
 111 
""";

heart = """
 o o 
ooooo
ooooo
 ooo 
  o  
""";

diamond = """
  o  
 ooo 
ooooo
 ooo 
  o  
""";
arrow = """
  o  
   o 
ooooo
   o 
  o  
""";

stars1 = """
    *
 *   
   * 
*    
  *  
""";

stars2 = """
  *  
    *
*    
   * 
 *   
""";

stars3 = """
*    
    *
 *   
   * 
  * 
""";

stars4 = """
   * 
*    
  *  
 *   
    *
""";

def whole_half(n):
    if n%2 == 0:
        return (int(n/2), int(n/2))
    else:
        return (int(n/2+0.5), int(n/2-0.5))
    
def display_character(s, canvas_size=(7,7)):
    s = s.split('\n')
    
    character_height = len(s)
    character_width = max([len(l) for l in s])
    canvas_height = character_height if (character_height>canvas_size[0]) else  canvas_size[0] 
    canvas_width = character_width if (character_width>canvas_size[1] ) else canvas_size[1] 

    fill_top, fill_bottom = whole_half(canvas_height-character_height)

    for i in range(0,fill_top):
        s.insert(0, " "*canvas_width)

    for j in range(0,fill_bottom):
        s.insert(len(s)-1, " "*canvas_width)

    for k in range(0,canvas_height):
        line_legth = len(s[k])
        fill_left, fill_right = whole_half(canvas_width-line_legth)

        for i in range(0,fill_left):
            s[k] = " "+s[k]
        
        for j in range(0,fill_right):
            s[k] = s[k]+" "
 
    return s


import numpy as np
from colorama import * 

def print_decorated_line(characters, color=Fore.BLACK):
    characters = np.array([display_character(c) for c in characters])
    
    line = characters[0]

    for c in characters[1:]:
        line = np.char.add(line, c) 
    
    for l in line:
        print(color + l)
        
#  characters = [diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond]
#  print_decorated_line(characters, Fore.RED)
#
#  characters = [stars1, H,A,P,P,Y, space, heart, space, stars2]
#  characters = [diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond]
#  print_decorated_line(characters, Fore.RED)
#  characters = [v,s1,space,s2,s0,s2,s1]
#  print_decorated_line(characters, Fore.RED)

#  characters = [M,O,R,R,I,S]
#  print_decorated_line(characters, Fore.YELLOW)
characters = [diamond, diamond, diamond, diamond, diamond, diamond]
print_decorated_line(characters, Fore.RED)
characters = [S,a,N,N,D,Y]
print_decorated_line(characters, Fore.YELLOW)
characters = [stars2, d2, d0, d2, d1, stars4]
print_decorated_line(characters, Fore.YELLOW)

#  characters = [diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond]
#  print_decorated_line(characters, Fore.RED)
#
#  characters = [stars3, N, E, W, space, Y, E, A, R, stars1]
#  print_decorated_line(characters, Fore.GREEN)

#  characters = [stars2, space, heart, heart, space, d2, d0, d2, d1, stars4]
#  print_decorated_line(characters, Fore.YELLOW)
#
#  characters = [diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond, diamond]
#  print_decorated_line(characters, Fore.RED)
