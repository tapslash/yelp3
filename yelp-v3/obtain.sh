#!/bin/bash
#
# Obtain an access token from yelp's api.
# https://www.yelp.com/developers/documentation/v3/get_started
#

CLIENT_ID="YOUR-CLIENT-ID"
CLIENT_SECRET="YOUR-CLIENT-SECRET"

curl -i -v "https://api.yelp.com/oauth2/token" \
--form "grant_type=client_credentials" \
--form "client_id=$CLIENT_ID" \
--form "client_secret=$CLIENT_SECRET"

