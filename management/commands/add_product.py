from django.core.management.base import BaseCommand
from mailing.models import Category, Product

class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        category4, _ = Category.objects.get_or_create(name='Фотокамеры', description='Цифровые фотокамеры')

        products = [
            {'name': 'Sony Alpha A7 III', 'description': 'Полнокадровая беззеркальная цифровая камера с 24,2-мегапиксельной матрицей, продвинутой системой автофокусировки и широкими возможностями видеосъемки в формате 4', 'category': category4, 'price': '131999', 'created_at':'2024-01-02','updated_at':'2024-01-03'},
            {'name': 'Canon EOS 5D Mark IV', 'description': 'Профессиональная цифровая зеркальная камера с 30,4-мегапиксельной полнокадровой матрицей, продвинутой системой автофокусировки и широкими возможностями фото- и видеосъемки', 'category': category4, 'price': '183099', 'created_at':'2024-01-02','updated_at':'2024-01-04'},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))
