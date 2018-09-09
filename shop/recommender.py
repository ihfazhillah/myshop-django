import redis
from django.conf import settings
from .models import Product


r = redis.StrictRedis(host=settings.REDIS_HOST,
                      port=settings.REDIS_PORT,
                      db=settings.REDIS_DB)

class Recommender(object):
    def get_product_key(self, id):
        return 'product:{}:purchased_with'.format(id)

    def products_bought(self, products):
        products_id = [p.id for p in products]
        for product_id in products_id:
            for with_id in products_id:
                if product_id != with_id:
                    r.zincrby(self.get_product_key(product_id), with_id, amount=1)

    def suggest_products_for(self, products, max_results=6):
       products_id = [p.id for p in products]

       if len(products_id) == 1:
           suggestions = r.zrange(self.get_product_key(products_id[0]), 0, -1, desc=True)[:max_results]
       else:
           flat_ids = ''.join([str(id) for id in products_id])
           temp = 'tmp_{}'.format(flat_ids)
           keys = [self.get_product_key(_id) for _id in products_id]
           r.zunionstore(temp_keys, keys)
           r.zrem(tmp_keys, *products_id)
           suggestions = r.zrange(tmp_key, 0, -1, desc=True)[:max_results]
           r.delete(tmp_keys)

       suggestion_product_ids = [int(id) for id in suggestions]

       sugested_products = list(Product.objects.filter(id__in=suggestion_product_ids))
       sugested_products.sort(key=lambda x: suggestion_product_ids.index(x.id))

       return sugested_products


