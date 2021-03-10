from graphQL_input import *
import csv
from argparse import ArgumentParser
import os


parser = ArgumentParser(description="This script should update schematics with part attributes")
parser.add_argument('-f', '--filename', default='', type=str, help='name of main schematic file')
args = parser.parse_args()
args.filename = "C:\\Users\\JerryGoss\\Documents\\ModularControlPCBA\\ModularControlPCBA.sch"
print('Extracting parts from {}'.format(args.filename))
os.system("kifield -nb -r -w -x {} -i temp.csv".format(args.filename))

with open('temp.csv', 'r') as tempfile:
    csv_reader = csv.reader(tempfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
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


# schem_data = pd.read_csv('temp.csv')
Rschemdata.fillna('', inplace=True)
# print((list(octopartdata.values())[0]['attribute.name']))
recov_attr = list(octopartdata.values())[1]['attribute.name']
# print('Recovered Attributes: \n', recov_attr, sep='')
for k in recov_attr:
    Rschemdata[k] = None
# print(Rschemdata)
for i in Rschemdata.index:
    if Rschemdata.iloc[i].PN in list(octopartdata.keys()):
        # print(list(octopartdata.keys()))
        Rschemdata[recov_attr] = list(octopartdata.values())[0]['display_value']
        print(Rschemdata)
        pass


Cschemdata.fillna('', inplace=True)
# print((list(octopartdata.values())[0]['attribute.name']))
recov_attr = list(octopartdata.values())[0]['attribute.name']
# print('Recovered Attributes: \n', recov_attr, sep='')
for k in recov_attr:
    Cschemdata[k] = None
# print(Cschemdata)
for i in Cschemdata.index:
    if Cschemdata.iloc[i].PN in list(octopartdata.keys()):
        # print(list(octopartdata.keys()))
        Cschemdata[recov_attr] = list(octopartdata.values())[0]['display_value']
        # print(Cschemdata)
        pass
# for i in Rschemdata.index:
#     Manf = Rschemdata.iloc[i].Manufacturer
#     PN = Rschemdata.iloc[i].PN
#     # print(Manf, PN, end=',,')
#     pass
