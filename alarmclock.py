import time
import datetime
import tkinter as tk


class mainWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title ("Alarm Clock")
        self.window.geometry("300x200+600+300")

        self.label = tk.Label(self.window,text = "0:00")
        self.label.place(x = 125, y = 75)

        self.entry = tk.Entry(self.window, text="Enter time", bg='black',fg='white', bd=5)
        self.entry.place(x = 50,y=100)

        self.start_button = tk.Button(self.window, text="Start Countdown", command=self.count_down)
        self.start_button.place(x=120, y=140)

    def count_down(self):
        try:
            countdown_time = int(self.entry.get())
            i = 0
            while(i <= countdown_time):
                remaining_time = countdown_time - i

                if remaining_time >= 60:
                    mins = remaining_time  // 60
                    sec = remaining_time % 60
                    if mins > 0 and sec <= 0:
                        i = 0
                        mins -= 1
                        sec = 59
                        countdown_time = sec + (mins*60)
            

                    time_text = f"{mins}:{sec:02}"
                        
                else:
                    time_text = f"0:{remaining_time:02}"
            
                self.label.config(text = time_text)
                self.window.update()
                time.sleep(1)
                i += 1
            
        except ValueError:
            print("Invalid input")
if __name__ == "__main__":
    app = mainWindow()
    tk.mainloop()
  