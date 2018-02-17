from django.db import models
from django.contrib.gis.db import models as mdl
class UnitType(models.Model):#Тип объекта
    name = models.CharField(max_length=20)
class Region(models.Model):#Округ
    name = models.CharField(max_length=20)
class District(models.Model):#Район
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region,
        on_delete=models.CASCADE)
class Owner(models.Model):#Балансодержатель
    name = models.CharField(max_length=150)    
class Unit(models.Model):#Объект
    systemId = models.IntegerField
    adress = models.CharField(max_length=200)
    isActual = models.BooleanField
    UnitType = models.ForeignKey(UnitType,
        on_delete=models.CASCADE)
    district = models.ForeignKey(District,
        on_delete=models.CASCADE)
    owner = models.ForeignKey(Owner,
        on_delete=models.CASCADE)
    polygon = mdl.MultiPolygonField
class Metric(models.Model):#Единицы измерения
    name = models.CharField(max_length=10)
class JobType(models.Model):#Виды работ
    name = models.CharField(max_length=50)
    metric = models.ForeignKey(Metric,
        on_delete=models.CASCADE)
class Program(models.Model):#Тип программы
    name = models.CharField(max_length=150) #благоустройство
    subName = models.CharField(max_length=150) #СЭРР
    extraName = models.CharField(max_length=150) #Комплексное
class JobGroup(models.Model):#Программа благоустройства
    program = models.ForeignKey(Program,
        on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit,
        on_delete=models.CASCADE)
    cost = models.IntegerField
    period = models.DateTimeField
    complete = models.DateTimeField    
class Job(models.Model):#Работы
    job = models.ForeignKey(JobType,
        on_delete=models.CASCADE)
    quantity = models.IntegerField
    jobgroup = models.ForeignKey(JobGroup,
        on_delete=models.CASCADE)
class Event(models.Model):#Событие/проверка
    name = models.CharField(max_length=50)
    jobgroup = models.ForeignKey(JobGroup,
        on_delete=models.CASCADE)
    date = models.DateTimeField
class Definer(models.Model):#Виды нарушений/Классификатор
    name = models.CharField(max_length=200)
class Issue(models.Model):#Нарушения
    event = models.ForeignKey(Event,
        on_delete=models.CASCADE)
    fixed = models.DateTimeField
    definer = models.ForeignKey(Definer,
        on_delete=models.CASCADE)
