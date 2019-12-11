def storeInDB(arr):
    try:
        print(arr[0].replace(":","")[0:9] + "\t" + arr[2].replace("\n",""))
    except:
        print(arr[0].replace(":","")[0:9] + "\t" + arr[1].replace("\n",""))

def splitLine(line):
    return line.split("\t")

listFile = "./test.txt"
i = 0

with open(listFile, "r") as f:
    for line in f:
        if "IEEE Registration Authority" in line:
            if len(splitLine(line)[0]) == 8:
                storeInDB(splitLine(line))
        if len(line) == 0:
            break
