
# Helper function for converting a MongoDB document's unique id to a string
def convert_id(document):
    document['_id'] = str(document['_id'])
    return document


def results_formatter(cursor):
    results = []
    for document in cursor:
        results.append(convert_id(document))
    print(results)
    return {
        "results": results
    }