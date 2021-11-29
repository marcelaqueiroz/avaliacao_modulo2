from flask import Flask, make_response
from flask_restful import Resource, Api
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

app = Flask(__name__)
api = Api(app)

df = pd.read_csv('escolas.csv')
df.set_index('cod_escola')

class Bairro(Resource):
    def group_data(self,dataframe, list_columns):
      grouped_data = dataframe.groupby(list_columns).agg(
          total_escolas = ('cod_escola', 'count'),
          total_turmas = ('qtd_turmas', 'sum'),
          media_alunos = ('qtd_alunos', 'mean'),
          media_prof = ('qtd_professores', 'mean')
          )
      return grouped_data
    
    def make_plot(self,dataframe, x_axis, y_axis):
      sns_plot=sns.boxplot(data=dataframe, x=x_axis, y=y_axis)
      return sns_plot

    def get(self, bairro):
        bairro_procurado = (df['bairro'] == bairro.upper())
        escolas_bairro = df[bairro_procurado]

        grouped_data = self.group_data(escolas_bairro,['bairro','tipo'])

        grouped_data.to_csv(f'relatorio_escolas_{bairro}.csv')
        grouped_data.to_json(f'relatorio_escolas_{bairro}.json')

        sns_plot =self. make_plot(escolas_bairro,'biblioteca','qtd_alunos')
        plt.savefig(f'boxplot_biblioteca_{bairro}.png')

        return make_response(escolas_bairro.to_json(orient='index',  force_ascii=False))

api.add_resource(Bairro, '/bairro/<string:bairro>')

if __name__ == '__main__':
    app.run(debug=True)