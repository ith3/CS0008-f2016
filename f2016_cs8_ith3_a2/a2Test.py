def processFile(file):
    f = open(file, "r")
    pDis = 0
    pLines = 0
    errors = 0
    errlist = []
    lineNum = 0
    for lines in f:
        lineNum += 1
        try:
            line = f.readline().rstrip('\n').split(',')

            a = "a" + line[0]
            b = 9.8 + line[1]
            print(line)
            pDis += float(line[1])
            pLines += 1
        except:
            errlist.append(lineNum)
            print(lines)
            errors += 1
    if(errors != 0):
        print("There were " + str(errors) + " errors in line(s) " + str(errlist) + " that were \nmisformatted and not included in the calculation.")


    return pDis,pLines

print(processFile("dataE.csv"))