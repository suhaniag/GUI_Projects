import tkinter
t = tkinter.Tk()



print("Hey there! Let's find an activity that will make you happy!")
print("Question 1: Do you like to spend time indoors or outdoors?")

def picnic():
  print("Here are your results: Have a themed picnic, Eat at a special place like the beach")
def sports():
  print("Here are your results: Learn a new sport, Go for a run, Go on a nature walk")
def camping():
  print("Here are your results: Go on a camping trip with your friends, Set up a tent in your backyard")

def art():
  print("Here are your results: Draw the view outside your window, Paint something that makes you happy, Make your favorite animal out of clay")
def reading():
  print("Here are your results: Spend some time at the library, Look at book reviews, Make a reading list")
def music():
  print("Here are your results: Make a playlist of your favorite songs, Learn a new instrument, Do karaoke")

def indoors():
  indoorsbutton.destroy()
  outdoorsbutton.destroy()
  print("Question 2: Do you prefer art, reading, or music?")
  artbutton = tkinter.Button(t, text = "Art", command = art, font= ("DejaVu Serif", 20), fg = "#FFFFFF", bg = "#F88379", activeforeground= "#FFFFFF", activebackground = "#F88379")
  artbutton.pack(expand= True, fill = tkinter.BOTH)
  readingbutton = tkinter.Button(t, text= "Reading", command = reading, font= ("DejaVu Serif", 20), fg = "#FFFFFF", bg = "#F88379", activeforeground= "#FFFFFF", activebackground = "#F88379")
  readingbutton.pack(expand= True, fill = tkinter.BOTH)
  musicbutton = tkinter.Button(t, text = "Music", command = music, font= ("DejaVu Serif", 20), fg = "#FFFFFF", bg = "#F88379", activeforeground= "#FFFFFF", activebackground = "#F88379")
  musicbutton.pack(expand= True, fill = tkinter.BOTH)
  
def outdoors():
  outdoorsbutton.destroy()
  indoorsbutton.destroy()
  print("Question 2: Do you prefer picnics, sports, or camping?")
  picnicbutton = tkinter.Button(t, text= "Picnic", command = picnic, font= ("DejaVu Serif", 20), fg = "#FFFFFF", bg = "#F88379", activeforeground= "#FFFFFF", activebackground = "#F88379")
  picnicbutton.pack(expand= True, fill = tkinter.BOTH)
  sportsbutton = tkinter.Button(t, text= "Sports", command =sports, font= ("DejaVu Serif", 20), fg = "#FFFFFF", bg = "#F88379", activeforeground= "#FFFFFF", activebackground = "#F88379")
  sportsbutton.pack(expand= True, fill = tkinter.BOTH)
  campingbutton = tkinter.Button(t, text="Camping", command = camping, font= ("DejaVu Serif", 20), fg = "#FFFFFF", bg = "#F88379", activeforeground= "#FFFFFF", activebackground = "#F88379")
  campingbutton.pack(expand= True, fill = tkinter.BOTH)
  

indoorsbutton = tkinter.Button(t, text = "Indoors", command = indoors, font= ("DejaVu Serif", 20), fg = "#FFFFFF", bg = "#F88379", activeforeground= "#FFFFFF", activebackground = "#F88379")


outdoorsbutton = tkinter.Button(t, text = "Outdoors", command = outdoors, font= ("DejaVu Serif", 20), fg = "#FFFFFF", bg = "#F88379", activeforeground= "#FFFFFF", activebackground = "#F88379")



  
  
  


indoorsbutton.pack(expand = True, fill = tkinter.BOTH)
outdoorsbutton.pack(expand = True, fill = tkinter.BOTH)

t.mainloop()
