from src import create_app
from config import ProductionConfig

app = create_app(ProductionConfig)

if __name__ == '__main__':
    app.run(debug=ProductionConfig.DEBUG, host='0.0.0.0')
