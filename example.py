from hierachical_aggregator.job import create_job, get_job, finish_job

host = "localhost"
port = 6379

create_job("a", "root", ["b", "c"], host, port)
create_job("b", "a", ["d", "e"], host, port)
create_job("c", "a", [], host, port)
create_job("d", "b", [], host, port)
create_job("e", "b", [], host, port)


def data_for_leaf_node(node_name):
    return "y"


def leaf_node_func(node_data):
    if node_data == "y":
        return "yes"
    else:
        return "no"


def branch_aggregation_func(children_data):
    return "\n".join(children_data)


print("----------------------------")

job = get_job(host, port)
while job is not None:
    print("This job is called " + str(job))
    # Do something with job -- here we'll only have a leaf node or a branch with children already done

    finish_job(job["node_name"], job["parent_node_name"], host, port)
    job = get_job(host, port)

