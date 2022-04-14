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
    # 공백 제거
    line.replace(" ", "");
    if di.get(line) == None :
        di[line] = 1;
    else :
        di[line] += 1;

di = sorted(di.items(),key=operator.itemgetter(1), reverse=True);
