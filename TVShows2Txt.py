# import modules
import os

# write tv show name, season number, and episodes to text file
def TVShow2txt(textfile, folder):
    # open the output text file, set it to write mode, and set the encoding to UTF-8
    output = open(textfile, "w", encoding = "utf-8")
    #Traverse all sub-directories.
    for subDir in os.walk(folder):
        # currently assumes no subfolders in the subdirectory, something to fix in the future - JH 12/29/2020
        if len(subDir[1]) == 0:         
            output.write(subDir[0].split('\\')[-2] + os.linesep)
            output.write("\t" + subDir[0].split('\\')[-1] + os.linesep)
            output.write("\t\t" + str(subDir[2]) + os.linesep)

TVShow2txt(r"C:\Users\Jacob Hartle\Desktop\output2.txt", r"I:\Synology_Backup\TV_Shows")