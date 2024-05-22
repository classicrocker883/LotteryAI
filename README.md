# README
To generate lottery numbers using predictive AI machine learning.
This uses historical data of past drawings adding weights to the most recent of drawings.

## Install modules
```
pip install scikit-learn pandas numpy
```
-- OR --
```
python3 -m pip install scikit-learn pandas numpy
```

## To use
I have uploaded data from two most popular lotteries:  
**Powerball** >> 'powerball.csv'  
**Mega Millions** >> 'megamillions.csv'

To change which file is used, in **generate_numbers.py** _comment out_ the corresponding names:
```py
#filename = 'powerball.csv'
filename = 'megamillions.csv'

# MegaMillions
max_white = 70
max_red = 25
# Powerball
#max_white = 69
#max_red = 26
```

Set how many rows of data you would like to use:
```
# Number of rows in data
set_rows = 200
```
- Each iteration will be the same unless this value is changed.
