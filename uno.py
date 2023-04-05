from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('uno_1.html')

@app.route('/AreaQuadrato')
def AreaQuadrato():
    lato = int(request.args.get('lato'))
    area = lato * lato
    return render_template('areaQuadrato.html', lato = lato, area = area)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)