from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

print("Enter your recipe search: ")
input = input()

es.indices.refresh(index="recipes")

res = es.search(index="recipes", query={ #perform sample search
    "multi_match": {
      "query": input,
      "fields": ["title"]
    }
  })
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(title)s: %(instructions)s" % hit["_source"])