# get name of current working directory
start_directory = os.getcwd()

# create dictionary to hold the size of each folder in 
# the current working directory
top_level_directory_sizes = {}

# initialize directory
for i in os.listdir(start_directory):
    if os.path.isdir(i):
        top_level_directory_sizes[i] = 0

# traverse all paths from current working directory
for dirpath, dirnames, filenames in os.walk(start_directory):

    for f in filenames:
        fp = os.path.join(dirpath, f)
        #increment appropriate dictionary element: += os.path.getsize(fp)

for k,v in top_level_directory_sizes.iteritems():
    print k, v