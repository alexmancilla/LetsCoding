from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    solution = []
    anagram_groups = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_groups[sorted_word].append(word)
    
    for group in anagram_groups.values():
        solution.append(group)
 

    return solution

sol = groupAnagrams(strs)
print(sol)
        

 
            
