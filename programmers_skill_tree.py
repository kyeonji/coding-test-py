def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_to_check = ""
        for s in skill_tree:
            # in : if element exist in list or string
            if s in skill:
                skill_to_check += s
        # string.find(e) : return index of char in string. if do not exits, return -1
        # string.index(e) : do same but, if do not exits, occurs error
        if skill.find(skill_to_check) == 0:
            answer += 1

    return answer

# [learned]
# 1. initialize list with 0 of specific length
#    l = [0] * length
# 2. can be implemented with for-end
#    if for loop ended with break -> just break
#    if for loop ended without break -> do sth. in else
#    don't need check flag!
# 3. list.pop(0)
#    queue can be implemented with list in python
#    list.pop(0) return list[0] and also pop() that element = pop_left
