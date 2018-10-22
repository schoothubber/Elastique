from django.views.generic import ListView, TemplateView

from bladzijde.models import Publishers, Authors, Books

class HomeView(TemplateView):
        template_name = 'base.html'

#Views that display all data
class PublishersView(ListView):
        model = Publishers


class AuthorsView(ListView):
        model = Authors


class BooksView(ListView):
        model = Books



#Views that display specific data based on id
class SpecificPublishersView(ListView):
        template_name = 'search_publishers.html'

        def get_queryset(self):
                num = self.request.GET.get('number')
                queryset = Publishers.objects.filter(number = num)
                return queryset


class SpecificAuthorsView(ListView):
        template_name = 'search_authors.html'

        def get_queryset(self):
                num = self.request.GET.get('number')
                queryset = Authors.objects.filter(number = num)
                return queryset


class SpecificBooksView(ListView):
        template_name = 'search_books.html'

        def get_queryset(self):
                num = self.request.GET.get('number')
                queryset = Books.objects.filter(number = num)
                return queryset


#Views that display specific data based on a keyword
class PublishersKeywordSearchView(ListView):
        template_name = 'search_keyword.html'
        context_object_name = 'publisher_list'

        def get_queryset(self):
                offset = self.request.GET.get('offset')
                limit = self.request.GET.get('limit')
                o,l = check_offset_and_limit(offset, limit)

                keyword = self.request.GET.get('keyword')
                if keyword is not None:
                        queryset = Publishers.objects.filter(name__icontains = keyword)[o:l]
                else: queryset = []

                return queryset



class AuthorsKeywordSearchView(ListView):
        template_name = 'search_keyword.html'
        context_object_name = 'author_list'

        def get_queryset(self):
                offset = self.request.GET.get('offset')
                limit = self.request.GET.get('limit')
                o,l = check_offset_and_limit(offset, limit)

                keyword = self.request.GET.get('keyword')
                if keyword is not None:
                        queryset = Authors.objects.filter(first_name__icontains = keyword)[o:l]
                else: queryset = []

                return queryset



class BooksKeywordSearchView(ListView):
        template_name = 'search_keyword.html'
        context_object_name = 'book_list'

        def get_queryset(self):
                offset = self.request.GET.get('offset')
                limit = self.request.GET.get('limit')
                o,l = check_offset_and_limit(offset, limit)

                keyword = self.request.GET.get('keyword')
                if keyword is not None:
                        queryset = Books.objects.filter(title__icontains = keyword)[o:l]
                else: queryset = []

                return queryset



def check_offset_and_limit(offset, limit):
        """
        Take the values 'offset' and 'limit' and make sure they go back as integers
        """


        if offset == '' or offset == None:
                o = 0
        else:
                try:
                        o = int(offset)
                except ValueError:
                        o = 0



        if limit == '' or limit == None:
                l = len(Publishers.objects.all())
        else:
                try:
                        l = int(limit)
                except ValueError:
                        l = len(Publishers.objects.all())


        return o,l+o
