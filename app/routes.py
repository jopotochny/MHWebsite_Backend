from app import app, db
@app.route('/articles/search/<search_terms>')
def articles_search(search_terms):
    terms = search_terms.replace('-', " ")
    query = {"title": {"$regex": ".*{}.*".format(terms)}}
    article = db.articles.find_one(query)
    return article["body"]
