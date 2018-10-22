from django.urls import path

from bladzijde import views

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('publishers/', views.PublishersView.as_view()),
    path('authors/', views.AuthorsView.as_view()),
    path('books/', views.BooksView.as_view()),
    path('publisher/', views.SpecificPublishersView.as_view()),
    path('author/', views.SpecificAuthorsView.as_view()),
    path('book/', views.SpecificBooksView.as_view()),
    path('publisher-kw-search/', views.PublishersKeywordSearchView.as_view()),
    path('author-kw-search/', views.AuthorsKeywordSearchView.as_view()),
    path('book-kw-search/', views.BooksKeywordSearchView.as_view()),
]

