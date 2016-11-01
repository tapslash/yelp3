from yelp3.client import Client

YELP_ACCESS_TOKEN = "YOUR-ACCESS-TOKEN"

client = Client(YELP_ACCESS_TOKEN)

resp = client.business_search(location="New York")

print(resp)

