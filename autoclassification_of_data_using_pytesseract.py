import pytesseract
import re
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Password\AppData\Local\Programs\Python\Python37-32\Scripts\tesseract\tesseract.exe"
text = pytesseract.image_to_string("aadhar.png",lang = 'eng') 

data=re.split(r'\d{6}',text)[0]
data1=re.split(r'To\n\n.*',data)[1]
name=data1.split('\n')[2]
pin=re.findall(r'\d{6}',text)[0].replace('\n','')
Address=data1.replace('\n',' ')+pin
aadhar_number=re.findall(r'\S{4}\s\S{4}\s\d{4}',text)[0]
DOB=re.findall('\d{2}\/\d{2}\/\d{4}',text)[0]
Enrollment_no=re.findall(r'\S{4}\/\S{5}\/\S{5}',text)[0]


def findDob(text):
    try:
        DOB=re.findall(r'\d{2}\/\d{2}\/\d{4}',text)[0]
    except:
        try:
            DOB=re.findall(r'Year of Birth|DOB[\:\s\d\/]+',text)[0].split()[-1]
        except:
            DOB=''
    return(DOB)

def findGender(text):
    wlist=re.findall('[A-Za-z]{4,6}',text)
    wlist=list(map(lambda x:x.lower(),wlist))
    if('female' in wlist):
        gender='FEMALE'
    elif 'male' in wlist:
        gender='MALE'
    else:
        gender='NOT FOUND'
    return(gender)

	

Personal_details={'Name':name,
'DOB':findDob(text),
'Address':Address,
'Aadhaar':aadhar_number,
'Enrollment_no':Enrollment_no,
'Gender':findGender(text)
'Pincode':pin}