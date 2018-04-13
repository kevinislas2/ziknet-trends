from pandas import read_csv, DataFrame

def getModel():

	
	modelFilename = "./MexicoCases2015-2018.csv"
	model = read_csv(modelFilename, index_col="CITY", header=0)

	output = DataFrame(index=model.index)

	for i in range(2015, 2019):
		col = str(i)
		temp = model[model.columns[model.columns.str.contains(col)]]
		output[col] =  temp.sum(axis=1)

	output.to_csv("yearlyMexico2015-2018.csv")
	


if __name__ == '__main__':
	dataset = getModel()