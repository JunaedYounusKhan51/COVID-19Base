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
full_X = full_data[['Minimum Distance Between Disease and Drug','Polarity(textblob)','Sentiment Rate (unsupervised)','Outlier Flag']].as_matrix() 
scalar = MinMaxScaler()
scalar.fit(full_X)
full_X = scalar.transform(full_X)





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



# make a prediction
full_y_class_list = loaded_model.predict_classes(full_X)
full_y_prob = loaded_model.predict_proba(full_X)

full_y_confidence = []
full_y_class = []

for i in range(len(full_y_class_list)):
	full_y_class.append(full_y_class_list[i][0])



for i in range(len(full_y_class)):
	confidence = "ERROR"
	if full_y_class[i] == 0:
		confidence  = 1.0 - full_y_prob[i][0]
	elif full_y_class[i] == 1:
		confidence = full_y_prob[i][0]
	full_y_confidence.append(confidence) 

full_data['Final Predicted Label (NN)'] = full_y_class
full_data['Confidence Score'] = full_y_confidence
full_data.to_csv('final_output_prediction_and_confidence.csv', index= False)


 
