from flask import Flask, request
app = Flask(__name__)
# http://127.0.0.1:5000/teste/1
@app.route('/teste/1', methods=['POST'])
def teste_json():
    objeto_json = request.get_json()
    if objeto_json is not None:
        triangulo = ''
        if 'valorX' in objeto_json:
            valorX = objeto_json['valorX']
        if 'valorY' in objeto_json:
            valorY = objeto_json['valorY']
        if 'valorZ' in objeto_json:
            valorZ = objeto_json['valorZ']
        
        x = float(valorX)
        y = float(valorY)
        z = float(valorZ)
            
        if x+y>z and x+z>y and y+z>x:
            triangulo = 'Podem ser um triangulo'
        else:
            triangulo = 'Não podem ser um triangulo'

        return '''
            ValorX: {}
            ValorY: {}
            ValorZ: {}
            Situação: {}
            '''.format(valorX, valorY,valorZ,triangulo)

if __name__ == '__main__':
    app.run(debug = True, port = 5000)