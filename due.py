from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('due_2.html')

@app.route('/AreaQuadrato', methods = ["GET"])
def AreaQuadrato():
    lato = int(request.args.get('lato'))
    area = lato **2
    if lato == 0:
        return('Errore')
    else:
        return render_template('areaQuadrato.html', lato = lato, Area = area)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)