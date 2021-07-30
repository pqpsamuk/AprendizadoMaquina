!pip install -U scikit-learn
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
url = 'http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data' 

nome_var = ['comprimento_sepala', 'largura_sepala', 'comprimento_petala', 'largura_petala', 'especie']
iris = pd.read_csv(url, header=None, names=nome_var)

amostraVersicolor = (iris[iris['especie']=='Iris-versicolor'].sample(n=10, random_state=1))
amostraSetosa = (iris[iris['especie']=='Iris-setosa'].sample(n=10, random_state=1))
amostraVirginica = (iris[iris['especie']=='Iris-virginica'].sample(n=10, random_state=1))

conjuntoteste = pd.concat([amostraVersicolor,amostraSetosa,amostraVirginica])
conjuntotreinamento = iris.drop(conjuntoteste.index)
classesVerdadeiras = conjuntoteste['especie'].tolist()

arvore = DecisionTreeClassifier()
arvore = arvore.fit(conjuntotreinamento.iloc[:,0:4],conjuntotreinamento['especie'])
respostaArvore = arvore.predict(conjuntoteste.iloc[:,0:4]);

errosArvore = 0

for i in range(len(conjuntoteste.index)):
  if classesVerdadeiras[i]!=respostaArvore[i]:
    errosArvore += 1

taxaErrosArvore = errosArvore/len(conjuntoteste.index)

print('Taxa de erro: ' + '%.2f' %(taxaErrosArvore*100)+'% ou Acurácia de: ' + '%.2f' %((1-taxaErrosArvore)*100)+'%')