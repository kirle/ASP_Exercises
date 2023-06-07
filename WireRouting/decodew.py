import sys
import os

def arguments(s,pred):
    s=s.split("(")
    if s[0]!=pred: return []
    args=[]
    s=s[1].split(",")
    args=s[:-1]    # take all arguments but last
    args.append(s[len(s)-1].split(")")[0])
    return args

import time
inicio = time.time()
if len(sys.argv)<2:
    print("decode.py file1 [file2 ... ]")
    sys.exit()

command = "telingo --verbose=0 --warn none"
for arg in sys.argv[1:]:
    command += " " + arg 
command += " > out.tmp"
os.system(command)
# Read input in array 'lines'
f = open("out.tmp", "r")
lines = []
for line in f:
  if line.strip() != "":
    lines.append(line.strip())
sollines = []   # lines of last solution
for i in range(len(lines)):
    if lines[i].startswith("State 0:"):   # New solution
        sollines = []
    sollines.append(lines[i])

nrows=-1; obstacles = []; fills=[]

for line in sollines:
    if not line.startswith("State"):
        atoms=line.split()
        for a in atoms:
            if a.startswith("dim"):
                args=arguments(a,"dim"); nrows=int(args[0]); ncols=int(args[1])
            elif a.startswith("obs"): obstacles.append(a)
            elif a.startswith("fill"): fills.append(a)
if nrows<0:
    print("Missing dimensions dim(X,Y)"); sys.exit()
board = [['.' for i in range(ncols)] for j in range(nrows)]
for a in fills:
    args=arguments(a,"fill"); board[int(args[0])][int(args[1])]=args[2]
for a in obstacles:
    args=arguments(a,"obs"); board[int(args[0])][int(args[1])]='#'
for row in board: print("".join(row))

fin = time.time()
print(fin-inicio) 
# print(obstacles)
# print(fills)
# print(sollines)