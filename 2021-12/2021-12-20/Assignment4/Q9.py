#Shaun Leing swl567 11241403
from Game_Va import problem_Va as problem
from Min_Max import Min_Max_Search as MM
from Alpha_Beta import Alpha_Beta_Search as AB
from Depth_Limited import Depth_Limited_Search as DL
from Alpha_Beta_Limited import Alpha_Beta_Limited_Search as ABL
from PvP import PvP
import time

"""
You can choose any search made in this assignment
MM for MiniMax
AB for Alpha Beta pruning
DL for Depth Limited
ABL for Alpha Beta with Depth Limited
"""

def scenario(n,C1,C2):
    """
    Plays N queens with the passed in cutoffs
    uses Alpha Beta Search with depth limited
    :param n:
    :param C1: player 1 search
    :param C2: player 2 search
    :return:
    """
    N=n+1
    cut_off_p1 = C1
    cut_off_p2 = C2
    wins = 0
    for j in range(1, N):
        start = time.time()
        p = problem(10)
        s1 = ABL(cut_off_p1)
        s2 = ABL(cut_off_p2)
        game = PvP(s1, s2, p)
        result = game.play()
        if result > 0:
            wins += 1
    print(N - 1, "|", cut_off_p1, "|", cut_off_p2, "|", wins, "W.", (N - 1) - wins, "L")

print("A4Q9")
print("N|Cut-off P1|Cut-off P2| Win/Loss P1")
scenario(10,4,4)
scenario(10,5,5)
scenario(10,5,3)
scenario(10,3,5)

scenario(20,4,4)
scenario(20,5,5)
scenario(20,5,3)
scenario(20,3,5)
















