from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework.response import Response
from .serializers import People,PeopleSerializer



@api_view(["GET","POST"])
def people_view(request):
    people = People("Tom",19,"M")
    serializer = PeopleSerializer(people)
    return Response({"message":serializer.data},200)

class FakeAPIView(APIView):
    
    def get(self,request, *args, **kwargs):
        people = People("Tom",19,"M")
        serializer = PeopleSerializer(people)

        
        return Response({"message":serializer.data},200)
    
    def post(self,request, *args, **kwargs):
        data = request.data
        people = PeopleSerializer(data)
        people.save()
        people.update()
        return Response({"message":data},201)
    
    # def update(self,request, *args, **kwargs):
    #     data = request.data

    #     return Response({"message":data},200)
    
    # def delete(self,request, *args, **kwargs):
    #     return Response({"message":"Data deleted"},204)
    
    # def retrieve(self,request, *args, **kwargs):
    #     return Response({"message":"Data retrieved"},200)