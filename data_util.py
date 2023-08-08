import os
import csv
from pathlib import Path
import pandas as pd

PROMPTS_DIR = Path(__file__).parent / "prompts"
DATA_DIR = Path(__file__).parent / "data"

SEPERATOR = ','
DROP_COLUMNS = ['Fname', 'stage temperature', 'monitor temperature', 'Rxx State', 'Rxy State']


def read_column_description():
    """

    Returns:
    """

    fn = os.path.join(DATA_DIR, "column_description.txt")
    with open(fn, "r") as f:
        cn_wds = f.readlines()
    cn_wds = [cn_line.strip() for cn_line in cn_wds]
    cns = []
    wds = []
    for cn_wd in cn_wds:
        cns.append(cn_wd.split(":")[0])
        wds.append(":".join(cn_wd.split(":")[1:]))
    df = pd.DataFrame(zip(cns, wds), columns=["column", "description"])
    return df



def csv2txt(file_name):
    """
    Converts data csv in txt format for prompting : adapted from Brian
    Args:
        file_name: string

    Returns:

    """
    out_fn = os.path.join(DATA_DIR, '{}.txt'.format(file_name))
    with open(os.path.join(DATA_DIR, file_name), mode='r', newline='') as r:
        with open(out_fn, mode='w') as w:
            reader = csv.reader(r)
            for i, row in enumerate(reader):
                if i == 0:
                    drop_idx = [row.index(col.strip()) for col in DROP_COLUMNS]
                filtered = [elem for idx, elem in enumerate(row) if idx not in drop_idx]
                w.write('{}{}'.format(SEPERATOR.join(filtered), os.linesep))
    return out_fn


def csv2prompt_data(file_name: str, column_list = None, max_rows = None, separator = ' | '):
    """

    Args:
        file_name: str: string filename
        column_list: list: list of columns to keep, default all columns
        max_rows: int: max number of rows, default all rows

    Returns: str:
    return format
    BatchID | Fidx | elapsed time | sigma square hall coefficient | conductivity
    P1HB | 1 | 739085.5081 | 0.000112568 | 0.005789713
    P1HB | 2 | 739085.5149 | 0.00011213 | 0.005853298
    P1HB | 3 | 739085.5217 | 3.33892048 | 0.005794994
    P1HB | 4 | 739085.5285 | 0.000111396 | 0.005780041
    P1HB | 5 | 739085.5353 | 0.000111971 | 0.005793127

    """
    prompt_data = []
    with open(os.path.join(DATA_DIR, file_name), mode='r', newline='') as r:
        reader = csv.reader(r)
        for i, row in enumerate(reader):
            if max_rows is not None and i >= max_rows + 1:
                break
            if column_list is None:
                prompt_data.append(separator.join(row))
            else:
                if i == 0:
                    col_idx = [row.index(col.strip()) for col in column_list]
                filtered = [elem for idx, elem in enumerate(row) if idx in col_idx]
                prompt_data.append(separator.join(filtered))

    return os.linesep.join(prompt_data)

print(csv2prompt_data('TB_demo_v2.csv', column_list=['BatchID', 'Fidx', 'elapsed time', 'sigma square hall coefficient', 'conductivity'], max_rows = 3, separator = ', '))