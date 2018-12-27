# import pickle

# '''
# 要保存數據，使用dump,'b'表示已二進為模式打開數據文件
# '''
# with open('mydata.pickle','wb') as mysavedata:
#     pickle.dump([1, 2, 'three'], mysavedata)

# '''
# 使用load，從文件恢復數據，將恢復的數據賦予一個變數
# '''
# with open('mydata.pickle','rb') as myrestoredata:
#     a_list = pickle.load(myrestoredata)

# print(a_list)
import sys, os
import pickle
abs_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(abs_path)
from nester import nester

new_man = []
new_other = []
try:
    with open('man_data.txt','rb') as man_file:
        new_man = pickle.load(man_file)
    with open('other_data.txt','rb') as other_file:
        new_other = pickle.load(other_file)
except IOError as err:
    print('File error: '+str(err))
except pickle.PickleError as perr:
    print('picking error: '+str(perr))

nester.print_lol(new_man)
print('------------------------------------------------')
nester.print_lol(new_other)