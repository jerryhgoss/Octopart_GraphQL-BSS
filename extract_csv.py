import csv
import pandas as pd
import requests

desired_width = 320

pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', None)


# important values: R, C, D, FB, L
def extract_bom_data(csvfile):
    with open(csvfile, 'r') as parts_raw:
        csv_reader = csv.reader(parts_raw, delimiter=',')  # csv reader filetype
        # print(type(csv_reader))
        line_count = 0
        for row in csv_reader:
            # print('csv: ', row)
            if line_count == 0:
                print(f'Column names are: {", ".join(row)}')
                colnames = row
                print(colnames)
                Rdf = pd.DataFrame(columns=colnames)  # shared attributes via the BOM
                Rdf.columns = Rdf.columns.str.lower()
                Rdf.columns = Rdf.columns.str.strip()
                Rdf.rename(columns={"pn": "mpn_or_sku"}, inplace=True)
                colnames = Rdf.columns

                Rlist = []
                Cdf = Rdf.copy(deep=True)  # capacitors
                Clist = []
                Ddf = Rdf.copy(deep=True)  # LEDs and Diodes
                Dlist = []
                FBdf = Rdf.copy(deep=True)  # ferrite bead
                FBlist = []
                Ldf = Rdf.copy(deep=True)  # inductors
                Llist = []
                line_count += 1

            elif row[0][0] == 'R':
                Rlist.append(row)
            elif row[0][0] == 'C':
                Clist.append(row)
            elif row[0][0] == 'D':
                Dlist.append(row)
            elif row[0][0:2] == 'FB':
                FBlist.append(row)
            elif row[0][0] == 'L':
                Llist.append(row)
            line_count += 1
        parts_raw.close()
    # print(Rdf.shape)

    print(colnames)
    limit = 1
    start = 0
    temp = pd.DataFrame(Rlist, columns=colnames)
    Rdf = pd.concat([temp, Rdf])
    Rdf = Rdf.drop(columns=['quantity', 'footprint', 'value', 'dnp', 'reference', 'datasheet'])
    Rdf['reference'] = Rdf["mpn_or_sku"]
    Rdf["limit"] = limit
    Rdf["start"] = start

    temp = pd.DataFrame(Clist, columns=colnames)
    Cdf = pd.concat([temp, Cdf])
    Cdf = Cdf.drop(columns=['quantity', 'footprint', 'value', 'dnp', 'reference', 'datasheet'])
    Cdf['reference'] = Cdf["mpn_or_sku"]
    Cdf["limit"] = limit
    Cdf["start"] = start

    temp = pd.DataFrame(Dlist, columns=colnames)
    Ddf = pd.concat([temp, Ddf])
    Ddf = Ddf.drop(columns=['quantity', 'footprint', 'value', 'dnp', 'reference', 'datasheet'])
    Ddf['reference'] = Ddf["mpn_or_sku"]
    Ddf["limit"] = limit
    Ddf["start"] = start

    temp = pd.DataFrame(FBlist, columns=colnames)
    FBdf = pd.concat([temp, FBdf])
    FBdf = FBdf.drop(columns=['quantity', 'footprint', 'value', 'dnp', 'reference', 'datasheet'])
    FBdf['reference'] = FBdf["mpn_or_sku"]
    FBdf["limit"] = limit
    FBdf["start"] = start

    temp = pd.DataFrame(Llist, columns=colnames)
    Ldf = pd.concat([temp, Ldf])
    Ldf = Ldf.drop(columns=['quantity', 'footprint', 'value', 'dnp', 'reference', 'datasheet'])
    Ldf['reference'] = Ldf["mpn_or_sku"]
    Ldf["limit"] = limit
    Ldf["start"] = start

    print("Final column names are: ", Ldf.columns)
    return Rdf, Cdf, Ddf, Ldf, FBdf


# bomdata = 'ModularControlPCBA.csv'
# Rdf, Cdf, Ddf, Ldf, FBdf = extract_bom_data(bomdata)
# print('R\n', Rdf)
# print('C\n', Cdf)
# print('D\n', Ddf)
# print('FB\n', FBdf)
# print('L\n', Ldf)


print('Hello Octopart!')
