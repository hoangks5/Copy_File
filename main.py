import shutil
import os

try:
    # Tao thu muc moi
    os.mkdir('AutoTool.Vn') 
except:
    pass


# Doc tat ca thu muc nick
os.chdir('./')
list = os.listdir()

for acc in list:
    try:
        src = './'+acc+'/'+acc+'.session'
        dst =  './AutoTool.Vn/'+acc+'.session'
        shutil.copyfile(src, dst)
    except:
        pass