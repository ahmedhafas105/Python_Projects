import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import os

def show_message():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    city = city_entry.get()
    education_state = education_entry.get()

    if not first_name or not last_name or not age or not city or not education_state:
        messagebox.showwarning("Warning", "Please fill in all fields.")
        return

    message = f"First Name: {first_name}\nLast Name: {last_name}\nAge: {age}\nCity: {city}\nEducation: {education_state}"
    
    # Clear previous content in the card_info
    for widget in card_info.winfo_children():
        widget.destroy()
    
    message_label = tk.Label(card_info, text=message, font=("Aptos", 14), justify=tk.LEFT, bg="#E6E6FA")
    message_label.pack(pady=20)

    if profile_image_path:
        img = Image.open(profile_image_path)
        img.thumbnail((150, 150))  # Resize image
        photo = ImageTk.PhotoImage(img)
        profile_picture_label = tk.Label(card_info, image=photo, bg="#E6E6FA")
        profile_picture_label.image = photo  # Keep a reference to prevent garbage collection
        profile_picture_label.pack(pady=10)

def upload_picture():
    global profile_image_path
    profile_image_path = filedialog.askopenfilename()
    if profile_image_path:
        messagebox.showinfo("Success", "Profile picture uploaded successfully!")

def load_wallpaper():
    global wallpaper_path
    wallpaper_path = filedialog.askopenfilename()
    if wallpaper_path:
        set_wallpaper()

def set_wallpaper():
    global wallpaper_path
    if wallpaper_path:
        img = Image.open(wallpaper_path)
        img = img.resize((root.winfo_width(), 200), Image.LANCZOS)  # Increase height to 200
        wallpaper = ImageTk.PhotoImage(img)
        wallpaper_label.config(image=wallpaper)
        wallpaper_label.image = wallpaper  # Keep a reference to prevent garbage collection

def set_default_wallpaper():
    global wallpaper_path
    if not wallpaper_path:
        default_wallpaper = "D:/MEGA-Ahmed/Wallpaper/wallpapersden.com_landscape-4k-glowing-light-road_1366x768.jpg"  # Replace with your default wallpaper path
        if os.path.exists(default_wallpaper):
            wallpaper_path = default_wallpaper
            set_wallpaper()

# Create the main window
root = tk.Tk()
root.title("User Information Form")
root.geometry("1000x600")

# Create a label to hold the wallpaper at the top
wallpaper_label = tk.Label(root)
wallpaper_label.pack(fill="x", ipady=20)  # Increase the height of the wallpaper area

# Add a heading "AI World" below the wallpaper
heading_label = tk.Label(root, text="Python GUI", font=("Georgia Bold", 50))
heading_label.pack()

# Create a frame to hold form and display information
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Create card-like frames with borders for the form and info sections
card_form = tk.Frame(main_frame, bd=2, relief="groove", padx=20, pady=20, bg="#F5FFFA")
card_form.place(relwidth=0.7, relheight=1.0)

card_info = tk.Frame(main_frame, bd=2, relief="groove", padx=20, pady=20, bg="#E6E6FA")
card_info.place(relx=0.7, relwidth=0.3, relheight=1.0)

# Common font for labels and entry widgets
font_label = ("Aptos", 14)
font_entry = ("Aptos", 12)

# Create labels and entry widgets for user information
tk.Label(card_form, text="First Name:", font=font_label, bg="#F5FFFA").grid(row=0, column=0, pady=10, sticky="e")
first_name_entry = tk.Entry(card_form, font=font_entry, width=30, highlightbackground="black", highlightcolor="black", highlightthickness=1)
first_name_entry.grid(row=0, column=1, padx = 10, pady = 10)

tk.Label(card_form, text="Last Name:", font=font_label, bg="#F5FFFA").grid(row=1, column=0, pady=10, sticky="e")
last_name_entry = tk.Entry(card_form, font=font_entry, width=30, highlightbackground="black", highlightcolor="black", highlightthickness=1)
last_name_entry.grid(row=1, column=1, pady=10, padx=10)

tk.Label(card_form, text="Age:", font=font_label, bg="#F5FFFA").grid(row=2, column=0, pady=10, sticky="e")
age_entry = tk.Entry(card_form, font=font_entry, width=30, highlightbackground="black", highlightcolor="black", highlightthickness=1)
age_entry.grid(row=2, column=1)

tk.Label(card_form, text="City:", font=font_label, bg="#F5FFFA").grid(row=3, column=0, pady=10, sticky="e")
city_entry = tk.Entry(card_form, font=font_entry, width=30, highlightbackground="black", highlightcolor="black", highlightthickness=1)
city_entry.grid(row=3, column=1)

tk.Label(card_form, text="Current Education State:", font=font_label, bg="#F5FFFA").grid(row=4, column=0, pady=10, sticky="e")
education_entry = tk.Entry(card_form, font=font_entry, width=30, highlightbackground="black", highlightcolor="black", highlightthickness=1)
education_entry.grid(row=4, column=1, padx = 10, pady = 10)

# Create a frame to hold the buttons side by side
button_frame = tk.Frame(card_form, bg="#F5FFFA")
button_frame.grid(row=2, column=3, sticky="nsew")

# Create a button for uploading profile picture
upload_button = tk.Button(button_frame, text="Upload Profile Picture", font=font_label, command=upload_picture, width=25)
upload_button.grid(row=2, column=3, padx = (10), pady = 0)

# Create a button that will display the user information
button = tk.Button(button_frame, text="Submit", font=font_label, command=show_message, width=25)
button.grid(row=3, column=3, padx = (10), pady = 0)

# Variable to store the paths of the uploaded images
profile_image_path = None
wallpaper_path = None

# Set default wallpaper on startup
root.after(100, set_default_wallpaper)

# Make the form window responsive
def on_resize(event):
    if wallpaper_path:
        set_wallpaper()

root.bind('<Configure>', on_resize)

# Run the application
root.mainloop()