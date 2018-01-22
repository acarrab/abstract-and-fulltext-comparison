#!/usr/bin/env python3
import pexpect

# creates names of file and creates directory if it does not exist
class Manager:
    def __init__(self, inDirectory, outDirectory, filePrefix):
        self.inDirectory = inDirectory
        self.outDirectory = outDirectory
        self.filePrefix = filePrefix
        pexpect.run("mkdir {}".format(self.outDirectory))

    def toTag(self, number):
        return "_" + str(number).zfill(3) + ".txt"

    def getReadFileName(self, procId = 0):
        return self.inDirectory + "/" + self.filePrefix + self.toTag(procId)

    def getWriteFileName(self, procId = 0):
        return self.outDirectory + "/" + self.filePrefix + self.toTag(procId)
