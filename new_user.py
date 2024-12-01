import customtkinter
import user
from datetime import datetime
import os
from cryptography.fernet import Fernet
import json
import base64

class new_user(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
        self.controller = controller  
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=8)
        self.grid_columnconfigure(2, weight=7)
        self.grid_rowconfigure((0, 1), weight=1)

        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="MediConnect", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.pack(pady=15)
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Back", font=customtkinter.CTkFont(size=15), command=lambda d="Initializing": controller.show_frame(user.User, d), width=140)
        self.sidebar_button_1.pack(pady=10)

        self.main_frame.grid(row=0, column=1, columnspan=2, rowspan=2, padx=18, pady=20, sticky="nsew")   
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.name = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.name.grid(row=0, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.name.grid_columnconfigure(1, weight=1)
        self.name_label = customtkinter.CTkLabel(self.name, text="Name:            ", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.name_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 20), sticky="nsew")
        self.name_entry = customtkinter.CTkEntry(self.name, placeholder_text="Full Name")
        self.name_entry.grid(row=0, column=1, columnspan=2, padx=(10, 20), pady=(20, 20), sticky="nsew")

        self.bod = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.bod.grid(row=1, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.bod.grid_columnconfigure(1, weight=1)
        self.bod_label = customtkinter.CTkLabel(self.bod, text="Date of Birth:", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.bod_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 20), sticky="nsew")
        self.bod_entry = customtkinter.CTkEntry(self.bod, placeholder_text="DD-MM-YYYY")
        self.bod_entry.grid(row=0, column=1, columnspan=2, padx=(10, 20), pady=(20, 20), sticky="nsew")

        self.blood_type = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.blood_type.grid(row=2, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.blood_type.grid_columnconfigure(1, weight=1)
        self.blood_type_label = customtkinter.CTkLabel(self.blood_type, text="Blood Type:  ", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.blood_type_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 20), sticky="nsew")
        self.blood_type_entry = customtkinter.CTkEntry(self.blood_type, placeholder_text="A+,  A-,  B+,  B-,  AB+,  AB-,  O+,  O-")
        self.blood_type_entry.grid(row=0, column=1, columnspan=2, padx=(10, 20), pady=(20, 20), sticky="nsew")

        self.height = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.height.grid(row=3, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.height.grid_columnconfigure(1, weight=1)
        self.height_label = customtkinter.CTkLabel(self.height, text="Height:          ", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.height_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 20), sticky="nsew")
        self.height_entry = customtkinter.CTkEntry(self.height, placeholder_text="(in cm)")
        self.height_entry.grid(row=0, column=1, columnspan=2, padx=(10, 20), pady=(20, 20), sticky="nsew")

        self.weight = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.weight.grid(row=4, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.weight.grid_columnconfigure(1, weight=1)
        self.weight_label = customtkinter.CTkLabel(self.weight, text="Weight:         ", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.weight_label.grid(row=0, column=0, padx=(20, 10), pady=(20, 20), sticky="nsew")
        self.weight_entry = customtkinter.CTkEntry(self.weight, placeholder_text="(in Kg)")
        self.weight_entry.grid(row=0, column=1, columnspan=2, padx=(10, 20), pady=(20, 20), sticky="nsew")

        self.button = customtkinter.CTkFrame(self.main_frame, corner_radius=0)
        self.button.grid(row=5, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.button.grid_columnconfigure(0, weight=1)
        self.submit_button = customtkinter.CTkButton(self.button, text="Submit", font=customtkinter.CTkFont(size=18), command=lambda : self.submit(), width=140)
        self.submit_button.grid(row=0, column=1, padx=(10, 20), pady=(20, 20), sticky="nsew")

    def submit(self):
        self.empty = customtkinter.CTkLabel(self.button, text="", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.empty.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="nsew")
        if self.name_entry.get().strip() == "":
            self.name_alert = customtkinter.CTkLabel(self.button, text="Please enter a valid name", font=customtkinter.CTkFont(size=18, weight="bold"), text_color="red")
            self.name_alert.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="nsew")
        elif not self.is_valid_date(self.bod_entry.get(), "%d-%m-%Y"):
            self.bod_alert = customtkinter.CTkLabel(self.button, text="Please enter a valid Date of Birth", font=customtkinter.CTkFont(size=18, weight="bold"), text_color="red")
            self.bod_alert.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="nsew")
        elif self.blood_type_entry.get() not in ["A+",  "A-",  "B+",  "B-",  "AB+",  "AB-",  "O+",  "O-"]:
            self.blood_type_alert = customtkinter.CTkLabel(self.button, text="Please enter a valid blood type", font=customtkinter.CTkFont(size=18, weight="bold"), text_color="red")
            self.blood_type_alert.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="nsew")
        elif not self.height_entry.get().isdigit():
            self.height_alert = customtkinter.CTkLabel(self.button, text="Please enter a valid Height (in cm)", font=customtkinter.CTkFont(size=18, weight="bold"), text_color="red")
            self.height_alert.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="nsew")
        elif not self.weight_entry.get().isdigit():
            self.weight_alert = customtkinter.CTkLabel(self.button, text="Please enter a valid Weight (in Kg)", font=customtkinter.CTkFont(size=18, weight="bold"), text_color="red")
            self.weight_alert.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="nsew")
        else:
            dob = datetime.strptime(self.bod_entry.get(), '%d-%m-%Y')
            current_date = datetime.now()
            age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
            medical_diagnosis = "Name: "+self.name_entry.get()+"\nAge: "+str(age)+"\nDate of Birth: "+self.bod_entry.get()+"\nBlood Type: "+self.blood_type_entry.get()+"\nHeight: "+self.height_entry.get()+"cm\nWeight: "+self.weight_entry.get()+"Kg\n----------------------------------------------------------------------------------------------"
            # print(medical_diagnosis)
            # folder_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\\User" + self.name_entry.get().strip()
            folder_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\User" + self.name_entry.get().strip()
            os.mkdir(folder_path)
            file_path = folder_path+"\\medical_diagnosis.txt"
            fp = open(file_path, "w")
            fp.write(medical_diagnosis)
            fp.close()
            file_path = folder_path+"\\medicine.txt"
            fp = open(file_path, "w")
            fp.close()
            file_path = folder_path+"\\blood_pressure.txt"
            fp = open(file_path, "w")
            fp.close()
            file_path = folder_path+"\\blood_sugar.txt"
            fp = open(file_path, "w")
            fp.close()
            file_path = folder_path+"\\cholesterol.txt"
            fp = open(file_path, "w")
            fp.close()
            file_path = folder_path+"\\heart_rate.txt"
            fp = open(file_path, "w")
            fp.close()
            file_path = folder_path+"\\weight.txt"
            fp = open(file_path, "w")
            fp.close()
            key = Fernet.generate_key()
            json_file_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\key.json"
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
            key_str = base64.urlsafe_b64encode(key).decode()
            data[self.name_entry.get()] = key_str
            with open(json_file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            self.controller.frames[user.User].refresh_directory_list()
            self.sucessfull = customtkinter.CTkLabel(self.button, text="Sucessfull", font=customtkinter.CTkFont(size=18, weight="bold"), text_color="green")
            self.sucessfull.grid(row=0, column=0, padx=(10, 20), pady=(20, 20), sticky="nsew")


    def is_valid_date(self, date_string, date_format):
        try:
            datetime.strptime(date_string, date_format)
            return True
        except ValueError:
            return False


# self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="print", font=customtkinter.CTkFont(size=15), command=lambda : self.p(), width=140)
# self.sidebar_button_2.pack(pady=10)
# def p(self):
#     print(self.name_entry.get())
# self.controller.show_frame(user.User, "Initializing")
