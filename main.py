from os import fspath
import datetime
import pathlib
import shutil
def getListOfFiles():
    res=[]
    path='E:/vitual1'
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
    for index in range(0,len(files),4):
        if pathlib.Path.exists(pathlib.Path("E:/","sorted", datetime.datetime.fromtimestamp(files[index+2]).strftime('%Y-%m-%d'))) != True:
            pathlib.Path("E:/","sorted", datetime.datetime.fromtimestamp(files[index+2]).strftime('%Y-%m-%d'),).mkdir()
        if files[index] not in results and files[index+3] not in results:
            results.append(files[index])
            results.append(files[index+1])
            results.append(files[index+2])
            results.append(files[index+3])         
    print(results)
    return results

def copy_and_delete_files():
    sort_files=sort_files_and_fotos()
    for index in range(0,len(sort_files),4):
        shutil.copy2(pathlib.Path(sort_files[index+1], sort_files[index]), pathlib.Path("E:/","sorted", datetime.datetime.fromtimestamp(sort_files[index+2]).strftime('%Y-%m-%d'), sort_files[index]))
        print('file ' + fspath(pathlib.Path(sort_files[index+1], sort_files[index])) + " copied")
        pathlib.Path(sort_files[index+1], sort_files[index]).unlink()
        print('file ' + fspath(pathlib.Path(sort_files[index+1], sort_files[index])) + ' deleted')
    
if __name__ == '__main__':
    copy_and_delete_files()