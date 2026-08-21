from stripe import StripeClient
from config.settings import STRIPE_API_KEY, STRIPE_SUCCESS_URL

client = StripeClient(STRIPE_API_KEY)


def create_stripe_product(name):
    """Создает продукт в страйпе"""
    return client.v1.products.create({
        "name": name,
    })


def create_stripe_price(product_id, amount):
    """Создает цену в страйпе"""
    return client.v1.prices.create({
        "currency": "rub",
        "unit_amount": amount * 100,
        "product": product_id,
    })

def create_stripe_session(price_id):
    """Создает сессию на оплату в страйпе"""
    session = client.v1.checkout.sessions.create({
        "success_url": STRIPE_SUCCESS_URL,
        "line_items": [{"price": price_id, "quantity": 1}],
        "mode": "payment",
    })
    return session.id, session.url

def create_payment_session(course):
    product = create_stripe_product(course.name)
    price = create_stripe_price(product.id, course.price)
    return create_stripe_session(price.id)
