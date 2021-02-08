import os
import sys
rootdir = "."
for root, subdirs, files in os.walk(rootdir):
    if("./content/" in root):
        for file_ in files:
           filepath = "/".join([root, file_])
           if("contents.lr" in filepath):
               content = open(filepath).read()
               path_tag=f'rootpath:{filepath}\n---\n'
               content=path_tag+content
               with open(filepath,"w") as outf:
                  outf.write(content) 
