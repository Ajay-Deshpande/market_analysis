# Market Analysis

## Overview

Candlestick patterns are a popular way to identify potential market reversals or continuations. By analyzing the shapes and sizes of candlesticks, traders can gain insights into market sentiment and make informed trading decisions.

## Data Collection
BeautifulSoup is used to parse Yahoo Finance's HTML pages and extract specific information, such as a stock's profile details or financial data. 
*For example, get_profile_data() parses a profile page for a given stock ticker and extracts its sector, industry, and description.*

Pandas, on the other hand, is used to process and manipulate financial data, and perform feature engineering techniques to add candlestick pattern information.

## Candlestick Patterns
The module includes functions to identify the following candlestick patterns:

1. *Marubozu (marubozu):* 

A Marubozu pattern occurs when the candlestick has a small wick (or none at all) and a large body that covers the entire range of the candlestick. Marubozu patterns are often considered strong indicators of bullish or bearish trends.


2. *Spinning Top or Doji (spinning_top_doji):* 

A spinning top pattern occurs when the candlestick has a small body and long upper and lower wicks, indicating indecision in the market. A doji pattern occurs when the candlestick has a small body and nearly equal upper and lower wicks, indicating a potential reversal in the market.


3. *Paper Umbrella (paper_umbrella):* 

A paper umbrella pattern occurs when the candlestick has a small body and a long lower wick, indicating a potential bullish reversal in the market.

4. *Shooting Star (shooting_star):*

A shooting star pattern occurs when the candlestick has a small body and a long upper wick, indicating a potential bearish reversal in the market.

5. *Engulfing (engulfing):*

An engulfing pattern occurs when the body of one candlestick completely engulfs the body of the previous candlestick, indicating a potential reversal in the market.

6. *Harami (harami):*

A harami pattern occurs when a small candlestick is contained within the body of the previous candlestick, indicating a potential reversal in the market.

7. *Partial Engulf (partial_engulf):*

A partial engulf pattern occurs when the body of one candlestick partially engulfs the body of the previous candlestick, indicating a potential reversal in the market.

8. *Gap Opening (gap_opening):*

A gap opening pattern occurs when the opening price of a candlestick is significantly higher or lower than the closing price of the previous candlestick, indicating a potential continuation or reversal in the market.

9. *Star (star):*

A star pattern occurs when the opening price of a candlestick is significantly higher or lower than the closing price of the previous candlestick, indicating a potential continuation or reversal in the market.
