from pywebio import start_server
from pywebio.input import * 
from pywebio.output import * 
from pywebio.session import * 
from pywebio.pin import * 


def App ():
    put_html('<center><h2>استمارة الطالب </h2></center>').style('background-color:#240A34; padding:25px;color:#FFF455;')
    put_html('<p>السيرة الذاتية للطلاب المقبولين </p>').style('text-align:center; font-weight:bold')
    put_html('<center><img src="https://www.zillacapital.com/wp-content/uploads/2021/09/education.jpg"></center>')
    data = input_group(
        'استمارة الطالب المؤهل ',
        [
            input('اسم الطالب ', name='student'),
            input('عنوان الطالب ', name='country'),
            input('البريد الإليكترونى', name='email'),
            input('رقم الهاتف ', name='phone', type=NUMBER),
            checkbox('مهارات الطالب ', options=['word', 'excel','powerpoint'], name='certi'),
            checkbox('اللغات ', options=['Arabic', 'English','France'],inline=True, name='language')

        ]

    )
    imags= file_upload(
        'تحميل صورة شخصية ',
        accept='image/*',
        multiple=True
    )
    for img in imags:
        global rr 
        rr = img['content']
    
    put_text('Student CV:')
    put_table([
        ['StudentImg', 'Name', 'Address', 'Phone', 'Certificate', 'Language'],
        [put_image(rr).style('width:50px;'), data['student'], data['country'], data['phone'], data['certi'], data['language']]
    ])

start_server(App, debug=True)
