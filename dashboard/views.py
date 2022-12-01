from django.shortcuts import render
import requests
import json
import cgi
from django.http import HttpResponse
def getNutrients(foodSelection) :
    
    r = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?query=' + foodSelection + '&dataType=&pageSize=1&sortBy=dataType.keyword&sortOrder=desc&api_key=qYgvm24Uuid52ZmJ6cM3wfhgbeWH33cYhssaUW5O')
    y = json.loads(r.text)
    nutrients = ['Protein', 'Sodium, Na', 'Potassium, K', 'Water', 'Phosphorus, P']
    for x in y['foods'] :
        
        values = [0, 0, 0, 0, 0]

        for nutrient in x['foodNutrients']:

            if nutrient['nutrientName'] in nutrients:
                
                if nutrient['nutrientName'] == 'Protein':
                    values[0] = f"{nutrient['value']}"

                if nutrient['nutrientName'] == 'Sodium, Na':
                    values[1] = f"{nutrient['value']}" 

                if nutrient['nutrientName'] == 'Potassium, K':
                    values[2] = f"{nutrient['value']}"

                if nutrient['nutrientName'] == 'Water':      
                    values[3] = f"{nutrient['value']}"

                if nutrient['nutrientName'] == 'Phosphorus, P': 
                    values[4] = f"{nutrient['value']}"
            
    values2 = []

    for i in values:
        values2.append(float(i))
    
    return values2


#{{graphData}}
def index(request):
    #data = getNutrients('Whole Milk')
   # context = {
       # 'graphData': data
 
    #}
    return render(request, 'dashboard/index.html')




def searchPageView(request):
    return render(request, 'dashboard/index.html')


def resultPageView(request):
    if request.method == 'POST':
        parameter = request.POST.get('searchbox')
        searchResult = getFoodList(parameter)

    context = {
        'search' : searchResult
    }
    #return HttpResponse("Hey " + searchs)
    return render(request, 'dashboard/result.html', context)


def getFoodList(foodSelection) :
    r = requests.get('https://api.nal.usda.gov/fdc/v1/foods/search?query=' + foodSelection + '&dataType=&pageSize=6&sortBy=dataType.keyword&sortOrder=asc&api_key=qYgvm24Uuid52ZmJ6cM3wfhgbeWH33cYhssaUW5O')
    y = json.loads(r.text)

    brand = []
    for x in y['foods'] :
        
        des = x['description']
        ss = x['servingSize']
        unit = x['servingSizeUnit']
        bra = x['brandName']
        
       # own = x['packageWeight']

        brand.append([des, bra, ss, unit])
    
    return brand