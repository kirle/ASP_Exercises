python3 encode.py < examples/dom06.txt > domain.lp 
clingo 0 problem.lp domain.lp 
python3 decode.py problem.lp domain.lp
