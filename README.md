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

## Flowchart

```flow
st=>start: Start
op1=>operation: Send GET requset to API Endpoint
cond1=>condition: All Paramerters are provided?
op2=>operation: Internal Error
cond2=>condition: Checking if city available
op3=>operation: Return Error Message
op4=>operation: Getting city data
op5=>operation: ML Model Predicting
op6=>operation: Return prediction Result
e=>end: End

st->op1->cond1
cond1(yes)->cond2
cond1(no)->op2->e
cond2(yes)->op4->op5->op6->e
cond2(no)->op3->e
```

