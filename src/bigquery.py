from google.cloud import bigquery

def dry_run(query):
        mbs = 10**6
        dry_config = bigquery.QueryJobConfig(dry_run=True)
        dry_job = client.query(query, job_config=dry_config)
        job_mbs = dry_job.total_bytes_processed/mbs
        return job_mbs

def juicy_run(query, thresh=10**9):
        mbs = 10**6
        juicy_config = bigquery.QueryJobConfig(maximum_bytes_billed=thresh)
        juicy_job = client.query(query, job_config=juicy_config)
        df = juicy_job.to_dataframe()
        return df

if __name__ == "__main__":
    client = bigquery.Client()
    dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")
    dataset = client.get_dataset(dataset_ref)
    table_ref = dataset_ref.table("comments")
    table = client.get_table(table_ref)
    client.list_rows(table, max_results=5).to_dataframe()
