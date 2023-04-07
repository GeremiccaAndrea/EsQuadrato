from flask import Flask, request, render_template
import math
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('quattro_4.html')

@app.route('/SceltaArea_E_Diagonale')
def SceltaArea_E_Diagonale():
  lato = int(request.args.get('lato'))
  scelta = request.args.getlist('scelta')
  if scelta == ['Area' , 'Diagonale']:
    area = lato **2 
    diagonale = lato * math.sqrt(2)
    return render_template('area_e_diagonale', lato = lato, Area = area, Diagonale = diagonale)
  elif 'Diagonale' in scelta:
    diagonale = lato * math.sqrt(2)
    return render_template('diagonaleQuadrato.html', lato = lato, Diagonale = diagonale)
  elif 'Area' in scelta:
    area = lato **2 
    return render_template('areaQuadrato.html', lato = lato, Area = area)

if __name__ == '__main__': 
  app.run(host='0.0.0.0', port=3245, debug=True)