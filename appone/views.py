from django.shortcuts import render
import pickle
from appone.models import breastCancer,diabetes,heart,liver,malaria,pneumonia,kidney
# import numpy as np
from PIL import Image
# from tensorflow.keras.models import load_model
# Create your views here.

def predict(values, dic):
    if len(values) == 8:
        model = pickle.load(open('models/diabetes.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 26:
        model = pickle.load(open('models/breast_cancer.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 13:
        model = pickle.load(open('models/heart.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 18:
        model = pickle.load(open('models/kidney.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]
    elif len(values) == 10:
        model = pickle.load(open('models/liver.pkl','rb'))
        values = np.asarray(values)
        return model.predict(values.reshape(1, -1))[0]



def home(request):
    # if request.method=='POST':

    return render(request,'index.html')

def cancerPage(request):
    if request.method=='POST':
        radius_mean = request.POST['radius_mean']
        texture_mean = request.POST['texture_mean']
        perimeter_mean = request.POST['perimeter_mean']
        area_mean = request.POST['area_mean']
        smoothness_mean = request.POST['smoothness_mean']
        compactness_mean = request.POST['compactness_mean']
        concavity_mean = request.POST['concavity_mean']
        concave_points_mean = request.POST['concave_points_mean']
        symmetry_mean = request.POST['symmetry_mean']
        radius_se=request.POST['radius_se']
        perimeter_se=request.POST['perimeter_se']
        compactness_se=request.POST['compactness_se']
        area_se=request.POST['area_se']
        concavity_se=request.POST['concavity_see']
        concave_points_se=request.POST['concave_points_se']
        fractal_dimension_se=request.POST['fractal_dimension_se']
        radius_worst=request.POST['radius_worst']
        texture_worst=request.POST['texture_worst']
        area_worst=request.POST['area_worst']
        smoothness_worst=request.POST['smoothness_worst']
        compactness_worst=request.POST['compactness_worst']
        concavity_worst=request.POST['concavity_worst']
        concave_points_worst=request.POST['concave_points_worst']
        symmetry_worst=request.POST['symmetry_worst']
        fractal_dimension_worst =request.POST['fractal_dimension_worst ']

        data = breastCancer.objects.create(
            radius_mean=radius_mean,
            texture_mean=texture_mean,
            perimeter_mean=perimeter_mean,
            area_mean=area_mean,
            smoothness_mean=smoothness_mean,
            compactness_mean=compactness_mean,
            concavity_mean=concavity_mean,
            concave_points_mean=concave_points_mean,
            symmetry_mean = symmetry_mean,
            radius_se=radius_se,
            perimeter_se=perimeter_se,
            compactness_se=compactness_se,
            area_se=area_se,
            concavity_se=concavity_se,
            concave_points_se= concave_points_se,
            fractal_dimension_se=fractal_dimension_se,
            radius_worst=radius_worst,
            texture_worst=texture_worst,
            area_worst=area_worst,
            smoothness_worst=smoothness_worst,
            compactness_worst=compactness_worst,
            concavity_worst=concavity_worst,
            concave_points_worst=concave_points_worst,
            symmetry_worst=symmetry_worst,
            fractal_dimension_worst=fractal_dimension_worst
                                            )
        data.save()
        
    
    return render(request,'bcancer.html')

def heartPage(request):
    if request.method=='POST':
        age = request.POST['age']
        sex = request.POST['sex']
        cp = request.POST['cp']
        trestbps = request.POST['trestbps']
        chol = request.POST['chol']
        fbs = request.POST['fbs']
        restecg = request.POST['restecg']
        thalach = request.POST['thalach']
        exang = request.POST['exang']
        oldpeak=request.POST['oldpeak']
        slope=request.POST['slpoe']
        ca=request.POST['ca']
        thal=request.POST['thal']
     

        data = heart.objects.create(
            age=age,
            sex=sex,
            cp=cp,
            trestbps=trestbps,
            chol=chol,
            fbs=fbs,
            restecg=restecg,
            thalach=thalach,
            exang=exang,
            oldpeak=oldpeak,
            slope=slope,
            ca=ca,
            thal=thal
         )
        data.save()
    return render(request,'heart.html')

def kidneyPage(request):
    if request.method=="POST":
        age = request.POST['age']
        bp = request.POST['bp']
        al = request.POST['al']
        su = request.POST['su']
        rbc = request.POST['rbc']
        pc = request.POST['pcf']
        pcc = request.POST['pcc']
        ba = request.POST['ba']
        bgr = request.POST['bgr']
        bu=request.POST['bu']
        sc=request.POST['sc']
        pot=request.POST['pot']
        wc=request.POST['wc']
        htn=request.POST['htn']
        dm=request.POST['dm']
        cad=request.POST['cad']
        pe=request.POST['pe']
        ane=request.POST['ane']

        data = kidney.objects.create(
            age=age,
            bp=bp,
            al=al,
            su=su,
            rbc=rbc,
            pc=pc,
            pcc=pcc,
            ba=ba,
            bgr=bgr,
            bu=bu,
            sc=sc,
            pot=pot,
            wc=wc,
            htn=htn,
            dm=dm,
            cad=cad,
            pe=pe,
            ane=ane
         )
        data.save()
    return render(request,'kidney.html')

def liverPage(request):
    if (request.method=='POST'):
        age=request.POST['age'],
        Total_Bilirubin=request.POST['Total_Bilirubin'],
        Direct_Bilirubin=request.POST['Direct_Bilirubin'],
        Alkaline_Phosphotase=request.POST['Alkaline_Phosphotase'],
        Alamine_Aminotransferase=request.POST['Alamine_Aminotransferase'],
        Aspartate_Aminotransferase=request.POST['Aspartate_Aminotransferase'],
        Total_Protiens=request.POST['Total_Protiens'],
        Albumin=request.POST['Albumin'],
        Albumin_and_Globulin_Ratio=request.POST['Albumin_and_Globulin_Ratio'],
        Gender_Male=request.POST['Gender_Male'],

        data=liver.objects.create(
            age=age,
            Total_Bilirubin=Total_Bilirubin,
            Direct_Bilirubin=Direct_Bilirubin,
            Alkaline_Phosphotase=Alkaline_Phosphotase,
            Alamine_Aminotransferase=Alamine_Aminotransferase,
            Aspartate_Aminotransferase=Aspartate_Aminotransferase,
            Total_Protiens=Total_Protiens,
            Albumin=Albumin,
            Albumin_and_Globulin_Ratio=Albumin_and_Globulin_Ratio,
            Gender_Male=Gender_Male
        )
        data.save()


    return render(request,'liver.html')

def malariaPage(request):
    if request.method=='POST':
        image=request.POST['image']

        data=malaria.objects.create(
            image=image
        )
        data.save()
    
    return render(request,'malaria.html')

def diabetesPage(request):
    if request.method=="POST":
        pregnancies = request.POST['pregancies']
        glucose = request.POST['glucose']
        bloodpressure = request.POST['bloodpressure']
        skinthickness = request.POST[' skinthickness']
        insulin = request.POST['insulin']
        bmi = request.POST['bmi']
        dpf = request.POST['pcc']
        age = request.POST['ba']
        

        data = diabetes.objects.create(
            pregnancies=pregnancies,
            glucose=glucose,
            bloodpressure=bloodpressure,
            skinthickness=skinthickness,
            insulin=insulin,
            bmi=bmi,
            dpf=dpf,
            age=age
            
         )
        data.save()
    return render(request,'diabetes.html')

def pneumoniaPage(request):
    if request.method=='POST':
        image=request.POST['image']

        data=pneumonia.objects.create(
            image=image
        )
        data.save()
    return render(request,'pneumonia.html')


def predictPage(request):
    try:
        if request.method == 'POST':
            to_predict_dict = request.form.to_dict()
            to_predict_list = list(map(float, list(to_predict_dict.values())))
            pred = predict(to_predict_list, to_predict_dict)
    except:
        message = { 'msg' : "Please enter valid Data"}
        return render(request,"index.html", message)

    return render(request,'predict.html', pred)

def malariapredictPage(request):
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                img = Image.open(request.files['image'])
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,3))
                img = img.astype(np.float64)
                model = load_model("models/malaria.h5")
                pred = np.argmax(model.predict(img)[0])
        except:
            message = "Please upload an Image"
            return render(request,'malaria.html', message = message)
    return render(request,'malaria_predict.html', pred = pred)

def pneumoniapredictPage(request):
    if request.method == 'POST':
        try:
            if 'image' in request.files:
                img = Image.open(request.files['image']).convert('L')
                img = img.resize((36,36))
                img = np.asarray(img)
                img = img.reshape((1,36,36,1))
                img = img / 255.0
                model = load_model("models/pneumonia.h5")
                pred = np.argmax(model.predict(img)[0])
        except:
            message = "Please upload an Image"
            return render(request,'pneumonia.html', message = message)
    return render(request,'pneumonia_predict.html', pred = pred)