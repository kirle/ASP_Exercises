import clingo
import sys
### Main program

if len(sys.argv)<2:
    print("decode.py file1 [file2 ... ]")
    sys.exit()

# Loading files and grounding
ctl = clingo.Control()
ctl.add("base", [], "")
for arg in sys.argv[1:]:
    ctl.load(arg)
ctl.ground([("base", []),("display",[])])

# Solving    
models = []
with ctl.solve(yield_=True) as handle:
  for model in handle:
      models.append(model.symbols(atoms=True))
if len(models)==0:
    print("No answer sets")
    sys.exit()
if len(models)>1:
    print("Multiple solutions found")
    sys.exit()
lits=models[0]
for l in lits:
    if l.name=="dim":
        n=l.arguments[0].number
        break
a=[[0 for x in range(n)] for y in range(n)]
for l in lits:
    if l.name=="cell":
        a[l.arguments[0].number][l.arguments[1].number]=l.arguments[2].number
for i in range(n):
    for j in range(n):
        print(a[i][j],end='')
    print("")