import tensorflow as tf
import numpy as np
import pandas as pd
import requests

from sklearn.preprocessing import LabelEncoder
from Weather import weather
from flask import Flask, request

'''
#Used to download the model if needed
response = requests.get("https://storage.googleapis.com/nanamyuk-bucket/model.h5")
open("model.h5", "wb").write(response.content)
'''

dataset_path = 'Dataset/dataset.csv'
df = pd.read_csv(dataset_path)
y = df.iloc[:,5].values
encoder = LabelEncoder()
encoder.fit_transform(y)

model_path = 'Machine Learning Model/model.h5'
reconstructed_model = tf.keras.models.load_model(model_path)

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    args = request.args
    city = args.get('city')
    soil = int(args.get('soil'))
    light = int(args.get('light'))
    weathers = weather(city)
    
    if weathers is False:
        return {"response": 404,
                "message": "Nama kota salah atau tidak terdaftar"}
    
    else:
        temp, humidity, rainfall = weathers
        input = reconstructed_model.predict([[temp, soil, light, humidity, rainfall]])
        predicted = np.argsort(input, axis=1)[:1]
        dicts = {"response": 200}
        for top_5 in predicted[:1,-5:]:
            top_5 = encoder.inverse_transform(top_5)
            i = 1
            for name in top_5[::-1]:
                dicts[str(i)] = name
                i += 1
                
        return dicts

if __name__ == "__main__":
  app.run()
