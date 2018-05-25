from pandas import read_csv, DataFrame, concat
from io import StringIO
import tensorflow as tf
from keras.models import model_from_json
import numpy as np
import matplotlib.pyplot as plt
import mpld3

def loadModel():
	with open("LSTM/LSTM.json", "r") as json_file:
			loaded_model_json = json_file.read()

			model = model_from_json(loaded_model_json)
			model.load_weights("LSTM/LSTM.h5")
			model.compile(loss="mse", optimizer="rmsprop", metrics=["mse"])
			return model

def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

def lstmPredict(csvText, habitants):
	x = 1
	try:
		habitants = int(habitants)
		csvText.replace("\r", "")
		csvFile = read_csv(StringIO(csvText), header=None)

		numberOfRows = csvFile.shape

		if(numberOfRows[0] < 4):
			return "Error, number of rows must be at least 4"

		if(numberOfRows[1] != 2):
			return "Error, must have only 2 features"
		# Scale
		csvFile[0] /= 100
		csvFile[1] = csvFile[[1]].apply(lambda x: x*100000/habitants, axis=1)

		#Ensure data is float values = dataset.values.astype("float32")
		values = csvFile.values.astype("float32")

		total_features = len(values[0])

		n_weeks = 4
		n_features = 2

		reframed = series_to_supervised(values, n_weeks-1, 1)
		values = reframed.values
		print("Reframed Shape: ", reframed.shape)
		# print(values)
		y = csvFile[1].values
		x = values
		# x = [	[  1.  10.   2.  20.   3.  30.   4.  40.]
 		#		[  2.  20.   3.  30.   4.  40.   5.  50.]
 		#		[  3.  30.   4.  40.   5.  50.   6.  60.]]
		# y = 	[10 20 30 40 50 60]
		x = x.reshape((x.shape[0], n_weeks, n_features)) # Reshape as 3-D
		yPred = []
		xYPred = []
		with tf.Session() as sess:
			model = loadModel()
			predictions = model.predict(x)
			print(predictions)

			diff = len(y)+1 - len(predictions)

			for i in range(len(predictions.flatten())):
				pred = predictions[i]
				xYPred.append(diff+i)
				yPred.append(pred)
				# yPred.append(pred)
		# print(yPred)

		fig = plt.figure()
		plt.ylabel("Cases")
		plt.xlabel("Week #")
		plt.plot(y, label="Cases")
		plt.plot(xYPred, yPred, label="Predictions")
		plt.legend()
		
		ht = mpld3.fig_to_html(fig)

		return ht

	except Exception as e:
		return "Something bad happened"