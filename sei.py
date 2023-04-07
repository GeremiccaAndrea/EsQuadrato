from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('sei_6.html')

@app.route('/sceltaFigure')
def sceltaFigure():
    figure = request.args.get('figure')
    if figure == 'Cerchio':
        return render_template('cerchio.html')
    elif figure == 'Pentagono':
        return render_template('pentagono.html')
    elif figure == 'Rettangolo':
        return render_template('rettangolo.html')
    elif figure == 'Quadrato':
        return render_template('quadrato.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)