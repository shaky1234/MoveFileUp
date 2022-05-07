#Moves file one level up from parent folder based on the extension
from os import walk, rename

#Parent path for directory
#Remember to use \\ for \ and to end with a \\
#ie "C:\\Program Files (x86)\\Common Files\\"
startpath = "C:\\Program Files (x86)\\Common Files\\"
extension = ".mp4"

#Grabs list of all directories in parent folder and places it in dirlist
dirlist = []
for (dirpath, dirname, filenames) in walk(startpath):
   
    for d in dirname:dirlist.append(d)

    break


for q in dirlist: 
    for(dpath,dname,fnames) in walk(startpath+q): 
        for f in fnames: 
            if f.endswith(extension): 
                print("Moving file: {0} from {1} to {2}".format(f,dpath,startpath))
                rename(dpath+"\\"+f, startpath+f)
        


    


