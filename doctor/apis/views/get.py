from rest_framework import status, decorators, permissions
from rest_framework.response import Response
from ..serializers import Department, DepartmentSerializer, DoctorSerializer

@decorators.api_view(['GET'])
def GetAllDepartments (request) : 
    try : 
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as error : 
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@decorators.api_view(['GET'])
@decorators.permission_classes([permissions.IsAuthenticated])
def DoctorProfile (request) : 
    try : 
        doctor = request.user
        serializer = DoctorSerializer(doctor)
        serializer.has_counter = True
        serializer.has_clients = True
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as error : 
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)