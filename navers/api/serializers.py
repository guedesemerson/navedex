from rest_framework.serializers import ModelSerializer, SerializerMethodField
from navers.models import Naver
from rest_framework import serializers
from projetos.models import Projetos

class ProjectsToSerializer(ModelSerializer):
    class Meta:
        model = Projetos
        fields = ['id', 'name']

class NaversIndexSerializer(ModelSerializer):
    class Meta:
        model = Naver
        fields = ['id','name', 'birthdate', 'admission_date', 'job_role']


class NaveGenericSerializer(ModelSerializer):
    class Meta:
        model = Naver
        fields = ['id','name', 'birthdate', 'admission_date', 'job_role']


class NaveRetrieveSerializer(ModelSerializer):
    projetos = SerializerMethodField()
    class Meta:
        model = Naver
        fields = ['id','name', 'birthdate', 'admission_date', 'job_role', 'projetos']

    def get_projetos(self, obj):

        list_projects = []
        naver_id = obj.id
        naver_object = Naver.objects.filter(id=naver_id)

        if naver_object:
            pass
        else:
            raise serializers.ValidationError({"result": "Naver/Navers inexistente"})

        projects_objects = Projetos.objects.filter(navers=naver_id)

        for row in projects_objects:
            object_aux = {'id':row.id, 'name':row.name}
            list_projects.append(object_aux)

        return list_projects

