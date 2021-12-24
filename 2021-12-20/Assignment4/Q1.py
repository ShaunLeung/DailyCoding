#Shaun Leing swl567 11241403
from Game_Va import problem_Va as problem
from Min_Max import Min_Max_Search as Search
import time

"""
Mini max search script for problem Va
"""
print("A4Q1")
print("size|utility|move|time")
for i in range(1,11):
    start = time.time()
    p = problem(i)
    s = Search()
    result = s.minimax_decision(p)

    print(i,"|",result[0],"|",result[1],"|",time.time()-start)








