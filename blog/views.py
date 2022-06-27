from django.contrib.auth.models import User
from rest_framework import mixins, viewsets
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Lecturer, Semester, Course, Class, Student, StudentEnrollment
from blog.permissions import IsLecturerOrReadOnly
from blog.serializers import LecturerSerializer, SemesterSerializer, CourseSerializer, ClassSerializer, \
    StudentSerializer, StudentEnrollmentSerializer, UserSerializer


def Index(request):
    return (HttpResponse("Hello World"))


# class LecturerList(APIView):
#     def get(self, request):
#         lecturers = Lecturer.objects.all()
#         serializer = LecturerSerializer(lecturers, many=True)
#         return Response(serializer.data)
#
#     def post(selfself, request):
#         serializer = LecturerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class LecturerDetails(APIView):
#     def get_object(self, staff_id):
#         try:
#             return Lecturer.objects.get(staff_id=staff_id)
#         except Lecturer.objects.get(staff_id=staff_id).DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, staff_id):
#         lecturer = self.get_object(staff_id)
#         serializer = LecturerSerializer(lecturer)
#         return Response(serializer.data)
#
#     def put(self, request, staff_id):
#         lecturer = self.get_object(staff_id)
#         serializer = LecturerSerializer(lecturer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, staff_id):
#         lecturer = self.get_object(staff_id)
#         lecturer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class SemesterList(APIView):
#     def get(self, request):
#         semester = Semester.objects.all()
#         serializer = SemesterSerializer(semester, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = SemesterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class SemesterDetails(APIView):
#     def get_object(self, sem_id):
#         try:
#             return Semester.objects.get(staff_id=sem_id)
#         except Semester.objects.get(staff_id=sem_id).DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, sem_id):
#         semester = self.get_object(sem_id)
#         serializer = SemesterSerializer(semester)
#         return Response(serializer.data)
#
#     def put(self, request, sem_id):
#         semester = self.get_object(sem_id)
#         serializer = SemesterSerializer(semester, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, sem_id):
#         semester = self.get_object(sem_id)
#         semester.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class CourseList(APIView):
#     def get(self, request):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class CourseDetails(APIView):
#     def get_object(self, staff_id):
#         try:
#             return Course.objects.get(staff_id=staff_id)
#         except Course.objects.get(staff_id=staff_id).DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, staff_id):
#         course = self.get_object(staff_id)
#         serializer = CourseSerializer(course)
#         return Response(serializer.data)
#
#     def put(self, request, staff_id):
#         course = self.get_object(staff_id)
#         serializer = CourseSerializer(course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, staff_id):
#         course = self.get_object(staff_id)
#         course.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class ClassList(APIView):
#     def get(self, request):
#         class_1 = Class.objects.all()
#         serializer = ClassSerializer(class_1, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = ClassSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class ClassDetails(APIView):
#     def get_object(self, staff_id):
#         try:
#             return Class.objects.get(staff_id=staff_id)
#         except Class.objects.get(staff_id=staff_id).DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, staff_id):
#         class_1 = self.get_object(staff_id)
#         serializer = ClassSerializer(class_1)
#         return Response(serializer.data)
#
#     def put(self, request, staff_id):
#         class_1 = self.get_object(staff_id)
#         serializer = ClassSerializer(class_1, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, staff_id):
#         class_1 = self.get_object(staff_id)
#         class_1.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class StudentDetails(APIView):
#     def get_object(self, student_id):
#         try:
#             return Student.objects.get(student_id=student_id)
#         except Student.objects.get(student_id=student_id).DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, student_id):
#         student = self.get_object(student_id)
#         serializer = StudentSerializer(student)
#         return Response(serializer.data)
#
#     def put(self, request, student_id):
#         student = self.get_object(student_id)
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, student_id):
#         student = self.get_object(student_id)
#         student.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# class StudentList(APIView):
#     def get(self, request):
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class StudentEnrollmentList(APIView):
#     def get(self, request):
#         studentEnrollment = StudentEnrollment.objects.all()
#         serializer = StudentEnrollmentSerializer(studentEnrollment, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = StudentEnrollmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class StudentEnrollmentDetails(APIView):
#     def get_object(self, student_id):
#         try:
#             return StudentEnrollment.objects.get(student_id=student_id)
#         except StudentEnrollment.objects.get(student_id=student_id).DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, student_id):
#         student = self.get_object(student_id)
#         serializer = StudentEnrollmentSerializer(student)
#         return Response(serializer.data)
#
#     def put(self, request, student_id):
#         studentEnrollment = self.get_object(student_id)
#         serializer = StudentEnrollmentSerializer(studentEnrollment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, student_id):
#         studentEnrollment = self.get_object(student_id)
#         studentEnrollment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class LecturerList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Lecturer.objects.all()
#     serializer_class = LecturerSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class LecturerDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin):
#     queryset = Lecturer.objects.all()
#     serializer_class = LecturerSerializer
#     lookup_field = 'id'
#
#     def get(self, request, id):
#         return self.retrieve(request, id=id)
#
#     def put(self, request, id):
#         return self.update(request, id=id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)
#
#
# class SemesterList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Semester.objects.all()
#     serializer_class = SemesterSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class SemesterDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                       mixins.DestroyModelMixin):
#     queryset = Semester.objects.all()
#     serializer_class = SemesterSerializer
#     lookup_field = 'id'
#
#     def get(self, request, id):
#         return self.retrieve(request, id=id)
#
#     def put(self, request, id):
#         return self.update(request, id=id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)
#
#
# class CourseList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class CourseDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer
#     lookup_field = 'id'
#
#     def get(self, request, id):
#         return self.retrieve(request, id=id)
#
#     def put(self, request, id):
#         return self.update(request, id=id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)
#
#
# class ClassList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Class.objects.all()
#     serializer_class = ClassSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class ClassDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin):
#     queryset = Class.objects.all()
#     serializer_class = ClassSerializer
#     lookup_field = 'id'
#
#     def get(self, request, id):
#         return self.retrieve(request, id=id)
#
#     def put(self, request, id):
#         return self.update(request, id=id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)
#
#
# class StudentList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class StudentDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#     lookup_field = 'id'
#
#     def get(self, request, id):
#         return self.retrieve(request, id=id)
#
#     def put(self, request, id):
#         return self.update(request, id=id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)
#
#
# class StudentEnrollmentList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = StudentEnrollment.objects.all()
#     serializer_class = StudentEnrollmentSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class StudentEnrollmentDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                                mixins.DestroyModelMixin):
#     queryset = StudentEnrollment.objects.all()
#     serializer_class = StudentEnrollmentSerializer
#     lookup_field = 'id'
#
#     def get(self, request, id):
#         return self.retrieve(request, id=id)
#
#     def put(self, request, id):
#         return self.update(request, id=id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id)


