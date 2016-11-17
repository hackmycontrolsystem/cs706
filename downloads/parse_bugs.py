# -*- coding: utf-8 -*-
from xml.dom import minidom
import re
doc = minidom.parse("show_bug1.xml")

cflowData = open("all_cflow",'r')
funcData = ""
for line in cflowData:
    funcData += line
bugs = doc.getElementsByTagName("bug")
outFile = open("output_bugList1.txt", "w")
for bug in bugs:
    bugId = bug.getElementsByTagName("bug_id")[0]
    print("id: %s" % bugId.firstChild.data)
    outFile.write("bug_id"+ ":" + bugId.firstChild.data +"\n")
    longDesc = bug.getElementsByTagName("long_desc")
    for descrpt in longDesc:
        textList = descrpt.getElementsByTagName("thetext")
        for text in textList:
            funcs = text.firstChild.data.replace(".", "")
            words = re.findall("(?:(?<=\s)|(?<=^))[a-zA-Z0-9_]*?(?=\s?\().*?(?=\s?\)*)", funcs)
            wordsList = words
            #re.findall(r'\b' + a + '()\b', funcData) >0
            wordsList = filter(lambda a: a!= "" and a + "()" in funcData, words)
            for word in wordsList:
                outFile.write("\t" + word + "\n")
    
    
