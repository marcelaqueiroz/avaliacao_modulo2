from flask import Flask, make_response
from flask_restful import Resource, Api
import pandas as pd

app = Flask(__name__)
api = Api(app)

df = pd.read_csv('escolas.csv')
df.set_index('cod_escola')

class Bairro(Resource):
    def get(self, bairro):
        bairro_procurado = (df['bairro'] == bairro.upper())
        escolas_bairro = df[bairro_procurado]
        escolas_bairro.to_csv(f'escolas_{bairro}.csv')
        return make_response(escolas_bairro.to_json(orient='index',  force_ascii=False))

class Escola(Resource):
    def get(self,cod_escola):
        escola_procurada = df.loc[[cod_escola]]
        return make_response(escola_procurada.to_json(orient='index',force_ascii=False))

class Tipo(Resource):
    def get(self, tipo_cod):
        tipo_procurado = (df['tipo_cod'] == tipo_cod)
        escolas_tipo = df[tipo_procurado]
        escolas_tipo.to_csv(f'tipo_{tipo_cod}.csv')
        return make_response(escolas_tipo.to_json(orient='index',  force_ascii=False))
    
api.add_resource(Bairro, '/bairro/<string:bairro>')
api.add_resource(Escola, '/escola/<int:cod_escola>')
api.add_resource(Tipo, '/tipo/<int:tipo_cod>')

if __name__ == '__main__':
    app.run(debug=True)
