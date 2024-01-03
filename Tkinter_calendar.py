from tkinter import *
import calendar

# Function for showing the calendar of the given year
def showCal() :

	new_gui = Tk()
	new_gui.config(background = "white")
	new_gui.title("CALENDAR")
	new_gui.geometry("550x600")

	fetch_year = int(year_field.get())
	cal_content = calendar.calendar(fetch_year)
	cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")
	cal_year.grid(row = 5, column = 1, padx = 20)
	new_gui.mainloop()

if __name__ == "__main__" :

	# Creating a GUI window
	root = Tk()
	root.config(background = "white")
	root.title("CALENDAR")
	root.geometry("500x500")
	cal = Label(root, text = "CALENDAR", bg = "dark gray",font = ("times", 28, 'bold'))

	year = Label(root, text = "Enter Year", bg = "light green")
	year_field = Entry(root)

	Show = Button(root, text = "Show Calendar", fg = "Black",bg = "Red", command = showCal)

	Exit = Button(root, text = "Exit", fg = "Black", bg = "Red", command = exit)

	cal.grid(row = 5, column = 5,padx=150,pady=20)
	year.grid(row = 7, column = 5,pady=10)
	year_field.grid(row = 9, column = 5,pady=10)
	Show.grid(row = 10, column = 5,pady=10)
	Exit.grid(row = 12, column = 5)

	root.mainloop()
	
