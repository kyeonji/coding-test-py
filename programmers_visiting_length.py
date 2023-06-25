def solution(dirs):
    move = {'U': [0, 1], 'D': [0, -1], 'R': [1, 0], 'L': [-1, 0]}
    edges = set()
    pose_from = (0, 0)
    for dir in dirs:
        x = pose_from[0] + move[dir][0]
        y = pose_from[1] + move[dir][1]
        if abs(x) <= 5 and abs(y) <= 5:
            pose_to = (x, y)
            pose = [pose_from, pose_to]
            edges.add(tuple(sorted(pose)))
            pose_from = pose_to
    answer = len(edges)
    return answer

# [learned]
# 1. hashable : An object is hashable if it has a hash value which never changes during its lifetime
# unhashable: list, set, dictionary   vs   hashable data : tuple
# Hashability makes an object usable as a dictionary key and a set member
# 2. set
# no order, no duplicated elements

# [cuation] difference between list1 + list2 and [list1, list2]
