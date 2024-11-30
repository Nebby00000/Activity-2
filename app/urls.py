from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfilePageView, AboutPageView, ContactPageView, RecipeListView, RecipeDetailView, RecipeCreateView, \
    RecipeUpdateView, RecipeDeleteView, LoginPageView ,RegisterPageView, LogoutPageView

urlpatterns = [

    path('', LoginPageView.as_view(), name='login'),
    path('register/', RegisterPageView.as_view(), name='register'),
    path('logout/', LogoutPageView.as_view(), name='logout'),

    path('home/', ProfilePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('recipe/', RecipeListView.as_view(), name='recipe'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/create', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/edit', RecipeUpdateView.as_view(), name='recipe_update'),
    path('recipe/<int:pk>/delete', RecipeDeleteView.as_view(), name='recipe_delete'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)