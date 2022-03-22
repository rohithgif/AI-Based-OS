#!/usr/bin/env python
import random
import os
import pyttsx3
import speech_recognition as sr
import datetime
import shutil
import glob
import pandas as pd
from pyaudio import PyAudio
from tkinter.filedialog import askdirectory
from tkinter import Tk
import os
import hashlib
from pathlib import Path
import datetime
import glob
import os
import pyttsx3
import speech_recognition as sr
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio: object) -> object:
    engine.say(audio)
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Unable to Recognize your voice.")
        return "None"

    return query
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning  !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !")

    else:
        speak("Good Evening  !")
def display_instructions():
    pass
def introduction_and_instructions():
    speak("Hello....!")
    wishMe()
    speak("Welcome to automated file management system")
    speak("This project deals with  memory allocation and deallocation as well as basic file operations using voice commands which was given by user")
    speak("As this is a voice assistant........")
    speak("please give the commands when you see listening.... in the screen")
    speak("it is my primary responsibility to display the user manual")
    '''display_instructions()'''
    speak("make sure you give proper commands to me .......so that i can compute your requests")
    speak("now...Handing over to you")
'''class Automatic_File_Management:
    def init(self):
        pass
    def get_folder_statistics(self, folder):
        d = {}
        creation = []
        last_modification = []
        size = []
        file_name = []
        l = os.listdir(format(folder))
        for ele in l:
            file_name.append(ele)
            c = datetime.datetime.fromtimestamp(os.path.getctime(f'{folder}/{ele}'))
            m = datetime.datetime.fromtimestamp(os.path.getmtime(f'{folder}/{ele}'))
            creation.append(str(c).split()[0])
            last_modification.append(str(m).split()[0])
            size.append((os.path.getsize(f'{folder}/{ele}') / (1024 * 1024)))
        d["File"] = file_name
        d['Created'] = creation
        d['last_modified'] = last_modification
        d['Size(MB)'] = size
        df = pd.DataFrame(d)
        return df
    def get_files_with_maximum_storage(self, df: object) -> object:
        return df.sort_values('Size(MB)', ascending=False)
    def get_files_within_time(self, df, time):
        year = time.split('-')[0]
        month = time.split('-')[1]
        day = time.split('-')[2]
        sorted_statistics = df.sort_values('last_modified')
        sorted_statistic_upto_date = df[df['last_modified'] < year]
        maximum = self.get_files_with_maximum_storage(sorted_statistic_upto_date)
        return maximum
    def get_actual_file_location(self, file_name):
        file_locations = []
        desktop_path = 'C:/Users/91938/Desktop/**/{}'.format(file_name)
        documen_path = 'C:/Users/91938/Documents/**/{}'.format(file_name)
        downloads_path = 'C:/Users/91938/Downloads/**/{}'.format(file_name)
        music_path = 'C:/Users/91938/Music/**/{}'.format(file_name)
        pictures_path = 'C:/Users/91938/Pictures/**/{}'.format(file_name)
        favorites_path = 'C:/Users/91938/Favorites/**/{}'.format(file_name)
        video_path = 'C:/Users/91938/Videos/**/{}'.format(file_name)
        Desktop_files = glob.glob(desktop_path, recursive=True)
        Document_files = glob.glob(documen_path, recursive=True)
        Downloads_files = glob.glob(downloads_path, recursive=True)
        Favorites_files = glob.glob(favorites_path, recursive=True)
        Music_files = glob.glob(music_path, recursive=True)
        Pictures_files = glob.glob(pictures_path, recursive=True)
        video_files = glob.glob(video_path, recursive=True)
        overall_files = [Desktop_files, Document_files, Downloads_files, Favorites_files, Music_files, Pictures_files,
                         video_files]
        for ele in overall_files:
            if len(ele) > 1:
                for ele1 in ele:
                    file_locations.append(ele1)
        return file_locations
    def deallocate(self, file_name):
        directories = ["Desktop", "Downloads", "Documents", "Videos", "Pictures", "Favorites", "Music"]
        for dir in directories:
            if file_name.find(dir) == 1:
                d = dir
        os.remove(file_name)
        print("Succesfully Deleted")
    def get_disk_storage(self):
        disk_size = shutil.disk_usage('C:/')
        disk_left_size = disk_size.used
        disk_total = disk_size.total
        return disk_left_size,disk_total
    def is_memory_allocation_possible(self,file):
        disk_left_size,disk_total=self.get_disk_storage()
        file_size = os.path.getsize(file) // ( 2 ** 30)
        if file_size < disk_total:
            return True
        else:
            return False'''
