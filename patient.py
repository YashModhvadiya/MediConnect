import customtkinter
import user
import os
import matplotlib.pyplot as plt
import medicine
import socket
import file_transfer
import key
import json
import base64
from cryptography.fernet import Fernet

import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

p = "Initializing"

class Patient(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
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
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Home", font=customtkinter.CTkFont(size=15), command=lambda: self.show_frame(home), width=140)
        self.sidebar_button_1.pack(pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Health Metrics", font=customtkinter.CTkFont(size=15), command=lambda: self.show_frame(health_metrics), width=140)
        self.sidebar_button_2.pack(pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Conversation", font=customtkinter.CTkFont(size=15), command=lambda: self.show_frame(conversation), width=140)
        self.sidebar_button_3.pack(pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, text="Back", font=customtkinter.CTkFont(size=15), command=lambda : self.back(controller),  width=140)
        self.sidebar_button_4.pack(pady=10)

        self.main_frame.grid(row=0, column=1, columnspan=2, rowspan=2, padx=18, pady=20, sticky="nsew")   
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (home, health_metrics, conversation):
            frame = F(self.main_frame, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(home)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def back(self, controller):
        # key.encrypt(p)
        controller.show_frame(user.User, "Initializing")

class home(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
        self.grid(row=0, column=1, columnspan=3, rowspan=4, padx=0, pady=0, sticky="nsew")
        self.grid_rowconfigure((0, 1), weight=1) 
        self.grid_columnconfigure(0, weight=1)  
        self.grid_columnconfigure(1, weight=1)

        self.medical_history_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.medical_history_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 10), sticky="nsew")
        self.medical_history_frame.grid_columnconfigure(1, weight=1)
        self.medical_history_frame.grid_rowconfigure(1, weight=1)
        self.medical_history_label = customtkinter.CTkLabel(self.medical_history_frame, text="Medical History", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.medical_history_label.grid(row=0, column=0, padx=(10, 10), pady=10, sticky="nsew")
        self.medical_history = customtkinter.CTkTextbox(self.medical_history_frame, width=250)
        self.medical_history.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky="nsew")

        self.medicine_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.medicine_frame.grid(row=1, column=0, padx=(10,10), pady=(10, 10), sticky="nsew")
        self.medicine_frame.grid_columnconfigure(1, weight=1)
        self.medicine_frame.grid_rowconfigure(1, weight=1)
        self.medicine_label = customtkinter.CTkLabel(self.medicine_frame, text="Medicine", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.medicine_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.medicine = customtkinter.CTkTextbox(self.medicine_frame, width=250)
        self.medicine.grid(row=1, column=0, columnspan=2, padx=(10,10), pady=(0, 10), sticky="nsew")

        self.medicine_Link = customtkinter.CTkFrame(self, width=250)
        # self.medicine_Link.grid(row=1, column=1, padx=(10,10), pady=(10,10), sticky="nsew")
        self.medicine_Link.grid_columnconfigure(1, weight=1)
        self.link_label = customtkinter.CTkLabel(self.medicine_Link, text="Medicine Links", font=customtkinter.CTkFont(size=18, weight="bold"))
        # self.link_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.medicine_link_textbox = customtkinter.CTkTextbox(self.medicine_Link, width=250)
        self.link_button = customtkinter.CTkButton(self.medicine_Link, text="Show Links", font=customtkinter.CTkFont(size=15), command=lambda : self.shoe_link(p), width=140)
        # self.link_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
    
    def intial(self):
        self.medicine_Link.grid_rowconfigure((0,1), weight=0)
        self.medicine_Link.grid(row=1, column=1, padx=(10,10), pady=(10,10), sticky="nsew")
        self.link_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.link_button.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.medicine_link_textbox.grid_forget()

    def shoe_link(self, p):
        self.medicine_Link.grid_rowconfigure(1, weight=1)
        self.medicine_Link.grid_rowconfigure((0,2), weight=0)
        self.medicine_link_textbox.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(0, 0), sticky="nsew")
        self.link_button.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")
        self.medicine_link_textbox.delete(0.0, 'end')
        l = medicine.links(p)
        self.medicine_link_textbox.insert("0.0", l)
        # print(l)

class health_metrics(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
        self.grid(row=0, column=1, columnspan=3, rowspan=4, padx=0, pady=0, sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        self.top = customtkinter.CTkFrame(self, corner_radius=0)
        self.top.grid(row=0, column=0, padx=(10,10), pady=(0, 0), sticky="nsew")
        self.top.grid_columnconfigure((0,1,2), weight=1)
        self.top.grid_rowconfigure(0, weight=1)

        self.weight_frame = customtkinter.CTkFrame(self.top, corner_radius=0)
        self.weight_frame.grid(row=0, column=0, padx=(10,5), pady=(10, 10), sticky="nsew")
        self.weight_frame.grid_columnconfigure(1, weight=1)
        self.weight_frame.grid_rowconfigure(1, weight=1)
        self.weight_label = customtkinter.CTkLabel(self.weight_frame, text="Weight", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.weight_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.weight_box = customtkinter.CTkTextbox(self.weight_frame)
        self.weight_box.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(0, 5), sticky="nsew")

        self.blood_pressure_frame = customtkinter.CTkFrame(self.top, corner_radius=0)
        self.blood_pressure_frame.grid(row=0, column=1, padx=(5,5), pady=(10, 10), sticky="nsew")
        self.blood_pressure_frame.grid_columnconfigure(1, weight=1)
        self.blood_pressure_frame.grid_rowconfigure(1, weight=1)
        self.blood_pressure_label = customtkinter.CTkLabel(self.blood_pressure_frame, text="Blood Pressure", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.blood_pressure_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.blood_pressure_box = customtkinter.CTkTextbox(self.blood_pressure_frame)
        self.blood_pressure_box.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(0, 10), sticky="nsew")

        self.heart_rate_frame = customtkinter.CTkFrame(self.top, corner_radius=0)
        self.heart_rate_frame.grid(row=0, column=2, padx=(5,10), pady=(10, 10), sticky="nsew")
        self.heart_rate_frame.grid_columnconfigure(1, weight=1)
        self.heart_rate_frame.grid_rowconfigure(1, weight=1)
        self.heart_rate_label = customtkinter.CTkLabel(self.heart_rate_frame, text="Heart Rate", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.heart_rate_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.heart_rate_box = customtkinter.CTkTextbox(self.heart_rate_frame)
        self.heart_rate_box.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(0, 10), sticky="nsew")

        self.bottom = customtkinter.CTkFrame(self, corner_radius=0)
        self.bottom.grid(row=1, column=0, padx=(10,10), pady=(0, 0), sticky="nsew")
        self.bottom.grid_columnconfigure((0,1), weight=1)
        self.bottom.grid_rowconfigure(0, weight=1)

        self.blood_sugar_frame = customtkinter.CTkFrame(self.bottom, corner_radius=0)
        self.blood_sugar_frame.grid(row=0, column=0, padx=(10,5), pady=(10, 10), sticky="nsew")
        self.blood_sugar_frame.grid_columnconfigure(1, weight=1)
        self.blood_sugar_frame.grid_rowconfigure(1, weight=1)
        self.blood_sugar_label = customtkinter.CTkLabel(self.blood_sugar_frame, text="Blood Sugar", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.blood_sugar_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.blood_sugar_box = customtkinter.CTkTextbox(self.blood_sugar_frame)
        self.blood_sugar_box.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(0, 10), sticky="nsew")

        self.cholesterol_frame = customtkinter.CTkFrame(self.bottom, corner_radius=0)
        self.cholesterol_frame.grid(row=0, column=1, padx=(5,10), pady=(10, 10), sticky="nsew")
        self.cholesterol_frame.grid_columnconfigure(1, weight=1)
        self.cholesterol_frame.grid_rowconfigure(1, weight=1)
        self.cholesterol_label = customtkinter.CTkLabel(self.cholesterol_frame, text="Cholesterol", font=customtkinter.CTkFont(size=18, weight="bold"))
        self.cholesterol_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.cholesterol_box = customtkinter.CTkTextbox(self.cholesterol_frame)
        self.cholesterol_box.grid(row=1, column=0, columnspan=3, padx=(10,10), pady=(0, 10), sticky="nsew")

    def update(self, m):
        file_path = 'C:\\Users\\Yash\\OneDrive\\Desktop\\main\\User\\Initializing'
        # file_path = os.path.join(file_path, m)

        weight = os.path.join(file_path, "weight.txt")
        with open(weight, 'r') as file:
            file_contents_weight = file.readlines()
        weight_string = "\n".join(file_contents_weight)
        self.weight_box.delete(0.0, 'end')
        self.weight_box.insert("0.0",weight_string)
        self.weight_box.configure(state="disabled")
        self.plot_weight = customtkinter.CTkButton(self.weight_frame, text="Plot", font=customtkinter.CTkFont(size=18), 
                                                   command=lambda d=[float(item[:-4]) for item in file_contents_weight]: plot_weight(d), width=140)
        self.plot_weight.grid(row=2, column=2, padx=(10, 10), pady=(5, 10), sticky="nsew")

        heart_rate = os.path.join(file_path, "heart_rate.txt")
        with open(heart_rate, 'r') as file:
            file_contents_heart_rate = file.readlines()
        heart_rate_string = "\n".join(file_contents_heart_rate)
        self.heart_rate_box.delete(0.0, 'end')
        self.heart_rate_box.insert("0.0",heart_rate_string)
        self.plot_weight = customtkinter.CTkButton(self.heart_rate_frame, text="Plot", font=customtkinter.CTkFont(size=18), 
                                                   command=lambda d=[float(item) for item in file_contents_heart_rate]: plot_heart_rate(d), width=140)
        self.plot_weight.grid(row=2, column=2, padx=(10, 10), pady=(5, 10), sticky="nsew")

        blood_pressure = os.path.join(file_path, "blood_pressure.txt")
        with open(blood_pressure, 'r') as file:
            file_contents_blood_pressure = file.readlines()
        blood_pressure_string = "\n".join(file_contents_blood_pressure)
        self.blood_pressure_box.delete(0.0, 'end')
        self.blood_pressure_box.insert("0.0",blood_pressure_string)
        self.blood_pressure_box.configure(state="disabled")
        self.plot_weight = customtkinter.CTkButton(self.blood_pressure_frame, text="Plot", font=customtkinter.CTkFont(size=18), 
                                                   command=lambda d=[float(item) for item in file_contents_blood_pressure]: plot_blood_pressure(d), width=140)
        self.plot_weight.grid(row=2, column=2, padx=(10, 10), pady=(5, 10), sticky="nsew")

        blood_sugar = os.path.join(file_path, "blood_sugar.txt")
        with open(blood_sugar, 'r') as file:
            file_contents_blood_sugar = file.readlines()
        blood_sugar_string = "\n".join(file_contents_blood_sugar)
        self.blood_sugar_box.delete(0.0, 'end')
        self.blood_sugar_box.insert("0.0",blood_sugar_string)
        self.blood_sugar_box.configure(state="disabled")
        self.plot_weight = customtkinter.CTkButton(self.blood_sugar_frame, text="Plot", font=customtkinter.CTkFont(size=18), 
                                                   command=lambda d=[float(item) for item in file_contents_blood_sugar]: plot_blood_sugar(d), width=140)
        self.plot_weight.grid(row=2, column=2, padx=(10, 10), pady=(5, 10), sticky="nsew")

        cholesterol = os.path.join(file_path, "cholesterol.txt")
        with open(cholesterol, 'r') as file:
            file_contents_cholesterol = file.readlines()
        cholesterol_string = "\n".join(file_contents_cholesterol)
        self.cholesterol_box.delete(0.0, 'end')
        self.cholesterol_box.insert("0.0",cholesterol_string)
        self.cholesterol_box.configure(state="disabled")
        self.plot_weight = customtkinter.CTkButton(self.cholesterol_frame, text="Plot", font=customtkinter.CTkFont(size=18), 
                                                   command=lambda d=[float(item) for item in file_contents_cholesterol]: plot_cholesterol(d), width=140)
        self.plot_weight.grid(row=2, column=2, padx=(10, 10), pady=(5, 10), sticky="nsew")

        def plot_weight(file_contents_weight):
            root = customtkinter.CTk()
            root.title("Weight Plot")
            frame = customtkinter.CTkFrame(root)
            frame.pack(expand=True, fill='both')
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(file_contents_weight)
            ax.set_ylabel('Weight (in Kg)')
            ax.set_title('Weight Plot')
            plt.show()

        def plot_blood_pressure(file_contents_blood_pressure):
            root = customtkinter.CTk()
            root.title("Blood Pressure Plot")
            frame = customtkinter.CTkFrame(root)
            frame.pack(expand=True, fill='both')
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(file_contents_blood_pressure)
            ax.set_ylabel('Blood Pressure')
            ax.set_title('Blood Pressure Plot')
            plt.show()

        def plot_heart_rate(file_contents_heart_rate):
            root = customtkinter.CTk()
            root.title("Heart Rate Plot")
            frame = customtkinter.CTkFrame(root)
            frame.pack(expand=True, fill='both')
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(file_contents_heart_rate)
            ax.set_ylabel('Heart Rate')
            ax.set_title('Heart Rate Plot')
            plt.show()

        def plot_blood_sugar(file_contents_blood_sugar):
            root = customtkinter.CTk()
            root.title("Blood Sugar Plot")
            frame = customtkinter.CTkFrame(root)
            frame.pack(expand=True, fill='both')
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(file_contents_blood_sugar)
            ax.set_ylabel('Blood Sugar')
            ax.set_title('Blood Sugar Plot')
            plt.show()

        def plot_cholesterol(file_contents_cholesterol):
            root = customtkinter.CTk()
            root.title("Cholesterol Plot")
            frame = customtkinter.CTkFrame(root)
            frame.pack(expand=True, fill='both')
            fig = plt.figure()
            ax = fig.add_subplot(111)
            ax.plot(file_contents_cholesterol)
            ax.set_ylabel('Cholesterol')
            ax.set_title('Cholesterol Plot')
            plt.show()

def pos(c,r):
    if c < 2:
        c = c + 1
    else:
        c = 0
        r = r + 1
    return c,r
    
class conversation(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
        self.grid(row=0, column=1, columnspan=3, rowspan=4, padx=0, pady=0, sticky="nsew")
        self.grid_columnconfigure((0,1), weight=1)
        self.grid_rowconfigure((0,1), weight=1)
        self.controller = controller
        self.frame_1 = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_1.pack(expand=True)
        
        self.connect_button = customtkinter.CTkButton(self.frame_1, text="Connect with Doctor", width=140, command=lambda:self.conn())
        self.connect_button.pack(padx=(10,10), pady=(10,10),)

    def conn(self):
        file_transfer.send_file()
        for widget in self.frame_1.winfo_children():
            widget.destroy()
        self.update_health_metrics = customtkinter.CTkButton(self.frame_1, text="Update Health Metrics", font=customtkinter.CTkFont(size=15), width=140, command=lambda : self.update_metrics())
        self.update_health_metrics.pack(padx=(10,10), pady=(10,5))
        self.update_medical_history = customtkinter.CTkButton(self.frame_1, text="Update Medical History", font=customtkinter.CTkFont(size=15), width=140, command=lambda : self.update_m_history())
        self.update_medical_history.pack(padx=(10,10), pady=(5,5))
        self.update_medicine = customtkinter.CTkButton(self.frame_1, text="Update Medicine", font=customtkinter.CTkFont(size=15), width=140, command=lambda : self.update_mediciene())
        self.update_medicine.pack(padx=(10,10), pady=(5,10))
        
    def update_metrics(self):
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host, port))
        s.listen(1)
        conn,addr=s.accept()

        received_data = b""
        while True:
            data_chunk = conn.recv(2048)
            if not data_chunk:
                break
            received_data += data_chunk

        conn.close()
        s.close()   

        json_file_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\key.json"
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        key = data[p]
        key = base64.urlsafe_b64decode(key)
        cipher_suite = Fernet(key)
        received_data = cipher_suite.decrypt(received_data)
        received_data = received_data.decode('utf-8')

        data = received_data.split("$$$$$$$$")
        # file_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\User\\Initializing"
        file_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\User\\"
        file_path = os.path.join(file_path, p)
        file_paths = [
                "weight.txt",
                "blood_pressure.txt",
                "heart_rate.txt",
                "blood_sugar.txt",
                "cholesterol.txt",
            ]
        i = 0
        for f in file_paths:
            f_path = os.path.join(file_path, f)
            data[i] = data[i].encode('utf-8')
            received_data = cipher_suite.encrypt(data[i])
            with open(f_path, "wb") as file:
                file.write(received_data)
            i = i + 1

    def update_m_history(self):
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host, port))
        s.listen(1)
        conn,addr=s.accept()

        received_data = b""
        while True:
            data_chunk = conn.recv(2048)
            if not data_chunk:
                break
            received_data += data_chunk

        conn.close()
        s.close()

        json_file_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\key.json"
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        key = data[p]
        key = base64.urlsafe_b64decode(key)
        cipher_suite = Fernet(key)
        received_data = cipher_suite.decrypt(received_data)
        received_data = received_data.decode('utf-8')
        received_data = received_data.encode('utf-8')
        received_data = cipher_suite.encrypt(received_data)

        file_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\User"
        file_path = os.path.join(file_path, p)
        file_path = os.path.join(file_path, "medical_diagnosis.txt")
        with open(file_path, "wb") as file:
            file.write(received_data)

    def update_mediciene(self):
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host, port))
        s.listen(1)
        conn,addr=s.accept()

        received_data = b""
        while True:
            data_chunk = conn.recv(2048)
            if not data_chunk:
                break
            received_data += data_chunk

        conn.close()
        s.close() 

        json_file_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\key.json"
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)
        key = data[p]
        key = base64.urlsafe_b64decode(key)
        cipher_suite = Fernet(key)
        received_data = cipher_suite.decrypt(received_data)
        received_data = received_data.decode('utf-8')
        received_data = received_data.encode('utf-8')
        received_data = cipher_suite.encrypt(received_data)

        file_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\User"
        file_path = os.path.join(file_path, p)
        file_path = os.path.join(file_path, "medicine.txt")
        with open(file_path, "wb") as file:
            file.write(received_data)

    def con_button(self):
        for widget in self.frame_1.winfo_children():
            widget.destroy()
        self.connect_new_doctor = customtkinter.CTkButton(self.frame_1, text="Connect with a new Doctor", width=140, command=lambda:self.connect_n_doctor())
        self.connect_new_doctor.pack(padx=(10,10), pady=(10,5))
        self.connect_button = customtkinter.CTkButton(self.frame_1, text="Connect with Doctor", width=140, command=lambda:self.conn())
        self.connect_button.pack(padx=(10,10), pady=(5,10))

    def connect_n_doctor(self):
        json_file_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\main\\key.json"
        with open(json_file_path, 'r') as json_file:
            data = json.load(json_file)

        data = data[p]
        print(data)
        print(type(data))
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host, port))
        s.listen(1)
        # print(host)
        print("Waiting for any incoming connections...")
        conn,addr=s.accept()
        data_bytes = data.encode('utf-8')  
        conn.send(data_bytes)
        conn.close()
        s.close()
















