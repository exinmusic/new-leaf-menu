from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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
				hybrids.append((each_flower['name'], each_flower['thcContent'], each_flower['cbdContent']))
			elif each_flower['strainCategory'] == 'Indica':
				indicas.append((each_flower['name'], each_flower['thcContent'], each_flower['cbdContent']))
			elif each_flower['strainCategory'] == 'Sativa':
				sativas.append((each_flower['name'], each_flower['thcContent'], each_flower['cbdContent']))
			else:
				nopheno.append((each_flower['name'], each_flower['thcContent'], each_flower['cbdContent']))

	scount= len(sativas)
	hcount= len(hybrids)
	icount= len(indicas)
	strains = scount + hcount + icount
	return JsonResponse({'sativas':sativas,'hybrids':hybrids,'indicas':indicas,'nopheno':nopheno,'scount':scount,'hcount':hcount,'icount':icount,'strains':strains})