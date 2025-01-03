from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import  ListView, DetailView
from .forms import ProductForm
from .models import Product
from django.urls import reverse_lazy


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'
    # success_url = reverse_lazy('catalog:catalog/product_list')


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'


    # path('',ProductListView.as_view(), name='products_list'),
    # path('catalog/<int:pk>',ProductDetailView.as_view(), name='product_detail'),
    # path('catalog/new/',ProductCreateView.as_view(), name='product_create'),
    # path('catalog/<int:pk>/edit/',ProductUpdateView.as_view(), name='product_edit'),
    # path('catalog/<int:pk>/delete/',ProductDeleteView.as_view(), name='product_delete'),


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_create.html'
    success_url = reverse_lazy('catalog:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', kwargs={'pk':self.object.pk})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

# : /Users/ekaterinakurockina/PycharmProjects/pythonProject14/templates/catalog/product_confirm_delete.html (Source does not exist)
# In template /Users/ekaterinakurockina/PycharmProjects/pythonProject14/catalog/templates/catalog/product_form.html, error at line 12


#
#
# def home(request):
#     return render(request, 'catalog/home.html')
#
# def contacts(request):
#     return render(request, 'catalog/contacts.html')
#
# def base(request):
#     return render(request, 'catalog/base.html')

# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request,'catalog/products_list.html', context)

# def product_detail(request, pk):
#     # product = Product.objects.get(pk=pk)
#     product = get_object_or_404(Product, pk=pk)
#     context = {'product': product}
#     return render(request, 'catalog/product_detail.html', context)

# def contact_data(request):
#     if request.method == 'POST':
#         # Получение данных из формы
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         # Обработка данных (например, сохранение в БД, отправка email и т. д.)
#         # Здесь мы просто возвращаем простой ответ
#         return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
#     return render(request, 'catalog/contacts.html')