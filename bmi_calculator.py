given_data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }, { "Gender": "Male", "HeightCm": 161, "WeightKg":
85 }, { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 }, { "Gender": "Female", "HeightCm": 166,
"WeightKg": 62}, {"Gender": "Female", "HeightCm": 150, "WeightKg": 70}, {"Gender": "Female",
"HeightCm": 167, "WeightKg": 82}]


class BmiManager:
    data=dict()

    @staticmethod
    def validate_data(data):
        if data:
            if not isinstance(data, list):
                raise Exception('Invalid Data')
            else:
                for i in data:
                    if not (isinstance(i, dict) and all(key in i for key in ('Gender', 'WeightKg','HeightCm'))):
                        raise Exception('Data should contain Gender, WeightKg, HeightCm')
                    else:
                        if not (isinstance(i['Gender'], str) and (i['Gender']=='Male' or i['Gender']=='Female')):
                            raise Exception ('Gender should be string and It should be either Male or Female')
                        else:
                            if not isinstance(i['WeightKg'], int or float):
                                raise Exception('Weight should be integer or float number')
                            else:
                                if not isinstance(i['HeightCm'], int or float):
                                    raise Exception('Height should be integer or float number')
                                else:
                                    pass
        else:
            raise Exception('Data not found')
        return data   


    @staticmethod
    def bmi_calc(data):
        calculated=[]
        if isinstance(BmiManager.validate_data(data), list):
            for i in data:
                        bmi = round((i["WeightKg"]/(i["HeightCm"]/100)**2),2)
                        if (bmi <= 18.4):
                            calculated.append({'BMI':bmi, 'BMI Category':'Underweight', 'Health Risk':'Malnutrition risk'})
                            #print (f"Your BMI is " + str(bmi) + ". You are underweight. " + "You are at malnutrition risk.")
                        elif (18.5 <= bmi <= 24.9):
                            calculated.append({'BMI':bmi, 'BMI Category':'Normal', 'Health Risk':'Low risk'})
                            #print ("Your BMI is " + str(bmi) + ". Your weight is Normal." + " You are at low risk.")
                        elif (25 <= bmi <= 29.9):
                            calculated.append({'BMI':bmi, 'BMI Category':'Overweight', 'Health Risk':'Enhanced risk'})
                            #print ("Your BMI is " + str(bmi) + ". You are overweight ." + " You are at enhanced risk.")
                        elif (30 <= bmi <=34.9):
                            calculated.append({'BMI':bmi, 'BMI Category':'Moderately obese', 'Health Risk':'Medium risk'})

                            #print ("Your BMI is " + str(bmi) + ". You are moderately obese." + " You are at medium risk.")
                        elif (35 <= bmi <= 39.9):
                            calculated.append({'BMI':bmi, 'BMI Category':'Severely obese', 'Health Risk':'High risk'})

                            #print ("Your BMI is " + str(bmi) + ". You are severely obese." + " You are at high risk.")
                        else:
                            calculated.append({'BMI':bmi, 'BMI Category':'Severely obese', 'Health Risk':'Very high risk'})
                            #print ("Your BMI is " + str(bmi) + ". You are very severely obese." + " You are at very high risk.")
        return calculated


    @staticmethod
    def overweight(calculated):
        count=0
        if BmiManager.bmi_calc:
            for i in calculated:
                if i['BMI Category']=='Overweight':
                    count+=1

        return count



if __name__=='__main__':
    data=given_data
    #data=input('Please Enter your data in list of json format: ')
    try:
        BmiManager.validate_data(data)
        bmi_data= BmiManager.bmi_calc(given_data)
        print('BMI Categorical Data: ',bmi_data)
        overweight=BmiManager.overweight(bmi_data)
        print('Total numbers of overweight people: ', overweight)

    except Exception as e:
        raise Exception(str(e))