class Automatic_File_Management:
    def init(self):
        pass
    def listdirs(self, root):
        l = []
        for path, subdirs, files in os.walk(root):
            for name in files:
                l.append(os.path.join(path, name))
        return l
    def get_folder_statistics(self, folder):
        d = {}
        creation = []
        last_modification = []
        size = []
        file_name = []
        l = os.listdir(folder)
        for ele in l:
            if os.path.isdir(os.path.join(folder,ele)):
                ld = self.listdirs(os.path.join(folder,ele))
                for i in ld:
                    file_name.append(i)
                    c = datetime.datetime.fromtimestamp(os.path.getctime(i))
                    m = datetime.datetime.fromtimestamp(os.path.getmtime(i))
                    creation.append(str(c).split()[0])
                    last_modification.append(str(m).split()[0])
                    size.append((os.path.getsize(i) / (1024 * 1024)))
            file_name.append(ele)
            c = datetime.datetime.fromtimestamp(os.path.getctime(f'{folder}/{ele}'))
            m = datetime.datetime.fromtimestamp(os.path.getmtime(f'{folder}/{ele}'))
            creation.append(str(c).split()[0])
            last_modification.append(str(m).split()[0])
            size.append((os.path.getsize(f'{folder}/{ele}') / (1024 * 1024)))
        d["File"] = file_name
        d['Created'] = creation
        d['last_modified'] = last_modification
        d['Size(MB)'] = size
        df = pd.DataFrame(d)
        return df
    def get_files_with_maximum_storage(self, df: object) -> object:
        return df.sort_values('Size(MB)', ascending=False)
    def get_files_within_time(self, df, time):
        year = time.split('-')[0]
        month = time.split('-')[1]
        day = time.split('-')[2]
        sorted_statistics = df.sort_values('last_modified')
        sorted_statistic_upto_date = df[df['last_modified'] < year]
        maximum = self.get_files_with_maximum_storage(sorted_statistic_upto_date)
        return maximum
    def get_actual_file_location(self, file_name):
        file_locations = []
        desktop_path = 'C:/Users/91938/Desktop/**/{}'.format(file_name)
        documen_path = 'C:/Users/91938/Documents/**/{}'.format(file_name)
        downloads_path = 'C:/Users/91938/Downloads/**/{}'.format(file_name)
        music_path = 'C:/Users/91938/Music/**/{}'.format(file_name)
        pictures_path = 'C:/Users/91938/Pictures/**/{}'.format(file_name)
        favorites_path = 'C:/Users/91938/Favorites/**/{}'.format(file_name)
        video_path = 'C:/Users/91938/Videos/**/{}'.format(file_name)
        Desktop_files = glob.glob(desktop_path, recursive=True)
        Document_files = glob.glob(documen_path, recursive=True)
        Downloads_files = glob.glob(downloads_path, recursive=True)
        Favorites_files = glob.glob(favorites_path, recursive=True)
        Music_files = glob.glob(music_path, recursive=True)
        Pictures_files = glob.glob(pictures_path, recursive=True)
        video_files = glob.glob(video_path, recursive=True)
        overall_files = [Desktop_files, Document_files, Downloads_files, Favorites_files, Music_files, Pictures_files,
                         video_files]
        for ele in overall_files:
            if len(ele) > 1:
                for ele1 in ele:
                    file_locations.append(ele1)
        return file_locations
    def deallocate(self, file_name):
        directories = ["Desktop", "Downloads", "Documents", "Videos", "Pictures", "Favorites", "Music"]
        for dir in directories:
            if file_name.find(dir) == 1:
                d = dir
        os.remove(file_name)
        print("Succesfully Deleted")
    def get_disk_storage(self):
        disk_size = shutil.disk_usage('C:/')
        disk_left_size = disk_size.used
        disk_total = disk_size.total
        return disk_left_size,disk_total
    def is_memory_allocation_possible(self,file):
        disk_left_size, disk_total = self.get_disk_storage()
        file_size = os.path.getsize(file) // ( 2 ** 30)
        if file_size < disk_total:
            return True
        else:
            return False
    def check_file_with_extenstion_if_it_is_present(self, file):
        df = pd.read_csv("C:/Users/91938/Desktop/Automated OS/allfiles.csv")
        l = list(df["File"])
        txt = []
        ppt = []
        pdf = []
        docx = []
        java = []
        python = []
        excel_and_csv = []
        ipy = []
        jpg_or_jpeg = []
        png = []
        c = []
        for ele in l:
            if ele.endswith(".txt"):
                txt.append(ele)
            elif ele.endswith(".c"):
                c.append(ele)
            elif ele.endswith(".png"):
                png.append(ele)
            elif ele.endswith(".jpg") or ele.endswith(".jpeg"):
                jpg_or_jpeg.append(ele)
            elif ele.endswith(".java"):
                java.append(ele)
            elif ele.endswith(".py"):
                python.append(ele)
            elif ele.endswith(".ipynb"):
                ipy.append(ele)
            elif ele.endswith(".xlsx") or ele.endswith(".csv"):
                excel_and_csv.append(ele)
            elif ele.endswith(".docx"):
                docx.append(ele)
            elif ele.endswith(".pdf"):
                pdf.append(ele)
            elif ele.endswith(".pptx"):
                ppt.append(ele)
        if file.endswith(".txt"):
            r = []
            for ele in txt:
                if ele.endswith(file):
                    r.append(1)
            return len(r)

        elif file.endswith(".pdf"):
            r = []
            for ele in pdf:
                if ele.endswith(file):
                    r.append(1)
            return len(r)
        elif file.endswith(".pptx"):
            r = []
            for ele in ppt:
                if ele.endswith(file):
                    r.append(1)
            return len(r)
        elif file.endswith(".docx"):
            r = []
            for ele in docx:
                if ele.endswith(file):
                    r.append(1)
            return len(r)
        elif file.endswith(".java"):
            r = []
            for ele in java:
                if ele.endswith(file):
                    r.append(1)
            return len(r)
        elif file.endswith(".py"):
            r = []
            for ele in python:
                if ele.endswith(file):
                    r.append(1)
            return len(r)
        elif file.endswith(".ipynb"):
            r = []
            for ele in ipy:
                if ele.endswith(file):
                    r.append(1)
            return len(r)
        elif file.endswith(".xlsx") or file.endswith(".csv"):
            r = []
            for ele in excel_and_csv:
                if ele.endswith(file):
                    r.append(1)
            return len(r)
        elif file.endswith(".jpeg") or file.endswith(".jpg"):
            r = []
            for ele in jpg_or_jpeg:
                if ele.endswith(file):
                    r.append(1)
            return len(r)
        elif file.endswith(".png"):
            r = []
            for ele in png:
                if ele.endswith(file):
                    r.append(1)
            return len(r)
        elif file.endswith(".c"):
            r = []
            for ele in c:
                if ele.endswith(file):
                    r.append(1)
            return len(r)
