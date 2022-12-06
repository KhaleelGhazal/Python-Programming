# CREATING PERSISTENT MODELS
# MODEL PERSISTENCE
import pandas as kung_fu_panda
from sklearn.tree import DecisionTreeClassifier
#import joblib
file = kung_fu_panda.read_csv('DATA.csv')

inputs = file.drop(columns =['Genre']) 
output = file['Genre']

model = DecisionTreeClassifier()
model.fit(inputs,output)
#joblib.dump(model, 'Genre_recommender.joblib')
result = model.predict([[65,1]])
print(result)
