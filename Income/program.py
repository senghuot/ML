from numpy import *
from sklearn import tree

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
INCOME = {'<=50K':-1, '>50K':1}
ITERATIONS = 100

def main():
  clf = tree.DecisionTreeClassifier(max_depth=2, criterion='entropy')
  train_tmp = genfromtxt('data.txt', delimiter=',',
      converters={1:convertData, 3:convertData, 5:convertData, 6:convertData, 7:convertData,
                  8:convertData, 9:convertData, 13:convertData, 14:convertData})
  
  # Setting up hyper parameters
  TRAIN_LEN = int(len(train_tmp) * (2.0/3))

  # Training weights
  d = [1.0/TRAIN_LEN] * TRAIN_LEN

  # Training set
  train_x = []
  train_y = []

  for i in range(0, TRAIN_LEN):
    tmp = train_tmp[i]
    x = []
    for j in range(0, len(tmp)-2):
      x.append(tmp[j])
    train_x.append(x)
    train_y.append(tmp[len(tmp)-1])

  # Testing set
  test_x = []
  test_y = []

  for i in range(TRAIN_LEN, len(train_tmp)):
    tmp = train_tmp[i]
    x = []
    for j in range(0, len(tmp)-2):
      x.append(tmp[j])
    test_x.append(x)
    test_y.append(tmp[len(tmp)-1])


  # Convert narrays to matrices
  train_x = matrix(train_x)
  train_y = matrix(train_y).reshape(len(train_y),1)
  test_x  = matrix(test_x)
  test_y  = matrix(test_y).reshape(len(test_y),1)

  # Accumulation of Ys
  final_y = [0] * len(test_y)
  for iteration in range(0, ITERATIONS): 
    # Checking for error rate for training data
    clf = clf.fit(train_x, train_y, sample_weight=d)
    predicted_y = clf.predict(train_x)

    # Getting epsilon
    epsilon = 0
    toal_weight = 0
    for i in range(0, len(predicted_y)):
      epsilon += d[i] * pi(predicted_y[i], train_y[i])
      toal_weight += d[i]
    epsilon /= toal_weight

    alpha = 1
    if epsilon != 0:
      # Updates and normalizing the weights
      alpha = math.log((1-epsilon)/epsilon)
      total_weight = 0
      for i in range(0, len(predicted_y)):
        power = alpha * pi(train_y[i], predicted_y[i])
        d[i] = d[i] * math.pow(math.e, power)
        total_weight += d[i]
      
      # Normalizing
      for i in range(0, len(predicted_y)):
        d[i] = d[i] / total_weight

    # Accumulate voting on training data
    error = 0
    final_y += alpha * clf.predict(test_x)
    for i in range(0, len(final_y)):
      if sign(final_y[i]) != test_y[i]:
        error += 1 
    
    print 100.0 * error / len(final_y)

def pi(n1, n2):
  if n1 != n2:
    return 1
  return 0

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