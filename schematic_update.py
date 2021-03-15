from graphql_query import *
import csv
from argparse import ArgumentParser
import os

"""
This is the main file, run this to execute the program. In order for Kifield to work, 
this file as well as the csv partlist 'ModularControlPCBA.csv', and the other two support files
'graphql_query.py' and 'extract_csv.py' will need to be in the KiCad project directory.
"""


parser = ArgumentParser(description="This script should update schematics with part attributes")
parser.add_argument('-f', '--filename', default='', type=str, help='name of main schematic file')
args = parser.parse_args()
args.filename = "ModularControlPCBA.sch"
print('Extracting parts from {}'.format(args.filename))
os.system("kifield -nb -r -w -x {} -i temp.csv".format(args.filename))

with open('ModularControlPCBA.csv', 'r') as tempfile:
    csv_reader = csv.reader(tempfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        row = [k.strip() for k in row]
        # print(row)
        if line_count == 0:
            line_count += 1
            colnames = row
            Rschemdata = pd.DataFrame(columns=colnames)
            Cschemdata = pd.DataFrame(columns=colnames)
        elif row[0][0] == 'R':
            Rschemdata.loc[len(Rschemdata)] = row
        elif row[0][0] == 'C':
            Cschemdata.loc[len(Cschemdata)] = row
    tempfile.close()

R_recov_attr = None
C_recov_attr = None
while (R_recov_attr is None) or (C_recov_attr is None):
    for key in octopartdata.keys():
        key_attr_list = list(octopartdata[key]['attribute.name'])
        if 'Resistance' in key_attr_list and R_recov_attr is None:
            R_recov_attr = key_attr_list
        elif 'Capacitance' in key_attr_list and C_recov_attr is None:
            C_recov_attr = key_attr_list

del key_attr_list

print("\n\n\n\n", "STEP 1 - LISTED ATTRIBUTES TO ADD", "\n\n\n\n\n")
print('RESISTORS', R_recov_attr, sep='\n')
print('CAPACITORS', C_recov_attr)

Rschemdata.fillna('', inplace=True)
R_recov_attr = list(octopartdata.values())[1]['attribute.name']
for k in R_recov_attr:
    Rschemdata[k] = None
for i in Rschemdata.index:
    if Rschemdata.iloc[i].PN in list(octopartdata.keys()):
        Rschemdata.loc[i][R_recov_attr] = list(octopartdata[Rschemdata.iloc[i].PN]['display_value'])
        # print(Rschemdata[recov_attr])
print(Rschemdata.head())
Rschemdata.to_csv('temp2.csv', index=False)
os.system("kifield -r -nb -w -x temp2.csv -i {}".format(args.filename))
# pprint(octopartdata.keys())

Cschemdata.fillna('', inplace=True)
C_recov_attr = list(octopartdata.values())[0]['attribute.name']
for k in C_recov_attr:
    Cschemdata[k] = None
for i in Cschemdata.index:
    if Cschemdata.iloc[i].PN in list(octopartdata.keys()):
        Cschemdata.loc[i][C_recov_attr] = list(octopartdata[Cschemdata.iloc[i].PN]['display_value'])
        # print(Cschemdata[recov_attr])
print('\n', Cschemdata.head(), '\n')
Cschemdata.to_csv('temp3.csv', index=False)
os.system("kifield -r -nb -w -x temp3.csv -i {}".format(args.filename))
print('Cleaning up temporary files')
os.system('del temp.csv temp2.csv temp3.csv')

# # for i in Rschemdata.index:
# #     Manf = Rschemdata.iloc[i].Manufacturer
# #     PN = Rschemdata.iloc[i].PN
# #     # print(Manf, PN, end=',,')
# #     pass
