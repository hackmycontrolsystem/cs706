from flask import Flask, request, render_template;
from GDiff import app;
import os
import sys
import re


app = Flask(__name__)
currentWorkingDir = os.getcwd()

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

sys.frozen = 1

if getattr(sys, 'frozen'):
    here = sys.executable
else:
    here = os.path.realpath(__file__)
    
# server
@app.route('/')
@app.route('/GDiff', methods=['GET', 'POST'])
def StructOpt():
    app.config.from_pyfile('config_file.cfg');
    if request.method == 'GET':
        graphData = ""
        bugLink = ""
        try:
            bugLink = "\"" + app.config["BUG_LINK"] + "\""
            file2 = app.config["CFLOW_VERSION2"]
            graphData = parseData(app.config["CFLOW_VERSION1"], file2)
            with open(currentWorkingDir + '/output/graphData.txt', 'w') as the_file:
                the_file.write(graphData)
            collapeModified = 1
            if(file2 == None): collapeModified = 0
            return render_template("gdiff.html", graphData=graphData, bugLink=bugLink, collapeModified=collapeModified, foo=1);
        except Exception as e:
            logging.exception('Error: %s', e)
        return render_template("gdiff.html");
    elif request.method == 'POST':
        graphData = ""
        bugLink = app.config["BUG_LINK"]
        graphData = parseData(app.config["CFLOW_VERSION1"], app.config["CFLOW_VERSION2"])
        return render_template('gdiff.html', graphData=graphData, bugLink=bugLink, foo=1);

def getDiffData(file1, file2):
    if(file2 == None):
        return file1
    else:
        return generatedDiffGraphData(file1, file2)

def getChildChangeCounts(file):
    f = open(file,"r")
    lines = f.readlines()
    maxDepth = -1
    
    linesLen = (len(lines))
    
    for i in range(0, linesLen):
        currIdx = int(lines[i].split("~~")[0])
        if(currIdx > maxDepth):
            maxDepth = int(currIdx)
    
    for j in range(maxDepth, -1, -1):
        i=0
        contents = []
        parentIdx = -1
        childFlag = 0
        while(i < (linesLen)):
            currIdx = int(lines[i].split("~~")[0])
            if(currIdx!=j):
                while(currIdx!=j and i < linesLen-1):
                    contents.append(lines[i])
                    i+=1
                    currIdx = int(lines[i].split("~~")[0])
            
            if(currIdx==j):
                while(currIdx==j and i < linesLen-1):
                    parentIdx = len(contents)
                    childFlag = 0
                    contents.append(lines[i])
                    i+=1
                    currIdx = int(lines[i].split("~~")[0])
            
            if(currIdx > j):
                while(currIdx>j and i < linesLen-1):
                    lineCnt = int(lines[i].split("~~")[2])
                    if(lineCnt!=0 and childFlag == 0): childFlag = 1
                    contents.append(lines[i])
                    i+=1
                    currIdx = int(lines[i].split("~~")[0])
            
            if(childFlag!=0 and parentIdx!=-1):
                parentData = contents[parentIdx].split("~~")
                contents[parentIdx] = parentData[0] + "~~" + parentData[1] + "~~" + parentData[2] + "~~" + str(childFlag) + "~~" + parentData[4] #+ "\n"
            
            parentIdx = -1
            childFlag = 0
            if(i == linesLen-1): 
                contents.append(lines[i])
                i+=1
            
        lines = contents
    
    with open(file, 'w') as the_file:
        for item in contents:
            the_file.write(item)
                
