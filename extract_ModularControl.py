import csv
import pandas as pd
import requests
desired_width = 320

pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', None)

headers = {"Authorization" : "Bearer YOUR API KEY"}

def run_query(query):  # S simple function to use requests.post to make the API call. Note the json= section.
    request = requests.post(a0445964-9763-4f8f-b9b2-11b51902237e, json={'query': query}, headers=headers)
    if request.status_code == 200:
        print("success")
        return request.json()
    else:
        raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

    # The GraphQL query (with a few additional bits included) itself defined as a multi-line string.

# important values: R, C, D, FB, L
def extract_bom_data(csvfile):
    with open(csvfile, 'r') as parts_raw:
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
                FBlist = []
                Ldf = Rdf.copy(deep=True)  # inductors
                Llist = []
                line_count += 1

            elif row[0][0] == 'R':
                Rlist.append(row[1:])
            elif row[0][0] == 'C':
                Clist.append(row[1:])
            elif row[0][0] == 'D':
                Dlist.append(row[1:])
            elif row[0][0:2] == 'FB':
                FBlist.append(row[1:])
            elif row[0][0] == 'L':
                Llist.append(row[1:])

            line_count += 1

        parts_raw.close()
    # print(Rdf.shape)
    bomdata = 'ModularControlPCBA'
    extract_bom_data(bomdata)
    temp = pd.DataFrame(Rlist, columns=headers)
    Rdf = pd.concat([temp, Rdf])

    temp = pd.DataFrame(Clist, columns=headers)
    Cdf = pd.concat([temp, Cdf])

    temp = pd.DataFrame(Dlist, columns=headers)
    Ddf = pd.concat([temp, Ddf])

    temp = pd.DataFrame(FBlist, columns=headers)
    FBdf = pd.concat([temp, FBdf])

    temp = pd.DataFrame(Llist, columns=headers)
    Ldf = pd.concat([temp, Ldf])
    del temp

    print('R\n', Rdf)
    print('C\n', Cdf)
    print('D\n', Ddf)
    print('FB\n', FBdf)
    print('L\n', Ldf)


print('Hello Octopart!')
