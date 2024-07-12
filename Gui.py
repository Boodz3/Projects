import PySimpleGUI as sg
import os
import shutil

tech_Degrees = ['Computer Science','Computer Engineering','Information Technology','Information Systems','Software Engineering','Data Science','Data Analytics','Cybersecurity','Information Security','Artificial Intelligence','Machine Learning']
non_tech_Degrees = ['Business','Economics']


tech_skills_langs = ['C++', 'C', 'C#' , 'Java', 'Python', 'R','SQL' , 'Assembly', 'Bash','HTML','CSS','JavaScript']
tech_skills_Req = ['Problem Solving','Foundation of Computing','Algorithms And Data Structures','Data Analysis','Data Mining','Data Visualization','Windows','Linux','Networking','Encryption','Security Protocols','Ethical Hacking','Web Development']
tech_skills_General =['Teamwork', 'Communication','Presentation','Troubleshooting']


tech_fields = ['SE','DS','IT','CS']
non_tech_fields = ['Sales','Accounting', 'Languages']

sg.theme('Dark Grey 13')   # Add a touch of color
# All the stuff inside your window.
NAME_SIZE = 30
def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + ' '*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

def newCert(i):
    return [[name('Field:'), sg.OptionMenu(tech_fields+ non_tech_fields,s=(15,2), key='-CertField-'+str(i))],
            [name('Name:'),  sg.InputText(key='-CertName-'+str(i), size=(15,1))]]

def newDegree(i):
    return [[name('Degree: '), sg.OptionMenu(tech_Degrees+non_tech_Degrees,s=(15,2), key='-Degree-'+str(i))]]

def newWork(i):
    return[[name('Field:'), sg.OptionMenu(tech_fields+ non_tech_fields,s=(15,2),key='-WorkField-'+str(i))],
           [name('years:'),sg.InputText(key='-WorkYears-'+str(i))]]
    
def newGen(i):
    return [[name('General Skill: '), sg.OptionMenu(tech_skills_General,s=(15,2), key='-Gen-'+str(i))]]

def newReq(i):
    return [[name('Required Skill: '), sg.OptionMenu(tech_skills_Req,s=(15,2), key='-Req-'+str(i))]]

def newLang(i):
    return [[name('Programing Language: '), sg.OptionMenu(tech_skills_langs,s=(15,2), key='-Lang-'+str(i))]]
# sg.theme(t)

layout_ll = [
            [name('Enter your gender'),sg.Radio('Male', 1, key='Male'),sg.Radio('Female',1, key='Female')],
            [name('Enter your degree(s):'), sg.Button('+', key='-+Deg-')],
            [sg.Frame('',[[]], key='-Degree-')],
            [name('Enter your certificate(s):'), sg.Button('+', key='-+Cert-')],
            [sg.Frame('',[[]], key='-Cert-')],
            [name('Enter your Work Experience(s):'), sg.Button('+', key='-+Work-')],
            [sg.Frame('',[[]], key='-Work-')],
            [name('Enter your General Skills(s):'), sg.Button('+', key='-+Gen-')],
            [sg.Frame('',[[]], key='-Gen-')],
            [name('Enter your Required Skill(s):'), sg.Button('+', key='-+Req-')],
            [sg.Frame('',[[]], key='-Req-')],
            [name('Enter your Programming Language(s):'), sg.Button('+', key='-+Lang-')],
            [sg.Frame('',[[]], key='-Lang-')],
        ]
layout_l = [
    [sg.Column(layout_ll, scrollable=True, vertical_scroll_only=True, size=(500,500),key='-COL-')]
]
layout_r = [
    [sg.Button('Ok', key='Submit'), sg.Button('Cancel')],
    [sg.Text('You Are Qualified For THe Following Jobs', size=(50,1), pad=(40,0), font='Courier 10')],
    [sg.Text('', key='-Jobs-', size=(50,10), pad=(40,120), font='Courier 10')]
]

