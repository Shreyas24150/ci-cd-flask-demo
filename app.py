from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "🚀 CI/CD works Shreyas bhai!"

if __name__ == "__main__":
    app.run()
