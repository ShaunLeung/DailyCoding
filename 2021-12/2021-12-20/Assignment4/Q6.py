#Shaun Leing swl567 11241403
from Game_Vb import problem_Vb as problem
from Depth_Limited import Depth_Limited_Search as Search
import time

"""
Alpha Beta search script for problem Vb
"""
print("A4Q6")
print("size|utility|move|time")
for i in range(1,21):
    start = time.time()
    p = problem(i)
    s = Search(4)
    result = s.minimax_decision(p)

    print(i,"|",result[0],"|",result[1],"|",time.time()-start)








