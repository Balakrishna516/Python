#---------------------------->PYTHON STRING PRACTICE QUESTIONS<------------------------------------------------------------------#

#Section 1: Basic String Manipulation

#1)Student Name Formatter
'''A college Registration system receives Student names is inconsistent formats.Normalize  the name so that each word begins
with a Capital letter.
name="sAkEtH kAlLePU" #input
print(name.title())'''
#Output = Saketh Kallepu

#2)Customer Email Cleanup
'''An online shopping application recieves an email address with accidental spaces and  Uppercase
letters.Clean it before storing it.
email="  Saketh.KALLEPU@GMAIL.COM  " #input
print(email.lower().strip())'''
#Output = saketh.kallepu@gmail.com

#3)Product Code Replacement
'''A Company has Changed its product prefix from OLD to NEW.update the product code.
product_code ="OLD-101-OLD-202  #input
print(product_code.replace("OLD","NEW"))'''
#Output = NEW-101-NEW-202

#4)Username Generator
'''A website creates usernames by combining a student's first name and graduation year,Separated by
an underscore.Convert the  first name to lowercase .
first_name = "SAKETH";year = 2027 #input
print(f"{first_name.lower()}_{year}")'''
#Output = saketh_2027

#5)Sentence Character Count
''' A Content -Writing application needs the total number of characters in a sentence, including spaces.
sentence="python makes coding easy" #input
print(len(sentence))'''
#Output = 24

#Section-2: INDEXING AND SLICING

#6)Employee Id Extraction
'''An  employee ID starts with EMP followed by six-digit number.Extract the numeric portion. 
employee_id = "EMP582741 "       #input
print(employee_id[3:])'''
#Output = 582742

#7)Mask a Bank Account Number
'''A banking application displays only the last four digits of an account number.
Replace the preceding digits with eigth asterisks.
account_number = "123456789012"    #input
print(f"{'*' *8}{account_number[-4:]}")'''
#Output = ********9012

#8)Alternating character Extraction
'''Extract every second character from the string, starting with the first character.
text = "CODEGNANPYTHON" #input
print(text[::2])'''
#Output = CDGAPTO

#9)Reverse a product serial Number
'''Reverse a serial number for  a device-testing format.
serial_number ="PYTHON123"  #input
print(serial_number[::-1])'''
#Output = 321NOHTYP

#10)Extract a file Extension
'''A document system needs the final three characters of a filename as its extension.
filename = "student_report.pdf" #input
print(filename[-3:])'''
#Output = pdf

#SECTION-3 :SEARCHING,SPLITTING,AND JOINING

#11)Search for a Course Name
'''Count the occurances of the word python in a course  description,ignoring case.
description = "Python is easy. I love Python. Learn Python today." #input
print(description.count("Python"))'''
#Output = 3

 #12)Convert a sentence into words
'''Separate a sentence into individual words.
sentence ="Learn Python Full Stack Development" #input
print(f"[{" 'Learn', 'Python', 'Full', 'Stack', 'Development' "}]")'''
#Output = [ 'Learn', 'Python', 'Full', 'Stack', 'Development' ]

#13)Generate a Formatted Adress
'''Combine the  House number, Street, City, and State into one address seperated by commas.
house = "12-4";street = "MG Road";city = "vijayawada";state = "Andhra Pradesh" #input
print(house,street,city,state,sep=',')'''
#Output = 12-4,MG Road,vijayawada,Andhra Pradesh

#14)Count words in a Message
'''Calculate the number of words in a message without using loops.
message = "Your application has been successfully submitted" #input
print(len(message.split()))'''
#Output = 6

#15)Validate the coupon Code
'''Display the result of checking whether a coupon code contains only alphabetic characters.'''
coupon_code = "CODEGNAN123" #input
print(coupon_code.isalpha())
#Output = False
