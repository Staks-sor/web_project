import re

from django.shortcuts import render


def home(request):
    global message_station
    if request.method == 'POST':
        url = request.POST['url']
        pr_url(url)
        if url == '':
            message = 'Введите URL.'
            return render(request, 'home.html', {'message': message})
        else:
            # Validate URL format using regex
            regex = re.compile(
                r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://
                r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
                r'localhost|'  # localhost...
                r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
                r'(?::\d+)?'  # optional port
                r'(?:/?|[/?]\S+)$', re.IGNORECASE
            )

            if not re.match(regex, url):
                message = 'Данный адрес не соответствует.'
            else:

                # Show thank you message
                message = 'Все отлично, мне нужно пару минут что бы создать статью.'
                # if message == 'Все отлично, мне нужно пару минут что бы создать статью.':
                message_station = "Тут будет статья!!! "
                # return render(request, "home.html", {"my_variable": message_station})

            return render(request, 'home.html', {'message': message, 'message_station': message_station})

    else:
        return render(request, 'home.html')


def pr_url(url_print):
    print(url_print, 'Это адресс который ввел какой то пиздюк')
    import subprocess

    # запустить скрипт script_to_run.py в консоли

    subprocess.run(["python3", "/home/staks/PycharmProjects/ytmp3-dl/ytmp3-dl.py", "-l", "2", f"{url_print}"],
                   check=True)