def sortFile(file):
    contents = ""
    f = open(file,"r")
    lines = f.readlines()
    maxDepth = -1
    
    linesLen = (len(lines))
    
    for i in range(0, linesLen):
        currIdx = int(lines[i].split("~~")[0])
        if(currIdx > maxDepth):
            maxDepth = int(currIdx)
            
    for j in range(maxDepth, 0, -1):
        contents = ""
        prevIdx = -1
        i=0
        while(i < (linesLen)):
            currIdx = int(lines[i].split("~~")[0])
            tempList = []
            if(currIdx == prevIdx):
                while(currIdx == prevIdx and i < linesLen-1):
                    contents += lines[i]
                    contents += "\n"
                    i += 1
                    currIdx = int(lines[i].split("~~")[0])
                    
            else:
                if(currIdx<j):
                    while(currIdx<j and i < linesLen-1):
                        contents += lines[i]
                        if(j!=maxDepth): contents += "\n"
                        i += 1
                        currIdx = int(lines[i].split("~~")[0])
                        
                prevIdx = currIdx
                currLine = ""
                while(currIdx >= prevIdx):
                    if(currIdx == prevIdx): 
                        while((i < linesLen-1 and int(lines[i+1].split("~~")[0]) == prevIdx) and i < linesLen-1):
                            tempList.append(lines[i])
                            i += 1
                            currIdx = int(lines[i].split("~~")[0])
                            
                    if((i < linesLen-1 and int(lines[i+1].split("~~")[0]) > prevIdx)):
                        currLine += lines[i]
                        currLine += "\n"
                        i += 1
                        currIdx = int(lines[i].split("~~")[0])
                    
                    else:
                        if(i < linesLen-1): 
                            tempList.append(lines[i])
                            i += 1
                            currIdx = int(lines[i].split("~~")[0])
                        
                    if(currIdx < prevIdx):
                        break
                    
                    if(currIdx > prevIdx):        
                        while(currIdx > prevIdx and i < linesLen-1):
                            currLine += lines[i]
                            currLine += "\n"
                            i += 1
                            currIdx = int(lines[i].split("~~")[0])
                             
                    if(i > (len(lines)-2)):
                        currLine += lines[i]
                        currLine += "\n"
                        i+=1
                        tempList.append(currLine[:-1])
                        currLine = ""
                        break
                    
                    tempList.append(currLine[:-1])
                    currLine = ""
                    
                    currIdx = int(lines[i].split("~~")[0])
                    
                tempList.sort(cmp=None, key=None, reverse=False)
                
                for item in tempList:
                    lenSplit = len(item.split("\n"))
                    if(item.endswith("\n")): item = item[:-1]
                    k = 0
                    for line in item.split("\n"):
                        k+=1
                        contents += line
                        if(lenSplit>1 and j!=maxDepth and k!=lenSplit): contents += "\n"
                    contents += "\n"
            if(i == linesLen): i+=1 
                  
        lines = contents.split("\n")
        lines = lines[:-1]
        
    with open(file, 'w') as the_file:
        the_file.write(contents)
    
def generatedDiffGraphData(file1, file2):
    resultFile = currentWorkingDir + '/output/output.txt'
    f = open(file1,"r")
    lines1 = f.readlines()
    f = open(file2,"r")
    lines2 = f.readlines()
    i = 0
    j = 0
    
    contents = ""
        
    while(i<len(lines1) and j<len(lines2)):
        data1 = lines1[i].split("~~")
        data2 = lines2[j].split("~~")
        fileName1 = str(getFilename(data1[1]))
        fileName2 = str(getFilename(data2[1]))
        if(int(data1[0]) == int(data2[0]) and ((data1[1][0:data1[1].find("(")] + "_" + fileName1) == (data2[1][0:data2[1].find("(")] + "_" + fileName2))): 
            sumVal = str(int(data1[2])+int(data2[2]))
            childFlag = 0
            if(int(data1[3]) != 0 or int(data2[3]) !=0):
                childFlag = 1
            contents += data1[0] + "~~" + data1[1] + "~~" + sumVal + "~~" + str(childFlag) +  "~~" + data1[4] 
            i += 1
            j += 1
        elif(int(data1[0]) == int(data2[0])):
            funcName1 = ""
            funcName2 = ""
            if(int(data1[0]) == 0):
                funcName1 = data1[1][0:data1[1].find("(")] + "_" + fileName1
                funcName2 = data2[1][0:data2[1].find("(")] + "_" + fileName2
            else:
                funcName1 = data1[1][0:data1[1].find("(")]
                funcName2 = data2[1][0:data2[1].find("(")]
            if(funcName1 > funcName2):
                contents += data2[0] + "~~" + data2[1] + "~~" + str(data2[2]) + "~~" + str(data2[3]) + "~~" + str(data2[4])
                j += 1
            else:
                contents += data1[0] + "~~" + data1[1] + "~~" + str(data1[2])+ "~~" + str(data1[3]) + "~~" + str(data1[4])
                i += 1
        elif(int(data1[0]) < int(data2[0])):
            contents += data2[0] + "~~" + data2[1] + "~~" + str(data2[2])+ "~~" + str(data2[3]) + "~~" + str(data2[4])
            j += 1
        else:
            contents += data1[0] + "~~" + data1[1] + "~~" + str(data1[2])+ "~~" + str(data1[3]) + "~~" + str(data1[4])
            i += 1
    while(i<len(lines1)):
        data1 = lines1[i].split("~~")
        contents += data1[0] + "~~" + data1[1] + "~~" + str(data1[2])+ "~~" + str(data1[3]) + "~~" + str(data1[4])
        i += 1
    
    while(j<len(lines2)):
        data2 = lines2[j].split("~~")
        contents += data2[0] + "~~" + data2[1] + "~~" + str(data2[2]) + "~~" + str(data2[3]) + "~~" + str(data2[4])
        j += 1
        
    with open(resultFile, 'w') as the_file:
        the_file.write(contents)                

