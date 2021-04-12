#!/usr/env/python
#opens the file
gen_file = open('test.txt', mode='r')
gen_failed_file = open('failed_pattern', mode='w')


#looks if there is a first line in the file
first_line = True
#removes space at the end of the line
for line in gen_file:
    line = line.rstrip("\n\r")
    #prints first line
    if first_line:
        print(line)
        #prevents the code from using the first line
        first_line = False
        continue

    translation = {}
    # looks if within the data there is (AT,AC,AG,TA,TC,TG,GT,GC,GA,CA,CT,CG) and converts them to 1
    if ('AT' in line) or ('AG' in line) or ('AC' in line) or ('GA' in line) \
            or ('GT' in line) or ('GC' in line) or ('TA' in line) or ('TG' in line) \
            or ('TC' in line) or ('CA' in line) or ('CT' in line) or ('CG' in line):
        translation = {'AT': '1', 'AG': '1', 'AC': '1', 'GA': '1', 'GT': '1',
                       'GC': '1', 'TA': '1', 'TG': '1', 'TC': '1', 'CA': '1',
                       'CT': '1', 'CG': '1'}

    #looks if withing data there is AA and GG and also will accept AG in that (AA GG)
    # convination. (same for the others)
    if ('AA' in line) and ('GG' in line):
        translation.update({'AA': '0', 'GG': '2'})
    elif ('TT' in line) and ('GG' in line):
        translation.update({'TT': '0', 'GG': '2'})
    elif ('AA' in line) and ('CC' in line):
        translation.update({'AA': '0', 'CC': '2'})
    elif ('CC' in line) and ('TT' in line):
        translation.update({'CC': '0', 'TT': '2'})
    elif ('AA' in line) and ('TT' in line):
        translation.update({'AA': '0', 'TT': '2'})
    elif ('GG' in line) and ('CC' in line):
        translation.update({'GG': '0', 'CC': '2'})
    elif 'AA' in line:
        translation.update({'AA': '0'})
    elif 'GG' in line:
        translation.update({'GG': '0'})
    elif 'TT' in line:
        translation.update({'TT': '0'})
    elif 'CC' in line:
        translation.update({'CC': '0'})
    elif 'FF' in line:
        translation.update({'FF': 'FF'})
    #elif '--' in line:
        #translation.update({'--': '--'})
    #if nothing matches previous combinations then "translation" is empty and
    # it prints the error and stops running.
    else:
        gen_failed_file.write(line)
        continue
        #print('Error: the line does not contain any of the tested genotypes')
        #print(line)
        #exit()

    #specifies that every element in each line is separated from each other by tabs
    line_elements = line.split('\t')
    #specifies that each line starts with the element 0 which is the marker id
    new_line = line_elements[0]
    #specifies that the code will start running in the second element which is the first genotype after the marker id.
    for word in line_elements[1:]:
        #if the word is in "translation" then it will be asigned to "new_word". If the word is an empty space (tab)
        #then it will be converted to x. If it does not look like anything, it will be converted to ERROR
        if word in translation:
            new_word = translation[word]
        elif word == '':
            new_word = 'x'
        else:
            new_word = 'Bad_call'

        new_line = new_line + '\t' + new_word
    print(new_line)
