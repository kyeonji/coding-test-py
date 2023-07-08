def solution(files):
    info = []
    for id, file in enumerate(files):
        head = ""
        number = ""
        for i in range(len(file)):
            # (string).isnumeric() return if it's number or not
            # isdigit() and isdecimal() also exist
            if not file[i].isnumeric():
                head += file[i].lower()  # if not, sort() sort upper to lower
            else:
                break
        for j in range(i, len(file)):
            if file[j].isnumeric():
                number += file[j]
            else:
                break
        n = int(number)  # string to int
        # if use 'file' instead of 'id', it sort with 'file' if head and number is same
        info.append([head, n, id])

    info.sort()
    answer = [files[e[-1]] for e in info]  # how to extract 2d list column

    return answer

# [more]
# 1. how to sort list of dictionary with key
#    new_list = sorted(list_to_be_sorted, key=lambda d: d['name']
# 2. re library
#    re for regex. includes functions like match(), fullmatch(), findall(), search() etc.
#    example1)
#    re.findall('\d+', 'abc123def56zz')  -> '\d+' option find all integer in string
#    # ['123', '56']
