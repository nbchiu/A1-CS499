from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "TESTING FLASK IN EC2"

if __name__ == "__main__":
    app.run()
