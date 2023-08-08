from Task1 import DATA_DIR
from Task1 import csv2txt, csv2prompt_data, read_column_description


clm_nm = read_column_description()
all_column_list = ["BatchID", "Fidx", "elapsed time", "optical density", "Monitor photo density", "stage temperature",
                        "sample temperature", "monitor temperature", "Type", "Rxx State", "Rxy State", "sheet resistance",
                        "Hall resistance", "Hall resistivity", "conductivity", "Hall coefficient", "sigma square hall coefficient",
                        "Hall density", "Hall mobility", "wavelength"
                      ]
useful_column_list = ["BatchID", "Fidx", "elapsed time", "optical density", "Monitor photo density", "sheet resistance",
                        "Hall resistance", "Hall resistivity", "conductivity", "Hall coefficient", "sigma square hall coefficient",
                        "Hall density" ]
string = csv2prompt_data("TB_demo_v2.csv", column_list=useful_column_list, max_rows=10)
print(string)



