#Shaun Leing swl567 11241403
from Game_Va import problem_Va as problem
from Depth_Limited import Depth_Limited_Search as Search
import time

"""
Depth Limited script for problem Va
"""
print("A4Q5")
print("size|utility|move|time")
for i in range(1,21):
    start = time.time()
    p = problem(i)
    s = Search(4)
    result = s.minimax_decision(p)

    print(i,"|",result[0],"|",result[1],"|",time.time()-start)








