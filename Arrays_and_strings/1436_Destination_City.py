
paths = [["B","C"],["D","B"],["C","A"]]
def destCity(paths: list[list[str]]) -> str:
    # nopath = set()
    # path = set()

    # for cities in paths:
    #     print(f'vamos en esta ciudad {cities}')
    #     if cities[0] not in nopath:
    #         print(f'Se agrego a paths {cities[0]}')
    #         path.add(cities[0])
    #     elif cities[0] in nopath:
    #         print(f'Se Quito de NO paths {cities[0]}')
    #         nopath.remove(cities[0])
    #     elif cities[1] not in paths:
    #         print(f'Se agrego a NO paths {cities[1]}')
    #         nopath.add(cities[1])
        
    # return nopath
    # # for i in nopath:
    # #     return i

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
 