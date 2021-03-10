import extract_ModularControl
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import urllib3
import time
import json
from extract_ModularControl import pd, desired_width
from pprint import pprint

""" The valuable data to run into Octopart are the part number and the manufacturer.
Might want to delete the erroneous information from the dataframe extraction. 
Constant values for the limit and the start values.
start : offset in results list : 0
limit : number of results to display : 1"""

start_time = time.time()
urllib3.disable_warnings()

pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)
pd.set_option('display.max_colwidth', None)

def execute(query_input):
    output = client.execute(query_input)
    return output


# update to octopart api link with token
sample_transport = RequestsHTTPTransport(
    url='https://rickandmortyapi.com/graphql',
    use_json=True,
    headers={
        "Content-type": "application/json",
    },
    verify=False,
)

client = Client(
    transport=sample_transport,
    fetch_schema_from_transport=True
)

target_csvfile = 'ModularControlPCBA.csv'
Rdf, Cdf, Ddf, Ldf, FBdf = extract_ModularControl.extract_bom_data(target_csvfile)

# parts_df = pd.concat([Rdf, Cdf, Ldf, FBdf, Ddf], axis=0, ignore_index=True)
# parts_df = Rdf.append([Cdf, Ldf, Ddf, FBdf]) # append is faster in this scenario
parts_df = Rdf.append([Cdf])

print(parts_df.shape)
part_queries = parts_df.to_json(orient="records", indent=4)
# print(part_queries, "\n\npart total: {q}".format(q=parts_df.shape[0]))

# query_var = {"queries": part_queries}
query = gql(
    """
query MultiMatch2($queries: [PartMatchQuery!]!) {
  multi_match(
    queries: $queries
    country: "US"
    currency: "USD"
    distributorapi_timeout: "3s"
  ) 
  {
    reference
    hits
    parts {
      id #octopart id
      name
      mpn
      specs {
        attribute {
          # id
          name
        }
        display_value
      }
      slug
    }
  }
} 
        
        """)

