from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


@app.route('/getGrid', methods=['GET'])
def getGrid():
  print(request)
  width = {'years':10, 'months':20, 'days':100}
  age = request.args.get('age', type=int)
  years = request.args.get('years', type=int)
  print(age, years)
  return render_template("grid.html", age=age, years=years, width=width['years'])


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
