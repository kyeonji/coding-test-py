# solution below is wrong answer (time out)
def timeout_solution(numbers):
    answer = [-1] * len(numbers)

    for idx, number in enumerate(numbers):
        for i in range(idx + 1, len(numbers)):
            if number < numbers[i]:
                answer[idx] = numbers[i]
                break

    return answer


# DIDN'T SOLVED IT
# TRY AGAIN!
def solution_from_other(numbers):
    answer = [-1]*(len(numbers))
    stack = []  # store index of numbers to find big_num
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer


# [learned]
# this problem can solved with STACK
# process
#   1. In stack, store index of numbers to find big_num (from 0)
#   2. check if numbers[i] is used as big_num of numbers[stack[-]] (numbers in front of it)
#   3-1. if it used, get answer and pop stack (because we found the big_num of it)
#   3-2. if not used, do nothing
#   4. append stack
# main idea:
#   if numbers[i] is big_num of numbers in front of it, we don't need to check back of it
# why do we check only for stack[-1]?
#   if numbers[i] < stack[-1], numbers[i] is less than stack[-] for every -

