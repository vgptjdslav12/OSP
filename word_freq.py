import sys
import operator

param1 = sys.argv[1]
param2 = int(sys.argv[2])

di = {}
# 파일 오픈
if ".txt" in param1:   
    # param1 에 .txt 가 포함되어 입력 되어 있을경우
    f = open(param1,"r");
else :
    # 아닐 경우
    f = open(param1+".txt","r");
lines = f.readlines();
# 파일 클로즈
f.close();

for line in lines :
    # 특수문자 제거
    line = ''.join(filter(str.isalnum, line.lower()));
    # 공백 제거
    line.replace(" ", "");
    if di.get(line) == None :
        # 딕셔너리에 없는 문자일경우
        di[line] = 1;
    else :
        # 딕셔너리에 있는 문자일경우
        di[line] += 1;

# 딕셔너리 정렬
di = sorted(di.items(),key=operator.itemgetter(1), reverse=True);
# param2 가 딕셔너리의 길이보다 클 경우 indexerror 가 발생함으로 param2 를 딕셔너리의 길이로 맞춰줌
if param2 > len(di) : param2 = len(di);

for i in range(param2):
    # 출력
    print("{:<15s} {:>15s}".format(di[i][0], str(di[i][1])));