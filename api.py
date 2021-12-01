from flask import Flask, make_response
from flask_restful import Resource, Api
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

app = Flask(__name__)
api = Api(app)

data = pd.read_csv('http://dados.recife.pe.gov.br/dataset/4d3a3b39-9ea9-46ed-bf21-a2670de519c1/resource/7c613836-9edd-4c0f-bc72-495008dd29c3/download/info_unidadesensino_07102021.csv',sep=';', skipinitialspace = True)

data.set_index('cod_escola')

class Bairro(Resource):
    def __group_data__(self,dataframe, list_columns):
        grouped_data = dataframe.groupby(list_columns).agg(
            total_escolas = ('cod_escola', 'count'),
            total_turmas = ('qtd_turmas', 'sum'),
            media_alunos = ('qtd_alunos', 'mean'),
            media_prof = ('qtd_professores', 'mean')
            )
        return grouped_data
    
    def __make_plot__(self,dataframe, x_axis, y_axis,bairro):
        plt.figure()
        sns.boxplot(data=dataframe, x=x_axis, y=y_axis)
        plt.savefig(f'boxplot_biblioteca_{bairro}.png')

    def get(self, bairro):
        bairro_procurado = (data['bairro'] == bairro.upper())
        escolas_bairro = data[bairro_procurado]

        grouped_data = self.__group_data__(escolas_bairro,['bairro','tipo'])

        grouped_data.to_csv(f'relatorio_escolas_{bairro}.csv')
        grouped_data.to_json(f'relatorio_escolas_{bairro}.json')

        self.__make_plot__(escolas_bairro,'biblioteca','qtd_alunos',bairro)
        

        return make_response(escolas_bairro.to_json(orient='index',  force_ascii=False))

api.add_resource(Bairro, '/bairro/<string:bairro>')

if __name__ == '__main__':
    app.run(debug=True)