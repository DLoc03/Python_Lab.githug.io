import tkinter as tk
from tkinter.ttk import Style, Frame
from tkinter import ttk

root=tk.Tk()

root.geometry("640x400")

root.columnconfigure(0, pad=4)

root.title("Đăng ký thông tin")

name_var=tk.StringVar()
mssv_var=tk.StringVar()
ngaySinh_var = tk.StringVar()
email_var = tk.StringVar()
sdt_var = tk.StringVar()
hk_var = tk.StringVar()

def submit():
    name = name_var.get()
    mssv = mssv_var.get()
    ngaySinh = ngaySinh_var.get()
    email = email_var.get()
    sdt = sdt_var.get()
    hk = hk_var.get()
    namHoc = namHoc_cbb.get()
    
    print(f"Mã số: {mssv}")
    print(f"Họ và tên: {name}")
    print(f"Ngày sinh: {ngaySinh}")
    print(f"Email: {email}")
    print(f"Số điện thoại: {sdt}")
    print(f"Năm học: {namHoc}")
    
    name_var.set("")
    mssv_var.set("")
    ngaySinh.set("")
    email.set("")
    sdt.set("")
    hk_var.set("")
    namHoc_cbb.current(0)

lblMain = tk.Label(text="THÔNG TIN ĐĂNG KÝ HỌC PHẦN", foreground='red', font=('Times New Roman', 16, 'bold')).grid(row = 0, column=2, pady=20, sticky="W")

lbl_mssv = tk.Label(text="Mã số sinh viên").grid(row = 1, column=1, sticky="W")
mssv_entry = tk.Entry(root, textvariable=mssv_var, width=40).grid(row=1, column=2, sticky="W")

lbl_name = tk.Label(text="Họ và tên sinh viên").grid(row = 2, column=1, sticky="W")
name_entry = tk.Entry(root, textvariable=name_var, width=40).grid(row = 2, column=2, sticky="W")

lbl_ngaySinh = tk.Label(text="Ngày sinh").grid(row=3, column=1, sticky="W")
ngaySinh_entry = tk.Entry(root, textvariable=ngaySinh_var, width=40).grid(row=3, column=2, sticky="W")

lbl_email = tk.Label(text="Email").grid(row=4, column=1, sticky="W")
email_entry = tk.Entry(root, textvariable=email_var, width=40).grid(row=4,column=2, sticky="W")

lbl_sdt = tk.Label(text="Số điện thoại").grid(row = 5, column=1, sticky="W")
sdt_entry = tk.Entry(root, textvariable=sdt_var, width=40).grid(row = 5, column=2, sticky="W")

lbl_hk = tk.Label(text="Học kỳ").grid(row=6, column=1, sticky="W")
hk_entry = tk.Entry(root, textvariable=hk_var, width=40).grid(row = 6, column= 2, sticky="W")

lbl_namHoc = tk.Label(text="Năm học").grid(row=7, column=1, sticky="W")

n = tk.StringVar()
namHoc_cbb = ttk.Combobox(root, width=37, textvariable=n)
namHoc_cbb['values']= ('2021', '2022', '2023', '2024')
namHoc_cbb.current(0)
namHoc_cbb.grid(row = 7, column=2, sticky="W")

lbl_chonMon = tk.Label(text="Chọn môn học").grid(row = 8, column=1, sticky="W")

py_check = tk.Checkbutton(text="Lập trình Python").grid(row = 9, column=2, sticky="W")
jav_check = tk.Checkbutton(text="Lập trình Java").grid(row = 9, column=3, sticky="W")
cnpm_check = tk.Checkbutton(text="Công nghệ phần mềm").grid(row = 10, column=2, sticky="W")
ptudw_check = tk.Checkbutton(text="Phát triển ứng dụng Web").grid(row = 10, column=3, sticky="W")

btn_dangKi = tk.Button(text="Đăng ký", command=submit).grid(row = 11, column= 2, sticky="W")
btn_thoat = tk.Button(text = "Thoát", command=exit).grid(row=11, column=3, sticky="W")



root.mainloop()