# Genotyping-format-converter
Converts a letter format (AA, AB, BB, error, empty) into a 'number format' (0,1,2, x) respectively.

To run the code : 

```
python change_genotype_format.py 
```
The name of the file test.txt is added in line 3 of the code. To used the code with other data change the file name in line 3.

After running the test you should get the following results:

```
probeset_id	variety_1	variety_2	variety_3	variety_4	variety_5	variety_6
marker_1	0	2	1	0	2	2
marker_2	0	2	Bad_call	1	0	2
marker_3	0	2	2	Bad_call	0	0
marker_4	0	Bad_call	2	1	1	2
```
If you want to save the results into a file run the code using:

```
python change_genotype_format.py > nameoffile.txt
```

Contributors
------------

- Virginia Rodriguez Almansa
- Miquel Perello Nieto
