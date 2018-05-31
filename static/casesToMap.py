import sys
import json
import csv

def readFile(filename):
	dictStates = {}
	with open("{}".format(filename)) as csvFile:
		reader = csv.DictReader(csvFile)
		for row in reader:
			dictStates[row["id"]] = {}
			dictStates[row["id"]]["State"] = row["State"]
			dictStates[row["id"]]["Cases"] = row["Cases"]
	return dictStates

def main():
	if len(sys.argv) != 4:
		print("Usage: casesToMap.py filename.csv source.js output.js")
		exit()

	dictStates = readFile(sys.argv[1])
	print(dictStates)
	template = None
	with open(sys.argv[2], encoding="utf-8") as templateFile:
		template = json.load(templateFile)

	for i in range(len(template["features"])):
		feature = template["features"][i]
		# print(feature["properties"])

		idFeature = str(feature["properties"]["id"])

		template["features"][i]["properties"]["density"] = dictStates[idFeature]["Cases"]

		# print(template["features"][i]["properties"])
	with open(sys.argv[3], "w") as out:
		out.write("mx = \n")
		json.dump(template, out)


if __name__ == '__main__':
	main()