class txtfiles:
    def _init_(self):
        pass

    def write_file(self, txt, file_name=None):
        if file_name != None:
            f = open(file_name, "w")
            f.writelines(txt)
            f.close()
        else:
            file_name = "C:/Users/{}/Automated OS/Files/Text/{}.txt".format(os.getlogin(),
                                                                            random.choice([i for i in range(1000)]))
            f = open(file_name, "w")
            f.writelines(txt)
            f.close()

    def read_file(self, file_name):
        file_name
        f = open(file_name, "r")
        l = []
        for i in f.readlines():
            l.append(i)
        f.close()
        return l

    def create_file(self, txt, file_name=None):

         if file_name != None:
            file_name1 = "C:/Users/91938/Desktop/Automated OS/Files/Text/{}.txt".format(file_name)
            f = open(file_name1, "w")
            f.writelines(txt)
            f.close()

    def update_file(self, txt, file_name):
        if file_name != None:
            file_name1  = "C:/Users/91938/Desktop/Automated OS/Files/Text/{}.txt".format(file_name)
            f = open(file_name1, "a")
            f.writelines(txt)
            f.close()
        else:
            speak("new file being created ")
            self.create_file(self, txt, file_name)

    def delete_file(self, file_name):
        if file_name != None:
            os.remove("C:/Users/91938/Desktop/Automated OS/Files/Text/{}.txt".format(file_name))
        else:
            speak("no file exists with name {} to delete".format(file_name))

    def copy(self, file_name, dest=None):

        if dest != None:
            shutil.copy(file_name, dest)
        else:
            path = 'C:/Users/91938/Desktop/Automated OS/Files/Text/{}-{}.txt'.format(file_name,"Copy")
            shutil.copy(file_name,'C:/Users/91938/Desktop/Automated OS/Files/Text')


    def move(self, file, dest):
        shutil.move(file, dest)
