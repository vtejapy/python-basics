import shutil
import os
source = os.listdir("/tmp/")
destination = "/tmp/newfolder/"
for files in source:
    if files.endswith(".txt"):
        shutil.copy(files,destination)
        
       
       
import shutil  
shutil.copyfile('/path/to/file', '/path/to/other/phile')  


import shutil
import os
source = os.listdir("/tmp/")
destination = "/tmp/newfolder/"
for files in source:
    if files.endswith(".txt"):
        shutil.move(files,destination)
        
import shutil
import os
SOURCE = "samples"
BACKUP = "samples-bak"
# create a backup directory
shutil.copytree(SOURCE, BACKUP)
print os.listdir(BACKUP)


import shutil
shutil.rmtree('one/two/three')


>>> import shutil
>>> shutil.move("server.log", "server.log.backup")
>>> shutil.move("image.png", "/home/user/")


>>> shutil.copy("image.png", "/home/user/")


>>> import shutil
>>> shutil.os
