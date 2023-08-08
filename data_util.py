import os
import csv
from pathlib import Path

PROMPTS_DIR = Path(__file__).parent / "prompts"
DATA_DIR = Path(__file__).parent / "data"

SEPERATOR = ','
DROP_COLUMNS = ['Fname', 'stage temperature', 'monitor temperature', 'Rxx State', 'Rxy State']


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