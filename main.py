from flask import Flask
from flask import request
# from flask_sqlalchemy import SQLAlchemy

from database import Database


app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://test.db'
#
# db = SQLAlchemy(app)
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
#     def __repr__(self):
#         return '<User %r>' % self.username


@app.route('/')
def hello():
    return """
    <html>
        <head>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
        </head>
        <body>
            <s>Hello World!</s>
            <div id="chat"></div>
            <form method="post" autocomplete="off" action="">
                <input type="text"  id="string"/>
                <input type="button" id="send" value="Send"/>
            </form>
        </body>
        <script>
            $("#send").click(function() {
                var string = $("#string").val();
                $("#chat").append("<p>1: " + string + "</p>");
                $.get("/chat", { string: string }, function( data ) {
                    $("#chat").append("<p>2: " + data + "</p>");
                });
            });
        </script>
    </html>
"""


@app.route('/chat')
def chat():
    string = request.args.get('string')
    db = Database()
    db.add_message(string)
    return "Hello " + string + "!"


if __name__ == '__main__':
    app.run()
