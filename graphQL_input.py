import extract_ModularControl
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
import urllib3
import time

""" The valuable data to run into Octopart are the part number and the manufacturer.
Might want to delete the erroneous information from the dataframe extraction. 
Constant values for the limit and the start values.
start : offset in results list : 0
limit : number of results to display : 1"""

start_time = time.time()
urllib3.disable_warnings()


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

# start and limti values for query - multi_match
# Rdf["limit"] = 3
# Rdf["start"] = 0
# Rdf["reference"] = Rdf['mpn_or_sku']
# Cdf["limit"] = 3
# Cdf["start"] = 0
# Cdf["reference"] = Rdf['mpn_or_sku']
# Ddf["limit"] = 3
# Ddf["start"] = 0
# Ddf["reference"] = Rdf['mpn_or_sku']
# Ldf["limit"] = 3
# Ldf["start"] = 0
# Ldf["reference"] = Rdf['mpn_or_sku']
# FBdf["limit"] = 3
# FBdf["start"] = 0
# FBdf["reference"] = Rdf['mpn_or_sku']

print(Rdf.to_json(orient="records", indent=4))
# part_queries = (Rdf.to_json(orient="records", indent=4))  # this looks like a promising format
# part_queries = part_queries.append(Cdf.to_json(orient='records', indent=4))

# query_variables = query_variables.append(Ddf.to_json(orient='records', indent=4))
# query_variables = query_variables.append(Ldf.to_json(orient='records', indent=4))

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

# print(Rdf.to_json(orient="split", indent=4))
# print(Rdf.to_json(orient="index", indent=4))
# print(Rdf.to_json(orient="columns", indent=4))
