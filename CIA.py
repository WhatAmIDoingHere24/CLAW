from functools import partial


def cia():
    print("hello world")

"""
Cipher index (a summation of a bunch of indicators for pattern recong. / repition / identiiers for crypto)
  -shannon index
  -bigram / trigram indecies
  -index of coincidence
  -frequency analysis
"""

#shannon index
"""
PS = product summation

H=ln(1/(PS;R;i=1)P_i && P^P_i)

float H = 0 #output
float  ln = 0 #any natrual log
int R = 0 #the length of the Dataset

"""

#generelized diversity equation
"""
SN = sigma notation


D^q = ((SN;R;i=1;)P_i && P^P_i)^1/(1-q)

float D = 0 #output
int q = 0 #allows for diffrent outcomes, as 'q' grows it will give diffrent value types, most notable are 0,1,2,3
int R = 0 #amout of types (diffrent char) in the dataset
float p = 0 #total point in dataset (honestly not 100% sure what p is)
int i = 0 #point in data set (what value is the loop at from 0)

"""

#renyi entropy
#only if q != 1
"""
H^q = ln(1/(q-1(sqrt((SN;R;i=1)P_i * P_i^q-1))))

float D = 0 #output
int q = 0 #allows for diffrent outcomes, as 'q' grows it will give diffrent value types, most notable are 0,1,2,3
int R = 0 #amout of types (diffrent char) in the dataset
float p = 0 #total point in dataset (honestly not 100% sure what p is)
int i = 0 #point in data set (what value is the loop at from 0)
float ln = #any natrual log

"""


#n-gram
#theres no deafeanet equation so i made on up
"""
float H = 0 #output
int R = 0 #dataset length
int n = 0 #length of search term
String q = #the string to search for


H = ((SN;R;i=n))

#just search through the data set looking for that specific String
#  than returnn how often it shows up
#n-grams get more accurate with more data

"""

#index of coinicidence
"""
this takes 2 or more encryptions of the same type and compares them for similiarties 

H = ((SN;c;i=1)n_i^(n_i - 1) / N(N-1)/c)

float H = 0 #output
int N = 0 #dataset length
int c = 0 #amount of char being used (english is 26)
int i = 0 #a single point in the dataset

"""
