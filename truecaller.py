import phonenumbers
from phonenumbers import geocoder
number = input("Enter the phone number with country code : ")
phone = phonenumbers.parse(number, "CH")
print("Country : ",(geocoder.description_for_number(phone,'en')))

from phonenumbers import carrier
car = phonenumbers.parse(number, "RO")
print ("Service Provider : ",(carrier.name_for_number(car, "en")))
