import tkinter as tk

root=tk.Tk()

root.geometry("600x400")

name_var=tk.StringVar()
passw_var=tk.StringVar()

def submit():

	name=name_var.get()
	password=passw_var.get()
	
	print("The name is : " + name)
	print("The password is : " + password)
	
	name_var.set("")
	passw_var.set("")

main_label = tk.Label(root, text="ĐĂNG NHẬP")
	
name_label = tk.Label(root, text = 'Tên đăng nhập')

name_entry = tk.Entry(root,textvariable = name_var)

passw_label = tk.Label(root, text = 'Mật khẩu')


passw_entry=tk.Entry(root, textvariable = passw_var, show = '*')

sub_btn=tk.Button(root,text = 'Đăng nhập', command = submit)


main_label.grid(row=1, column=5)
name_label.grid(row=3,column=4)
name_entry.grid(row=3,column=5)
passw_label.grid(row=4,column=4)
passw_entry.grid(row=4,column=5)
sub_btn.grid(row=5,column=5)

root.mainloop()
