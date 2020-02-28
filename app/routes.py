from app import app, db
from helpers import results_formatter, get_regex_count
from flask import request, jsonify
# Performs a case insensitive search over article titles and bodies for the search terms provided
# Returns a json with one field, "results", which contains a list of articles
@app.route('/articles/search', methods=['GET'])
def search_articles():
    if request.method == 'GET':
        search_terms = request.args.get('searchTerms')
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
        results_dict = results_formatter(cursor)
        results_dict['results'].sort(key=lambda x: get_regex_count(x['body'], terms), reverse=True)
        results_dict['results'].sort(key=lambda x: get_regex_count(x['title'], terms), reverse=True)

        return jsonify(results_dict)

# Queries database for a random article
# Returns a json with one field, "results", which contains a list of articles (in this case of one article)

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

@app.route('/articles/all', methods=['GET'])
def all_articles():
    if request.method == 'GET':
        cursor = db.articles.find({})
        return jsonify(results_formatter(cursor))
