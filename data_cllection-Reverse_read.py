#open file and read all lines and store in 'lines' variable
file1 = open('C:\\Users\\rathithya\\Desktop\\Project1\\Mini_Project1_Data.log','r')
lines = file1.readlines()

#data is stored in file
#read lines and import the data to dictionaries pertaining to data:

csv_file = open('temp_files.csv','a+')
#csv_file.truncate() #ensure clean file
chunk_movt, chunk_homing = [], []
dictt = {}
no_of_lines = len(lines)

# at end of every iteration we will have path and its homing path in their corr. chunks
for i in range(no_of_lines-1, 0 , -1):
    if('END' in lines[i]):
        start = i
        end = 0
        for j in range(start, end, -1):
            if('STMOV' in lines[j]):
                i = end = j
                break
        # end has 'STMOV'
        #start has 'END'
        cache_path_name = ((lines[end].split())[1]).strip()

        #now get movt data of the port
        chunk_movt = lines[end+1 : start-1]
        
        #now get the corresponding homing point
        for j in range(end, 0, -1):
            if('END' in lines[j]):
                start  = j
                break
        #end has 'STMOV'
        #start is at 'END' of previous path 
        # so from this start->end we have homing point of our requested path
        chunk_homing = lines[start+1 : end-1]
        i = start+1 #updating i to help reduce iterations

        key = cache_path_name
        value = {'movt': chunk_movt, 'homing': chunk_homing}

        dictt.update({key : value})
        
        
