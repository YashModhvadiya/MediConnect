from cryptography.fernet import Fernet
import json
import base64
import os

def decrypt(user):
    json_file_path = "C:\\Users\\Yash\\OneDrive\\Desktop\\main\\key.json"
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    file_path = "C:\\Users\\Yash\\OneDrive\\Desktop\\main\\User"
    file_path = os.path.join(file_path, user)
    print(file_path)

    file_paths = [
        "medical_diagnosis.txt",
        "medicine.txt",
        "weight.txt",
        "blood_pressure.txt",
        "heart_rate.txt",
        "blood_sugar.txt",
        "cholesterol.txt",
    ]

    data = data["Meghal"]
    key = base64.urlsafe_b64decode(data)
    cipher_suite = Fernet(key)
    temp_file = "C:\\Users\\Yash\\OneDrive\\Desktop\\main\\User\\Initializing"

    for f in file_paths:
        filename = file_path + "\\" + f
        with open(filename, "rb") as file:
            file_data = file.read()

        decrypted_message = cipher_suite.decrypt(file_data)

        fp = os.path.join(temp_file, f)
        with open(fp, "wb") as file:
            file.write(decrypted_message)

def encrypt(user):
    json_file_path = "C:\\Users\\Yash\\OneDrive\\Desktop\\main\\key.json"
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    file_path = "C:\\Users\\Yash\\OneDrive\\Desktop\\main\\User"
    file_path = os.path.join(file_path, user)

    file_paths = [
        "medical_diagnosis.txt",
        "medicine.txt",
        "weight.txt",
        "blood_pressure.txt",
        "heart_rate.txt",
        "blood_sugar.txt",
        "cholesterol.txt",
    ]

    data = data["Meghal"]
    key = base64.urlsafe_b64decode(data)
    cipher_suite = Fernet(key)

    for f in file_paths:
        filename = file_path + "\\" + f
        with open(filename, "rb") as file:
            file_data = file.read()

        encrypted_data = cipher_suite.encrypt(file_data)
        
        with open(filename, "wb") as file:
            file.write(encrypted_data)
        
# encrypt("Meghal")
decrypt("Meghal")