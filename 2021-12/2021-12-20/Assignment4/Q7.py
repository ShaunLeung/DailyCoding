#Shaun Leing swl567 11241403
from Game_Va import problem_Va as problema
from Game_Vb import problem_Vb as problemb
from Alpha_Beta_Limited import Alpha_Beta_Limited_Search as Search
import time

"""
Alpha Beta search with depth limited script for problem Va and Vb
"""
print("A4Q7")
print("Alpha Beta With Depth Limit 4: Va")
print("size|utility|move|time")
for i in range(1,21):
    start = time.time()
    p = problema(i)
    s = Search(4)
    result = s.minimax_decision(p)

    print(i,"|",result[0],"|",result[1],"|",time.time()-start)

print("Alpha Beta With Depth Limit 4: Vb")
print("size|utility|move|time")
for i in range(1,21):
    start = time.time()
    p = problemb(i)
    s = Search(4)
    result = s.minimax_decision(p)

    print(i,"|",result[0],"|",result[1],"|",time.time()-start)