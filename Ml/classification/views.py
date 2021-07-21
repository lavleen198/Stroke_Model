from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np
import joblib

# Create your views here.
logistics_model=joblib.load('./models/strokemodel.pkl')
def index(request):
    return render(request,'form_log.html')
def result(request):
    if request.method=='POST':
        temp={}
        temp['Gender']=request.POST.get('Gender')
        temp['Age']=request.POST.get('Age')
        temp['HyperTension']=request.POST.get('HyperTension')
        temp['HeartDisease']=request.POST.get('HeartDisease')
        temp['EverMarried']=request.POST.get('EverMarried')
        temp['Residence']=request.POST.get('Residence')
        temp['AvgGlucose']=request.POST.get('AvgGlucose')
        temp['BMI']=request.POST.get('BMI')
    testdata=pd.DataFrame({'x':temp}).transpose()
    output=logistics_model.predict(testdata)[0]
    if output==1:
        output='There is a high Probability of Stroke'
    else:
        output:'There is a low Probability of Stroke'
    context={'output':output}
    return render(request,'form_log.html',context)
