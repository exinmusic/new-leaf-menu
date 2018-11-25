from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models
import json
import urllib
import re

def index(request):
	return render(request, 'menu/index.html')

def json_menu(request):
	splitmark = '__NEXT_DATA__ = '
	cutout = ' module={}'

	pattern = re.compile(cutout)
	pattern2 = re.compile(splitmark)

	htmlfile = urllib.request.urlopen('https://www.leafly.com/dispensary-info/canna-connection/menu')
	htmltext = htmlfile.read().decode('utf-8')

	splittext = re.split(pattern2,htmltext)
	splittext = re.split(pattern,splittext[1])

	leafly_json=splittext[0]
	leafly_json=json.loads(leafly_json)

	hybrids = []
	indicas = []
	sativas = []
	nopheno = []

	flower_data = leafly_json['props']['menu']

	for each_flower in flower_data:
		if 'strainCategory' in each_flower:
			if each_flower['strainCategory'] == 'Hybrid':
				hybrids.append([each_flower['name'], each_flower['thcContent'], each_flower['cbdContent']])
			elif each_flower['strainCategory'] == 'Indica':
				indicas.append([each_flower['name'], each_flower['thcContent'], each_flower['cbdContent']])
			elif each_flower['strainCategory'] == 'Sativa':
				sativas.append([each_flower['name'], each_flower['thcContent'], each_flower['cbdContent']])
			else:
				nopheno.append([each_flower['name'], each_flower['thcContent'], each_flower['cbdContent']])

	sOut = []
	hOut = []
	iOut = []
	nOut = []

	strains_in_db = models.Strain.objects.all()

	for s in sativas:
		test = strains_in_db.filter(name=s[0])
		if test:
			s.append(test.values()[0]['cbd'])
			s.append(test.values()[0]['favorite'])
			if test.values()[0]['pheno'] == 'indica':
				iOut.append(s)

			elif test.values()[0]['pheno'] == 'hybrid':
				hOut.append(s)

			else:
				sOut.append(s)
		else:
			s.append(False); s.append(False)
			sOut.append(s)

	for s in hybrids:
		test = strains_in_db.filter(name=s[0])
		if test:
			s.append(test.values()[0]['cbd'])
			s.append(test.values()[0]['favorite'])
			if test.values()[0]['pheno'] == 'sativa':
				sOut.append(s)

			elif test.values()[0]['pheno'] == 'indica':
				iOut.append(s)

			else:
				hOut.append(s)
		else:
			s.append(False); s.append(False)
			hOut.append(s)

	for s in indicas:
		test = strains_in_db.filter(name=s[0])
		if test:
			s.append(test.values()[0]['cbd'])
			s.append(test.values()[0]['favorite'])
			if test.values()[0]['pheno'] == 'sativa':
				sOut.append(s)

			elif test.values()[0]['pheno'] == 'hybrid':
				hOut.append(s)

			else:
				iOut.append(s)
		else:
			s.append(False); s.append(False)
			iOut.append(s)

	for s in nopheno:
		test = strains_in_db.filter(name=s[0])
		if test:
			s.append(test.values()[0]['cbd'])
			s.append(test.values()[0]['favorite'])
			if test.values()[0]['pheno'] == 'sativa':
				sOut.append(s)

			elif test.values()[0]['pheno'] == 'hybrid':
				hOut.append(s)

			elif test.values()[0]['pheno'] == 'indica':
				iOut.append(s)

			else:
				nOut.append(s)
		else:
			s.append(False); s.append(False)
			nOut.append(s)

	scount= len(sOut)
	hcount= len(hOut)
	icount= len(iOut)
	strains = scount + hcount + icount
	return JsonResponse({'sativas':sOut,'hybrids':hOut,'indicas':iOut,'nopheno':nOut,'scount':scount,'hcount':hcount,'icount':icount,'strains':strains})