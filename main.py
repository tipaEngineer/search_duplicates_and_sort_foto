import os
import datetime
import pathlib
def getListOfFiles():
    res=[]
    path='E:/vitual'
    for p in pathlib.Path(path).rglob("*"):
        if p.is_dir():
            continue
        else:
          #  print(datetime.datetime.fromtimestamp(p.stat().st_mtime).strftime('%Y-%m-%d %H:%M'))
          # print(p.parent)
            res.append(p.name)
            res.append(p.parent)
            res.append(p.stat().st_mtime)
            res.append(p.stat().st_size)
    #print(res)
    return(res)

def show_path_files():
    res=getListOfFiles()
    
    for index in range(1,len(res),4):
       print(res[index])
        
if __name__ == '__main__':
    show_path_files()
    #getListOfFiles()