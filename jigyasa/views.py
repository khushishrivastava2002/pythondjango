import openai
from django.shortcuts import render, redirect
from jigyasa.models import Contact
import speech_recognition as sr
import pyttsx3


# Set up the OpenAI API client
openai.api_key = "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"

def index(request):
    return render(request,'index.html')

def save(request):
    if request.method=='POST':
        name=request.POST.get('name')
        surname=request.POST.get('surname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        en=Contact(name=name,surname=surname,email=email,phone=phone)
        en.save()
    return render(request,'index.html')
        
def search_by_text(request):
    if request.method=="POST":
        if request.POST.get('prompt')!=None and request.POST.get('prompt')!='' :
            prompt = request.POST.get('prompt')
            model_engine = "text-davinci-003"
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            # extracting useful part of response
            response = completion.choices[0].text
        else:
            prompt=None
        return redirect(f"/{prompt}_text_search_result/")  
    return render(request,"text_search.html")

def search_by_text_result(request,prompt):
    if request.method=="POST":
        if request.POST.get('prompt')!=None and request.POST.get('prompt')!='' :
            prompt = request.POST.get('prompt')
            model_engine = "text-davinci-003"
            # Generate a response
            completion = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
            )
            response = completion.choices[0].text
            context = {
                 "response":response,
                 "prompt":prompt,
                  }
        else:
            aa=None
        return redirect(f"/{prompt}_text_search_result/")
    else:
        pass
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    response = completion.choices[0].text
    context = {
        "response":response,
        }
    return render(request, 'text_search_result.html',context)