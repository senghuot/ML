from numpy import *

# Data encoding
WORKCLASS = {'Private':0, 'Self-emp-not-inc':1, 'Self-emp-inc':2, 'Federal-gov':3, 'Local-gov':4, 'State-gov':5, 'Without-pay':6, 'Never-worked':7}
EDUCATION = {'Bachelors':0, 'Some-college':1, '11th':2, 'HS-grad':3, 'Prof-school':4, 'Assoc-acdm':5, 'Assoc-voc':6, '9th':7, '7th-8th':8, '12th':9,
              'Masters':10, '1st-4th':11, '10th':12, 'Doctorate':13, '5th-6th':14, 'Preschool':15}
MARITAL_STATUS = {'Married-civ-spouse':0, 'Divorced':1, 'Never-married':2, 'Separated':3, 'Widowed':4, 'Married-spouse-absent':5, 'Married-AF-spouse':6}
OCCUPATION = {'Tech-support':0, 'Craft-repair':1, 'Other-service':2, 'Sales':3, 'Exec-managerial':4, 'Prof-specialty':5, 'Handlers-cleaners':6,
              'Machine-op-inspct':7, 'Adm-clerical':8, 'Farming-fishing':9, 'Transport-moving':10, 'Priv-house-serv':11, 'Protective-serv':12, 'Armed-Forces':13}
RELATIONSHIP = {'Wife':0, 'Own-child':1, 'Husband':2, 'Not-in-family':3, 'Other-relative':4, 'Unmarried':5}
RACE = {'White':0, 'Asian-Pac-Islander':1, 'Amer-Indian-Eskimo':2, 'Other':3, 'Black':4}
SEX = {'Female':0, 'Male':1}
NATIVE_COUNTRY = {'United-States':0, 'Cambodia':1, 'England':2, 'Puerto-Rico':3, 'Canada':3, 'Germany':4, 'Outlying-US(Guam-USVI-etc)':5, 
                'India':6, 'Japan':7, 'Greece':8, 'South':9, 'China':10, 'Cuba':11, 'Iran':12, 'Honduras':13, 'Philippines':14, 'Italy':15, 
                'Poland':16, 'Jamaica':17, 'Vietnam':18, 'Mexico':19, 'Portugal':20, 'Ireland':21, 'France':22, 'Dominican-Republic':23, 
                'Laos':24, 'Ecuador':25, 'Taiwan':26, 'Haiti':27, 'Columbia':28, 'Hungary':29, 'Guatemala':30, 'Nicaragua':31, 'Scotland':32, 
                'Thailand':33, 'Yugoslavia':34, 'El-Salvador':35, 'Trinadad&Tobago':36, 'Peru':37, 'Hong':38, 'Holand-Netherlands':39}
INCOME = {'<=50K':0, '>50K':1}

def main():
  training_tmp = genfromtxt('data.txt', delimiter=',',
      converters={1:convertData, 3:convertData, 5:convertData, 6:convertData, 7:convertData,
                  8:convertData, 9:convertData, 13:convertData, 14:convertData})
  print training_tmp

def convertData(string):
  string = string.lstrip()
  if string in WORKCLASS:
    return WORKCLASS[string]
  
  if string in EDUCATION:
    return EDUCATION[string]

  if string in MARITAL_STATUS:
    return MARITAL_STATUS[string]

  if string in OCCUPATION:
    return OCCUPATION[string]

  if string in RELATIONSHIP:
    return RELATIONSHIP[string]

  if string in RACE:
    return RACE[string]

  if string in SEX:
    return SEX[string]

  if string in NATIVE_COUNTRY:
    return NATIVE_COUNTRY[string]

  if string in INCOME:
    return INCOME[string]

  return -1

if __name__ == '__main__':
  main()