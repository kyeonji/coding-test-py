# [learned] python default recursion limit is 1000
# need codes below (line 3 ~ 4)
import sys

sys.setrecursionlimit(1000001)


def dp(current_pose, land):
    # dp don't need to implemented with recursive function
    return


def solution(land):
    answer = 0

    N = len(land)
    for i in range(1, N):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    answer = max(land[N - 1])
    return answer

# [more]
# - used greedy algorithm at first
# - but that was wrong : can't handle the case if same scores in a row exists
# - it takes only one case among them

# - dp algorithm should be used
# - solution that stacks the results are dp algorithm (NOT greedy)
# - because they consider both case (if there are same scores in a row)
