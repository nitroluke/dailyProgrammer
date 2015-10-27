appendToFile = open("staticTables.sql", "r")
sortToFile = open("sortedFile", "w")

for line in sorted(appendToFile, key = str.lower):
    sortToFile.write(line)