import pandas as pd



#input: file.readlines() object
def go_to_start(file1):
    file1.seek(0,0)

#returns all the lines in form of one list with each line as a string
def get_file(data_file, acess_type):
    file1 = open(data_file, acess_type)
    go_to_start(file1)
    return file1


def print_all_paths(lines_from_file) -> int: 
    print("src. to dst. port details:")
    
    line_count = 0
    for i in lines_from_file:
        line_count += 1
        if ('STMOV' in i) :
            ports = list(((i.split(' '))[1]).split('_'))
            #print(ports[1],' to ', ports[2],end=' ')
    return line_count

joint_titles= []
def create_dictt(lst, start_, end_) ->dict :
    joint_titles = lst[start_].split()
    len_of_cols = len(joint_titles)
    temp_dictt = dict.fromkeys(joint_titles)
    for i in range(start_ + 1, end):
        temp_lst = lst[i].split()

        for x in range(len_of_cols):
            temp_dictt.update({temp_dictt.x : temp_lst[x]})

    print(lst[start_ + 1])




    

#--------------------------------------------------------------------------------------------------
data_file = get_file("C:\\Users\\rathithya\\Desktop\\Project1\\Mini_Project1_Data.log", 'r')
data_lst = data_file.readlines()
line_count = print_all_paths(data_lst)

#starting to chunk data as per SRC. and DST.
#from Joint command to the 1st start => is the homing movt.
#from start to end => movt data of joints from given src_to_dst'
#from onr end to next start => homing point!

#put the chunk in temp_file.txt
data_frame = 0
temp_file = open('temp_file.csv', 'w+')
for i in range(line_count):
    if 'Joint command' in data_lst[i]:
        start, end = i+1, 0
        for temp in range(start, line_count):
            if ('END' in data_lst[temp]) or ('STMOV' in data_lst[temp]):
                i = end = temp
                break
        temp_file.writelines(data_lst[start:end])
        data_frame = pd.DataFrame(temp_file)
        #print(data_lst[start], '\n', data_lst[end])
        
        #data_series = pd.DataFrame(data_lst[start : end])
    if ('END' in data_lst[i]) or ('STMOV' in data_lst[i]):
        

    



"""

 obj = pd.Series()

#print(obj)
print(obj[3:])


file1.close() 
"""