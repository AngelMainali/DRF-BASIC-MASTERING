#from django.shortcuts import render
#from django.http import JsonResponse
from rest_framework.response import Response
from .serializers import StudentSerializer , EmployeeSerializer
from students.models import Student
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from employee.models import Employee



"""
manual serializers

def StudentsView(request):
    students_obj= Student.objects.all()
    print(students_obj)
    students_list= list(students_obj.values()) #manual serializers
    print(students_list)
    return JsonResponse(students_list, safe=False)
"""

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
   

class EmployeeView(APIView):
    def get(self, request):
        employees_obj = Employee.objects.all()
        serializer = EmployeeSerializer(employees_obj, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EmployeeDetailView(APIView):
    def get(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        
        employee.delete()
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)






