from flask import Flask, render_template, redirect, flash
from visualizer import getCurrentStatusPlot
from forms import VisualizerForm, ScatterForm
from config import Config
from scatterplot import getScatterPlot
import csv
app = Flask(__name__)
app.config.from_object(Config)
import os


@app.route("/")
def home():
	return render_template("pages/home.html")

@app.route("/index")
def index():
	user = {"username":"Kevin"}
	return render_template("index.html", title="Ziknet Trends", user=user)


def basicPlotter(filename):
	import matplotlib.pyplot as plt
	from io import BytesIO
	import base64

	#Set up Form
	form = VisualizerForm()

	#Check if POST
	numberOfStates = (form.numberOfStates.data and int(form.numberOfStates.data)) or 5
	year = (form.year.data and str(form.year.data)) or "ALL"
	states = form.statesCheckbox.data

	#Getting plot
	currentStatusPlot = getCurrentStatusPlot(numberOfStates, year, states, filename)
	currentStatusPlot.plot()

	### Saving plot to disk in png format
	# plt.savefig('img/test_plot.png')

	### Rendering Plot in Html
	figfile = BytesIO()
	plt.savefig(figfile, format='png')
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	result = figdata_png
	### Remove b' from begining and ' in the end
	### So that we can send the string within base64 noation
	result = str(figdata_png)[2:-1]
	return render_template('output.html',
		result=result, 
		form=form)

@app.route("/cases", methods=["GET", "POST"])
def cases():
	return basicPlotter("data/MexicoCases2015-2017.csv")

@app.route("/searches", methods=["GET", "POST"])
def searches():
	return basicPlotter("data/MexicoSearches2015-2017.csv")

@app.route("/scatterplot", methods=["GET", "POST"])
def scatterplot():
	import matplotlib.pyplot as plt
	from io import BytesIO
	import base64
	from pandas.plotting import scatter_matrix
	#Set up Form
	form = ScatterForm()

	#Check if POST
	year = (form.year.data and str(form.year.data)) or "ALL"
	state = form.statesCheckbox.data
	#Getting plot
	scatterplot = getScatterPlot(year, state)
	scatter_matrix(scatterplot)

	### Saving plot to disk in png format
	# plt.savefig('img/test_plot.png')

	### Rendering Plot in Html
	figfile = BytesIO()
	plt.savefig(figfile, format='png')
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	result = figdata_png
	### Remove b' from begining and ' in the end
	### So that we can send the string within base64 noation
	result = str(figdata_png)[2:-1]
	return render_template('scatter.html',
		result=result, 
		form=form)

@app.route("/scatter", methods=["GET", "POST"])
def scatter():
	import matplotlib.pyplot as plt
	from io import BytesIO
	import base64
	from pandas.plotting import scatter_matrix
	#Set up Form
	form = ScatterForm()

	#Check if POST
	year = (form.year.data and str(form.year.data)) or "ALL"
	state = form.statesCheckbox.data
	#Getting plot
	scatterplot = getScatterPlot(year, state)
	scatter_matrix(scatterplot)

	figfile = BytesIO()
	plt.savefig(figfile, format='png')
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	result = figdata_png
	### Remove b' from begining and ' in the end
	### So that we can send the string within base64 noation
	result = str(figdata_png)[2:-1]
	return render_template('pages/scatterplot.html',
		result=result, 
		form=form)

@app.route("/map2016", methods=["GET", "POST"])
def map2016():
	return render_template("pages/map2016.html")

@app.route("/map2017", methods=["GET", "POST"])
def map2017():
	return render_template("pages/map2017.html")

@app.route("/map2018", methods=["GET", "POST"])
def map2018():
	return render_template("pages/map2018.html")

@app.route("/brazil2016", methods=["GET"])
def brazil2016():
	brazilCasesFile = "\"/static/js/brazilCases2016.js\""
	name = "Brazil 2016 Cases"
	return render_template("pages/brasilCases.html",
		brazilCasesFile = brazilCasesFile,
		name = name)

@app.route("/brazil2017", methods=["GET"])
def brazil2017():
	brazilCasesFile = "\"/static/js/brazilCases2017.js\""
	name = "Brazil 2017 Cases"
	return render_template("pages/brasilCases.html", 
		brazilCasesFile = brazilCasesFile,
		name = name)

@app.route("/team", methods=["GET"])
def team():
	return render_template("pages/team.html")

@app.route("/licence", methods=["GET"])
def licence():
	return render_template("pages/licence.html")

if __name__ == "__main__":
	app.run()
