from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

from scrapy import Spider

app = Flask(__name__, static_url_path='')
CORS(app)

@app.route('/api/v1/datasource/', methods=['GET', 'POST'])
def datasource():
    if request.method == 'POST':
        uid = request.form.get('uid')
        print(uid)
        if uid:
            url = f'http://space.bilibili.com/ajax/channel/getChannel?mid={uid}&guest=1'
            spider = Spider(url)
            res = spider.getContents()
            return res
        else:
            return "No UID provided"
    return "Invalid request method"

if __name__ == '__main__':
    app.run(port=5050, host="0.0.0.0", debug=True)
