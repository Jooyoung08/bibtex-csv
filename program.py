import tkinter as tk
from tkinter import filedialog, messagebox
from os import getcwd
from os import listdir
from re import match
from re import search
from re import findall
from sys import stdin
from string import capwords

entries = []
entry = {}
input_list = []

input_file = ""
output_file = ""

def select_file():
    file_path = filedialog.askopenfilename()
    global input_file
    if file_path:
        try:
            print("Selected File: " + file_path)
            input_file = file_path
        except Exception as e:
            print("Can't open file: " ,e)
        label.config(text="Selected File: " + file_path)
    else:
        label.config(text="No File Selected")

def author_list():
    list_path = filedialog.askopenfilename()
    global input_list
    if list_path:
        try:
            print("Selected List File: " + list_path)
            with open(list_path, 'r') as lf:
                for line in lf:
                    input_list.append(line.strip())
        except Exception as e:
            print("Can't open file: " ,e)
        label.config(text="Selected List File: " + list_path)
    else:
        label.config(text="No List File Selected")

def conv_file():
    new_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("csv file", "*.csv")])
    global entry
    global spAu
    global new_list
    global Nauthor
    global title
    global journal
    global year
    global month
    global pages
    global volume
    global issue
    global doi
    global issn

    if new_file_path:
        try:
            with open(input_file, 'r') as f:
                print("Converting File: " + input_file)
                for line in f:
                    if (match('^@', line.strip())):
                        print("Find Entry")
                        if entry != {}:
                            entries.append(entry)
                            entry = {}
                            print(entries)
                    elif (search('=', line.strip())):
                        key, value = [v.strip(" {},\n") for v in line.split("=", maxsplit=1)]
                        entry[key] = value
                entries.append(entry)
                with open(new_file_path, 'a') as nf:
                    nf.write("Title|Journal|ISSN|DOI|Vol|Issue|Year|Month|page|Number of Author|Authors"+'\n')
                    for entry in entries:
                        author = "NA"
                        if "author" in entry:
                            author = entry["author"]
                        elif "authors" in entry:
                            author = entry["authors"]
                        spAu = author.split('and')
                        #Number of Authors
                        Nauthor = len(spAu)
                        new_list = [i.strip() for i in spAu]
                        f_au = set(new_list) & set(input_list)
                        author = ','.join(f_au)
                        #Title
                        title = "NA"
                        if "title" in entry:
                            title = entry["title"]
                        #Journal
                        journal = "NA"
                        if "journal" in entry:
                            journal = entry["journal"]
                        #Year
                        year = "NA"
                        if "year" in entry:
                            year = entry["year"]
                        #Month
                        month = "NA"
                        if "month" in entry:
                            month = entry["month"]
                        #Page
                        pages = "NA"
                        if "pages" in entry:
                            pages = entry["pages"]
                        #Volume
                        volume = "NA"
                        if "volume" in entry:
                            volume = entry["volume"]
                        #Issue
                        issue = "NA"
                        if "issue" in entry:
                            issue = entry["issue"]
                        #ISSN
                        issn = "NA"
                        if "issn" in entry:
                            issn = entry["issn"]
                            issn = "-".join([issn[:4], issn[4:8]])
                        #DOI
                        doi = "NA"
                        if "doi" in entry:
                            doi = entry["doi"]
                        #Write to new file
                        nf.write(title+'|'+journal+'|'+issn+'|'+doi+'|'+volume+'|'+issue+'|'+year+'|'+month+'|'+pages+'|'+str(Nauthor)+'|'+author+'\n') 
            messagebox.showinfo("Completed!", "Successfully converted the file!")
        except Exception as e:
            messagebox.showerror("Fail to converting", f"Error occured!: {str(e)}")

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("Convert BibTex to CSV")
window.geometry("600x650")

# 파일 선택 버튼
sfbutton = tk.Button(window, text="Select File", command=select_file)
sfbutton.pack(side="top", padx=20, pady=20)
sfbutton.place(x=20, y=20, width=550, height=200)

libutton = tk.Button(window, text="Add List", command=author_list)
libutton.pack(side="top", padx=20, pady=20)
libutton.place(x=20, y=220, width=550, height=200)

cvbutton = tk.Button(window, text="File Converting", command=conv_file)
cvbutton.pack(side="top", padx=20, pady=20)
cvbutton.place(x=20, y=420, width=550, height=200)

# 선택된 파일 경로를 보여줄 레이블
label = tk.Label(window, text="")
label.pack(pady=10)

# 윈도우 실행
window.mainloop()

