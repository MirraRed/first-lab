from waitress import serve
from main import app  # Переконайтеся, що шлях до вашого файлу main.py вказаний вірно

# http://localhost:8080/api/v1/hello-world-3

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)
