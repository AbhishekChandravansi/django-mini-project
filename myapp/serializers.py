from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
        
class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    assigned_to = UserSerializer(many=True, source='users', read_only=True)
    created_by = serializers.ReadOnlyField(source='created_by.username')


    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'assigned_to', 'created_at', 'created_by']
        read_only_fields = ['id', 'created_at', 'created_by']


    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if self.context['request'].method == 'GET':
            representation.pop('assigned_to', None)
            representation.pop('users', None)
        if self.context['request'].method == 'POST':
            # representation.pop('assigned_to', None)
            representation.pop('users', None)    

        return representation

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='created_by.username')
    updated_by = serializers.ReadOnlyField(source='updated_by.username')
    projects = ProjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Client
        fields = ['id', 'client_name','projects', 'created_at', 'created_by', 'updated_at', 'updated_by']
        read_only_fields = ['id', 'created_at', 'created_by', 'updated_at', 'updated_by', 'projects']
        
    def create(self, validated_data):
        print('validated_data-------------->', validated_data)
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request and not request.resolver_match.kwargs.get('pk'):
            representation.pop('projects', None)
        return representation

