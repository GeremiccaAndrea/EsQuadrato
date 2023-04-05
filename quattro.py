from flask import Flask, request, render_template
import math
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('quattro_4.html')

@app.route('/AreaQuadrato')
def AreaQuadrato():
    lato = int(request.args.get('lato'))
    area = lato **2 
    if lato == 0:
        return('Errore')
    else:
        return render_template('areaQuadrato.html', lato = lato, area = area)


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

@app.route('/SceltaArea_E_Diagonale')
def SceltaArea_E_Diagonale():
  lato = int(request.args.get('lato'))
  scelta = request.args.getlist('scelta')
  area = lato **2 
  diagonale = lato * math.sqrt(2)
  if area in scelta and diagonale in scelta:
     area = lato **2 
     diagonale = lato * math.sqrt(2)
     return render_template('area_e_diagonale', lato = lato, area = area, diagonale = diagonale)
  elif diagonale in scelta:
    diagonale = lato * math.sqrt(2)
    return render_template('diagonaleQuadrato.html', lato = lato, diagonale = diagonale)
  else:
    area = lato **2 
    return render_template('areaQuadrato.html', lato = lato, area = area)

if __name__ == '__main__': 
  app.run(host='0.0.0.0', port=3245, debug=True)