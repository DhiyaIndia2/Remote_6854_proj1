
#function: convert the list into dictionary pertaining to homing point of the corresponding port
def add_chunk_to_dictt_homing_point(chunk):
    pass

#
def add_chunk_to_dictt_port_move(chunk)
#open file and read all lines and store in 'lines' variable
file1 = open('C:\\Users\\rathithya\\Desktop\\Project1\\Mini_Project1_Data.log','r')
lines = file1.readlines()

#data is stored in file
#read lines and import the data to dictionaries pertaining to data:

csv_file = open('temp_files.csv','a+')
#csv_file.truncate() #ensure clean file
chunk = []
dictt = {}
no_of_lines = len(lines)
for i in range(no_of_lines):
    if( 'Joint command' in lines[i]):
        start = i+1
        end = 0
        for j in range(start, no_of_lines):
            if('STMOV' in lines[j]):
                i = end = j
                break
        chunk = lines[start:end]
        #csv_file.writelines(chunk)
        add_chunk_to_dictt_homing_point(chunk)

        chunk.clear()
    
    if('STMOV' in lines[i]):
        start = i
        end = 0
        for j in range(start, no_of_lines):
            if('END' in lines[j]):
                i = end = j
                break
        chunk.append(start:end)
        add_chunk_to_dictt_port_move(chunk)


csv_file.close()
