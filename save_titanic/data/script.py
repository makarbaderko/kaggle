import numpy 
import pandas 
import matplotlib.pyplot as plt

train_data = pandas.read_csv('train.csv', delimiter=',', 
	    names=['PassengerId','Survived','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'])
status = pandas.read_csv('gender_submission.csv', delimiter=',',
                    names=['PassengerId', 'Survived'])

print(status.Survived)