import pandas as pd
from sklearn.tree import DecisionTreeClassifier

music_data = pd.read_csv('music.csv')
x = music_data.drop(columns=['genre'])
y = music_data['genre']


model = DecisionTreeClassifier()
model.fit(x, y)
print(music_data)
# predications = model.predict([ [21, 1], [22, 0]])
# print(predications)