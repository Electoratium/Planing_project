from . import models
from .serializers import *
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.status import (
	HTTP_500_INTERNAL_SERVER_ERROR,
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_422_UNPROCESSABLE_ENTITY,
	HTTP_204_NO_CONTENT,
	HTTP_201_CREATED,
	HTTP_200_OK
)
from rest_framework import permissions
from rest_framework.response import Response








# class CreateUser(CreateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = UserSerializer
#
#     def create(self, request, *args, **kwargs): # <- here i forgot self
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         token, created = Token.objects.get_or_create(user=serializer.instance)
#         return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)









class CheckTokenView(APIView):
	permission_classes = [permissions.AllowAny]

	def post(self, request, format=None):
		token = request.data['token']
		userByToken = get_object_or_404(Token, key=token)

		response = {
			'userId': userByToken.user.pk,
			'email': userByToken.user.email,
		}
		return Response(response, status=HTTP_200_OK)


# Зачем это нужно если можно чекать токен непосредственно при подгрузке

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def checkToken(request):
# 	userToken = request.data.get("token")
#
# 	userData = get_object_or_404(Token, key=userToken)
#
# 	response = {
# 		# 'userId': userData.user.pk,
# 		'email': userData.user.email,
# 	}
#
# 	return Response(response, status=HTTP_200_OK)


# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((AllowAny,))
# def login(request):
# 	email = request.data.get("email")
# 	password = request.data.get("password")
# 	if email is None or password is None:
		# return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
# 	user = authenticate(email=email, password=password)
# 	if not user:
# 		return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
# 	token, _ = Token.objects.get_or_create(user=user)
#
#
# 	return Response({'token': token.key, 'user_id': user.id}, status=HTTP_200_OK)



# ТУТ ЕЩЕ ПЕРЕДАЕТЬСЯ IS_CHECKED ПОДУМАЙ ЗАЧЕМ ОН НУЖНЕН!?
# class Login(APIView):
# 	permission_classes = [permissions.AllowAny]
# 	def post(self, request, format=None):
# 		print(request.data)
# 		serializer = LoginSerializer(data=request.data)
# 		if serializer.is_valid():
# 			print('ddf')
# 		else:
# 			print('dsfdepigjkdflk')


class LoginView(APIView):
	permission_classes = [permissions.AllowAny]

	def post(self, request, format=None):
		data = request.data

		email = data.get('email', None)
		password = data.get('password', None)

		user = authenticate(email=email, password=password)

		if user is not None:
			if user.is_active:
				token, created = Token.objects.get_or_create(user=user)
				return Response({'token': token.key, 'user_id': user.id},status=HTTP_200_OK)
			else:
				return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)
		else:
			return Response({'error': 'Invalid Credentials'}, status=HTTP_404_NOT_FOUND)


class DayTaskListView(APIView):
	permission_classes = [permissions.AllowAny]

	def get(self, request, format=None):
		user_id = request.GET.get('user_id')
		if not user_id:
			return Response(status=HTTP_422_UNPROCESSABLE_ENTITY)
		user_tasks = models.DayTasks.objects.all().filter(owner__id=user_id).only('taskName', 'expirationTime', 'priority__name')
		serializer = DayTasksSerializer(user_tasks, many=True)


		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = DayTasksSerializer(request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'data':serializer.data}, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DayTaskDetailView(APIView):
	permission_classes = [permissions.AllowAny]

	def get_object(self, pk):
		try:
			return models.DayTasks.objects.get(pk=pk)
		except models.DayTasks.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		task = self.get_object(pk)
		serializer = DayTasksSerializer(task)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		task = self.get_object(pk)
		serializer = DayTasksSerializer(task, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		task = self.get_object(pk)
		task.delete()
		return Response(status=HTTP_204_NO_CONTENT)



class UserList(APIView):
	permission_classes = [permissions.AllowAny]

	def post(self, request, format=None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({'data': serializer.data}, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
