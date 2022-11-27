import qrcode

first_name = input("First Name: ")
last_name = input("Last Name: ")
phone = input("Phone: ")

image = qrcode.make(f"Name: {first_name} {last_name}\nPhone: {phone}")
image.save("ContactInformation.jpg")