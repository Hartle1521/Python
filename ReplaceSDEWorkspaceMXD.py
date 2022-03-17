#################################################################################################################
#
# Author: Jacob Hartle
# Creation Date: 03/17/2022
# 
# Goal: Go through a directory of MXDs and replace the workspace for layers from one SDE connection to another. 
#       The names of the layers must be the same in both SDE databases. Ex: DB1.SDE.TestFC   DB2.SDE.TestFC
#
#################################################################################################################

# importing modules
import arcpy, os

# set variables: Folder with MXDs, new SDE file, old SDE file
folderPath = r"C:\Users\jaco9840\Desktop\Mxds"
oldSDEConnection = r"C:\Users\jaco9840\AppData\Roaming\ESRI\Desktop10.7\ArcCatalog\Connection to supt0011367.sde"
NewSDEConnection = r"C:\Users\jaco9840\AppData\Roaming\ESRI\Desktop10.8\ArcCatalog\Connection to supt0011367 (2).sde"

# go through the folder specified above and check for .mxd files
for filename in os.listdir(folderPath):
        fullpath = os.path.join(folderPath, filename)
        # print(fullpath)
        if os.path.isfile(fullpath):
                basename, extension = os.path.splitext(fullpath)
                if extension.lower() == ".mxd":
                        mxd = arcpy.mapping.MapDocument(fullpath)
                        # get MXD name and append _New to the name and will be used at the end to save a copy with the updated workspace paths
                        mapPath = mxd.filePath
                        fileName = os.path.basename(mapPath)
                        mxdName = fileName.split('.')[0]
                        mxdOutput = mxdName + "_New"
                        print("Beginning to go through " + fileName)
                        # list layers in the MXD
                        for lyr in arcpy.mapping.ListLayers(mxd):
                                # if layer supports the DataSource property, check if layer workspace path is set to the old SDE and if so extract the name and replace it with the new SDE
                                if lyr.supports('DATASOURCE'):
                                        if lyr.workspacePath == oldSDEConnection: 
                                                print("Finding layers that use the old SDE Connection")
                                                newName = lyr.name
                                                NewNameSegment = newName.split('.')[2] # take everything after second . ex: DBName.SDE.SomeFC -> Result SomeFC
                                                print("Layer name Slice: " + str(NewNameSegment))
                                                print(lyr.dataSource)
                                                lyr.replaceDataSource(NewSDEConnection, 'SDE_WORKSPACE', NewNameSegment)
                                                print("Replace DataSource completed")
                                                print(lyr.dataSource)
                                                print("Renaming layers in TOC")
                                                lyr.name = lyr.datasetName
                                                # save a copy of the MXD with the changes made to those datasets
                                                mxd.saveACopy(folderPath + r"\\" + mxdOutput + ".mxd")
        

