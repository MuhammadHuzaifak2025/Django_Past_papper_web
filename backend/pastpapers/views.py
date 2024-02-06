from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
import requests
from django.http import JsonResponse
import json
from rest_framework import status
from .models import subjects,papers,years 
# Create your views here.
api_view(['GET'])
def index(request,subject_code):
    sub = subjects.objects.filter(sub_code = subject_code).values('sub_name','sub_id')
    arr = []
    for e in sub:
        if sub:
            year = years.objects.filter(sub_id =e.get("sub_id")).values('years_id','years')
            if year:
                for y in year:
                    print(y.get("years"))
                    resp = {
                    'name' : e.get('sub_name'),
                    'year' :   ' ',
                    'mid_1'  :   ' ',
                    'mid_2'  :   ' ',
                    'final'  :   ' ',
                    'lab_mid' :  ' ',
                    'lab_final' :' ',

                }
                    resp['year'] = y.get('years')

                    mid_1 = papers.objects.filter(year_id = y.get("years_id"),is_mid_i = True).values('link')
                    val = mid_1[0]
                    resp['mid_1'] = val.get('link')
                    
                    
                    mid_2 = papers.objects.filter(year_id = y.get("years_id"),is_mid_ii = True).values('link')
                    if mid_2:
                        val = mid_2[0]
                        resp['mid_2'] = val.get('link')
                    
                    
                    final = papers.objects.filter(year_id = y.get("years_id"),is_finals = True).values('link')
                    if final:
                        val = final[0]
                        resp['final'] = val.get('link')
                    
                    
                    lab_mid = papers.objects.filter(year_id = y.get("years_id"),is_lab_mid = True).values('link')
                    if lab_mid:
                        val = lab_mid[0]
                        resp['lab_mid'] = val.get('link')
                    
                    
                    lab_final = papers.objects.filter(year_id = y.get("years_id"),is_lab_finals = True).values('link')
                    if lab_final:
                        val = lab_final[0]
                        resp['lab_final'] = val.get('link')                   
                     
                    arr.append(resp)
    if not arr:
        return JsonResponse({'message': f'No Reult Found'},status=status.HTTP_404_NOT_FOUND)
    else: 
        return JsonResponse({'Response': f'{arr}'},status=status.is_success)