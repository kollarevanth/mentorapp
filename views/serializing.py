from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from onlineapp.models import *



class collegeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=120)
    location = serializers.CharField(max_length=64)
    acronym =serializers.CharField(max_length=8)
    contact = serializers.EmailField()

    def create(self, validated_data):
         return College.objects.create(**validated_data)

    def update(self, instance, validated_data):
         instance.name = validated_data.get('name', instance.name)
         instance.location = validated_data.get('location', instance.location)
         instance.acronym = validated_data.get('acronym', instance.acronym)
         instance.contact = validated_data.get('contact', instance.contact)
         instance.save()
         return instance


class studentSerializer(ModelSerializer):
    class Meta:
        model=Student
        exclude=['college']

    def __str__(self):
        return self.data



class marksSerializer(ModelSerializer):
    class Meta:
        model=MockTest1
        fields=('problem1','problem2','problem3','problem4','total')

    def __str__(self):
        return str(self.data)


class studentDetailSerialize(ModelSerializer):
    mocktest1 = marksSerializer()
    class Meta:

        model=Student
        fields=('name','dob','email','db_folder','dropped_out','mocktest1')

    # def create(self, validated_data):
    #     marks_data=validated_data.pop('mocktest1')
    #     student=Student.objects.create(**validated_data)
    #     MockTest1.objects.create(student=student.id,**marks_data)
    #     return student

    def update(self, instance, validated_data):
        marks_data = validated_data.pop('mocktest1')
        marks=instance.mocktest1
        instance.name=validated_data.get('name',instance.name)
        instance.dropped_out=validated_data.get('dropped_out',instance.dropped_out)
        instance.email=validated_data.get('email',instance.email)
        instance.save()
        marks.problem1=marks_data.get('problem1',marks.problem1)
        marks.problem2=marks_data.get('problem2',marks.problem2)
        marks.problem3=marks_data.get('problem3',marks.problem3)
        marks.problem4=marks_data.get('problem4',marks.problem4)
        marks.total=marks_data.get('total',marks.total)
        marks.save()
        instance.marks=marks
        return instance
    def __str__(self):
        return str(self.data)