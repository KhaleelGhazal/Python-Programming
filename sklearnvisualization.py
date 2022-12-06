import pandas as kung_fu_panda
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
file = kung_fu_panda.read_csv('DATA.csv')

inputs = file.drop(columns =['Genre']) 
output = file['Genre']

model = DecisionTreeClassifier()
model.fit(inputs,output)
tree.export_graphviz(model, 
                     out_file = 'Genre_recommender.dot',
                     feature_names = ['age', 'gender'],
                     class_names = sorted(output.unique()),
                    filled = True,
                    rounded = True,
                    label = 'all')
# prediction = model.predict([[14,1]])
# print(prediction)
