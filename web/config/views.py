from django.shortcuts import render
from dotenv import load_dotenv
import os

load_dotenv()

KAKAO_API_KEY = os.getenv('KAKAO_API_KEY')

def base(request):

    context = {
        'KAKAO_Key' : KAKAO_API_KEY
    }
    return render(request, 'base.html', context)