from src import create_app
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
