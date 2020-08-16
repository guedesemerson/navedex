from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from navers.models import Naver
from projetos.models import Projetos

class NaversToSerializer(ModelSerializer):
    class Meta:
        model = Naver
        fields = ['id', 'name', 'birthdate','admission_date', 'job_role']

class ProjetosIndexSerializer(ModelSerializer):
    class Meta:
        model = Projetos
        fields = ['id','name']


class ProjetosCreateUpdateSerializer(ModelSerializer):

    class Meta:
        model = Projetos
        fields = ['id','name', 'navers']

    def validate(self, attrs):
        user = self.context['request'].user
        navers = attrs.get('navers', '')
        for row in navers:
            objeto = Naver.objects.filter(user=user, id=row.id)
            if objeto:
                pass
            else:
                raise serializers.ValidationError({"result": "Naver/Navers inexistente"})
        return super().validate(attrs)


class ProjetosRetrieveSerializer(ModelSerializer):
    navers = NaversToSerializer(many=True)
    class Meta:
        model = Projetos
        fields = ['id','name','navers']