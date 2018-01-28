import os
import re
import copyfile


class Line:
    line = ""

    def __init__(self, line):
        self.line = line
        return
    def getName(self):
        pattern = re.compile('"\S+"')
        name = re.search(pattern, self.line)
        # name = self.line.match(pattern)
        # print(name.group())
        if name:
            return name.group()
        else:
            return ""

class File:
    filePath = ""
    fileHeader = ""
    headerFinish = False
    fileBody = []
    fileFooter = ""
    def __init__(self, filePath):
        self.filePath = filePath


    def copyFileTo(self, newFilePath):
        if (os.path.exists(newFilePath)):
            print("%s file exists, need merge"%newFilePath)
            self.mergeFile(newFilePath)
        else:
            print("%s new file"%newFilePath)
            copyfile.copyFile(self.filePath, newFilePath)

    def mergeFile(self, newFilePath):

        with open(self.filePath,"r", encoding="utf-8") as oldFile:
            for line in oldFile.readlines():
                if "name" in line:
                    self.fileBody.append(line)
                    self.headerFinish = True
                elif not self.headerFinish:
                    self.fileHeader += line + "\n"
                else:
                    self.fileFooter += line + "\n"
        # print("file header is " + self.fileHeader)
        # print("file footer is " + self.fileFooter)

        with open(newFilePath, "r", encoding="utf-8") as newFile:
            for line in newFile.readlines():
                if "name" in line:
                    self.fileBody.append(line)
        self.dedupeFile()
        with open(newFilePath, "w", encoding="utf-8") as newFile:
            newFile.write(self.fileHeader)
            for line in self.newFileBody:
                newFile.write(line)
            newFile.write(self.fileFooter)


    nameList = []
    newFileBody = []
    def dedupeFile(self):
        for line in self.fileBody:
            name = Line(line).getName()
            if name not in self.nameList:
                self.nameList.append(name)
                self.newFileBody.append(line)


if __name__=="__main__":
    originPath = ".\\camera\\mode\\res\\strings.xml"
    targetpath = ".\\camera\\mode\\res\\value\\strings.xml"
    file = File(originPath)
    file.copyFileTo(targetpath)
