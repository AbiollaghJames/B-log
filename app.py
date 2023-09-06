from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'title': 'Introduction',
        'date': 'YY-MM-DD',
        'content': 'You have to know somebody in order to be friends with him'
    },
]

@app.route('/')
def home():
    return render_template("home.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)