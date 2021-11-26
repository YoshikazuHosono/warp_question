def create_answer(index):
    if index <= 0:
        return []

    start = 2
    geta = 2 ** (index - 1)
    before_result_list = create_answer(index -1)
    before_result_idx = 0
    result = []

    for num in range(geta):
        before_result = before_result_list[before_result_idx] if len(before_result_list) > before_result_idx else start
        if num % 2 == 0:
            result += [before_result]
        else:
            result += [before_result + geta]
            before_result_idx+=1

    return result

print(create_answer(0))
print(create_answer(1))
print(create_answer(2))
print(create_answer(3))
print(create_answer(4))
print(create_answer(5))
print(create_answer(6))
print(create_answer(7))
