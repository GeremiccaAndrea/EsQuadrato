from flask import Flask, request, render_template
import math
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('quattro_4.html')


@app.route('/SceltaArea_E_Diagonale', methods = ["GET"])
def SceltaArea_E_Diagonale():
    scelta = request.args.getlist("geometria")
    lato = float(request.get.args('lato'))
    if "Area" in scelta and "Diagonale" in scleta:
        area = lato **2
        diagonale = lato * math.sqrt(2)
        return render_template('area_e_diagonale.html', Area = area, Diagonale = diagonale)
    elif "Area" in scelta:
        area = lato **2
        return render_template('areaQuadrato.html', Area = area)
    elif "Diagonale" in scelta:
        diagonale = lato * math.sqrt(2)
        return render_template('diagonaleQuadrato.html', Diagonale = diagonale)

if __name__ == '__main__': 
  app.run(host='0.0.0.0', port=3245, debug=True)