from django.shortcuts import render
from django.http import JsonResponse
from .models import UserModel,Student
from .serializers import UserSerializer,StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import SAFE_METHODS,BasePermission,IsAdminUser,DjangoModelPermissionsOrAnonReadOnly,IsAuthenticatedOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import viewsets


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UsSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UserViewset(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def API(request, format=None):
    return Response({
    'create':reverse('create',request=request,format=format),
    'view':reverse('view',request=request,format=format),
    # 'update':reverse('crud',request=request,format=None)
    })

class UserPermission(BasePermission):
    message="Restricted page"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.name == request.user




#Using Mixin
class UserMixins(mixins.ListModelMixin,generics.GenericAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset=UserModel.objects.all()
    serializer_class = UserSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

class CrudMixins(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)


class MixinCreate(mixins.CreateModelMixin,generics.GenericAPIView,UserPermission):
    permission_classes = [UserPermission]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)




#update,Delete,View in one class and Authentication and permission
class Details(generics.RetrieveUpdateDestroyAPIView, DjangoModelPermissionsOrAnonReadOnly):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


#class based View
class UserBio(APIView):
    def get(self,request):
        user=UserModel.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserBioUpdate(APIView):
    def get_object(self,id):
        try:
            return UserModel.objects.get(id=id)
        except UserModel.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id):
        user=self.get_object(id=id)
        serializer=UserSerializer(user)
        return Response(serializer.data)

    def put(self,request,id):
        user=self.get_object(id)
        serializer=UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        user=self.get_object(id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




#Function based View

#         serializer=UserSerializer(user,many=True)
#         return Response({'user':serializer.data})
#     if request.method=='POST':
#         serializer=UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','PUT','DELETE'])
# def UserDetail(request,id,format=None):
#     try:
#         user=UserModel.objects.get(pk=id)
#     except UserModel.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if  request.method=="GET":
#         serializer=UserSerializer(user)
#         return Response(serializer.data)
#     elif request.method=="PUT":
#         serializer = UserSerializer(user,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method=="DELETE":
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#
# @api_view(['GET'])
# def User_View(request,id):
#     user=UserModel.objects.get(id=id)
#     serializer=UserSerializer(user)
#     return Response(serializer.data)
#
# @api_view(['POST'])
# def User_create(request):
#     user = UserModel.objects.all()
#     serializer = UserSerializer(user, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#
# @api_view(['POST'])
# def User_Update(request,id):
#     user=UserModel.objects.get(id=id)
#     serializer=UserSerializer(instance=user,data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#


