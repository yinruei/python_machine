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
    data_man = open('man_data.txt','w')
    data_other = open('other_data.txt','w')
    
    print(man, file = data_man)
    print(other, file = data_other)

except IOError:
    print("FILE error.")

finally:#不論什麼情況，finally底下都會運行
    data_man.close()
    data_other.close()