class Cluster_the_Files:
    def _init_(self):
        pass

    def get_extention(self, file_name):
        return str(file_name).split('.')[-1]

    def create_copy_of_that_file(self, filename):
        path = str(filename).split('.')[-2]
        copied_file = path + '-Copy'
        copy = copied_file + "." + self.get_extention(filename)
        shutil.copyfile(filename, copy)
        return copy

    def cluster_files_from_dir(self, dir):
        path = "C:/Users/91938/" + dir + "/"
        textfiles = glob.glob(path + "*.txt", recursive=True)
        docxfiles = glob.glob(path + "*.docx", recursive=True)
        pdffiles = glob.glob(path + "*.pdf", recursive=True)
        csvfiles = glob.glob(path + "*.csv", recursive=True)
        excelfiles = glob.glob(path + "*.xlsx", recursive=True)
        pptfiles = glob.glob(path + "*.ppt", recursive=True)
        javafiles = glob.glob(path + "*.java", recursive=True)
        pythonfiles = glob.glob(path + "*.py", recursive=True)
        pngfiles = glob.glob(path + "*.png", recursive=True)
        jpgfiles = glob.glob(path + "*.jpg", recursive=True)
        ipynbfiles = glob.glob(path + "*.ipynb", recursive=True)
        cfiles = glob.glob(path + "*.c", recursive=True)
        for ele in textfiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\Text")
        for ele in docxfiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\docx")
        for ele in pptfiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\PPTS")
        for ele in pngfiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\PNG")
        for ele in javafiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\Java Scripts")
        for ele in pythonfiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\Python Scripts")
        for ele in excelfiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\Excels and CSV's")
        for ele in csvfiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\Excels and CSV's")
        for ele in jpgfiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\jpeg or jpg")
        for ele in ipynbfiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\IPY NoteBooks")
        for ele in pdffiles:
            ele1 = self.create_copy_of_that_file(ele)
            shutil.copy(ele1, r"C:\Users\91938\Desktop\Automated OS1\Files\PDFS")
        print("all files are clustered from {}".format(dir))

    def cluster_files(self):
        self.cluster_files_from_dir("3D Objects")
        self.cluster_files_from_dir("Contacts")
        self.cluster_files_from_dir("Cookies")
        self.cluster_files_from_dir("Desktop")
        self.cluster_files_from_dir("Documents")
        self.cluster_files_from_dir("Downloads")
        self.cluster_files_from_dir("Favorites")
        self.cluster_files_from_dir("Links")
        self.cluster_files_from_dir("Music")
        self.cluster_files_from_dir("My Documents")
        self.cluster_files_from_dir("Pictures")
        self.cluster_files_from_dir("PycharmProjects")
        self.cluster_files_from_dir("Saved Games")
        self.cluster_files_from_dir("Recent")
        self.cluster_files_from_dir("Videos")
