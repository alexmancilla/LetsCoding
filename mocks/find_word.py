sentence = "t"
target = "tt"



def lookWord(sentence, target):
    s_ptr = 0
    t_ptr = 0

    for i in range(len(sentence)):
        print(sentence[i], target[t_ptr])
        if sentence[i] != target[t_ptr]:
            i += 1
            t_ptr = 0
        elif sentence[i] == target[t_ptr]:
            t_ptr += 1
            if t_ptr == len(target):
                return True
        elif i == len(sentence) - 1:
            return False
    return False

sol = lookWord(sentence, target)
print(sol)



# print("  ")

# while s_ptr <= len(sentence) - 1:
#     print(sentence[s_ptr])
#     s_ptr += 1

