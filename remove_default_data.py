import os
import shutil
dir_path = os.getcwd() + "/dataset/"

print(dir_path + '내 파일을 모두 삭제합니다.')
shutil.rmtree(dir_path)
print(dir_path + '내 파일을 모두 삭제하였습니다.')
os.makedirs(dir_path)
f = open(dir_path+'dataset','w')
f.write(' ')
f.close()