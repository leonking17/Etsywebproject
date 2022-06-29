from flask import Flask, render_template, flash
from urllib import response
import random
import requests
import json

app = Flask(__name__)
app.secret_key = '06241994'


@app.route('/')
def index():
    flash('Click below for inspiration')
    return render_template("index.html")    
@app.route('/find_color', methods=['POST', 'GET'])
def find_color():

    #getting random hex codes
    r1 = lambda: random.randint(0,255)
    color1 = '#%02X%02X%02X' % (r1(),r1(),r1())

    r2 = lambda: random.randint(0,255)
    color2 ='#%02X%02X%02X' % (r2(),r2(),r2())

    r3 = lambda: random.randint(0,255)
    color3 = '#%02X%02X%02X' % (r3(),r3(),r3())

    #set of random themes to cycle through
    themes = ['minimal', 'nature themed', 'modern', 'pizza themed','industrial','yassify','cheugy','casual', 'theatrical', 'sleek', 'chic', 'magnificent']

    design_themes = themes
    design_theme = random.choice(design_themes)

    correct = design_theme

    #collection of products to cycle through -- all products can be dropshipped
    products = ['t-shirt', 'sweatshirt', 'hoodie', 'long sleeve', 'tank top', 'sportswear piece', 'bottom', 'shoes', 'kids clothing piece', 'skirt/dress', 'swimwear piece', 'baby clothing', 
    'face mask', 'phone case', 'bag', 'pair of socks', 'pair of underwear', 'hat','mouse pad', 'mug', 'bottle/tumbler', 'canvas', 'poster', 'postcard', 'ornament', 'journal/notebook']
    printify_products = products
    printify_product = random.choice(printify_products)

    #final sentence --what will show after pressing the generate button
    vowel = ['a','e','i','o','u','y']

    if design_theme[0] in vowel:
        design_sentence = 'Design an ' +design_theme+ ' ' +printify_product+ ", and make it work with these colors:"
    else:
        design_sentence = 'Design a ' +design_theme+ ' ' +printify_product+ ", and make it work with these colors:"

    correct = printify_product

    final_sentence2 = design_sentence

    flash(final_sentence2)

    #colors section

    #color1
    params = {'hex' : color1}
    response = requests.get('https://www.thecolorapi.com/id?', params=params)
    data = json.loads(response.text)
    data_text = json.dumps(data)

    json_objects = json.loads(data_text)
    color_name1 = json_objects['name']['value']
    color_hex1 = json_objects['name']['closest_named_hex']
    color_img1 = json_objects['image']['bare']
    color_sentence1 = color_name1 +' '+ color_hex1
    #color2 
    params = {'hex' : color2}
    response = requests.get('https://www.thecolorapi.com/id?', params=params)
    data = json.loads(response.text)
    data_text = json.dumps(data)

    json_objects = json.loads(data_text)
    color_name2 = json_objects['name']['value']
    color_hex2 = json_objects['name']['closest_named_hex']
    color_img2 = json_objects['image']['bare']
    color_sentence2 = color_name2 +' '+ color_hex2

    #color3
    params = {'hex' : color3}
    response = requests.get('https://www.thecolorapi.com/id?', params=params)
    data = json.loads(response.text)
    data_text = json.dumps(data)

    json_objects = json.loads(data_text)
    color_name3 = json_objects['name']['value']
    color_hex3 = json_objects['name']['closest_named_hex']
    color_img3 = json_objects['image']['bare']
    color_sentence3 = color_name3 +' '+ color_hex3


    final_color_sentence = color_sentence1 + ' - ' +color_sentence2+ ' - ' +color_sentence3

    final_color_sentence

    return render_template('imgtemp.html', color_img1=color_img1, color_img2=color_img2, color_img3=color_img3, final_color_sentence=final_color_sentence)