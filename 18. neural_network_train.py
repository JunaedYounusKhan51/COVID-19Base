# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import shuffle
from keras.models import model_from_yaml


full_data = pd.read_csv('final_output_with_len.csv')
# load the dataset
data = pd.read_csv('final_output_labeled_only_with_len.csv')
#data=data[data['Outlier Flag'] != 1]
data = shuffle(data)
#recipes

print("csv load done")










'''
scaler = UniformScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

'''
#Id,Disease Name,Drug Name,Common Sentence,Chosen Sentence,Minimum Distance Between Disease and Drug,Common Paper Doi,Polarity(textblob),Label(textblob),Agree/Disagree(textblob),Outlier Flag,Sentiment Rate (unsupervised),Label (unsupervised),(delete this) sentence
full_X = full_data[['Minimum Distance Between Disease and Drug','Polarity(textblob)','Sentiment Rate (unsupervised)','Outlier Flag']].as_matrix() 
XX = data[['Minimum Distance Between Disease and Drug','Polarity(textblob)','Sentiment Rate (unsupervised)','Outlier Flag']].as_matrix()
yy = np.array(data['Manual Label'])

split_point = 125

X_train = XX[0:split_point]
y_train = yy[0:split_point]

X_test = XX[split_point:]
y_test = yy[split_point:]

X = XX
y = yy

scalar = MinMaxScaler()
scalar.fit(full_X)
X = scalar.transform(X)
X_test = scalar.transform(X_test)
XX = scalar.transform(XX)
#'Minimum Distance Between Disease and Drug','Polarity(textblob)','Sentiment Rate (unsupervised)','Article Len'
#'Manual Label'




# define the keras model
model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
#model.add(Dense(8))
#model.add(LeakyReLU(alpha=0.1))
model.add(Dense(4, activation='tanh'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
#model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
#model.compile(loss='cosine_proximity', optimizer='adam', metrics=['accuracy'])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


# fit the keras model on the dataset
model.fit(X, y, epochs=500, batch_size=5)



# make a prediction
y_class = model.predict_classes(X)
y_prob = model.predict_proba(X)
# show the inputs and predicted outputs
for i in range(len(X)):
	if y[i] == 1 and y_class[i] == 0:
		print("PROBLEM-1")
	if y[i] == 0 and y_class[i] == 1:
		print("PROBLEM-2")	
	print("serial=%s y=%s, y_c=%s, y_p=%s" % (i, y[i], y_class[i], y_prob[i]))
	 
	#if y[i] != y_class[i]:
		#print("serial=%s y=%s, y_c=%s, y_p=%s" % (i, y[i], y_class[i], y_prob[i]))


# evaluate the keras model
_, accuracy = model.evaluate(X_test, y_test)
print('Accuracy: %.2f' % (accuracy*100))


# serialize model to YAML
model_yaml = model.to_yaml()
with open("model.yaml", "w") as yaml_file:
    yaml_file.write(model_yaml)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")



# later...

# load YAML and create model
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
score = loaded_model.evaluate(XX, yy)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
