from functools import partial
from crypto import  encodeBase64, decodeBase64, encodeBase32, decodeBase32

def cia():
  cia = customtkinter.CTk()
  cia.title("Cipher Index Analisys")
  cia.geometry('500x500')

  TextInput = customtkinter.CTkEntry(cia, placeholder_text='Enter Encrypted Text', width=140, height=28)
  entry.place(x=0, y=0)

  def enterEvent():
    print('button pressed')

  def enterNcipher():
    #create another text prompt infintily
    print("hello world")
  
  Enterbutton = customtkinter.CTkButton(cia, text='See Stats',command=enterEvent ,width=140, height=28)
  Enterbutton.place(x=10, y=10)

  cipherNButton = customtkinter.CTkButton(cia, text='enter another cipher',command=enterNcipher ,width=140, height=28)
  cipherNButton.place(x=10, y=10)
  
  ShannonOut = customtkinter.CTkLabel(cia, text=shannonIndex, width=40, height=28, fg_color=' ace(x=10, y=6)

  gdeOut = customtkinter.CTkLabel(cia, text=gde, width=40, height=28, fg_color=' ace(x=10, y=10)

  renyiOut = customtkinter.CTkLabel(cia, text=renyi, width=40, height=28, fg_color=' ace(x=10, y=14)

  ngramOut = customtkinter.CTkLabel(cia, text=ngram, width=40, height=28, fg_color=' ace(x=10, y=18)

  iocOut = customtkinter.CTkLabel(cia, text=ioc, width=40, height=28, fg_color=' ace(x=10, y=20)
  
  prob1Out = customtkinter.CTkLabel(cia, text=ioc, width=40, height=28, fg_color=' ace(x=10, y=20)
  
  prob2Out = customtkinter.CTkLabel(cia, text=ioc, width=40, height=28, fg_color=' ace(x=10, y=20)
  
  if(ciperNButton.click()):
    #create another cipher text field and run test agian
    print("idk, brayden fix the button system so i can debug cia")
    



"""
Cipher index (a summation of a bunch of indicators for pattern recong. / repition / identiers for crypto)
  -shannon index
  -bigram / trigram indecies
  -index of coincidence
  -frequency analysis
"""

#shannon index

shannonIndex = 0

"""
PS = product summation

H=ln(1/(PS;R;i=1)P_i && P^P_i)

float H = 0 #output
float  ln = 0 #any natrual log
int R = 0 #the length of the Dataset

"""

#generelized diversity equation

gde = 0

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

renyi = 0

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

ngram = 0

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
ioc = 0
"""
this takes 2 or more encryptions of the same type and compares them for similiarties 

H = ((SN;c;i=1)n_i^(n_i - 1) / N(N-1)/c)

float H = 0 #output
int N = 0 #dataset length
int c = 0 #amount of char being used (english is 26)
int i = 0 #a single point in the dataset

"""

prob1Out = 0
prob2Out = 0
"""
prob1 = Takes two diffrent ciphers and outputs the probabillity that they are the same cipher

//////////

prob2 = Takes the outputs of other equations for known ciphers and matches it agianst the
user input cipher to return a probillity oif what cipher it could be 
"""