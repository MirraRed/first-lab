from flask import Flask

app = Flask(__name__)

# http://localhost:5000/api/v1/hello-world-3

@app.route('/api/v1/hello-world-<int:variant>')
def hello_world(variant):
    message = f'Hello World {variant}'
    return message, 200

if __name__ == '__main__':
    app.run(debug=True)
