#Shaun Leing swl567 11241403
from Game_Vb import problem_Vb
from Min_Max import Min_Max_Search as Search
import time


"""
Mini max search script for problem Vb
"""
print("A4Q2")
print("size|utility|move|time")
for i in range(1,11):
    start = time.time()
    p = problem_Vb(i)
    s = Search()
    result = s.minimax_decision(p)

    print(i,"|",result[0],"|",result[1],"|",time.time()-start)








