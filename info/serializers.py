from rest_framework import serializers
from info.models import Info, Job


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('date_start', 'date_end', 'company', 'job_image', 'description', 'job_url', 'category')



class InfoSerializer(serializers.ModelSerializer):

    jobs = JobSerializer(many=True)

    class Meta:
        model = Info
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'city', 'phone_number',
                  'email', 'facebook_link', 'linkedin_link', 'photo', 'jobs')
