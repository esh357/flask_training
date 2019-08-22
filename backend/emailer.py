from webapp import celery


@celery.task
def notify_production_creation(product_name, product_company):
    print(f"[*] Product Created {product_name} {product_company}")


@celery.task
def notify_category_creation(category_name):
    print(f"[*] Category Created {category_name}")