raw_output = """
{
  "data": {
    "multi_match": [
      {
        "reference": "GRM21BC71C106KE11L",
        "hits": 1,
        "parts": [
          {
            "id": "46693500",
            "name": "Murata GRM21BC71C106KE11L",
            "specs": [
              {
                "attribute": {
                  "name": "Capacitance"
                },
                "display_value": "10 µF"
              },
              {
                "attribute": {
                  "name": "Case/Package"
                },
                "display_value": "0805"
              },
              {
                "attribute": {
                  "name": "Case Code (Imperial)"
                },
                "display_value": "0805"
              },
              {
                "attribute": {
                  "name": "Case Code (Metric)"
                },
                "display_value": "2012"
              },
              {
                "attribute": {
                  "name": "Composition"
                },
                "display_value": "Ceramic"
              },
              {
                "attribute": {
                  "name": "Dielectric"
                },
                "display_value": "X7S"
              },
              {
                "attribute": {
                  "name": "Height"
                },
                "display_value": "1.25 mm"
              },
              {
                "attribute": {
                  "name": "Length"
                },
                "display_value": "2 mm"
              },
              {
                "attribute": {
                  "name": "Lifecycle Status"
                },
                "display_value": "Production (Last Updated: 6 days ago)"
              },
              {
                "attribute": {
                  "name": "Manufacturer Lifecycle Status"
                },
                "display_value": "IN PRODUCTION (Last Updated: 6 days ago)"
              },
              {
                "attribute": {
                  "name": "Material"
                },
                "display_value": "Ceramic"
              },
              {
                "attribute": {
                  "name": "Max Operating Temperature"
                },
                "display_value": "125 °C"
              },
              {
                "attribute": {
                  "name": "Min Operating Temperature"
                },
                "display_value": "-55 °C"
              },
              {
                "attribute": {
                  "name": "Mount"
                },
                "display_value": "Surface Mount"
              },
              {
                "attribute": {
                  "name": "Packaging"
                },
                "display_value": "Tape & Reel (TR)"
              },
              {
                "attribute": {
                  "name": "RoHS"
                },
                "display_value": "Compliant"
              },
              {
                "attribute": {
                  "name": "Schedule B"
                },
                "display_value": "8532240020"
              },
              {
                "attribute": {
                  "name": "Termination"
                },
                "display_value": "SMD/SMT"
              },
              {
                "attribute": {
                  "name": "Thickness"
                },
                "display_value": "1.25 mm"
              },
              {
                "attribute": {
                  "name": "Tolerance"
                },
                "display_value": "10 %"
              },
              {
                "attribute": {
                  "name": "Voltage Rating"
                },
                "display_value": "16 V"
              },
              {
                "attribute": {
                  "name": "Voltage Rating (DC)"
                },
                "display_value": "16 V"
              },
              {
                "attribute": {
                  "name": "Weight"
                },
                "display_value": "9.49709 mg"
              },
              {
                "attribute": {
                  "name": "Width"
                },
                "display_value": "1.25 mm"
              }
            ],
            "slug": "/grm21bc71c106ke11l-murata-46693500"
          }
        ]
      },
      {
        "reference": "CRCW040210K0FKED",
        "hits": 1,
        "parts": [
          {
            "id": "40298764",
            "name": "Vishay CRCW040210K0FKED",
            "specs": [
              {
                "attribute": {
                  "name": "Case/Package"
                },
                "display_value": "0402"
              },
              {
                "attribute": {
                  "name": "Case Code (Metric)"
                },
                "display_value": "0402"
              },
              {
                "attribute": {
                  "name": "Composition"
                },
                "display_value": "Thick Film"
              },
              {
                "attribute": {
                  "name": "Height"
                },
                "display_value": "400 µm"
              },
              {
                "attribute": {
                  "name": "Lead Free"
                },
                "display_value": "Lead Free"
              },
              {
                "attribute": {
                  "name": "Max Operating Temperature"
                },
                "display_value": "155 °C"
              },
              {
                "attribute": {
                  "name": "Min Operating Temperature"
                },
                "display_value": "-55 °C"
              },
              {
                "attribute": {
                  "name": "Number of Pins"
                },
                "display_value": "2"
              },
              {
                "attribute": {
                  "name": "Packaging"
                },
                "display_value": "Cut Tape"
              },
              {
                "attribute": {
                  "name": "Power Rating"
                },
                "display_value": "63 mW"
              },
              {
                "attribute": {
                  "name": "Resistance"
                },
                "display_value": "10 kΩ"
              },
              {
                "attribute": {
                  "name": "RoHS"
                },
                "display_value": "Compliant"
              },
              {
                "attribute": {
                  "name": "Schedule B"
                },
                "display_value": "8533210045"
              },
              {
                "attribute": {
                  "name": "Temperature Coefficient"
                },
                "display_value": "100 ppm/°C"
              },
              {
                "attribute": {
                  "name": "Tolerance"
                },
                "display_value": "1 %"
              },
              {
                "attribute": {
                  "name": "Voltage Rating"
                },
                "display_value": "50 V"
              },
              {
                "attribute": {
                  "name": "Voltage Rating (DC)"
                },
                "display_value": "50 V"
              }
            ],
            "slug": "/crcw040210k0fked-vishay-40298764"
          }
        ]
      }
    ]
  }
}"""
graphql_output_sample = json.loads(raw_output)
desired_attributes = ['Voltage Rating', 'Case/Package', 'Capacitance', 'Dielectric',
                      'Tolerance', 'Power Rating', 'Resistance']
octopartdata = dict()
partlist = graphql_output_sample['data']['multi_match']
# print(partlist[0]['reference'])
for item in range(len(partlist)):
    ref_mpn = partlist[item]['reference']
    octopartdata[ref_mpn] = partlist[item]['parts'][0]['specs']
    df_json = pd.json_normalize(octopartdata[ref_mpn])
    # print(df_json.shape, type(df_json), df_json)
    df_json = df_json[df_json['attribute.name'].isin(desired_attributes)].reset_index(drop=True)
    octopartdata[ref_mpn] = df_json

pprint(octopartdata)
print("time elapsed: {:.4f}s".format(time.time() - start_time))
