
paths = [["B","C"],["D","B"],["C","A"]]
def destCity(paths: list[list[str]]) -> str:
    dest = {}
    source = {}
    for i in paths:
        dest[i[1]]=1
        source[i[0]]=1
    for i in dest:
        if i not in source:
            return i  
sol = destCity(paths)
print(sol)
 
