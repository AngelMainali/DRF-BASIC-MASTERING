#from django.shortcuts import render
#from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import StudentSerializer , EmployeeSerializer
from students.models import Student
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from employee.models import Employee
from rest_framework import mixins, generics, viewsets
from blogs.models import Blog,Comment
from blogs.serializers import BlogSerializer,CommentSerializer
from .paginations import CustomPagination
from employee.filters import EmployeeFilter
from rest_framework.filters import SearchFilter, OrderingFilter





# manual serializers

# def StudentsView(request):
#     students_obj= Student.objects.all()
#     print(students_obj)
#     students_list= list(students_obj.values()) #manual serializers
#     print(students_list)
#     return JsonResponse(students_list, safe=False)


#functional based view

@api_view(['GET', 'POST'])
def StudentsView(request):
    if request.method == "GET":
        students_obj = Student.objects.all()
        serializer = StudentSerializer(students_obj, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = StudentSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
       
@api_view(['GET', 'PUT', 'DELETE'])
def StudentsDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)  
    
    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        student.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)       
   

# class EmployeeView(APIView):
#     def get(self, request):
#         employees_obj = Employee.objects.all()
#         serializer = EmployeeSerializer(employees_obj, many=True)
#         return Response(serializer.data ,status=status.HTTP_200_OK)
    
#     def post(self,request):
#         serializer = EmployeeSerializer(data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class EmployeeDetailView(APIView):
#     def get(self, request, pk):
#         try:
#             employee = Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         try:
#             employee = Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         try:
#             employee = Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         employee.delete()
#         return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)



# Mixins

# class EmployeeView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    
# class EmployeeDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer  

#     def get(self, request, pk):
#         return self.retrieve(request, pk)
    
#     def put(self, request, pk):
#         return self.update(request, pk)
    
#     def delete(self, request, pk):
#         return self.destroy(request, pk)



# Generics
# class EmployeeView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer 

# class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field='pk'



# viewset.ViewSet

# class EmployeeViewSet(viewsets.ViewSet):
#     def list(self,request):
#         queryset = Employee.objects.all()
#         serializer = EmployeeSerializer(queryset, many=True)
#         return Response(serializer.data)
   
#     def create(self,request):
#         serializer = EmployeeSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk):
#         queryset = Employee.objects.all()
#         employee = Employee.objects.get(pk=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)
    
#     def update(self,request):
#         employee = Employee.objects.get(pk=pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = Employee.objects.get(pk=pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# model viewset

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination
    #filterset_fields= ['designation']
    filterset_class = EmployeeFilter


class BlogView(generics.ListCreateAPIView):
    queryset= Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['blog_title','blog_body']
    ordering_fields=['id', 'blog_title']
    
      


class CommentView(generics.ListCreateAPIView):
    queryset= Comment.objects.all()
    serializer_class = CommentSerializer


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer 

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer         