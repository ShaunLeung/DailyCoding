#Shaun Leing swl567 11241403
from Game_Vb import problem_Vb as problem
from Alpha_Beta import Alpha_Beta_Search as Search
import time

"""
Alpha Beta search script for problem Vb
"""
print("A4Q4")
print("size|utility|move|time")
for i in range(1,11):
    start = time.time()
    p = problem(i)
    s = Search()
    result = s.minimax_decision(p)

    print(i,"|",result[0],"|",result[1],"|",time.time()-start)