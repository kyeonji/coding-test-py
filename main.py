import programmers_parking_fee_calculation as pfc
import programmers_hopscotch as h
import programmers_visiting_length as vl
import programmers_skill_tree as st

if __name__ == '__main__':
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

    answer = st.solution(skill, skill_trees)
    print(answer)