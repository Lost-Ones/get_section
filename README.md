# get_section

Once can gather matching 'sections' of a text file.  To sample this app, use the sample.txt with the First word as 'Fa' and End word as '\n' ( new line )

The output is a dictionary.

This can be called by another applicatin 

start = 'Fa'
stop = '\n'
data = gs.GetSection(text=text, start=start, stop=stop)

