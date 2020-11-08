#bmi calculator
height = float(input('enter your height (cms)\n'))
weight = float( input('enter your weight (kg)\n'))
bmi = round(weight/(height/100)**2,2)

if bmi < 18.5:
    bmi_type="Under Weight"
elif bmi < 25 :
    bmi_type="Normal"
elif bmi < 30 :
    bmi_type="Over Weight"
elif bmi< 35 :
    bmi_type="Obesity"
else:
    bmi_type="Clinical Obesity"

print(f'yout bmi is {bmi}, which is {bmi_type}')
