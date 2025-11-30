from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    # REPLACE [YourLastname] with your actual name
    return "Hello from fatima ECS Container."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)