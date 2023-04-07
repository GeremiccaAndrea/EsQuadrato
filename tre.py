from flask import Flask, request, render_template
import math
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('tre_3.html')


@app.route('/SceltaArea_Diagonale')
def SceltaArea_Diagonale():
  lato = int(request.args.get('lato'))
  scelta = request.args.get('scelta')
  area = lato **2 
  diagonale = lato * math.sqrt(2)
  if scelta == 'Area':
    return render_template('areaQuadrato.html', lato = lato, area = area)
  else:
    return render_template('diagonaleQuadrato.html', lato = lato, diagonale = diagonale)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)