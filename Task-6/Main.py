# ----------------------------------
#
# Created by Volodymyr Burtsev
#
# on 03.07.2018 in 20:51
#
# The project is < OdooTestTask >
#
# ----------------------------------

import os, sys

workingPath = "./"
filesToRemove = "*.tmp"
filesToRename = "*.rnm"
filesToCopy = ["*.copy", "./copied"]
filesToReplace = ["*.replace", "./replaced"]

workingDir = os.listdir(workingPath)
tmp = workingDir
for fname in workingDir:
    break

print(workingDir)

while True:
    workingDir = os.listdir(workingPath)
    if not workingDir.__eq__(tmp):
        print("Directory was changed")
        break


def getlocaldata(sms, dr, flst):
    for f in flst:
        fullf = os.path.join(dr, f)
        if os.path.islink(fullf):
            continue  # don't count linked files
        if os.path.isfile(fullf):
            sms[0] += os.path.getsize(fullf)
            sms[1] += 1
        else:
            sms[2] += 1


def dtstat(dtroot):
    sums = [0, 0, 1]  # 0 bytes, 0 files, 1 directory so far
    os.path.walk(dtroot, getlocaldata, sums)
    return sums


report = dtstat('.')
print(report)
