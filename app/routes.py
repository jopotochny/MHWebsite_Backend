from app import app, db
from helpers import results_formatter
from flask import request, jsonify
# Performs a case insensitive search over article titles and bodies for the search terms provided
# Returns a json with one field, "results", which contains a list of articles
@app.route('/articles/<search_terms>', methods=['GET'])
def articles(search_terms):
    if request.method == 'GET':
        terms = search_terms.strip().replace('-', " ")
        regex = ".*{}.*".format(terms)
        query = {
            "$or": [
                {
                    "title":
                        {
                            "$regex": regex,
                            "$options": "i"
                        }
                },
                {
                    "body":
                        {
                            "$regex": regex,
                            "$options": "i"
                        }
                }

            ]

        }
        cursor = db.articles.find(query)

        return jsonify(results_formatter(cursor))

# queries database for a random article and returns it
@app.route('/articles/random', methods=['GET'])
def random_article():
    if request.method == 'GET':
        query = {
            "$sample": {
                "size": 1
            }
        }
        cursor = db.articles.aggregate([query])
        return jsonify(results_formatter(cursor))