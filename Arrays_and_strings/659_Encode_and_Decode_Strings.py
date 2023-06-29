# 659
# Encode and Decode Strings
# https://www.lintcode.com/problem/659/
# https://github.com/alexmancilla/LetsCoding/blob/main/Arrays_and_strings/659_Encode_and_Decode_Strings.py

"""
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.
"""

strs = ["123","4567","890101010"]
# Output: ["lint","code","love","you"]

"""
@param: strs: a list of strings
@return: encodes a list of strings to a single string.
"""
def encode(strs):
    res = ""
    for element in strs:
        res += str(len(element)) + "#" + element
    return res


"""
@param: str: A string
@return: decodes a single string to a list of strings
"""

def decode(s):
    # write your code here
    decode_list = []
    # Iterate over each character using a while loop
    i = 0
    while i < len(s):
        if (s[i].isdigit()) and s[i + 1] == '#':
             l = int(s[i])    
             new_word = s[i + 2:i + (l + 2)]
             decode_list.append(new_word)
             i += l + 2  # Increment index by word length + 2
        else:
            i += 1  # Increment index by 1 if not a valid word

        # i += 1  # Increment the index
    return decode_list


sol = encode(strs)
print(sol)

new_sol = decode(sol)
print(new_sol)