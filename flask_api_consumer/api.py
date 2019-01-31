import requests
from decimal import Decimal
from functools import partial, reduce


INDUSTRY_WEIGHT_FACTOR = 250


def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def calculate_cubic_size(kwargs):
    return reduce(
        lambda x, y: x * y,
        [kwargs[key] for key in ['width', 'length', 'height']],
        1
    )


calculate_cubic_weight = compose(
    lambda cubsize: round(cubsize * INDUSTRY_WEIGHT_FACTOR, 9),
    calculate_cubic_size,
    lambda size: {k: Decimal(v) / 100 for k, v in size.items()},
    lambda x: x['size']
)


extract_weights = compose(
    list,
    partial(map, calculate_cubic_weight),
    partial(filter, lambda x: x['category'] == 'Air Conditioners'),
)


def retrieve_weights(kwargs):
    host = kwargs['host']
    endpoint = kwargs['endpoint']
    weights_list = []
    while True:
        r = requests.get('{}{}'.format(host, endpoint))
        endpoint = r.json()['next']
        weights_list.extend(extract_weights(r.json()['objects']))
        if not endpoint:
            break
    return weights_list


calculate_aircon_cubic_weight_avg = compose(
    lambda weights: sum(weights) / len(weights),
    retrieve_weights,
)
