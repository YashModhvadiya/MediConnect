import patient
import os
import socket
from cryptography.fernet import Fernet
import json
import base64

def send_file():
    file_path = "C:\\Users\\Yash\\OneDrive\\Desktop\\main\\User\\Initializing"
    # file_path = os.path.join(file_path, patient.p)
    # file_path = os.path.join(file_path, "Meghal")

    file_paths = [
        "medical_diagnosis.txt",
        "medicine.txt",
        "weight.txt",
        "blood_pressure.txt",
        "heart_rate.txt",
        "blood_sugar.txt",
        "cholesterol.txt",
    ]

    data = ""
    for f in file_paths:
            f_path = os.path.join(file_path, f)
            with open(f_path, "r") as file:
                file_content = file.read()
                data = data + file_content
                data = data + "$$$$$$$$"

    json_file_path = "C:/Users/Yash/OneDrive/Desktop/main/key.json"
    with open(json_file_path, 'r') as json_file:
        k = json.load(json_file)

    k = k[patient.p]
    key = base64.urlsafe_b64decode(k)
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data.encode('utf-8'))

    s=socket.socket()
    host=socket.gethostname()
    port=8080
    s.bind((host, port))
    s.listen(1)
    # print(host)
    print("Waiting for any incoming connections...")
    conn,addr=s.accept()
    data_bytes = encrypted_data
    conn.send(data_bytes)
    conn.close()
    s.close()

# data_parts = data.split("$$$$$$$$")

# # Now, data_parts is a list of strings containing the separate data
# for part in data_parts:
#     print(part)
