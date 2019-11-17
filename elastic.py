from elasticsearch import Elasticsearch
es = Elasticsearch()

es.indices.create(index='test',)