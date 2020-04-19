from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.


#Generic API View and Mixins 

class GenericAPIView (generics.GenericAPIView, mixins.ListModelMixin,  mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin, 
mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field='id'

    def get(self,request,id=None):

        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)

    def post(self,request):
        return self.create(request)

    def put(self,request,id=None):
        return self.update(request,id)

    def delete(self,request,id=None):
        return self.destroy(request,id)




print("Hello")


#Class based APIviews 

class ArticleAPIView(APIView):

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        articles = Article.objects.all()
        Serializer = ArticleSerializer(articles, many=True)
        return Response(Serializer.data, status=status.HTTP_200_CREATED)

    def post(self,request):
        Serializer = ArticleSerializer(data=request.data)

        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailApiView(APIView):

    def get_object(self,id):
         try:
           return Article.objects.get(id=id)
            
         except Article.DoesNotExist:
             raise Http404

    def get(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self,request,id):
        article = self.get_object(id)
        serializer = ArticleSerializer(article ,data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#Function Based  View APIs
@api_view(['GET','POST'])
def Article_List(request):

    if request.method == "GET":
        Articles = Article.objects.all()
        Serializer = ArticleSerializer(Articles , many =True)
        return Response(Serializer.data,status=status.HTTP_200_OK)

    elif request.method == "POST":
        Serializer = ArticleSerializer (data= request.data)

        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data , status.HTTP_201_CREATED)

        else:
            return Response(Serializer.errors , status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Article_detail(request,id):
    try :
        articles = Article.objects.get(pk=id)

    except Article.DoesNotExist:
        return HttpResponse (status=404)

    if request.method == "GET":    
        Serializer = ArticleSerializer(articles)
        return Response(Serializer.data , status=status.HTTP_200_OK)

    elif request.method == "PUT":
        Serializer = ArticleSerializer(articles,data=request.data)

        if Serializer.is_valid():
            Serializer.save()
            return Response(Serializer.data , status=status.HTTP_200_OK)
        else :
            return Response(Serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        Article.delete(articles)
        return Response(status = status.HTTP_204_NO_CONTENT)













    


