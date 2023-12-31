from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from .models import Users, Roles
from .serializers import UsersSerializer, RolesSerializer
from rest_framework import generics
from rest_framework.views import APIView

# Create your views here.
# TODO: add a view (Actually not allowed for lab #2)
def index(request):
    return HttpResponse("<h1> Lab #2: A simple CRUD with HTTP. <br> Hello World!</h1>")

class UserListCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    #function to manage the GET request if the queryset is empty
    def list(self, request, *args, **kwargs):
        users = self.get_queryset()
        response = super().list(request, *args, **kwargs)
        if not users.exists():
            response = JsonResponse(status=204, data={})
        return response
    
class UserByNameView(generics.ListAPIView):
    serializer_class = UsersSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None) # Obtiene el parámetro 'name' de la solicitud GET
        #TODO: add a limit to the queryset
        #limit = self.request.query_params.get('nums', None) # Obtiene el parámetro 'nums' de la solicitud GET
        response = Users.objects.none()         # Si no se proporcionó el parámetro 'name', devuelve un queryset vacío
        if name is not None:# Realiza una búsqueda por nombre (puede personalizar la búsqueda según necesidades)
            response = Users.objects.filter(first_name__icontains=name)
        return response

class CreateMultipleUsers(APIView):
    def post(self, request, format=None):
        users_data = request.data  # Aquí se espera una lista de objetos JSON

        if not isinstance(users_data, list):
            return Response({"non_field_errors": ["Se esperaba una lista de objetos JSON."]}, status=status.HTTP_400_BAD_REQUEST)

        users_created = []
        response = None #TODO: manage response
        for user_data in users_data:
            serializer = UsersSerializer(data=user_data)
            if serializer.is_valid():
                response = Response(users_created, status=status.HTTP_201_CREATED)
                serializer.save()
                users_created.append(serializer.data)

        return response

#PUT requests
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class RoleListCreateView(generics.ListCreateAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer
    
    #function to manage the GET request if the queryset is empty
    def list(self, request, *args, **kwargs):
        roles = self.get_queryset()
        response = super().list(request, *args, **kwargs)
        if not roles.exists():
            response = JsonResponse(status=204, data={})
        return response
    
class CreateMultipleRoles(APIView):
    def post(self, request, format=None):
        roles_data = request.data  # Aquí se espera una lista de objetos JSON

        if not isinstance(roles_data, list):
            return Response({"non_field_errors": ["Se esperaba una lista de objetos JSON."]}, status=status.HTTP_400_BAD_REQUEST)

        roles_created = []

        for role_data in roles_data:
            serializer = RolesSerializer(data=role_data)
            if serializer.is_valid():
                serializer.save()
                roles_created.append(serializer.data)

        return Response(roles_created, status=status.HTTP_201_CREATED)

#PUT requests
class RoleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializer