def car_info(manufacturer,model_name,**extra_info):# prints arbitrary info of Car
    car_profile = {}
    car_profile['Company'] = manufacturer
    car_profile['Car Name'] = model_name
    for key,value in extra_info.items():
        car_profile[key] = value
    return car_profile
info = car_info("Ford","GT",MaxSpeed = "250km/hrs")
print(info)