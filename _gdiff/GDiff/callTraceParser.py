from os import listdir
from os.path import isfile, join
from GDiff import app;
import glob

def parseBugCallTrace():
    app.config.from_pyfile('config_file.cfg');
    folderPath = app.config["BUG_DIRECTORY"]
    allFiles = glob.glob(folderPath+"*.txt")
    contents = ""
    for file in allFiles:
        val = getCallHierarchy(file)
        if(val != ""):
            contents += val + "\n"
    
    outFile = app.config["BUG_PARSING_OUTPUT"]
    with open(outFile, 'w') as the_file:
        the_file.write(contents)
        
def getCallHierarchy(file):
    f = open(file,"r")
    lines = f.readlines()
    i=0
    found = 0
    funcList = []
    while(i<len(lines)):
        while(lines[i].find("Call Trace:") == -1 and found == 0 and i < len(lines)-1):
            i += 1
        if(i == len(lines)-2):
            i+=1
        if(i>=len(lines)):
            break
        if(lines[i].find("Call Trace:")!=-1):
            found = 1
            funcList = []
            i+=1
        while(found == 1 and i<len(lines) and lines[i].find("---[ end trace")==-1):
            funcName = lines[i][lines[i].find(">] ")+3:]
            funcName = funcName[:funcName.find("+")]
            funcList.append(funcName)
            i+=1
        if(i<len(lines) and lines[i].find("---[ end trace")!=-1):
            found = 0
            i = len(lines) + 1
        if(i == len(lines)-2 or i == len(lines)-1):
            i+=1
        if(i>len(lines) + 1):
            break
    
    if(len(funcList) == 0):
        return ""
    funcNames = ""
    for funcName in funcList:
        funcNames += funcName + "#"
    
    funcName = file[(file.rindex("/")+1):file.find(".txt")] + ": " + funcNames[:-1]
    return funcName

if __name__ == "__main__":
    parseBugCallTrace()