def generateOutputFile(fileName, version):
    content = ""
    actualFileName = fileName[(fileName.rindex("/")+1):]
    childrenChangedFlag = 0
    recursiveFlag = 0
    linkCount = 0
    if(version == 1):
        linkCount = -1
    else:
        linkCount = 1
    data = open(fileName)
    flag = 0
    for line in data:
        recursiveFlag = 0
        leading_spaces = ((len(line) - len(line.strip())) - 1)/4
        ln = line.strip()
        if(leading_spaces == 0 and ln.find("main()")!=-1):
            flag = 1
        elif(leading_spaces == 0):
            flag = 1
        if(line.strip().find("recursive:")!=-1):
            recursiveFlag = 1
        if(flag == 1): 
            idxStr = ""
            if(leading_spaces <= 9): 
                idxStr = "0" + str(leading_spaces)
            else:
                idxStr = str(leading_spaces)
            content += idxStr + "~~" + line.strip() + "~~" + str(linkCount) + "~~" + str(childrenChangedFlag) + "~~" + str(recursiveFlag) + "\n"
            
    with open(currentWorkingDir + '/output/' + actualFileName + '_output.txt', 'w') as the_file:
        the_file.write(content)

def associateBugData(file):
    app.config.from_pyfile('config_file.cfg');
    bugFile = app.config["BUGDATA_FILE"]
    f = open(bugFile,"r")
    lines = f.readlines()
    f = open(file, "r")
    outputLines = f.readlines()
    outLines = []
    for line in outputLines:
        outLines.append(line)
    
    for line in lines:
        data = line.split(": ")
        bugId = data[0]
        if(data[1].endswith("\n")): data[1] = data[1][:-1]
        functions = data[1].split("#")
        i=0
        j=0
        pathLength = len(functions)
        bugIndices = []
        while i < len(outLines):
            if(j > len(functions)): break
            if(outLines[i].find(functions[j]+"()")!=-1):
                bugIndices.append(i)
                j+=1
                prevIdx = int(outLines[i].split("~~")[0])
                i+=1
                if(j > len(functions)): break
                if(len(bugIndices) == pathLength):
                    for inx in bugIndices:
                        outData = outLines[inx].split("~~")
                        if(len(outData) > 5):
                            outLines[inx] = outLines[inx][:-1] + "##" + bugId + "\n"
                        else: outLines[inx] = outLines[inx][:-1] + "~~" + bugId + "\n"
                    #break
                    outLines = outLines
                    bugIndices = []
                    #prevIdx = -1
                    j=0
                currIdx = int(outLines[i].split("~~")[0])
                while(currIdx > prevIdx and i<len(outLines)-1):
                    if(outLines[i].find(functions[j]+"()")!=-1):
                        bugIndices.append(i)
                        j+=1
                        prevIdx = int(outLines[i].split("~~")[0])
                        i+=1
                        currIdx = int(outLines[i].split("~~")[0])
                    else:
                        i+=1
                        currIdx = int(outLines[i].split("~~")[0])
                if(len(bugIndices) == pathLength):
                    for inx in bugIndices:
                        outData = outLines[inx].split("~~")
                        if(len(outData) > 5):
                            outLines[inx] = outLines[inx][:-1] + "##" + bugId + "\n"
                        else: outLines[inx] = outLines[inx][:-1] + "~~" + bugId + "\n"
                outLines = outLines
                bugIndices = []
                prevIdx = -1
                j=0
            else:
                i+=1
                continue
    with open(file, 'w') as the_file:
        for line in outLines:
            the_file.write(line)
    
