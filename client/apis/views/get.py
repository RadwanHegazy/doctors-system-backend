from rest_framework import status, decorators
from rest_framework.response import Response
from doctor.apis.serializers import Doctor, DoctorSerializer, Department

@decorators.api_view(["GET"])
def GetDocsForClient (request) :
    try :

        departmanet = request.GET.get('department',None)
        search = request.GET.get('search',None)

        doctors = Doctor.objects.all()

        if departmanet is not None : 
            
            try : 
                dep_model = Department.objects.get(name=departmanet)
            except Department.DoesNotExist:
                return Response({
                    'message' : "department not found"
                },status=status.HTTP_400_BAD_REQUEST) 

            doctors = doctors.filter(department=dep_model)

        if search is not None : 
            doctors = doctors.filter(full_name__icontains=search)

        serializer = DoctorSerializer(doctors,many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as error : 
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@decorators.api_view(["GET"])
def GetDoctor (request, doc_id) :
    try :

        try : 
            doctor = Doctor.objects.get(id=doc_id)
        except Doctor.DoesNotExist:
            return Response({
                'message' : f'doctor with this id not found'
            },status=status.HTTP_404_NOT_FOUND)
         
        serializer = DoctorSerializer(doctor)
        serializer.has_counter = True
        return Response(serializer.data,status=status.HTTP_200_OK)
    except Exception as error : 
        return Response({
            'message' : f'an error accoured : {error}'
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
