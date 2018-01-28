import os
import os.path
from file import File as myFile
# import copyfile.copyfile as copyfile
from shutil import copyfile as copyfile


maybeNeedMergeFiles = ["strings.xml", "color.xml", "dimens.xml"]
class Directory:
    rooPath = ""
    fileToRead = []
    fileToCopy = []
    def __init__(self, rootPath):
        self.rooPath = rootPath


    def transDir(self):
        for dir,path,files in os.walk(self.rooPath):
            if ("\\robotest" in dir):
                continue
            if ('\\res' in dir):
                for file in files:
                    print("process file: " + dir + "\\" +file)
                    if  file in maybeNeedMergeFiles:
                        self.fileToRead.append(os.path.join(dir, file))
                    else:
                        self.fileToCopy.append(os.path.join(dir, file))
                # self.fileToRead.extend(dir + "\\" + file for file in files)

        self.readFile()
        self.copyFile()

    def readFile(self):
        for file in self.fileToRead:
            # self.generateNewPath(file)
            targetPath = self.generateNewPath(file)
            # print(os.curdir(targetDir))
            # if not os.path.exists(os.curdir(targetfile)):
            #     os.makedirs(os.curdir(targetfile))
            print("origin " + file)

            f = myFile(file)
            filenName = file.split('\\')[-1]
            print("target " + os.path.join(targetPath, filenName))
            f.copyFileTo(os.path.join(targetPath, filenName))


    def copyFile(self):
        for file in self.fileToCopy:
            # print(self.generateNewPath(file))
            targetPath = self.generateNewPath(file)
            fileName = file.split('\\')[-1]
            copyfile(file, os.path.join(targetPath, fileName))


    def generateNewPath(self, file):
        # for path in file.split("\\")[:-1]:
        #     print(path)
        targetPath = targetDir + "\\res" + ("\\").join(file.split("\\res")[-1].split("\\")[:-1])
        if not os.path.exists(targetPath):
            os.makedirs(targetPath)
        return targetPath
        # return targetDir + "\\res" + file.split("\\res")[-1]

rootPath = ".\\camera"
targetDir = ".\\camera\\robotest"
D = Directory(rootPath)
D.transDir()
