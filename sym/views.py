from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from sym.models import sym_all
def hello(request):

    return HttpResponse("hello,sym")
def show(request):
    li=sym_all.objects.filter(id='17')
    for i in li:
        allperson=i.allperson
        male=i.male
        female=i.female
        fever=i.fever
        tiredness=i.tiredness
        drycough=i.drycough
        difbrea=i.difficultybreathing
        sorethroat=i.sorethroat
        nonesym=i.nonesympton
        pains=i.pains
        nasa=i.nasalcongestion
        runnose=i.runnynose
        diarrhea=i.diarrhea
        noneexp=i.noneexperiencing
        age09=i.age09
        age1019=i.age1019
        age2024=i.age2024
        age2559=i.age2559
        age60=i.age60field
        age091=i.age091
        age10191=i.age10191
        age20241=i.age20241
        age25591=i.age25591
        age601=i.age60field1
        age090=i.age090
        age10190=i.age10190
        age20240=i.age20240
        age25590=i.age25590
        age600=i.age60field0
        sevmild=i.severitymild
        sevmod=i.severitymoderate
        sevsev=i.severitysevere
        contactor=i.contactor
        return render(request,'sym/sym_index.html',{'allperson':allperson,'male':male,'female':female,'fever':fever,
                                                    'tiredness':tiredness,'drycough':drycough,'difficultybreathing':difbrea,
                                                    'sorethroat':sorethroat,'nonesympton':nonesym,'pains':pains,'nasalcongestion':nasa,
                                                    'runnynose':runnose,'diarrhea':diarrhea,'noneexperiencing':noneexp,'age09':age09,
                                                    'age1019':age1019,'age2024':age2024,'age2559':age2559,'age60':age60,
                                                    'age091': age091,
                                                    'age10191': age10191, 'age20241': age20241, 'age25591': age25591,
                                                    'age601': age601,
                                                    'age090': age090,
                                                    'age10190': age10190, 'age20240': age20240, 'age25590': age25590,
                                                    'age600': age600,
                                                    'severitymild':sevmild,'severitymoderate':sevmod,'severitysevere':sevsev,'contactoryes':contactor})

