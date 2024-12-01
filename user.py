import customtkinter
import patient
import os
import new_user

def pos(c,r):
    if c < 2:
        c = c + 1
    else:
        c = 0
        r = r + 1
    return c,r

class User(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, corner_radius=0)
        self.controller = controller
        self.frame_1 = customtkinter.CTkFrame(self, corner_radius=0)
        self.frame_1.pack(expand=True)
        
        # Add a refresh button
        refresh_button = customtkinter.CTkButton(self.frame_1, text="Refresh List", command=self.refresh_directory_list)
        refresh_button.grid(row=0, column=0, padx=10, pady=10)
        
        # Initially, populate the list of directories
        self.refresh_directory_list()

    def refresh_directory_list(self):
        # Clear existing buttons
        for widget in self.frame_1.winfo_children():
            widget.destroy()
        
        r = 1  # Start from row 1 to place the buttons
        c = 0
        target_directory = "C:\\Users\\Yash\\OneDrive\\Desktop\\main\\User"
        all_items = os.listdir(target_directory)
        # directories = [item for item in all_items if os.path.isdir(os.path.join(target_directory, item))]
        
        for d in all_items:
            if d != "Initializing":
                button = customtkinter.CTkButton(self.frame_1, text=d, command=lambda dir=d: self.controller.show_frame(patient.Patient, dir))
                button.grid(row=r, column=c, padx=10, pady=10)
                c, r = pos(c, r)
        
        add_user_button = customtkinter.CTkButton(self.frame_1, text="Add new User", command=lambda dir="Initializing": self.controller.show_frame(new_user.new_user, dir))
        add_user_button.grid(row=r, column=c, padx=10, pady=10)







# width=150, height=80
# class User(customtkinter.CTkFrame):
#     def __init__(self, parent, controller):
#         super().__init__(parent, corner_radius=0)
#         frame_1 = customtkinter.CTkFrame(self, corner_radius=0)
#         frame_1.pack(expand=True)
#         r = 0
#         c = 0
#         target_directory = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\User"
#         all_items = os.listdir(target_directory)
#         directories = [item for item in all_items if os.path.isdir(os.path.join(target_directory, item))]
#         for d in directories:
#             if d != "Initializing":
#                 button = customtkinter.CTkButton(frame_1, text=d, command=lambda dir=d: controller.show_frame(patient.Patient, dir))
#                 button.grid(row=r, column=c, padx=10, pady=10)
#                 c, r = pos(c,r)
#         button = customtkinter.CTkButton(frame_1, text="Add new User", command=lambda dir="Initializing": controller.show_frame(new_user.new_user, dir))
#         button.grid(row=r, column=c, padx=10, pady=10)


# target_directory = "D:\\PDEU\\Sem-5\\9) Python & Information Security Project\\User"
# all_items = os.listdir(target_directory)
# directories = [item for item in all_items if os.path.isdir(os.path.join(target_directory, item))]