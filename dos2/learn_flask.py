''' Experimenting with flash to create a website '''


from flask import Flask, render_template
import data



app = Flask(__name__)




@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/articles")
def article():
    return render_template("articles.html", articles = data.articles())

@app.route("/articles/<string:number>")
def articles(number):
    return render_template('articles.html', id=number)

if __name__ == "__main__":
    app.run(debug=True)

