from flask import *
import json
import os


app = Flask(__name__)

@app.route('/', methods=['GET', "POST"])
def date():
    print(request.method)
    if request.method == 'GET':
        day = request.args.get('day')
        month = request.args.get('month')
        year = request.args.get('year')
        date = f'{day}-{month}-{year}'
        print(day, month, year)
        with open(f'{date}.json', encoding='utf8') as f:
            data = json.load(f)
        return  data
    data = request.json.get('data')
    date = request.json.get('date')
    with open(date) as f:
        dat = list(map(int, f.readline().split()))
        if dat == data:
            return jsonify({"massage": "correct answer"})
        return jsonify({"massage": "wrong answer"})


@app.route('/date', methods=['GET'])
def get_dates():
    ans = []
    for el in os.listdir():
        if '.json' in el:
            ans.append(el.split('.')[0])
    return {"massage": ans}


app.run()
