from src import create_app
from config import ProductionConfig

app = create_app(ProductionConfig)

if __name__ == '__main__':
    app.run(port = 5000, debug=True, host='0.0.0.0')
