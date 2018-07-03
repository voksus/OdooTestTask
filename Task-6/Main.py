# ----------------------------------
#
# Created by Volodymyr Burtsev
#
# on 03.07.2018 in 20:51
#
# The project is < OdooTestTask >
#
# ----------------------------------

import json
import os
import sys
import shutil

with open("config.json") as configData:
    cfg = json.load(configData)

workingPath = cfg["workingPath"]
if not os.path.isdir(workingPath):
    print("The directory to be watching does not exist.\nProgram will terminated.")
    sys.exit()

doRemove = cfg["operations"]["filesToRemove"]
doRename = cfg["operations"]["filesToRename"]
doCopy = cfg["operations"]["filesToCopy"]
doReplace = cfg["operations"]["filesToReplace"]
doArch = cfg["operations"]["arch"]

workingDir = os.listdir(workingPath)
tmpDir = workingDir

print(">> " + os.getcwd())
print("Dir watching is started...")
while True:
    workingDir = os.listdir(workingPath)
    if not workingDir == tmpDir:
        print("Directory was changed")
        for file in workingDir:
            if not os.path.isdir(file):
                # check file type
                if file.endswith(doRemove):
                    os.remove(file)
                    print('File %s removed' % (file))
                elif file.endswith(doCopy[0]):
                    if not os.path.isdir(doCopy[1]):
                        os.mkdir(doCopy[1])
                    shutil.copyfile(file, os.path.join(doCopy[1], file))
                    print('File %s was copied' % (file))
                elif file.endswith(doRename[0]):
                    os.rename(file, file + doRename[1])
                    print('File %s was renamed' % (file))
                elif file.endswith(doArch[0]):
                    print("-- %s archivating is not implemented yet --" % (doArch[1]))

        tmpDir = workingDir

