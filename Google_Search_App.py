from flask import Flask, render_template, request
from googlesearch import search

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def main():
    return render_template('search.html')

@app.route('/search_result', methods = ['GET','POST'])
def searchResult():
    searchResults = []
    if request.method == 'POST':
        query = request.form['keyword']
        numberOfResults = request.form['number_of_results']
        finalResult = request.form['final_result']
        
        if query == '' or numberOfResults == '' or finalResult == '':
            return 'Do not leave the fields blank'
        if numberOfResults.isalpha() or numberOfResults.isalpha():
            return "Only Number."

        for results in search(query, tld='co.in', num=int(numberOfResults), stop=int(finalResult), pause=2):
            searchResults.append(results)

        return render_template('search_result.html', search_results = searchResults, key_word = query)
    
    else:
        return 'For post requests only.'

if __name__ == '__main__':
    app.run(debug=True, port=5000)

