#http://docs.python-requests.org/en/latest/user/quickstart/

#http://docs.python-requests.org/en/latest/user/quickstart/#more-complicated-post-requests

import requests


class restRequest(object):
    """description of class"""
    url = 'http://ES_search_demo.com/document/record/_search?pretty=true'
    data = '{
      "query": {
        "bool": {
          "must": [
            {
              "text": {
                "record.document": "SOME_JOURNAL"
              }
            },
            {
              "text": {
                "record.articleTitle": "farmers"
              }
            }
          ],
          "must_not": [],
          "should": []
        }
      },
      "from": 0,
      "size": 50,
      "sort": [],
      "facets": {}
    }'
    response = requests.post(url, data=data)

