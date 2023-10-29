"""Working with Text Files"""
import os
import toolkit_config as cfg

#Path
DATADIR = '<file path>'
NEWDIR = os.path.join(cfg.DATADIR, '<New File.txt>')

#Opening
fobj = open('<file name', mode= '<mode>')

#Reading
#Content
fobj = open('<file name', mode= '<mode>')
cnts = fobj.read()

<function>

cnts = fobj.close()

#Line Content
for line in fobj:
    <function>

"""Overview"""
# ----------------------------------------------------------------------------
# Comparing different approaches to get the contents
# ----------------------------------------------------------------------------
# Remember that we previously closed the file so we need to open it again
fobj = open(SRCFILE, mode='r')
# Contents using `.read`
cnts = fobj.read()
print(f"First 20 characters in cnts: '{cnts[:20]}'")
# Start with an empty string
cnts_copy = ''
# Iterate over each line of fobj
for line in fobj:
 # Add this line to the string `cnts_copy`
 cnts_copy += line
# Print the result
print(f"First 20 characters in cnts_copy: '{cnts_copy[:20]}'")
# Close the file
fobj.close()


"""In-Class Exercise"""
def freqword(filepath):
    with open(filepath) as file:
        counts = dict()
        for line in file:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word,0) + 1

    maxcount = None
    maxword = None
    for word,count in counts.items():
        if maxcount in None or count > maxcount:
            maxword = word
            maxcount = count
    return (f'The most frequent word is: {maxword}, and the number of times appear is: {maxcount}')

"""PANDAS"""
# Pandas Series
<data> = [...,...,...]
<index> = [...,...,...]
ser = pd.Series(data= <data>, index= <index>)

# Pandas Array
arr = pd.Array()

#Pandas Index
ind = pd.Index()

#Pandas Dataframe
df = pd.DataFrame()

"""In-Class Exercise"""
columns = ['a','b']
index = ['c','d','e']
a_data = [1,2,3]
b_data = [4,5,6]

ser1 = pd.Series(data= a_data, index= index)
ser2 = pd.Series(data= b_data, index= index)

df = pd.DataFrame({columns[0] : ser1, columns[1] : ser2})

'''or'''

df = pd.DataFrame(
        {
            'a': [1,2,3],
            'b': [4,5,6],
        },
        index= ['c','d','e']
    )
