from pandas import read_csv, DataFrame, concat
from keras import Sequential
from keras.layers import Dense, Dropout, LSTM
from keras.constraints import non_neg
import keras.backend as K
from matplotlib import pyplot
from math import sqrt
from sklearn.metrics import mean_squared_error
from keras.models import model_from_json
from os.path import isfile
from numpy  import apply_along_axis
import math
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

def readCSV(filename, lagWeeks):
	dataset = read_csv(filename, header=0, index_col=0)

	dataset[["searches"]] = dataset[["searches"]] / 100
	# dataset[["cases"]] = dataset[["cases"]] / 100
	values = dataset.values
	values = values.astype('float32')
	# print(values)
	#Here goes scaling/normalization
	reframed = series_to_supervised(values, lagWeeks, 1)

	n_features = 2
	# split into train and test sets
	values = reframed.values
	n_train_weeks = 0
	train = values[:n_train_weeks, :]
	test = values[n_train_weeks:, :]

	#Separate input from output
	n_obs = lagWeeks * n_features
	train_X, train_y = train[:-lagWeeks, :n_obs], train[lagWeeks:, 1]
	test_X, test_y = test[:-lagWeeks, :n_obs], test[lagWeeks:, 1]
	print(train_X.shape, len(train_X), train_y.shape)
	return train_X, train_y, test_X, test_y

def soft_acc(y_true, y_pred):
    return K.mean(K.equal(K.round(y_true), K.round(y_pred)))

def getNN(shape):

	if(isfile("modelNN.json") and isfile("modelNN.h5")):
		json_file = open("modelNN.json", "r")
		loaded_model_json = json_file.read()
		json_file.close()
		model = model_from_json(loaded_model_json)

		#load weights
		model.load_weights("modelNN.h5")
		model.compile(loss="mae", optimizer="adam", metrics=["acc"])
		return model, False
	else:
		model = Sequential()
		model.add(Dense(256, input_shape=shape, activation="relu"))
		model.add(Dropout(0.5))
		model.add(Dense(256, activation="relu"))
		model.add(Dense(1, activation="linear", kernel_constraint=non_neg()))
		model.compile(loss="mae", optimizer="adam", metrics=["acc"])
		return model, True

def testAcc(model, test_X, test_y):
	#Make predictions
	yhat = model.predict(test_X)
	inv_yhat = test_y

	# print("FSHAPE", yhat.shape, inv_yhat.shape)

	# yhat = apply_along_axis(lambda x: x * 100, 1, yhat)
	# test_y = apply_along_axis(lambda x: x * 100, 0, test_y)

	# # calculate RMSE
	rmse = sqrt(mean_squared_error(yhat, test_y))
	print('Test RMSE: %.3f' % rmse)
	print("Total", sum(test_y))
	print("len", len(test_y))
	# print("REAL",inv_y)

	x = []
	y = []
	pred = []
	for i in range(len(test_y)):
		x.append(i)


	print("REAL: ", test_y)
	print("PRED: ", yhat)

	pyplot.plot(x, yhat, label="Predicition")
	pyplot.plot(x, test_y, label="Actual Values")
	pyplot.legend()
	pyplot.show()


def run():
	# train_X, train_y, test_X, test_y = readCSV("data/Weekly-Veracruz_15-11-2015_848.csv", 4)
	train_X, train_y, test_X, test_y = readCSV("data/Weekly-NuevoLeon_15-11-2015_848.csv", 4)
	# train_X, train_y, test_X, test_y = readCSV("data/Weekly-Yucatan_15-11-2015_848.csv", 4)

	# train_X, train_y, test_X, test_y = readCSV("data/Weekly-Chiapas_15-11-2015_848.csv", 4)
	# train_X, train_y, test_X, test_y = readCSV("data/Weekly-Guerrero_15-11-2015_848.csv", 4)
	# train_X, train_y, test_X, test_y = readCSV("data/Weekly-Bahia_04-01-2015_504.csv", 4)
	# train_X, train_y, test_X, test_y = readCSV("data/WORLD.csv", 4)

	model, TRAIN = getNN((train_X.shape[1],))
	if(TRAIN):
		history = model.fit(train_X, train_y, epochs=80, batch_size=128, validation_data=(test_X, test_y), verbose=2, shuffle=True)


		if("loss" in history.history):
			pyplot.plot(history.history['loss'], label='train')
		
		if("val_loss" in history.history):
			pyplot.plot(history.history['val_loss'], label='test')

		pyplot.legend()
		pyplot.show()

		model_json = model.to_json()
		with open("modelNN.json", "w") as json_file:
			json_file.write(model_json)
			#seralize weights to HDF5
			model.save_weights("modelNN.h5")
			print("Saved model to disk")

	testAcc(model, test_X, test_y)


run()