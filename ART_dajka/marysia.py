import re

with open('dajka.tex', 'r') as file:
    data = file.read().split('\n')

tex_file = open("dajka-PU.tex", "w")




for line in data:
    printendline = True
    line = re.sub('(\\s)([a-zA-Z])\\s', '\g<1>\g<2>~', line)
    line = re.sub('(\\{)([a-zA-Z])\\s', '\g<1>\g<2>~', line)
    line = re.sub('^([a-zA-Z])\\s', '\g<1>~', line)
    if bool(re.search('(\\s)([a-zA-Z])$', line)):
        printendline = False
    line = re.sub('(\\s)([a-zA-Z])$', '\g<1>\g<2>~', line)
    tex_file.write(line)
    if printendline:
       tex_file.write('\n')




tex_file.close()