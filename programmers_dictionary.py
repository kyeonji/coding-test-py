def solution(word):
    answer = 0

    # ==== BRAIN STORMING ====
    # AAAAE = 1+1+1+1+2 = 6
    # 1 + 1 + 1 + 1 + AAAAA시작 + 1 = 6

    # AAAE = 1+1+1+2+5(AAAA 시작) = 10
    # 1 + 1 + 1 + AAAA 시작 + 1 = 10

    # I
    # A 시작 + E 시작 + 1
    # 625+125+25+5+1 = 781

    # EIO
    # A 시작 + 1 + EA 시작 + EE 시작 +  1 + EIA 시작 + EIE 시작 + 1

    num = [781, 156, 31, 6, 1]
    alphabet = ["A", "E", "I", "O", "U"]
    for n, letter in enumerate(word):
        answer += 1  # python has no ++ or --
        for i in range(alphabet.index(letter)):
            answer += num[n]

    return answer

# [learned]
# 1. list has no .find() -> method of string not list
# 2. python has no ++ or --

# nice brainstorming!
# (but actually it was summation of geometric sequence)
