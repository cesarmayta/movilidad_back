from rest_framework import serializers


from .models import *

class ParentescoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblParentesco
        fields = '__all__'
        
class ApoderadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblApoderado
        fields = '__all__'
        
    def to_representation(self,instance):
        
        representation = super().to_representation(instance)
        representation['parentesco_nombre'] = instance.parentesco.parentesco_nombre
        return representation
        
   