import csv
import json
import sys

if(len(sys.argv)!=2):
	print("usage: python3 c2j.py <filename.csv>")
	exit(0)


def formjson(csvFilePath):
	data = {}
	lk = []
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		for rows in csvReader:
			key = rows['company']
			#print(rows)
			lk.append(key)
		f = list(set(lk))
		a = {k: [] for k in f}
	with open(csvFilePath, encoding='utf-8') as csvf:
		csvReader = csv.DictReader(csvf)
		for rows in csvReader:
			key = rows['company']
			if(rows['company']==key):
				a[key].append(rows)
		print(json.dumps(a,indent=4))
formjson(csvFilePath(sys.argv[1])
