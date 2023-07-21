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


# def show_path_files():
#     res=getListOfFiles()
    
#     for index in range(1,len(res),4):
#        print(res[index])
        
def sort_files_and_fotos():
    files = getListOfFiles()
    print(111)
    print(pathlib.Path(files[1],files[0]))
    print(pathlib.Path("E:/","sorted", datetime.datetime.fromtimestamp(files[2]).strftime('%Y-%m-%d')))
    for index in range(0,len(files),4):
        if pathlib.Path.exists(pathlib.Path("E:/","sorted", datetime.datetime.fromtimestamp(files[index+2]).strftime('%Y-%m-%d'))) != True:
            pathlib.Path("E:/","sorted", datetime.datetime.fromtimestamp(files[index+2]).strftime('%Y-%m-%d'),).mkdir()
        for p in range(index+4,len(files)-index,4):
            if files[index]==files[p]:
                print('file is the same')
                             
               
               #  print(datetime.datetime.fromtimestamp(p.stat().st_mtime).strftime('%Y-%m-%d %H:%M'))
               
    # for index in range(0,len(files),4):
    #     if pathlib.Path.exists(files[index+1]) != True:
            
            
        
        
if __name__ == '__main__':
   sort_files_and_fotos()
   #show_path_files()
    #getListOfFiles()