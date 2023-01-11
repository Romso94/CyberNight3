x = [ f"{chr(i)} = {i*13}" for i in range(32,127)]
tab = [871 ,1157, 858, 1014, 1599, 1287, 507 ,663, 1508, 1261, 1365, 1508, 1235, 1456, 676, 1495, 1235, 637, 1235, 1287, 663, 1495, 1261, 1482, 1625]

for val in tab:
    for element in x:
        if str(val) in element: 
            print(f"{element[0]}",end="")