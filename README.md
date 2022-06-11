# NanamYuk-ML
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

# How to run this Flask app locally
- Clone this repo
- Open terminal and go to this project's root directory
- Create your own OpenWeatherMap API_KEY (\*Notes)
- Create a config.py file and type `api_key="your_api_key"` then save
- Create and activate a python virtual environment if you want
- Type `pip install -r requirements.txt`
- Serve the Flask app by typing `flask run`
- It will run on `http://127.0.0.1:5000`

