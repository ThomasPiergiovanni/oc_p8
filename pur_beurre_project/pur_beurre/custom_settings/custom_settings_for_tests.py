""" Custom settings module
"""
# DESCRIPTION: OFF API categorie response emulation.  Dictionnary
#   has all keys.
# MANDATORY: Yes.
# CUSTOM SETTINGS: To adapt if tests changes.
OFF_API_CATEGORIES_W_KEYS = {
    "count": 19982,
    "tags": [
        {
            "id": "en:snacks",
            "known": 1,
            "name": "Snacks",
            "products": 54568,
            "url": "https://fr.openfoodfacts.org/categorie/snacks"
        },
        {
            "id": "en:viennoiseries",
            "known": 1,
            "name": "Viennoiseries",
            "products": 4498,
            "url": "https://fr.openfoodfacts.org/categorie/viennoiseries"
        }
    ]
}

# DESCRIPTION: OFF API categorie response emulation.  Dictionnary
#   misses a keys.
# MANDATORY: Yes.
# CUSTOM SETTINGS: To adapt if tests changes.
OFF_API_CATEGORIES_WO_KEYS = {
    "count": 19982,
    "tags": [
        {
            "id": "en:snacks",
            "known": 1,
            "products": 54568,
            "url": "https://fr.openfoodfacts.org/categorie/snacks"
        }
    ]
}

# DESCRIPTION: OFF API products response emulation.  Dictionnary
#   has two products. The first one has keys the second is missing the
#   nutriscore_grade key.
# MANDATORY: Yes.
# CUSTOM SETTINGS: To adapt if tests changes.
OFF_API_PRODUCTS = {
    "count": 54568,
    "page": 1,
    "page_count": 50,
    "page_size": 50,
    "products": [
        {
            "categories": "Snacks,Snacks sucrés,Biscuits et gâteaux,"\
                "Biscuits,Biscuits au chocolat",
            "categories_hierarchy": [
                "en:snacks",
                "en:sweet-snacks",
                "en:biscuits-and-cakes",
                "en:biscuits",
                "en:chocolate-biscuits"
            ],
            "id": "7622210449283",
            "image_small_url": "https://static.openfoodfacts.org/"\
                "images/products/762/221/044/9283/"\
                "front_fr.429.200.jpg",
            "nutriments": {
                "fat_100g": 17,
                "salt_100g": 0.58,
                "saturated-fat_100g": 5.6,
                "sugars_100g": 32
            },
            "nutriscore_grade": "d",
            "product_name": "Prince Chocolat",
            "url": "https://fr.openfoodfacts.org/produit/"\
                "7622210449283/prince-chocolat-lu",
        },
        {
            "categories": "Snacks,Snacks sucrés,Biscuits et gâteaux,"\
                "Biscuits,Biscuits au chocolat",
            "categories_hierarchy": [
                "en:snacks",
                "en:sweet-snacks",
                "en:biscuits-and-cakes",
                "en:biscuits",
                "en:chocolate-biscuits"
            ],
            "id": "7622210449283",
            "image_small_url": "https://static.openfoodfacts.org/"\
                "images/products/762/221/044/9283/"\
                "front_fr.429.200.jpg",
            "nutriments": {
                "fat_100g": 17,
                "salt_100g": 0.58,
                "saturated-fat_100g": 5.6,
                "sugars_100g": 32
            },
            "product_name": "Prince Chocolat Test 2",
            "url": "https://fr.openfoodfacts.org/produit/"\
                "7622210449283/prince-chocolat-lu",
        },
    ],
    "skip": 0
}

# DESCRIPTION: It consist of valid catgeories that have been filtered out 
#   from OFF API response to ensure it suits db requirements.
# MANDATORY: Yes.
# CUSTOM SETTINGS: To adapt if tests changes.
OFF_API_FILTERED_CATEGORIES = [
    {
        'id': 'en:snacks',
        'known': 1,
        'name': 'Snacks',
        'products': 54568,
        'url': 'https://fr.openfoodfacts.org/categorie/snacks'
    },
    {
        "id": "en:breakfast-cereals",
        "known": 1,
        "name": "Céréales pour petit-déjeuner",
        "products": 4602,
        "url": "https://fr.openfoodfacts.org/categorie/cereales-pour-petit-dejeuner"
    }
]


# DESCRIPTION: Filterd out OFF API products. It only has valid products(ie: 
#   it has the correct keys.)
# MANDATORY: Yes.
# CUSTOM SETTINGS: To adapt if tests changes.
OFF_API_FILTERED_PRODUCTS = [
    {
        "categories": "Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits,Biscuits au chocolat",
        "categories_hierarchy": [
            "en:snacks",
            "en:sweet-snacks",
            "en:biscuits-and-cakes",
            "en:biscuits",
            "en:chocolate-biscuits"
        ],
        "id": "7622210449283",
        "image_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.200.jpg",
        "nutriments": {
            "fat_100g": 17,
            "salt_100g": 0.58,
            "saturated-fat_100g": 5.6,
            "sugars_100g": 32
        },
        "nutriscore_grade": "d",
        "product_name": "Prince Chocolat",
        "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-chocolat-lu",
    },
    {
        "categories": "Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits,Biscuits au chocolat",
        "categories_hierarchy": [
            "en:snacks",
            "en:sweet-snacks",
            "en:biscuits-and-cakes",
            "en:biscuits",
            "en:chocolate-biscuits"
        ],
        "id": "7622210449283_dummy",
        "image_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.200.jpg",
        "nutriments": {
            "fat_100g": 17,
            "salt_100g": 0.58,
            "saturated-fat_100g": 5.6,
            "sugars_100g": 32
        },
        "nutriscore_grade": "d",
        "product_name": "Prince Chocolat 2",
        "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-chocolat-lu",
    },
]