# Add a refresh button
#     refresh_button = customtkinter.CTkButton(self.frame_1, text="Refresh List", command=self.refresh_directory_list)
#     refresh_button.grid(row=0, column=0, padx=10, pady=10)
#     self.refresh_directory_list()

# def refresh_directory_list(self):
#     for widget in self.frame_1.winfo_children():
#         widget.destroy()

#     print(p)
#     r = 1  # Start from row 1 to place the buttons
#     c = 0
#     target_directory = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\User\\"+str(p)+"\\Doctor\\"
#     print(target_directory)
#     all_items = os.listdir(target_directory)

#     for d in all_items:
#         button = customtkinter.CTkButton(self.frame_1, text=d[:-4])
#         button.grid(row=r, column=c, padx=10, pady=10)
#         c, r = pos(c, r)

#     add_user_button = customtkinter.CTkButton(self.frame_1, text="Connect with a new Doctor")
#     add_user_button.grid(row=r, column=c, padx=10, pady=10)

# s=socket.socket()
# host=socket.gethostname()
# port=8080
# s.bind((host, port))
# s.listen(1)
# print(host)
# print("Waiting for any incoming connections...")
# conn,addr=s.accept()
# file_path = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\User"
# file_path = os.path.join(file_path, p)

# file_path_medical_diagnosis = os.path.join(file_path, "medical_diagnosis.txt")
# file=open(file_path_medical_diagnosis, 'rb')
# file_data=file.read(1024)
# conn.send(file_data)
# file.close()
# print("Data has been transmitted successfully")

