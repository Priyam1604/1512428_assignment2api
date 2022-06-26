from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from blog.models import Lecturer, Class, Semester, Course, Student, StudentEnrollment


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = ['staffID', 'first_name', 'last_name', 'email', 'DOB', 'classLists', 'password']


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['number', 'course', 'lecturer_details']


class SemesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester
        fields = ['year', 'semester']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['code', 'name', 'semesters']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['studentID', 'first_name', 'last_name', 'email', 'DOB', 'password']


class StudentEnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentEnrollment
        fields = ['student_id', 'class_id', 'grade', 'enrolTime', 'gradeTime']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', ]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'groups']

        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }

        }

        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            user.groups.add(1)
            return user
