maxCount = -1
for i in [0,n-1]
    count = 0
    for x in [0,n]
        for y in [i,n] U [0,i-1]
            z = n-x-y
            if z < 0 continue
            if (none of x,y,z tested before)
                save(x,y,z) in toPrint
                makeTested(x,y,z)
                count++
    if count > maxCount
        maxCount = count
        maxToPrint = toPrint
print(maxCount)
printAllOf(maxToPrint)