# file_path_medicine = os.path.join(file_path, "medicine.txt")
# file=open(file_path_medicine, 'rb')
# file_data=file.read(1024)
# conn.send(file_data)
# file.close()
# print("Data has been transmitted successfully")

# file_path_blood_pressure = os.path.join(file_path, "blood_pressure.txt")
# file=open(file_path_blood_pressure, 'rb')
# file_data=file.read(1024)
# conn.send(file_data)
# file.close()
# print("Data has been transmitted successfully")

# file_path_blood_sugar = os.path.join(file_path, "blood_sugar.txt")
# file=open(file_path_blood_sugar, 'rb')
# file_data=file.read(1024)
# conn.send(file_data)
# file.close()
# print("Data has been transmitted successfully")

# file_path_cholesterol = os.path.join(file_path, "cholesterol.txt")
# file=open(file_path_cholesterol, 'rb')
# file_data=file.read(1024)
# conn.send(file_data)
# file.close()
# print("Data has been transmitted successfully")

# file_path_heart_rate = os.path.join(file_path, "heart_rate.txt")
# file=open(file_path_heart_rate, 'rb')
# file_data=file.read(1024)
# conn.send(file_data)
# file.close()
# print("Data has been transmitted successfully")

# file_path_weight = os.path.join(file_path, "weight.txt")
# file=open(file_path_weight, 'rb')
# file_data=file.read(1024)
# conn.send(file_data)
# file.close()
# print("Data has been transmitted successfully")








