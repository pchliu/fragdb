import os, time
import pandas as pd

def blocks_v1():
        this_file  = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(this_file, "blocks_PDB_105.json")
        return pd.read_json(path)


if  __name__ == "__main__":
    print(blocks_v1())