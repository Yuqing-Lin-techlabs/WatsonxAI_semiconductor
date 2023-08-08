import csv
import os

file_name = 'TB_demo_v2'
separator = ','
drop_columns = ['Fname', 'stage temperature', 'monitor temperature', 'Rxx State', 'Rxy State']

with open('{}.csv'.format(file_name), mode='r', newline='') as r:
    with open('{}.txt'.format(file_name), mode='w') as w:
        reader = csv.reader(r)
        for i, row in enumerate(reader):
            if i == 0:
                drop_idx = [row.index(col.strip()) for col in drop_columns]
            filtered = [elem for idx, elem in enumerate(row) if idx not in drop_idx]
            w.write('{}{}'.format(separator.join(filtered), os.linesep))