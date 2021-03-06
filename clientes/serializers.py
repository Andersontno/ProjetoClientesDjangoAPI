from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):    
            raise serializers.ValidationError({'cpf':"CPF inválido."})

        if not nome_valido(data['nome']):    
            raise serializers.ValidationError({'nome':"Não incluir números no nome."})

        if not rg_valido(data['rg']):    
            raise serializers.ValidationError({'rg':"O RG deve ter 9 dígitos"})    
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O número de celular deve seguir este padrão: 00 00000-0000"})                
        
        return data
    