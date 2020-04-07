import pandas as pd
df = pd.read_csv('investments_VC.csv', encoding='unicode_escape')

# Data columns (total 39 columns):
#  #   Column                Non-Null Count  Dtype  
# ---  ------                --------------  -----  
#  0   permalink             49438 non-null  object 
#  1   name                  49437 non-null  object 
#  2   homepage_url          45989 non-null  object 
#  3   category_list         45477 non-null  object 
#  4    market               45470 non-null  object 
#  5    funding_total_usd    49438 non-null  object 
#  6   status                48124 non-null  object 
#  7   country_code          44165 non-null  object 
#  8   state_code            30161 non-null  object 
#  9   region                44165 non-null  object 
#  10  city                  43322 non-null  object 
#  11  funding_rounds        49438 non-null  int64  
#  12  founded_at            38554 non-null  object 
#  13  founded_month         38482 non-null  object 
#  14  founded_quarter       38482 non-null  object 
#  15  founded_year          38482 non-null  float64
#  16  first_funding_at      49438 non-null  object 
#  17  last_funding_at       49438 non-null  object 
#  18  seed                  49438 non-null  int64  
#  19  venture               49438 non-null  int64  
#  20  equity_crowdfunding   49438 non-null  int64  
#  21  undisclosed           49438 non-null  int64  
#  22  convertible_note      49438 non-null  int64  
#  23  debt_financing        49438 non-null  int64  
#  24  angel                 49438 non-null  int64  
#  25  grant                 49438 non-null  int64  
#  26  private_equity        49438 non-null  int64  
#  27  post_ipo_equity       49438 non-null  int64  
#  28  post_ipo_debt         49438 non-null  int64  
#  29  secondary_market      49438 non-null  int64  
#  30  product_crowdfunding  49438 non-null  int64  
#  31  round_A               49438 non-null  int64  
#  32  round_B               49438 non-null  int64  
#  33  round_C               49438 non-null  int64  
#  34  round_D               49438 non-null  int64  
#  35  round_E               49438 non-null  int64  
#  36  round_F               49438 non-null  int64  
#  37  round_G               49438 non-null  int64  
#  38  round_H               49438 non-null  int64  
# dtypes: float64(1), int64(22), object(16)
# memory usage: 14.7+ MB


""" DETECT MISSING VALUES """ 
Missing_values_in_every_column = df.isnull().sum()

# permalink                   0
# name                        1
# homepage_url             3449
# category_list            3961
#  market                  3968
#  funding_total_usd          0
# status                   1314
# country_code             5273
# state_code              19277
# region                   5273
# city                     6116
# funding_rounds              0
# founded_at              10884
# founded_month           10956
# founded_quarter         10956
# founded_year            10956
# first_funding_at            0
# last_funding_at             0
# seed                        0
# venture                     0
# equity_crowdfunding         0
# undisclosed                 0
# convertible_note            0
# debt_financing              0
# angel                       0
# grant                       0
# private_equity              0
# post_ipo_equity             0
# post_ipo_debt               0
# secondary_market            0
# product_crowdfunding        0
# round_A                     0
# round_B                     0
# round_C                     0
# round_D                     0
# round_E                     0
# round_F                     0
# round_G                     0
# round_H                     0
# dtype: int64

Total_missing_values = df.isnull().sum().sum()
# print(Total_missing_values) 
#Total missing values in the entire dataset is 92384 


"""Filter the missing values using dropna"""
old_df = df.shape  # The original dataset has 49438 rows and 39 columns 

new_df = df.dropna()
# After using the dropna to drop the rows, which have missing values. 
# The new dataset has 21840 rows and 39 columns 

""""Drop columns in the new dataset"""
new_df.drop(['name', 'permalink','category_list','founded_quarter','state_code','seed', 'venture', 'equity_crowdfunding',
       'undisclosed', 'convertible_note', 'debt_financing', 'angel', 'grant',
       'private_equity', 'post_ipo_equity', 'post_ipo_debt',
       'secondary_market', 'product_crowdfunding', 'round_A', 'round_B',
       'round_C', 'round_D', 'round_E', 'round_F', 'round_G', 'round_H'], axis=1, inplace = True)
# After dropping the columns, the new_df has 21840 rows and 13 columns 








