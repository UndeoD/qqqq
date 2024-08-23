from django.shortcuts import render


def catalog(request):
    context = {
        'title': 'Catalog',
        'goods': [
        {
            'image': 'deps/images/goods/14.jpg',
            'name': 'Чайный столик и три стула',
            'description': 'Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.',
            'price': 150.00
        },
        {
            'image': 'deps/images/goods/2.jpg',
            'name': 'Чайный столик и два стула',
            'description': 'Набор из стула и двух стульев в минималистическом стиле.',
            'price': 93.00
        },
        {
            'image': 'deps/images/goods/3.jpg',
            'name': 'Двухспальная кровать',
            'description': 'Кровать двухспальная с надголовником и очень ортопедичная.',
            'price': 670.00
        },
        {
            'image': 'deps/images/goods/4.jpg',
            'name': 'Кухонный стол с раковиной',
            'description': 'Кухонный стол для обеда с встроенной раковиной и стульями.',
            'price': 365.00
        },
        {
            'image': 'deps/images/goods/5.jpg',
            'name': 'Кухонный стол с встройкой',
            'description': 'Кухонный стол со встроенной плитой и раковиной. Много полок и красивый.',
            'price': 430.00
        },
        {
            'image': 'deps/images/goods/6.jpg',
            'name': 'Угловой диван для гостинной',
            'description': 'Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей.',
            'price': 610.00
        },
        {
            'image': 'deps/images/goods/7.jpg',
            'name': 'Прикроватный столик',
            'description': 'Прикроватный столик с двумя выдвижными ящиками.',
            'price': 55.00
        },
        {
            'image': 'deps/images/goods/8.jpg',
            'name': 'Диван обыкновенный',
            'description': 'Диван, он же софа обыкновенная, ничего примечательного.',
            'price': 190.00
        },
        {
            'image': 'deps/images/goods/9.jpg',
            'name': 'Стул офисный',
            'description': 'Описание товара, про то какой он классный.',
            'price': 30.00
        },
        {
            'image': 'deps/images/goods/10.jpg',
            'name': 'Растение',
            'description': 'Растение для украшения интерьера.',
            'price': 10.00
        },
        {
            'image': 'deps/images/goods/11.jpg',
            'name': 'Цветок стилизированный',
            'description': 'Дизайнерский цветок для украшения интерьера.',
            'price': 15.00
        },
        {
            'image': 'deps/images/goods/12.jpg',
            'name': 'Прикроватный столик',
            'description': 'Столик для размещения рядом с кроватью.',
            'price': 25.00
        }
    ]
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    return render(request, 'goods/catalog.html')