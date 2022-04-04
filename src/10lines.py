import os
import argparse
import pandas as pd

def read_df(filename):
    filepath = os.path.join("..", '..', '..', "CDS-LANG", "tabular_examples", filename)
    data = pd.read_csv(filepath)
    tenlines = data[0:10]
    print(tenlines)

def parse_args():
    # Initialise argparse
    ap = argparse.ArgumentParser()
    # command line parameters
    ap.add_argument("-f", "--filename", required = True, help = "The filename we want to work with")
    args = vars(ap.parse_args())
    return args

def main():
    args = parse_args()
    read_df(args["filename"])

# if namespace variable is "__main__"
#translation: when this script is executed from the command line, do the following
if __name__ == "__main__":
    main()

    