# class home(customtkinter.CTkFrame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, corner_radius=0)
#         self.grid(row=0, column=1, columnspan=3, rowspan=4, padx=0, pady=0, sticky="nsew")
#         self.grid_rowconfigure((0, 1), weight=1)
#         # parent.grid_rowconfigure(0, weight=1)
#         # parent.grid_columnconfigure(1, weight=1)  
#         self.grid_columnconfigure(0, weight=1)  
#         self.grid_columnconfigure(1, weight=1)

#         self.medical_history = customtkinter.CTkTextbox(self, width=250)
#         self.medical_history.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 10), sticky="nsew")
#         self.medicine = customtkinter.CTkTextbox(self, width=250)
#         self.medicine.grid(row=1, column=0, padx=(10,10), pady=(10, 10), sticky="nsew")
#         self.medicine_Link = customtkinter.CTkFrame(self, width=250)
#         self.medicine_Link.grid(row=1, column=1, padx=(10,10), pady=(10,10), sticky="nsew")

# class home(customtkinter.CTkFrame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, corner_radius=0)
#         self.grid(row=0, column=1, columnspan=3, rowspan=4, padx=0, pady=0, sticky="nsew")
#         self.grid_rowconfigure((0, 1), weight=1)
#         parent.grid_rowconfigure(0, weight=1)
#         parent.grid_columnconfigure(1, weight=1)  
#         self.grid_columnconfigure(0, weight=1)  
#         self.grid_columnconfigure(1, weight=1)  
#         self.medical_history = customtkinter.CTkTextbox(self, width=250)
#         self.medical_history.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="nsew")
#         file_path = 'D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\User\\medical_diagnosis.txt'
#         with open(file_path, 'r') as file:
#             file_contents = file.read()
#         self.medical_history.insert("0.0", "Medical History\n\n" + file_contents)
#         self.medicine = customtkinter.CTkTextbox(self, width=250)
#         self.medicine.grid(row=1, column=0, padx=(20,10), pady=(10, 20), sticky="nsew")
#         self.medicine_history = customtkinter.CTkFrame(self, width=250)
#         self.medicine_history.grid(row=1, column=1, padx=(10,20), pady=(10,20), sticky="nsew")


