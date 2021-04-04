from django.shortcuts import render, get_object_or_404
from .models import Articles, Stopwords
from django.http import HttpResponse


def save_stopwords_to_model(request):
    # with open('/Users/macbook/Desktop/ml_in_business/hw/course_project/ml_models/stopwords.txt', 'r') as f:
    #     stopwords = [i.replace('\n', '') for i in f.readlines()]
    # for word in stopwords:
    #     words = Stopwords.objects.create(word=word)
    #     words.save()
    return HttpResponse('Success')