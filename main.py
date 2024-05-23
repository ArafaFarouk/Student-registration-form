from pywebio import start_server
from pywebio.input import * 
from pywebio.output import * 
from pywebio.session import * 
from pywebio.pin import * 
import csv

def save_data(student_data):
    with open('students_data.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(student_data)

def App():
    put_html('<center><h2>استمارة تسجيل الطلاب</h2></center>').style('background-color:#240A34; padding:25px; color:#FFF455;')
    put_html('<p>السيرة الذاتية للطلاب المقبولين</p>').style('text-align:center; font-weight:bold')
    put_html('<center><img src="https://www.zillacapital.com/wp-content/uploads/2021/09/education.jpg"></center>')
    
    data = input_group(
        'استمارة الطالب',
        [
            input('اسم الطالب', name='student', required=True, placeholder="أدخل اسم الطالب"),
            input('عنوان الطالب', name='country', required=True, placeholder="أدخل عنوان الطالب"),
            input('البريد الإليكتروني', name='email', type=TEXT, required=True, placeholder="أدخل البريد الإليكتروني", validate=lambda e: "بريد إليكتروني غير صالح" if "@" not in e else None),
            input('رقم الهاتف', name='phone', type=NUMBER, required=True, placeholder="أدخل رقم الهاتف"),
            input('تاريخ الميلاد', name='birthdate', type=DATE, required=True, placeholder="اختر تاريخ الميلاد"),
            select('المرحلة التعليمية/الكورس', options=['المرحلة الإبتدائية', 'المرحلة الإعدادية', 'المرحلة الثانوية', 'الجامعة', 'كورسات خاصة'], name='level', required=True),
            checkbox('مهارات الطالب', options=['Word', 'Excel', 'PowerPoint'], name='certi'),
            checkbox('اللغات', options=['Arabic', 'English', 'French'], inline=True, name='language')
        ]
    )
    
    img = file_upload('تحميل صورة شخصية', accept='image/*', multiple=False, required=True)
    student_img = img['content']
    
    put_text('Student CV:')
    put_table([
        ['StudentImg', 'Name', 'Address', 'Phone', 'Birthdate', 'Level', 'Certificate', 'Language'],
        [put_image(student_img).style('width:50px;'), data['student'], data['country'], data['phone'], data['birthdate'], data['level'], ', '.join(data['certi']), ', '.join(data['language'])]
    ])
    
    save_data([data['student'], data['country'], data['email'], data['phone'], data['birthdate'], data['level'], ', '.join(data['certi']), ', '.join(data['language'])])

start_server(App, debug=True)
