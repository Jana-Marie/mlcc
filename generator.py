#!/usr/bin/python3
# -*- coding: utf-8 -*-

from jinja2 import Template, Environment, FileSystemLoader
import os
import shutil
from pathlib import Path

schemes = [
	{	"name": "dull neons", 
		"color": ["#007d64", "#008234", "#308500", "#7a8100", "#b67400", "#eb5b04", "#e33758", "#b64084", "#764f91", "#3e517d", "#2f4858"],
	},
	{	"name": "pink-purple", 
		"color": ["#0c1627", "#2a2c5d", "#e73d82", "#fae7ec"],
	},
	{	"name": "purplecream", 
		"color": ["#0f0d0a", "#3d225c", "#e56775", "#f7ddcb"],
	},
	{	"name": "cold reds", 
		"color": ["#1a171e", "#4c479a", "#801225", "#cb3367", "#d0c5bd"],
	},
	{	"name": "complementary accents", 
		"color": ["#0f0611", "#1d7287", "#c5170f", "#ddd0c4"],
	},
	{	"name": "creamy mints", 
		"color": ["#221b26", "#1d4141", "#4cbaaa", "#f2dcb0"],
	},
	{	"name": "happy autumn", 
		"color": ["#081f30", "#0e6b88", "#c74505", "#ffad5d", "#fadbbf"],
	},
	{	"name": "nightshade", 
		"color": ["#06061b", "#0f0c21", "#180d24", "#23102c", "#fde5d1"],
	},
	{	"name": "mossy mushroom", 
		"color": ["#071615", "#0c262c", "#3e2d3f", "#7b3f70", "#ffd4b6"],
	},
	{	"name": "toxic purple", 
		"color": ["#2b2747", "#7338bd", "#baaa44", "#514e59", "#fafdf7"],
	},
	{	"name": "dull accents", 
		"color": ["#2f333a", "#3c6f71", "#fd6b70", "#d9d9d9"],
	},
	{	"name": "toned accents", 
		"color": ["#2f333a", "#005753", "#fd6b70", "#d9d9d9"],
	},
	{	"name": "plumbee", 
		"color": ["#0a0b0c", "#912d57", "#f6d91c", "#d5b2d5"],
	},
	{	"name": "landingpage", 
		"color": ["#030303", "#960200", "#f8f7f9"],
	},
	{	"name": "dispossessed", 
		"color": ["#2f333a", "#3c6f71", "#d9d9d9", "#eb6f92"],
	},
	{	"name": "shark", 
		"color": ["#1b1a22", "#3a5769", "#457f8d", "#dcdcdc", "#f0c1b7"],
	},
]

def svgpathgen(s, idx, sumcolors):
	return str('<path fill="' + s + '" d="M0 0h' + str(100-(100/(sumcolors)*idx)) + 'v100H0z"/>')

def annotationgen(s, idx, sumcolors):
	return str('<div class="col annotation-color" style="--col: ' + s + '">' + s + '<br>' + str(tuple(int(s.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))) + '</div>')


def generate_folder_structure():
	os.makedirs("www", exist_ok = True)

def copy_statics():
	shutil.copy2('static/style.css', 'www')

def generate_and_copy_index():
	env = Environment(loader=FileSystemLoader('static/'))
	env.filters["svgpathgen"] = svgpathgen
	env.filters["annotationgen"] = annotationgen

	# index
	index = env.get_template('index.html')
	f = open("www/index.html", "w")
	f.write(index.render(schemes=schemes))
	f.close()

if __name__ == "__main__":
	generate_folder_structure()
	copy_statics()
	generate_and_copy_index()
