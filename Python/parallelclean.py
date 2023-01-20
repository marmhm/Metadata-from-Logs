from pandarallel import pandarallel
import pandas as pd


def cleanspace(query):
    return query.replace("\n", " ").replace("\r", " ")


pandarallel.initialize(progress_bar=True, use_memory_fs=False)

# process_file = r'bio2rdf-processed-sample.csv'
process_file =  r'values-nonsen-all-bio.csv'

df = pd.read_csv(process_file)

df["query"] = df["query"].parallel_apply(lambda row: cleanspace(row))

df.to_csv('results/values-nonsen-all-bio.tsv', sep='\t', encoding='utf-8', index=False)
