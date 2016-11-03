# yelp3-python

WIP Python implementation of [Yelp's V3 Fusion API](https://www.yelp.com/developers/documentation/v3/).

`git clone "https://github.com/af-inet/yelp3-python"`

## running the example

1. Replace `YOUR-ACCESS-TOKEN` in `example.py` with your access token.

2. run `python example.py`

```
from yelp3.client import Client

YELP_ACCESS_TOKEN = "YOUR-ACCESS-TOKEN"

client = Client(YELP_ACCESS_TOKEN)

resp = client.business_search(location="New York")

print(resp)

```

## running the tests

`python test.py YOUR-ACCESS-TOKEN`

## notes

Getting a v3 access token from yelp:

- https://www.yelp.com/developers/documentation/v3/get_started

Don't forget to check out other yelp v2 api's:

- https://github.com/Yelp/yelp-python

- https://github.com/gfairchild/yelpapi

- https://github.com/adamhadani/python-yelp

- https://github.com/mathisonian/python-yelp-v2
