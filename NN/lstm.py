from pandas import read_csv, DataFrame, concat
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from keras import Sequential
from keras.layers import LSTM, Dense, BatchNormalization
from keras.constraints import non_neg
from matplotlib import pyplot
from numpy import concatenate, apply_along_axis
from math import sqrt
from sklearn.metrics import mean_squared_error
from keras.models import model_from_json
from os.path import isfile
import keras.backend as K

def root_mean_squared_error(y_true, y_pred):
        return K.sqrt(K.mean(K.square(y_pred - y_true), axis=-1)) 

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

# dataset = read_csv('data/Weekly-Veracruz_15-11-2015_848.csv', header=0, index_col=0)
# dataset = read_csv('data/Weekly-Yucatan_15-11-2015_848.csv', header=0, index_col=0)
# dataset = read_csv('data/Weekly-Bahia_04-01-2015_504.csv', header=0, index_col=0)
# dataset = read_csv('data/Weekly-NuevoLeon_15-11-2015_848.csv', header=0, index_col=0)
# dataset = read_csv('data/Weekly-Guerrero_15-11-2015_848.csv', header=0, index_col=0)
dataset = read_csv('data/Weekly-Chiapas_15-11-2015_848.csv', header=0, index_col=0)
#Standarize
dataset[["searches"]] = dataset[["searches"]]/100

# population = 8112505 #Veracruz
# population = 2097175 #Yucatan
# population = 3533251 #Guerrero
population = 5217908 #Chiapas
# population = 15203934 #Bahia
# population = 5119504 # NUevoLeon
dataset[["cases"]] = dataset[["cases"]] * (100000 / population)
# 
values = dataset.values
# ensure all data is float
values = values.astype('float32')


# specify the number of lag hours
n_hours = 3
n_features = 2
# frame as supervised learning
reframed = series_to_supervised(values, n_hours, 1)
print(reframed.shape)
 
# split into train and test sets
values = reframed.values
n_train_hours = 0
train = values[:n_train_hours, :]
test = values[n_train_hours:, :]
# split into input and outputs
n_obs = n_hours * n_features
train_X, train_y = train[:-n_hours, :n_obs], train[n_hours:, 1]
test_X, test_y = test[:-n_hours, :n_obs], test[n_hours:, 1]
print(train_X.shape, len(train_X), train_y.shape)

# reshape input to be 3D [samples, timesteps, features]
train_X = train_X.reshape((train_X.shape[0], n_hours, n_features))
test_X = test_X.reshape((test_X.shape[0], n_hours, n_features))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

model = None
if(isfile("model.json") and isfile("model.h5")):
# if False:
	json_file = open("model.json", "r")
	loaded_model_json = json_file.read()
	json_file.close()
	model = model_from_json(loaded_model_json)

	#load weights
	model.load_weights("model.h5")
	model.compile(loss=root_mean_squared_error, optimizer="adam")
	print("Loaded model from disk")
else:

	# design network
	model = Sequential()
	model.add(LSTM(32, input_shape=(train_X.shape[1], train_X.shape[2]), return_sequences=True))
	model.add(LSTM(32, return_sequences=False))
	# model.add(LSTM(100, input_shape=(train_X.shape[1], train_X.shape[2]), return_sequences=False))
	model.add(Dense(128, activation="relu"))
	# model.add(BatchNormalization())
	# model.add(Dense(1, activation="sigmoid", kernel_constraint=non_neg()))
	model.add(Dense(1))

	model.compile(loss=root_mean_squared_error, optimizer='adam')
	# fit network
	history = model.fit(train_X, train_y, epochs=50, batch_size=80, validation_data=(test_X, test_y), verbose=2, shuffle=False)

	#Save model
	model_json = model.to_json()
	with open("model.json", "w") as json_file:
		json_file.write(model_json)
	#seralize weights to HDF5
	model.save_weights("model.h5")
	print("Saved model to disk")

	# plot history

	if("loss" in history.history):
		pyplot.plot(history.history['loss'], label='train')
	
	if("val_loss" in history.history):
		pyplot.plot(history.history['val_loss'], label='test')
	pyplot.legend()
	pyplot.show()

#Make predictions
yhat = model.predict(test_X)

print("FSHAPE", yhat.shape, test_y.shape)

yhat = apply_along_axis(lambda x: x/(100000 / population), 1, yhat)
test_y = apply_along_axis(lambda x: x/(100000 / population), 0, test_y)

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
pyplot.title("Chiapas_15-11-2015")
pyplot.ylabel("Casos")
pyplot.xlabel("Semana")
pyplot.plot(x, yhat, label="Predicition")
pyplot.plot(x, test_y, label="Actual Values")
pyplot.legend()
pyplot.show()
