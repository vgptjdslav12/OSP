import sys
import operator

param1 = sys.argv[1]
param2 = int(sys.argv[2])

di = {}
if ".txt" in param1:   
    f = open(param1,"r");
else :
    f = open(param1+".txt","r");
lines = f.readlines();
f.close();

for line in lines :
    # 특수문자 제거
    line = ''.join(filter(str.isalnum, line.lower()));