def parseData(fileName1, fileName2):
    actualFileName1 = fileName1[(fileName1.rindex("/")+1):]
    generateOutputFile(fileName1, 1)
    file1 = currentWorkingDir + '/output/' + actualFileName1 + '_output.txt'
    
    if(fileName2 == None):
        file2 = None
    else:
        actualFileName2 = fileName2[(fileName2.rindex("/")+1):]
        generateOutputFile(fileName2, 2)
        file2 = currentWorkingDir + '/output/' + actualFileName2 + '_output.txt'
    
    prevIdx = -1

    outFile = currentWorkingDir + '/output/output.txt'
    sortFile(file1)
    if(file2 != None):
        sortFile(file2)
        getDiffData(file1, file2)
        getChildChangeCounts(outFile)
    else:
        f = open(file1,"r")
        lines1 = f.readlines()
        with open(outFile, 'w') as the_file:
            for line in lines1:
                the_file.write(line)

    associateBugData(outFile)
    outData = open(outFile)
           
    finalContent = "{\"idx\": \"-1\", \"name\": \"root\", \"filename\": \"\", \"linkCount\": 0, \"childrenChangedFlag\": 0, \"recursive\": 0, \"bugs\": \"\", \"children\":["
    for line in outData:
        data = line.split("~~")
        idx = int(data[0])
        name = data[1][0:data[1].find("(")]
        linkCount= data[2]
        if(file2 == None):
            linkCount = 0
        childrenChangedFlag = int(data[3])
        recursive = int(data[4])
        if(len(data)>5):
            bugs = "\"" + data[5][:-1] + "\""
        else:
            bugs = "\"\""
        if(idx > prevIdx):
            finalContent += "\n" + printTabs(idx) + "{\"idx\": \"" +  str(idx) + "\",\"name\": \"" +  name + "\",\"filename\": \"" + str(getFilename(data[1])) + "\",\"linkCount\": " + str(linkCount) + ",\"childrenChangedFlag\": " + str(childrenChangedFlag) + ",\"recursive\": " + str(recursive) + ",\"bugs\": " + bugs +",\"children\": [" 
        elif idx < prevIdx:
            finalContent += "]}\n" + printTabs(prevIdx) + addClosingBraces(prevIdx-idx)#"]"
            finalContent += ","
            finalContent += "\n" + printTabs(idx) + "{\"idx\": \"" +  str(idx) + "\",\"name\": \"" +  name + "\",\"filename\": \"" + str(getFilename(data[1])) + "\",\"linkCount\": " + str(linkCount) + ",\"childrenChangedFlag\": " + str(childrenChangedFlag) + ",\"recursive\": " + str(recursive) + ",\"bugs\": " + bugs + ",\"children\": [" 
        else:
            finalContent += "]},\n" + printTabs(idx) + "{\"idx\": \"" +  str(idx) + "\",\"name\": \"" +  name + "\",\"filename\": \"" + str(getFilename(data[1])) + "\",\"linkCount\": " + str(linkCount) + ",\"childrenChangedFlag\": " + str(childrenChangedFlag) + ",\"recursive\": " + str(recursive) + ",\"bugs\": " + bugs + ",\"children\": [" 
        prevIdx = idx 
    
    finalContent += printClosures(prevIdx)
    finalContent += "\n]}"
    return finalContent

def getFilename(data):
    pattern = r'<*\.c'
    fileName = ""
    m = re.search(pattern, data)
    if(m!=None):
        names = re.findall(r'\b(\w+\.c)\b',data)
        fileName += names[0]
    return fileName
    
def addClosingBraces(count):
    outStr = ""
    for i in range(count):
        outStr += "\n" + printTabs(count-i+1) + "]}"
    return outStr

def printClosures(count):
    outStr = ""
    for i in range(count+1):
        if i==0:
            outStr += "]}"
        else:
            outStr += "\n" + printTabs(count-i+1) + "]}"
    return outStr

def printTabs(count):
    outStr = ""
    for i in range(count):
        outStr += "\t"
    return outStr        

@app.route('/Success', methods=['GET', 'POST'])
def Success():
    return render_template('gdiff.html'); 
