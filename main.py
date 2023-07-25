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
            res.append(p.name)
            res.append(p.parent)
            res.append(p.stat().st_mtime)
            res.append(p.stat().st_size)
    return(res)
        
def sort_files_and_fotos():
    results = []
    files = getListOfFiles()
    # print(111)
    # print(pathlib.Path(files[1],files[0]))
    # print(pathlib.Path("E:/","sorted", datetime.datetime.fromtimestamp(files[2]).strftime('%Y-%m-%d')))
    for index in range(0,len(files),4):
        if pathlib.Path.exists(pathlib.Path("E:/","sorted", datetime.datetime.fromtimestamp(files[index+2]).strftime('%Y-%m-%d'))) != True:
            pathlib.Path("E:/","sorted", datetime.datetime.fromtimestamp(files[index+2]).strftime('%Y-%m-%d'),).mkdir()
        if files[index] not in results and files[index+3] not in results:
            
            results.append(files[index])
            results.append(files[index+1])
            results.append(files[index+2])
    print(results)
    return results

def copy_and_delete_files():
    sort_files=sort_files_and_fotos()
    pathlib.Path("E:/", "sorted", datetime.datetime.fromtimestamp(sort_files[2]).strftime('%Y-%m-%d'),).mkdir
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                
        
        
if __name__ == '__main__':
   sort_files_and_fotos()
   #show_path_files()
    #getListOfFiles()