class Delete_duplicate_content:
    def _init_(self):
        pass

    def get_subdirectories(self, path):
        return os.listdir(path)

    def delete_duplicate_files_from_folder(self,path):


            file_list = os.listdir(path)

            unique = dict()

            for file in file_list:
                file_name = Path(os.path.join(path, file))

                if file_name.is_file():
                    fileHash = hashlib.md5(open(file_name, 'rb').read()).hexdigest()

                    if fileHash not in unique:
                        unique[fileHash] = file_name

                    else:
                        os.remove(file_name)
                        print("successfully  deleted at {}".format(path))

                else:
                    print("No Duplicates in {}".format(path))
    def delete_duplicate_files(self):
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/C Scripts")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/docx")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/Excels and CSV's")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/IPY NoteBooks")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/Java Scripts")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/jpeg or jpg")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/PDFS")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/PNG")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/PPTS")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/Python Scripts")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop/Automated OS1/Files/Text")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Desktop")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Documents")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Downloads")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Pictures")
        self.delete_duplicate_files_from_folder("C:/Users/91938/Videos")

obj1 = txtfiles()
obj2 = Automatic_File_Management()
obj3 = Delete_duplicate_content()
obj4 = Cluster_the_Files()


speak("Hello....!")
wishMe()
speak("Welcome to automated file management system")
speak("This project deals with  memory allocation and deallocation as well as basic file operations using voice commands which was given by user")
display_instructions()
speak("make sure you give proper commands to me .......so that i can compute your requests")
speak("Clustering all the files from DISK")
obj4.cluster_files()
speak("Clustering is Completed")
speak("Deleting duplicate files")
obj3.delete_duplicate_files()
speak("Duplicate files are deleted")
speak("As this is a voice assistant........")
speak("please give the commands when you see listening.... in the screen")
speak("it is my primary responsibility to display the user manual")
speak("now...Handing over to you")
obj1 = txtfiles()
obj2 = Automatic_File_Management()
obj3 = Delete_duplicate_content()
obj4 = Cluster_the_Files()
while True:
    query = takeCommand().lower()
    if "hello" in query:
        speak("hello user")
    elif 'exit' in query:
        speak("ok")
        speak("thank you")
        exit()
    elif "how are you" in query:
        speak("iam fine")
    elif "delete" in query:
        speak("please tell me the name of the file you want me to delete")
        q6 = takeCommand().lower()
        obj1.delete_file(q6)
        speak("deleted the file" + q6)
    elif "copy" in query:
        speak("tell me the name of the file you want me to copy")
        q7 = takeCommand().lower()
        speak("do you want to specify the directory to which the file needs to be copied ?")
        q8 = takeCommand()
        if "yes" in q8:
            speak("what is your destination file path with out extention?")
            q9 = takeCommand()
            q = q9[0].upper()+q9[1:]
            obj1.copy(q7, q)
            obj3.delete_duplicate_files()
        elif "no" in q8:
            obj1.copy(q7)
            speak("Alert an duplicate object is been created ")
            obj3.delete_duplicate_files()
    elif "update" in query:
        speak("mention the name of the file which you want to update without extention")
        q10 = takeCommand()
        speak("tell me the text which needs to be added into the file")
        q11 = takeCommand()
        obj1.update_file(q11, q10)
        obj3.delete_duplicate_files()
    elif "move" in query:
        speak("please mention the filename which needs to be moved")
        q12 = takeCommand().lower()
        print(q12)
        speak("mention the directory to which the file needs to be moved")
        q13 = takeCommand().lower()

        dest1  = q13[0].upper()+q13[1:]
        print(dest1,type(dest1))
        dest = "C:/Users/91938/{}".format(dest1)
        src = "C:/Users/91938/Desktop/Automated OS/Files/Text/{}.txt".format(q12)
        obj1.move(src, dest)
    elif "open" in query:
        speak("please tell  me the name of file which you want to view or read contents")
        q4 = takeCommand().lower()
        speak("do you want me to share the content on screen ? please say yes or no")
        q5 = takeCommand().lower()
        file = "C:/Users/91938/Desktop/Automated OS/Files/Text/{}.txt".format(q4)
        if "yes" or "yeah" in q5:
            content = obj1.read_file(file)
            for ele in content:
                print(ele)
                speak(ele)
        elif "no" in q5:
            content = obj1.read_file(file)
            for ele in content:
                speak(ele)
    elif "create" in query:
        speak("do you want me to create a text file or not ?")
        speak("please answer yes or no")
        q1 = takeCommand().lower()
        if "yes" in q1:
            speak("please mention the name of the file you want to save it as without extention")
            q2 = takeCommand().lower()
            speak("enter the content you wanted to speak")
            q3 = takeCommand().lower()
            obj1.create_file(q3, q2)
            speak("Checking if the available storage")
            if obj2.is_memory_allocation_possible("C:/Users/91938/Desktop/Automated OS/Files/Text/{}.txt".format(q2)):
                speak("file is allocated")
                speak("file saved")
                obj3.delete_duplicate_files()
            else:
                speak("deallocation is required....")
                mdf = obj2.get_files_within_time("2021-08-01")
                speak("all files are displayed from different directories with maximum storages of files in it")
                for d in ["Desktop", "Downloads", "Documents", "Videos", "Pictures", "Favorites", "Music"]:
                    print("--------------------------------------------------------------------------------------------------------------------")
                    print("                                                 {}                                                                 ".format(dir))
                    print("--------------------------------------------------------------------------------------------------------------------")
                    print(obj2.get_files_with_maximum_storage(d))
                    print("--------------------------------------------------------------------------------------------------------------------")
                    print("--------------------------------------------------------------------------------------------------------------------")
                speak("pick up the directory from the above")
                dir2 = takeCommand().lower()
                dir2 = dir2[0].upper()+dir2[1:]
                speak("enter the index of the file from the choosen directory")
                index = takeCommand().lower()
                df = obj2.get_files_with_maximum_storage(dir2)
                file_location = obj2.get_actual_file_location(str(df["File"][index]))
                if len(file_location) > 1:
                    speak("the file you wanted to dealloacte is located at multiple locations....")
                    for ele in file_location:
                        obj2.deallocate(ele)
                    speak("deallocation is done")
                else:
                    obj2.deallocate(file_location[0])
                    obj3.delete_duplicate_files()
                    speak("deallocation is done")
        else:
            speak("sorry....im designed in a way to save the text files")
    elif "folder statistics" in query:
        speak("please enter the name of the folder or directory  from the disk")
        q14 = takeCommand().lower()
        dir  = q14[0].upper()+q14[1:]
        dir1 = "C:/Users/91938/{}".format(dir)
        statistics = obj2.get_folder_statistics(dir1)
        speak("The folder statistics will be displayed on screem")
        print("-------------------------------------------------------------------------------------------------------------------")
        print("                                                {}                                                                    ".format(dir))
        print("-------------------------------------------------------------------------------------------------------------------")
        print(statistics)
        print("-------------------------------------------------------------------------------------------------------------------")
        print("-------------------------------------------------------------------------------------------------------------------")
    elif "file location" in query:
        speak("please tell enter the name  of file with extention as the extention is important")
        q15 = input("Enter the name of the file with extention : ")
        locations = obj2.get_actual_file_location(q15)
        speak("the location of the files are being displayed in screen")
        print(locations)
    elif "disk statistics" in query:
        disk_left, disk_total = obj2.get_disk_storage()
        speak("Your disk statistics are ")
        speak("you have used {} out of {} GB in C Drive".format(((disk_total - disk_left) // (2 * 30)),(disk_total // (2 * 30))))

    elif 'duplicate' in query:
        speak("enter the name of file with extention you wanted to duplicate")
        q16 = input("enter the name of the file you wanted to create a duplicate with extention : ")
        locations1 = obj2.get_actual_file_location(q16)
        if len(locations1) > 1:
            speak("the file you wanted to replicate is located at multiple locations....")
            speak("do you still want to make duplicate of that which occupies more storage?please answer yes or no")
            q17 = takeCommand().lower()
            if q17 == "yes":
                for ele in locations1:
                    obj4.create_copy_of_that_file(ele)
                speak("duplicates are created")
            elif q17 == "no":
                speak("pick up the index which denotes a single location of the given file")
                for i in range(len(locations1)):
                    print("{} - > {}".format(i+1,locations1[i]))
                q18 = takeCommand().lower()
                obj4.create_copy_of_that_file(locations1[int(q18)-1])
                speak("duplicate is created")
        else:
            obj4.create_copy_of_that_file(locations1[0])
            speak("duplicate is created")
        obj3.delete_duplicate_files()