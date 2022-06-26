from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from blog.views import Index, LecturerViewset, SemesterViewset, CourseViewset, ClassViewset, StudentViewset, \
    StudentEnrollmentViewset, UserViewset

# , LecturerList, LecturerDetails, SemesterList, SemesterDetails, CourseList, CourseDetails,ClassList, ClassDetails, StudentList, StudentDetails, StudentEnrollmentList, StudentEnrollmentDetails

router = DefaultRouter()
router.register('lecturer', LecturerViewset, "lecturer")
router.register('semester', SemesterViewset, "semester")
router.register('course', CourseViewset, "course")
router.register('class', ClassViewset, "class")
router.register('student', StudentViewset, "student")
router.register('studentEnrollment', StudentEnrollmentViewset, "studentEnrollment")
router.register('user', UserViewset, 'user')
urlpatterns = [
    path('', Index, name="home"),
    # path('lecturer', LecturerList.as_view(), name="lecturers"),
    path('api/', include(router.urls)),
    path('auth/', obtain_auth_token)
]
