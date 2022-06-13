# NanamYuk-ML
![Banner](https://raw.githubusercontent.com/NanamYuk/NanamYuk-ML/main/images/banner.png)

ML Part of Product Based Bangkit Capstone Project Team C22-PS316

## Machine Learning Team
|  Name | Bangkit ID | Contacts |
| ------------ | ------------ | ------------ |
| Muhammad Syah Zichrullah Habibie | M2322F2811 | [Github](https://github.com/MSZHabibie)  |
| Naufaldi Hafidhigbal | M2224W2072 | [Github](https://github.com/GajAhmadaaa) |

## What we do?
We are making a crop recommendation system for recommending the top 5 crops to be grown based on the users city and environment.

## Built with
- [Python](https://www.python.org/ "Python")
- [TensorFlow](https://www.tensorflow.org/ "TensorFlow")
- [Flask](https://flask.palletsprojects.com/en/2.1.x/ "Flask")
- [OpenWeatherMap API](https://openweathermap.org/ "OpenWeatherMap API")
- [Google Cloud Run](https://cloud.google.com/run)
- [Google Colab](https://colab.research.google.com/ "Google Colab")

## Flowchart
![Flowchart](https://raw.githubusercontent.com/GajAhmadaaa/NanamYuk-ML/main/images/NanamYuk!-ML_Flowchart.png)

## API Endpoint
[Click here](https://nanamyuk-g5ck3ypmca-as.a.run.app/predict?soil=1&light=1&city=jakarta) ( Deployed using [Google Cloud Run](https://cloud.google.com/run) )

## Endpoint
| Endpoint | Method | Return |
| :------------: |  :------------: |  :------------: |
| /predict | GET | JSON |

## Parameters
| Parameter | Expected input | Explanation |
| :------------: |  :------------: |  :------------: |
| city | str(city name) | - |
| soil | int(1, 2 or 3)| 1: Pasir, 2: Lempung, 3: Liat |
| light | int(1 or 2) | 1: Full sun, 2: Semi shade |

## Machine Learning Model
![image](https://user-images.githubusercontent.com/66265368/173277288-6b6173da-60a2-47fa-8bf1-f1457c7c5b0e.png)
In our machine learning model we use a deep neural network with 4 layers, 1 layer for input with input_dim is 5 which will enter 5 data, namely temperature, humidity, rainfall, soil, and light, then 2 layers for the hidden layer, and the last 1 layer for the output, in the output layer we use softmax activation so that later we can take a sequence of 5 predictions with the highest accuracy. Here we can see after we train the model we get 33% loss and 89% accuracy, from this training result as you can see highest accuracy prediction and actual data are the same and then it will be followed up to second-highest accuracy to the fifth-highest accuracy


# How to run this Flask app locally
- Clone this repo
- Open terminal and go to this project's root directory
- Create your own OpenWeatherMap API_KEY (\*[Notes](https://github.com/GajAhmadaaa/NanamYuk-ML/blob/main/Weather%20API/readme.md))
- Create a config.py file and type `api_key="your_api_key"` then save
- Create and activate a python virtual environment if you want
- Type `pip install -r requirements.txt`
- Serve the Flask app by typing `flask run`
- It will run on `http://127.0.0.1:5000`

