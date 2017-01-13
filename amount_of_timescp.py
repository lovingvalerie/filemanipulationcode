#take in a file object and string query and return the amount
#of times it happens in a file.


#this functoin takes in the name of a file,
#reads it and returns a file object.`

def get_file_object(file_name):
    f = open(file_name, 'r')
    list_of_lines = f.readlines()
    return list_of_lines
    f.close()
#print get_file_object('some_text.txt')

#this function prompts the user for a string query
#and returns that string
def get_query():
    query = raw_input('What word are you looking for?')
    return query

#print get_query()

def num_times(file_object, query):
    #make a list to later append # of times to
    list_of_locations = []
    #iterate through each line
    #if query is in that line
    #append it to list_of_locations
    for line in file_object:
        if query in line:
            list_of_locations.append(line)
    #return the len or # of times the query 
    #occured in file
    return len(list_of_locations)

print num_times(get_file_object('some_text.txt'), get_query())
