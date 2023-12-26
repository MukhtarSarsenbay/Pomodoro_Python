import time
import threading 
import tkinter as tk
from tkinter import ttk, PhotoImage

class OrmanTimer():
  def __init__(self):
    self.root=tk.Tk()
    self.root.geometry("600x600")
    self.root.title("Orman")
    self.root.tk.call("wm","iconphoto",self.root._w,PhotoImage(file="tree.png"))

    self.s=ttk.Style()
    self.s.configure("TNotebook.tab", font=("Ubuntu",16))
    self.s.configure("TButton", font=("Ubuntu",16))

    self.tabs=ttk.Notebook(self.root)
    self.tabs.pack(fill="both",pady=10,expand=True)

    self.tab1=ttk.Frame(self.tabs,width=600,height=100)
    self.tab2=ttk.Frame(self.tabs,width=600,height=100)
    self.tab3=ttk.Frame(self.tabs,width=600,height=100)

    self.orman_timer_label=ttk.Label(self.tab1, text ="25:00",font=("Ubuntu",50))
    self.orman_timer_label.pack(pady=20)
    
    self.short_break_timer_label=ttk.Label(self.tab2, text ="05:00",font=("Ubuntu",50))
    self.short_break_timer_label.pack(pady=20)
    
    self.long_break_timer_label=ttk.Label(self.tab3, text ="15:00",font=("Ubuntu",50))
    self.long_break_timer_label.pack(pady=20)

    self.grid_layout=ttk.Frame(self.root)
    self.grid_layout.pack(pady=10)

    self.start_button=ttk.Button(self.grid_layout,text="Basta",command=self.start_timer_thread)
    self.start_button.grid(row=0, column=0)

    self.skip_button=ttk.Button(self.grid_layout,text="Otkyzu",command=self.skip_clock)
    self.skip_button.grid(row=0, column=1)

    self.reset_button=ttk.Button(self.grid_layout,text="Basynan",command=self.reset_clock)
    self.reset_button.grid(row=0, column=2)

    self.tabs.add(self.tab1, text ="Orman")
    self.tabs.add(self.tab2, text ="Qysqa Demalys")
    self.tabs.add(self.tab3, text ="Uzaq Demalys")

    self.orman_counter_label=ttk.Label(self.grid_layout,text="kezen sany:0",font=("Ubuntu",16))
    self.orman_counter_label.grid(row=1,column=0,columnspan=3,pady=10)
    ##UI PART ABOVE
    self.orman=0
    self.skipped=False
    self.stopped=False
    self.running=False
    self.root.mainloop()



  def start_timer_thread(self):
    if not self.running: 
      t=threading.Thread(target=self.start_timer)
      t.start()
      self.running=True
  def start_timer(self):
    self.stopped=False
    self.skipped=False
    timer_id=self.tabs.index(self.tabs.select())+1

    if timer_id==1:
      full_seconds=60*25 
      while full_seconds>0 and not self.stopped:
        minutes,seconds=divmod(full_seconds,60)
        self.orman_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        self.root.update()
        time.sleep(1)
        full_seconds-=1
      if not self.stopped or self.skipped:
        self.orman+=1
        self.orman_counter_label.config(text=f"kezen sany:{ self.orman}")
        if self.orman%4==0:
          self.tabs.select(2)
          self.start_timer() 
        else:
          self.tabs.select(1)
        self.start_timer()
        #case #1
    elif timer_id==2:
      full_seconds=60*5
      while full_seconds>0 and not self.stopped:
        minutes,seconds=divmod(full_seconds,60)
        self.short_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        self.root.update()
        time.sleep(1)
        full_seconds-=1
      if not self.stopped or self.skipped:
        self.tabs.select(0)
        self.start_timer()
        #case #2
    elif timer_id==3:
      full_seconds=60*15
      while full_seconds>0 and not self.stopped:
        minutes,seconds=divmod(full_seconds,60)
        self.long_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
        self.root.update()
        time.sleep(1)
        full_seconds-=1
      if not self.stopped or self.skipped:
        self.tabs.select(0)
        self.start_timer()
    else:
      print("Invalid timer ID")
  def reset_clock(self):
    self.stopped=True
    self.skipped=False
    self.orman=0
    self.orman_timer_label.config(text="25:00")
    self.short_break_timer_label.config(text="05:00")
    self.long_break_timer_label.config(text="15:00")
    self.orman_counter_label.config(text="kezen sany:0")
    self.running=False
  def skip_clock(self):
    current_tab=self.tabs.index(self.tabs.select())
    if current_tab==0:
      self.orman_timer_label.config(text="25:00")
    elif current_tab==1:
      self.short_break_timer_label.config(text="05:00")
    elif current_tab==2:
      self.long_break_timer_label.config(text="15:00")
    self.stopped=True
    self.skipped=True


OrmanTimer()