# class health_metrics(customtkinter.CTkFrame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, corner_radius=0)
#         self.grid(row=0, column=1, columnspan=3, rowspan=4, padx=0, pady=0, sticky="nsew")
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)

# class conversation(customtkinter.CTkFrame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, corner_radius=0)
#         self.grid(row=0, column=1, columnspan=3, rowspan=4, padx=0, pady=0, sticky="nsew")
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)

# if __name__ == "__main__":
#     Patient.path = "meghal"  
#     app = Patient()
#     app.mainloop()

# customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


# class Patient(customtkinter.CTkFrame):

# class Patient(customtkinter.CTk):
# class Patient(customtkinter.CTkFrame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, corner_radius=0)
#         parent.grid_rowconfigure(0, weight=10)
#         parent.grid_columnconfigure(0, weight=1)  
#         parent.grid_columnconfigure(1, weight=1)
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=8)
#         self.grid_columnconfigure(2, weight=7)
#         self.grid_rowconfigure((0, 1, 2), weight=1)

#         self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
#         self.sidebar_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
#         self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
#         self.sidebar_frame.grid_rowconfigure(4, weight=1)
#         self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="MediConnect", font=customtkinter.CTkFont(size=30, weight="bold"))
#         self.logo_label.pack(pady=15)
#         self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Home", font=customtkinter.CTkFont(size=15), command=lambda: self.show_frame(patient_1.home), width=140)
#         self.sidebar_button_1.pack(pady=10)
#         self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Health Metrics", font=customtkinter.CTkFont(size=15), command=lambda: self.show_frame(patient_1.health_metrics), width=140)
#         self.sidebar_button_2.pack(pady=10)
#         self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, text="Conversation", font=customtkinter.CTkFont(size=15), command=lambda: self.show_frame(patient_1.conversation), width=140)
#         self.sidebar_button_3.pack(pady=10)

#         self.main_frame.grid(row=0, column=1, columnspan=2, rowspan=4, padx=18, pady=20, sticky="nsew")
#         self.frames = {}
#         for F in (patient_1.home, patient_1.health_metrics, patient_1.conversation):
#             frame = F(self.main_frame, self)

#             self.frames[F] = frame
#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame(patient_1.home)

#     def show_frame(self, cont):
#         frame = self.frames[cont]
#         frame.tkraise()

# parent.columnconfigure(0, weight=1)
# parent.rowconfigure(0, weight=1)
# print(self.path)
# path = "Meghal"