from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'ⁿᵒᵒᵇシ︎ՏᗩᐯᐯY ☠'


if __name__ == "__main__":
    app.run()
