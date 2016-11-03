import unittest
import argparse
from yelp3.client import Client

class TestYelp(unittest.TestCase):

    client = None

    def runTest(self):
        self.test_business_search()
        self.test_phone_search()
        self.test_transaction_search()
        self.test_business()
        self.test_business_search()
        self.test_review()
        self.test_autocomplete()

    def test_business_search(self):
        resp = self.client.business_search(location="New York")
        self.assertTrue(resp['total'] > 0)

    def test_phone_search(self):
        resp = self.client.phone_search(phone = "+12123661182")
        self.assertTrue(resp['total'] > 0)

    def test_transaction_search(self):
        resp = self.client.transaction_search("delivery", location="New York")
        self.assertTrue(resp['total'] > 0)

    def test_business(self):
        businesses = self.client.business_search(location="New York")
        business_id = businesses['businesses'][0]['id']

        resp = self.client.business(business_id)
        self.assertTrue(resp['id'] == business_id)

    def test_review(self):
        businesses = self.client.business_search(location="New York")
        business_id = businesses['businesses'][0]['id']

        resp = self.client.review(business_id)
        self.assertTrue(resp['total'] >= 0)

    def test_autocomplete(self):

        resp = self.client.autocomplete(
            text = "pizz",
            longitude = "40.721769",
            latitude = "-73.993114"
        )

        self.assertTrue(len(resp['businesses']) >= 0)

if __name__ == '__main__':

    parser = argparse.ArgumentParser("test.py")

    parser.add_argument(
        "yelp_token",
        type = str,
        help = "Yelp API access token."

    )

    args = parser.parse_args()

    yelp_token = args.yelp_token

    client = Client(yelp_token, debug=True)

    TestYelp.client = client
    
    t = TestYelp()

    suite = unittest.TestSuite()
    suite.addTest(t)
    unittest.TextTestRunner(verbosity=2).run(suite)

