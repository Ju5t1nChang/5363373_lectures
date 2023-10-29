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