layout = [[sg.Col(layout_l), sg.Col(layout_r, element_justification='c')]]
def writeToFile(Gender, Degs, Certs, Work, Gen, Req, Lang):
    with open('facts.kfb', 'a') as f:
        if(Gender[0] == 1):
            f.write("gender('male')\n")
        elif (Gender[1] == 1):
            f.write("gender('female')\n")
        for deg in Degs:
            if(deg in tech_Degrees):
                f.write("tech_degree('"+deg+"')\n")
            elif(deg in non_tech_Degrees):
                f.write("business_degree('"+deg+"')\n")
        for cert in Certs:
            cert = cert.split()
            if(cert[0] in tech_fields):
                f.write("tech_cert('"+cert[0]+"','"+ cert[1] +"')\n")
            elif(cert[0] in non_tech_fields):
                f.write("business_cert('"+cert[0]+"','"+ cert[1] +"')\n")
        for work in Work:
            work = work.split()
            if(work[0] in tech_fields):
                f.write("tech_experience('"+work[0]+"',"+ work[1] +")\n")
            elif(work[0] in non_tech_fields):
                f.write("business_experience('"+work[0]+"',"+ work[1] +")\n")
        for gen in Gen:
            f.write("tech_skill(General,'" + gen + "')\n")
        for req in Req:
            f.write("tech_skill(Req,'"+req+"')\n")
        for lang in Lang:
            f.write("tech_skill(Lang,'"+lang+"')\n")


        

# Create the Window
window = sg.Window('HR', layout, resizable=True)
certs = 0
degs = 0
work= 0
elements= 0
gen= 0
lang= 0
req= 0
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read() 
    window['-COL-'].contents_changed()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if (event == '-+Deg-'):
        window.extend_layout(window['-Degree-'], newDegree(degs))
        degs+=1
    if (event == '-+Cert-'):
        window.extend_layout(window['-Cert-'], newCert(certs))
        certs+=1
    if (event == '-+Work-'):
        window.extend_layout(window['-Work-'], newWork(work))
        work+=1
    if (event == '-+Gen-'):
        window.extend_layout(window['-Gen-'], newGen(gen))
        gen+=1
    if(event == '-+Req-'):
        window.extend_layout(window['-Req-'], newReq(req))
        req+=1
    if(event == '-+Lang-'):
        window.extend_layout(window['-Lang-'], newLang(lang))
        lang+=1
    if (event == 'Submit'):
        Gender = [values['Male'], values['Female']]
        Degs = [values['-Degree-'+str(i)] for i in range(degs)]
        Certs = [values['-CertField-'+str(i)] + ' ' + values['-CertName-'+str(i)] for i in range(certs)]
        Work = [values['-WorkField-'+str(i)] + ' ' + values['-WorkYears-'+str(i)] for i in range(work)]
        Gen = [values['-Gen-'+str(i)] for i in range(gen)]
        Req = [values['-Req-'+str(i)] for i in range(req)]
        Lang = [values['-Lang-'+str(i)] for i in range(lang)]
       
        writeToFile(Gender, Degs, Certs, Work, Gen, Req, Lang)
        os.system('python driver.py')
        with open('results.txt', 'r') as f:
            result = f.readlines()
        rstring = ''
        for res in result:
            rstring += res + '\n'

        # window['-Jobs-'].update(value='')
        print(rstring)
        window['-Jobs-'].update(str(rstring))
        # removes the content of the facts.kfb file
        defaultFacts= "tech_experience('SE',0)\n" +  "tech_experience('DS',0)\n" + "tech_experience('CS',0)\n" + "tech_experience('IT',0)\n" + "tech_experience('Sales',0)\n" + "tech_experience('Accounting',0)\n"
        with open('facts.kfb', 'w') as f:
            f.write(defaultFacts)
        try:
            shutil.rmtree('compiled_krb')
        except FileNotFoundError:
            pass


window.close()