from rest_framework import serializers

from .models import *


class Company_Serializer(serializers.ModelSerializer):
    logo_url = serializers.ReadOnlyField()

    class Meta:
        model = Employer_Model
        fields = ['id', 'name',  'logo_url', 'logo']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop("logo")

        return representation


class Job_Serializer(serializers.ModelSerializer):
    # company = Company_Serializer()
    # # company_info = serializers.SerializerMethodField()
    # # date_created = serializers.SerializerMethodField()

    class Meta:

        model = Job_Model

        # fields = ['image', 'time', 'location', 'description']
        fields = ['title', 'contract_type', 'location',
                  'level', 'description']
        # depth = 3

    # def get_company_info(self, obj):
    #     company_obj = Employer_Model.objects.get(id=obj.company.id)
    #     return {'company_name': company_obj.name, 'company_logo': company_obj.logo_url, }
