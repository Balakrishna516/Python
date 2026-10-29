#Task : Create your student profile with fields as ids number
#Email id,Mobile Number,Parent Whatsappnumber,subjects,
#batch no, daily exam marks,weekly exam marks,batch rank,
#github_url,Linkedin_id
student = {"student_id": "CGVI0241",
             "full_name": "UDDANDAM BALA KRISHNA", 
             "email_id": "balakrishnauddandam@gmail.com",          
             "mobile_number": "8074028533",                   
             "parent_whatsapp_number": "9290252759",          
             "institute": "Codegnan",                         
             "course": "Python Full Stack Development",       
             "batch_number": "PFS-VSP-007",                   
             "subjects": {"Python", "MYSQL", "Aptitude", "english"},
             "daily_exam_marks": [28, 29, 27, 30, 28],            
             "weekly_exam_marks": [45,48, 50, 47],           
             "batch_rank": 8,                                 
             "attendance_percentage": 92.5,                   
             "github_url": "https://github.com/Balakrishna516", 
             "linkedin_url": "https://www.linkedin.com/in/bala-krishna-uddandam-607427432/",
             "resume_file": "balakrishnauddandam_resume.pdf",              
             "certifications": ["Python Fundamentals", "SQL Basics"],
        "skills": {"Python", "MySQL", "Git"},            
        "placement_status": "Preparing",                 
        "fees_status": "Paid",                           
        "profile_completion": 92,                        
        "student_details": ("CGVI0241","Uddandam Bala krishna",   
                        "Codegnan","PFS-VSP-007"),}
print(student)
print(len(student))
print(student.keys())
print(student.values())

 
