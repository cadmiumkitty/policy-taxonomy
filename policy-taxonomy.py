import pandas as pd
import rdfpandas
from rdflib import Graph, Namespace
from rdflib.namespace import NamespaceManager, SKOS, DCTERMS

df = pd.read_csv('policy-taxonomy.csv', index_col = '@id', keep_default_na = True)
namespace_manager = NamespaceManager(Graph())
namespace_manager.bind('skos', SKOS, override = True)
namespace_manager.bind('dcterms', DCTERMS, override = True)
namespace_manager.bind('policy', Namespace('https://dalstonsemantics.com/ns/org/isbn-international/978-0124158290/'), override = True)
namespace_manager.bind('pav', Namespace('http://purl.org/pav/'), override = True)
g = rdfpandas.to_graph(df, namespace_manager)
ttl = g.serialize(format = 'turtle')
with open('policy-taxonomy.ttl', 'w') as file:
   file.write(ttl)
