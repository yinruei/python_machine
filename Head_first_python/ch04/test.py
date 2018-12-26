# try:
#     data = open('missing.txt')
#     print(data.readline(), end='')
# except IOError as err:
#     print('File error'+ str(err))
# finally:
#     if 'data' in locals():
#         data.close()
''' 
若用with就不需要finally，使用with時，不再需要操心關閉打開的文件
因為python解釋器會自動為你考慮這一點。
'''

import sys
import os
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('C:\\Users\\yinruei\\Desktop\\python機器學習\\python_machine\\Head_first_python')
# import nester
from nester import nester

man = []
other = []
try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':',1)
            line_spoken = line_spoken.strip()#刪除line_spoken變量中不需要的空白符
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)

        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')

try:
    with open('man_data.txt','w') as man_file:
        nester.print_lol(man, fn = man_file)
        # print(man, file=man_file)
    with open('other_data.txt','w') as other_file:
        nester.print_lol(other, fn = other_file)
        # print(other, file=other_file)
except IOError as err:
    print('File error: '+ str(err))