from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MemoSerializer
from .models import Memo

class MemoViewSet(viewsets.ModelViewSet):
    serializer_class = MemoSerializer
    queryset = Memo.objects.all()