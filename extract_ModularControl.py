import csv
import pandas as pd

desired_width = 320

pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', None)


# important values: R, C, D, FB, L
with open('ModularControlPCBA.csv', 'r') as parts_raw:
    csv_reader = csv.reader(parts_raw, delimiter=',')  # csv reader filetype
    # print(type(csv_reader))
    line_count = 0
    for row in csv_reader:
        # print('csv: ', row)
        if line_count == 0:
            print(f'Column names are: {", ".join(row[1:])}')
            headers = row[1:]
            Rdf = pd.DataFrame(columns=headers)  # shared attributes via the BOM
            Rdf.columns = Rdf.columns.str.strip()
            headers = Rdf.columns
            print(Rdf.columns)
            Rlist = []
            Cdf = Rdf.copy(deep=True)  # capacitors
            Clist = []
            Ddf = Rdf.copy(deep=True)  # LEDs and Diodes
            Dlist = []
            FBdf = Rdf.copy(deep=True)  # ferrite bead
            Ldf = Rdf.copy(deep=True)  # inductors
            line_count += 1

        elif row[0][0] == 'R':
            Rlist.append(row[1:])
            line_count += 1
        elif row[0][0] == 'C':
            Clist.append(row[1:])
            line_count += 1
        elif row[0][0] == 'D':
            Dlist.append(row[1:])
            line_count += 1
        elif row[0][0] == 'FB':
            FBdf = FBdf.append(row[1:])
            line_count += 1
        elif row[0][0] == 'L':
            Ldf = Ldf.append(row[1:])
            line_count += 1

    parts_raw.close()
    # print(Rdf.shape)
    temp = pd.DataFrame(Rlist, columns=headers)
    Rdf = pd.concat([temp, Rdf])

    temp = pd.DataFrame(Clist, columns=headers)
    Cdf = pd.concat([temp, Cdf])

    temp = pd.DataFrame(Dlist, columns=headers)
    Ddf = pd.concat([temp, Ddf])


    print(Rdf)
    print(Cdf)
    print(Ddf)
    print(FBdf)
    print(Ldf)

print('hello_world')
