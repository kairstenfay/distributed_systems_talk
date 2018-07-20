from hierachical_aggregator.job import create_job, get_job, finish_job

host = "localhost"
port = 6379

create_job("a", "root", ["b", "c"], host, port)
create_job("b", "a", ["d", "e"], host, port)
create_job("c", "a", [], host, port)
create_job("d", "b", [], host, port)
create_job("e", "b", [], host, port)

job = get_job(host, port)
while job is not None:
    print(job)
    finish_job(job["node_name"], job["parent_node_name"], host, port)
    job = get_job(host, port)
