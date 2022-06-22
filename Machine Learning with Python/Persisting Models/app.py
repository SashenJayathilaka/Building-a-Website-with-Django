from pyexpat import model
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib

# music_data = pd.read_csv('music.csv')
# x = music_data.drop(columns=['genre'])
# y = music_data['genre']

# model = DecisionTreeClassifier()
# model.fit(x, y)

model = joblib.load('music-recommender.joblib')
predications = model.predict([[21, 1]])
print(predications)