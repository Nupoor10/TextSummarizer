from flask import Flask, render_template, request
from textsummary import final_text_summary

app = Flask(__name__)

@app.route("/")
def index() :
    return render_template('index.html')

@app.route("/summary", methods=['GET', 'POST'])
def summary() :
    if request.method == 'POST' :
        text_content = request.form['text-content']
        original_text, summary_results, count_original, count_summary = final_text_summary(text_content)

    return render_template('summary.html', original = original_text,summary = summary_results, 
                           words_original = count_original, words_summary =  count_summary)

if __name__ == "__main__" :
    app.run(debug=True)