from  rest_framework import serializers
from .models import Info




class InfoSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Info
        fields="__all__"


