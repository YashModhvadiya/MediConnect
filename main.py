import customtkinter
import patient
import user
import new_user
import os
import key

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class mainApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("MediConnect")
        self.geometry(f"{1100}x{580}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (patient.Patient, user.User, new_user.new_user):
            frame = F(self.main_frame, self)

            self.frames[F] = frame
            frame.columnconfigure(0, weight=1)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(user.User, "Initializing")

    def show_frame(self, cont, dir):
        # print(dir)
        file_path = 'C:\\Users\\Yash\\OneDrive\\Desktop\\main\\User\\Initializing'
        if dir != "Initializing":
            key.decrypt(dir)
        # file_path = os.path.join(file_path,dir)
        medical_history = os.path.join(file_path, "medical_diagnosis.txt")
        with open(medical_history, 'r') as file:
            file_contents_medical_history = file.read()
        medicine = os.path.join(file_path, "medicine.txt")
        with open(medicine, 'r') as file:
            file_contents_medicine = file.read()
        home_instance = self.frames[patient.Patient].frames[patient.home]
        home_instance.medical_history.delete(0.0, 'end')
        home_instance.medical_history.insert("0.0",file_contents_medical_history)
        home_instance.medicine.delete(0.0, 'end')
        home_instance.medicine.insert("0.0", file_contents_medicine)
        self.frames[patient.Patient].show_frame(patient.home)
        patient.p = dir
        patient.home.intial(home_instance)
        health_metrics = self.frames[patient.Patient].frames[patient.health_metrics]
        health_metrics.update(dir)
        conversation = self.frames[patient.Patient].frames[patient.conversation]
        conversation.con_button()
        frame = self.frames[cont]
        frame.tkraise()

if __name__ == "__main__":
    app = mainApp()
    app.mainloop()

# Edit personal Details
# self.frames[patient.Patient].frames[patient.conversation].refresh_directory_list()
# patient.Patient.main_frame.medical_history.insert("0.0", "Medical History\n\n" + file_contents)
# frame = self.frames[cont]
# home_instance = self.frames[patient.home]  # Create an instance of the home class
# home_instance.medical_history.insert("0.0", "Medical History\n\n" + file_contents)
# +dir+'\\medical_diagnosis.txt'
# "medical_diagnosis.txt"