# Metadata-from-logs

 
Datasets:

We made the Bio2RDF SPARQL query logs available at https://download.dumontierlab.com/bio2rdf/logs/.

Wikidata logs are accessible through a public dataset from the international center for computational logic https://iccl.inf.tu-dresden.de/web/Wikidata\_SPARQL\_Logs/en. 

*Do the following steps to generate results of the paper:*

We collect SPARQL query logs of Bio2RDF based on the steps described in "dump-sparql-logs" folder in this repository.

We use python to manuplate input data: 

1. We remove queries that contain "http://nonsensical" 
2. We remove VALUES section of the queries
3. We remove spaces/new lines with a parralel programing
4. We convert dataset to .tsv.gzip

Workflow of the method is shown below:

![alt text](https://github.com/marmhm/Metadata-from-logs/workflow.png)

Implemantation of the workflow could be found in Java folder. 

