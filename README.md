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
I have uploaded data from two most popular lotteries.  
### Click to download the **latest** updated results
 
**[Powerball](https://www.texaslottery.com/export/sites/lottery/Games/Powerball/Winning_Numbers/download.html)** >> '[powerball.csv](https://www.texaslottery.com/export/sites/lottery/Games/Powerball/Winning_Numbers/powerball.csv)'  
**[Mega Millions](https://www.texaslottery.com/export/sites/lottery/Games/Mega_Millions/Winning_Numbers/download.html)** >> '[megamillions.csv](https://www.texaslottery.com/export/sites/lottery/Games/Mega_Millions/Winning_Numbers/megamillions.csv)'

#### (found from `https://www.texaslottery.com`)

<br>

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

Set how many of the *most recent* rows of data you would like to use:
```
# Number of rows in data
set_rows = 200
```
- Each iteration will be the same unless this value is changed.
