from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from patient.models import patient, pa_organ,total,patient_pca
def hello(request):
    return HttpResponse("hello,patient")
def echarts(request):
    # "心"，
    # "大肠"，
    # "小肠"，
    # "脾脏"，
    # "肾"，
    # "肺"，
    # "肝脏"
    tt = total.objects.filter(id='2')
    for t in tt:
        feiyan = int(t.feiyan)
        renshen = int(t.renshen)
        tangniaobing = int(t.tangniaobing)
        feiqizhong = int(t.feiqizhong)
        xiaochuan = int(t.xiaochuan)
        gaoxueya = int(t.gaoxueya)
        xinxueguan = int(t.xinxueguan)
        feipang = int(t.feipang)
        shenshuaijie = int(t.shenshuaijie)
        smoking = int(t.smoking)
        others = int(t.other)
        return render(request, 'patient/geo.html',
                      {'feiyan': feiyan, 'renshen': renshen,
                       'tangniaobing': tangniaobing, 'feiqizhong': feiqizhong,
                       'xiaochuan': xiaochuan, 'gaoxueya': gaoxueya,
                       'xinxueguan': xinxueguan, 'feipang': feipang,
                       'shenshuaijie': shenshuaijie, 'smoking': smoking,
                       'others': others, })
    pa=pa_organ.objects.filter(id='2')
    for p in pa:
        heart=int(p.heart)
        spleen=int(p.spleen)
        kidney=int(p.kidney)
        lung=int(p.lung)
        liver=int(p.liver)
        other=int(p.other)
        return render(request, 'patient/geo.html', {'heart':heart, 'spleen':spleen, 'kidney':kidney, 'lung':lung,
                                                    'liver':liver, 'other':other })

def pat(request):
    tot=total.objects.filter(id='2')
    for t in tot:
        male=int(t.male)
        female=int(t.female)
        children=int(t.children)
        young=int(t.young)
        adults=int(t.adults)
        older = int(t.older)
        childrenN = int(t.childrenN)
        youngN = int(t.youngN)
        adultsN = int(t.adultsN)
        olderN = int(t.olderN)
        patienin = int(t.patienin)
        patienout = int(t.patienout)
        infectY = int(t.infectY)
        all = int(t.all)
        icuY =int(t.icuY)
        deadY =int(t.deadY)
        deadN =int(t.deadN)
        chaguan = int(t.chaguan)
        feiyan = int(t.feiyan)
        renshen = int(t.renshen)
        tangniaobing = int(t.tangniaobing)
        feiqizhong = int(t.feiqizhong)
        xiaochuan = int(t.xiaochuan)
        gaoxueya = int(t.gaoxueya)
        xinxueguan = int(t.xinxueguan)
        feipang = int(t.feipang)
        shenshuaijie = int(t.shenshuaijie)
        smoking = int(t.smoking)
        contacts = int(t.contacts)
        other=int(t.other)
        pfeiyan = t.pfeiyan
        prenshen = t.prenshen
        ptangniaobing =t.ptangniaobing
        pfeiqizhong = t.pfeiqizhong
        pxiaochuan = t.pxiaochuan
        pgaoxueya = t.pgaoxueya
        pxinxueguan = t.pxinxueguan
        pfeipang = t.pfeipang
        pshenshuaijie = t.pshenshuaijie
        psmoking = t.psmoking
        pcontacts = t.pcontacts
        pother = t.pother
        return render(request, 'patient/patient_index.html', {'male': male, 'female': female, 'children': children,
                                                   'young': young, 'adults': adults, 'older': older,
                                                   'patienin': patienin, 'patienout': patienout,
                                                   'infectY': infectY, 'all': all,
                                                   'icuY': icuY, 'deadY': deadY, 'deadN': deadN,
                                                   'chaguan': chaguan, 'feiyan': feiyan, 'renshen': renshen,
                                                   'tangniaobing': tangniaobing, 'feiqizhong': feiqizhong,
                                                   'xiaochuan': xiaochuan, 'gaoxueya': gaoxueya,
                                                   'xinxueguan': xinxueguan, 'feipang': feipang,
                                                   'shenshuaijie': shenshuaijie, 'smoking': smoking,
                                                   'contacts': contacts, 'other': other,'childrenN':childrenN,
                                                              'youngN':youngN, 'adultsN':adultsN, 'olderN':olderN, 'pfeiyan':pfeiyan,
                                                              'prenshen':prenshen, 'ptangniaobing':ptangniaobing, 'pfeiqizhong':pfeiqizhong,
                                                              'pxiaochuan':pxiaochuan, 'pgaoxueya':pgaoxueya, 'pxinxueguan':pxinxueguan,
                                                              'pfeipang':pfeipang, 'pshenshuaijie':pshenshuaijie, 'psmoking':psmoking,
                                                              'pcontacts':pcontacts, 'pothers':pother})
