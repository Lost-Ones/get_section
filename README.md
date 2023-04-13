# get_section

One can gather matching 'sections' of a text file.  To sample this app, use the sample.txt with the 'First' word as 'Fa' and 'End' word as '\n' ( new line ). This sample text is a very small sample of a cisco configuration.

Data is returned as a dictionary and print text id provided when the application is ran.

This can be called by another application.

ex:
import get_section as gs

text = 'sample.txt'
start = 'Fa'
stop = '\n'
data = gs.GetSection(text=text, start=start, stop=stop)

