from flask import Flask, jsonify
import sys
sys.path.append('./translate')

from translate_number import TranslateNumber, TranslateNumberException

app = Flask(__name__)

@app.route('/')
def index():
    with open("web/index.html", "r", encoding='utf-8') as f:
        page = f.read()
        return page

@app.route('/<number>', methods=['GET'])
def translate(number):

    try:
        t = TranslateNumber(number)
        resp = {'extenso': t.translate()}
        return jsonify(resp)

    except TranslateNumberException as e:
        resp = {'error': e.message}
        return jsonify(resp)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

