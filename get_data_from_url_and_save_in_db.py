import requests
import sys, os
#The following lines enable this script to contact django
sys.path.append('C:/Users/Apple/djangoprojects/bookbrowser/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bookbrowser.settings')

import django
django.setup()
from bladzijde.models import Publishers, Authors, Books

"""
After creating a project and app....
do the makemigration and migrate commands....
and then run this file
It will load and save all data in the sqlite3 database
"""
p_url = requests.get(url='http://assessment.elastique.nl/publishers/list')
a_url = requests.get(url='http://assessment.elastique.nl/authors/list')
b_url = requests.get(url='http://assessment.elastique.nl/books/highlighted')


#Upload Publishers to database
data = p_url.json()
for k, v in data.items():

        for item in v:

            for kk, vv in item.items():

                if kk == 'id':

                        p = Publishers(number = item['id'],
                                       name = item['name']
                                       )

                        p.save()
                else:
                        pass






#Upload Authors to database
data = a_url.json()
for k, v in data.items():

        for item in v:

            for kk, vv in item.items():

                if kk == 'id':

                        a = Authors(number = item['id'],
                                    first_name = item['first_name'],
                                    last_name = item['last_name'],
                                    )

                        a.save()
                else:
                        pass




#Upload Books to database
data = b_url.json()
for k, v in data.items():

    if type(v) == list:

        for item in v:

            for kk, vv in item.items():

                if kk == 'id':

                        publisher_dict = item['publisher']
                        author_dict = item['author']

                        b = Books(number = item['id'],
                                  title = item['title'],
                                  description = item['description'],
                                  cover_url = item['cover_url'],
                                  isbn = item['isbn'],
                                  publisher = Publishers.objects.get(number=publisher_dict['id']),
                                  author = Authors.objects.get(number=author_dict['id']),
                                  )

                        b.save()
                else:
                        pass

    else:
        pass



#display = Publishers.objects.filter(number=1)
#print (display)

#display = Authors.objects.filter(number=1)
#print (display)

#display = Books.objects.filter(number=1)
#print (display)
