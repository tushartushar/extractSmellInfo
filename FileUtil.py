
def writeFile(fileName, text):
    f = open(fileName, "a", errors='ignore')
    f.write(text + "\n")
    f.close()