# class LecturerViewset(viewsets.ViewSet):
#     def list(self,request):
#         lecturers = Lecturer.objects.all()
#         serializer = LecturerSerializer(lecturers, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = LecturerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self,request, pk=None):
#         queryset= Lecturer.objects.all()
#         lecturers = get_object_or_404(queryset, pk=pk)
#         serializer = LecturerSerializer(lecturers)
#         return  Response(serializer.data, status= status.HTTP_200_OK)
#
#     def update(self, request, pk= None):
#         lecturers = Lecturer.objects.get(pk=pk)
#         serializer = LecturerSerializer(Lecturer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self,request, pk = None):
#         lecturers = Lecturer.objects.get(pk=pk)
#         lecturers.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
#
# class SemesterViewset(viewsets.ViewSet):
#     def list(self,request):
#         semester = Semester.objects.all()
#         serializer = LecturerSerializer(semester, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = SemesterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self,request, pk=None):
#         queryset= Semester.objects.all()
#         semester = get_object_or_404(queryset, pk=pk)
#         serializer = SemesterSerializer(semester)
#         return  Response(serializer.data, status= status.HTTP_200_OK)
#
#     def update(self, request, pk= None):
#         semester = Semester.objects.get(pk=pk)
#         serializer = SemesterSerializer(Semester, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self,request, pk = None):
#         semester = Semester.objects.get(pk=pk)
#         semester.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
#
# class CourseViewset(viewsets.ViewSet):
#     def list(self,request):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = CourseSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self,request, pk=None):
#         queryset= Course.objects.all()
#         course = get_object_or_404(queryset, pk=pk)
#         serializer = CourseSerializer(course)
#         return  Response(serializer.data, status= status.HTTP_200_OK)
#
#     def update(self, request, pk= None):
#         course = Course.objects.get(pk=pk)
#         serializer = CourseSerializer(Course, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self,request, pk = None):
#         course = Course.objects.get(pk=pk)
#         course.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
#
#
# class ClassViewset(viewsets.ViewSet):
#     def list(self,request):
#         class_1 = Class.objects.all()
#         serializer = ClassSerializer(class_1, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ClassSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self,request, pk=None):
#         queryset= Class.objects.all()
#         class_1 = get_object_or_404(queryset, pk=pk)
#         serializer = ClassSerializer(class_1)
#         return  Response(serializer.data, status= status.HTTP_200_OK)
#
#     def update(self, request, pk= None):
#         class_1 = Class.objects.get(pk=pk)
#         serializer = ClassSerializer(Class, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self,request, pk = None):
#         class_1 = Course.objects.get(pk=pk)
#         class_1.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
#
#
# class StudentViewset(viewsets.ViewSet):
#     def list(self,request):
#         student = Student.objects.all()
#         serializer = StudentSerializer(student, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self,request, pk=None):
#         queryset= Student.objects.all()
#         student = get_object_or_404(queryset, pk=pk)
#         serializer = StudentSerializer(student)
#         return  Response(serializer.data, status= status.HTTP_200_OK)
#
#     def update(self, request, pk= None):
#         student = Student.objects.get(pk=pk)
#         serializer = StudentSerializer(Student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self,request, pk = None):
#         student = Student.objects.get(pk=pk)
#         student.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)
#
#
# class StudentEnrollmentViewset(viewsets.ViewSet):
#     def list(self,request):
#         studentEnrollment = StudentEnrollment.objects.all()
#         serializer = StudentEnrollmentSerializer(studentEnrollment, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = StudentEnrollmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self,request, pk=None):
#         queryset= StudentEnrollment.objects.all()
#         studentEnrollment = get_object_or_404(queryset, pk=pk)
#         serializer = StudentEnrollmentSerializer(studentEnrollment)
#         return  Response(serializer.data, status= status.HTTP_200_OK)
#
#     def update(self, request, pk= None):
#         studentEnrollment = StudentEnrollment.objects.get(pk=pk)
#         serializer = StudentEnrollmentSerializer(StudentEnrollment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self,request, pk = None):
#         studentEnrollment = Course.objects.get(pk=pk)
#         studentEnrollment.delete()
#         return Response(status= status.HTTP_204_NO_CONTENT)


class LecturerViewset(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = [IsAuthenticated, IsLecturerOrReadOnly]



class SemesterViewset(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer


class CourseViewset(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ClassViewset(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentEnrollmentViewset(viewsets.ModelViewSet):
    queryset = StudentEnrollment.objects.all()
    serializer_class = StudentEnrollmentSerializer


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer