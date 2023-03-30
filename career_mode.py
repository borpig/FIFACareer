import tkinter as tk

class MYGUI:

	def __init__(self):
		self.root = tk.Tk()

		self.root.title("FIFA Realism Calculator GUI")
		self.root.geometry("500x500")

		self.label = tk.Label(self.root, text="FIFA Realism Calculator", font=('Arial', 14))
		self.label.pack(padx=20, pady=20)

		self.label2 = tk.Label(self.root, text="What do you want to do?", font=('Arial', 14))
		self.label2.pack(padx=20, pady=20)

		self.btn1 = tk.Button(self.root, text="Calculate Team Rating", font=('Arial', 14), command=self.go_to_team_rating)
		self.btn1.pack(padx=20, pady=20)

		self.btn2 = tk.Button(self.root, text="Calculate Offer Price", font=('Arial', 14), command=self.go_to_offer_price)
		self.btn2.pack(padx=20, pady=20)

		self.btn3 = tk.Button(self.root, text="Calculate Selling Price", font=('Arial', 14), command=self.go_to_selling_price)
		self.btn3.pack(padx=20, pady=20)

		self.root.mainloop()

	def go_to_team_rating(self):
		self.top = tk.Toplevel()
		self.top.title('Team Rating Calculator')

		self.label1 = tk.Label(self.top, text="P1", font=('Arial', 14))
		self.label1.pack()
		self.entry = tk.Entry(self.top)
		self.entry.pack()

		self.label2 = tk.Label(self.top, text="P2", font=('Arial', 14))
		self.label2.pack()
		self.entry2 = tk.Entry(self.top)
		self.entry2.pack()

		self.label3 = tk.Label(self.top, text="P3", font=('Arial', 14))
		self.label3.pack()
		self.entry3 = tk.Entry(self.top)
		self.entry3.pack()

		self.label4 = tk.Label(self.top, text="P4", font=('Arial', 14))
		self.label4.pack()
		self.entry4 = tk.Entry(self.top)
		self.entry4.pack()

		self.label5 = tk.Label(self.top, text="P5", font=('Arial', 14))
		self.label5.pack()
		self.entry5 = tk.Entry(self.top)
		self.entry5.pack()

		self.label6 = tk.Label(self.top, text="P6", font=('Arial', 14))
		self.label6.pack()
		self.entry6 = tk.Entry(self.top)
		self.entry6.pack()

		self.label7 = tk.Label(self.top, text="P7", font=('Arial', 14))
		self.label7.pack()
		self.entry7 = tk.Entry(self.top)
		self.entry7.pack()

		self.label8 = tk.Label(self.top, text="P8", font=('Arial', 14))
		self.label8.pack()
		self.entry8 = tk.Entry(self.top)
		self.entry8.pack()

		self.label9 = tk.Label(self.top, text="P9", font=('Arial', 14))
		self.label9.pack()
		self.entry9 = tk.Entry(self.top)
		self.entry9.pack()

		self.label10 = tk.Label(self.top, text="P10", font=('Arial', 14))
		self.label10.pack()
		self.entry10 = tk.Entry(self.top)
		self.entry10.pack()

		self.label11 = tk.Label(self.top, text="P11", font=('Arial', 14))
		self.label11.pack()
		self.entry11 = tk.Entry(self.top)
		self.entry11.pack()

		self.btn1 = tk.Button(self.top, text="Calculate Team Rating", font=('Arial', 14), command=self.calculate_team_rating)
		self.btn1.pack()

	def calculate_team_rating(self):
		calculated_value = tk.Label(self.top, text=((int(self.entry.get())+int(self.entry2.get())+int(self.entry3.get())+int(self.entry4.get())+int(self.entry5.get())+int(self.entry6.get())+int(self.entry7.get())+int(self.entry8.get())+int(self.entry9.get())+int(self.entry10.get())+int(self.entry11.get()))/11), font=('Arial', 20))
		#calculated_value = tk.Label(self.top, text=(int(total_value//11)), font=('Arial', 20))
		calculated_value.pack()

	def go_to_offer_price(self):
		self.top = tk.Toplevel()
		self.top.title('Offer Price Calculator')

		self.label1 = tk.Label(self.top, text="Age of Player", font=('Arial', 14))
		self.label1.pack()
		self.entry = tk.Entry(self.top)
		self.entry.pack()

		self.label2 = tk.Label(self.top, text="Player Value", font=('Arial', 14))
		self.label2.pack()
		self.entry2 = tk.Entry(self.top)
		self.entry2.pack()

		self.btn1 = tk.Button(self.top, text="Calculate Offer Price", font=('Arial', 14), command=self.calculate_offer_price)
		self.btn1.pack()

	def calculate_offer_price(self):
		if 16 <= int(self.entry.get()) <= 24:
			calculated_offer_price = 1.8 * int(self.entry2.get())
		elif 25 <= int(self.entry.get()) <= 29:
			calculated_offer_price = 1.5 * int(self.entry2.get())
		else:
			calculated_offer_price = calculated_offer_price
		calculated_offer_price = tk.Label(self.top, text=f"{calculated_offer_price}", font=('Arial', 20))
		calculated_offer_price.pack()

	def go_to_selling_price(self):
		self.top = tk.Toplevel()
		self.variable = tk.StringVar()
		self.top.title('Selling Price Calculator')


		OPTIONS = ["Starting",
		"Bench",
		"Reserve"]

		self.variable.set(OPTIONS[0]) #default value

		w = tk.OptionMenu(self.top, self.variable, *OPTIONS)
		w.pack()

		self.label1 = tk.Label(self.top, text="Age of Player", font=('Arial', 14))
		self.label1.pack()
		self.entry = tk.Entry(self.top)
		self.entry.pack()

		self.label2 = tk.Label(self.top, text="Player Value", font=('Arial', 14))
		self.label2.pack()
		self.entry2 = tk.Entry(self.top)
		self.entry2.pack()

		self.btn1 = tk.Button(self.top, text="Calculate Selling Price", font=('Arial', 14), command=self.calculate_selling_price)
		self.btn1.pack()


	def calculate_selling_price(self):
		if self.variable.get() == "Starting":
			if 16 <= int(self.entry.get()) <= 21:
				calculated_selling_price = 2.25 * int(self.entry2.get())
			else:
				calculated_selling_price = 2 * int(self.entry2.get())
		elif self.variable.get() == "Bench":
			if 16 <= int(self.entry.get()) <= 21:
				calculated_selling_price = 2.25 * int(self.entry2.get())
			elif 22 <= int(self.entry.get()) <= 24:
				calculated_selling_price = 1.7 * int(self.entry2.get())
			else:
				calculated_selling_price = 1.6 * int(self.entry2.get())
		else:
			if 16 <= int(self.entry.get()) <= 21:
				calculated_selling_price = 2.25 * int(self.entry2.get())
			elif 22 <= int(self.entry.get()) <= 24:
				calculated_selling_price = 1.35 * int(self.entry2.get())
			else:
				calculated_selling_price = 1.25 * int(self.entry2.get())

		calculated_selling_price = tk.Label(self.top, text=f"{calculated_selling_price}", font=('Arial', 20))
		calculated_selling_price.pack()


MYGUI()