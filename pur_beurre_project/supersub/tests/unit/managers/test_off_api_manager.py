from django.test import TestCase, RequestFactory
from unittest.mock import patch

from django.http import HttpResponse

from supersub.manager.off_api_manager import OffApiManager


class OffApiManagerTest(TestCase):
    """
    """
    @classmethod
    def setUpTestData(cls):
        # cls.emulate_categories_response()
        cls.emulate_products_response()
        cls.manager = OffApiManager()
    
    @classmethod
    def emulate_categories_response(cls):
        cls.categories_response = {
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

    # @patch('supersub.manager.off_api_manager.OffApiManager.download_categories')
    # def test_download_catgories_with_mock(self, mock_download_categories):
    #     self.assertEqual(mock_download_categories.called, True)

    def test_filter_categories_with_raw_datas(self):
        self.manager.categories_response = self.categories_response
        self.manager.filter_categories()
        self.assertEqual(self.manager.categories[0]['id'], "en:snacks")
    
    def test_filter_products_with_raw_datas(self):
        self.manager.products_response = self.products_response
        self.manager.filter_products()
        self.assertEqual(
            self.manager.products[0]['product_name'],
            "Prince Chocolat")
    
    @classmethod
    def emulate_products_response(cls):
        cls.products_response = {
            "count": 54568,
            "page": 1,
            "page_count": 50,
            "page_size": 50,
            "products": [
                {
                    "_id": "7622210449283",
                    "_keywords": [
                        "biscuit",
                        "snack",
                        "sucre",
                        "lu",
                        "gateaux",
                        "conservateur",
                        "et",
                        "fourre",
                        "chocolat",
                        "35",
                        "prince",
                        "san",
                        "parfum",
                        "au"
                    ],
                    "added_countries_tags": [],
                    "additives_debug_tags": [
                        "en-e322i-added",
                        "en-e450-added",
                        "en-e500ii-added",
                        "en-e503ii-added"
                    ],
                    "additives_n": 3,
                    "additives_old_n": 4,
                    "additives_old_tags": [
                        "en:e503",
                        "en:e500",
                        "en:e1403",
                        "en:e322"
                    ],
                    "additives_original_tags": [
                        "en:e503ii",
                        "en:e500ii",
                        "en:e322i"
                    ],
                    "additives_prev_original_tags": [
                        "en:e503",
                        "en:e500",
                        "en:e450i",
                        "en:e322"
                    ],
                    "additives_tags": [
                        "en:e322",
                        "en:e322i",
                        "en:e500",
                        "en:e500ii",
                        "en:e503",
                        "en:e503ii"
                    ],
                    "allergens": "en:eggs,en:gluten,en:milk,en:soybeans",
                    "allergens_from_ingredients": "blé, lécithine de soja, lactose, protéines de lait",
                    "allergens_from_user": "(fr) Œufs,Gluten,Lait,Soja",
                    "allergens_hierarchy": [
                        "en:eggs",
                        "en:gluten",
                        "en:milk",
                        "en:soybeans"
                    ],
                    "allergens_lc": "fr",
                    "allergens_tags": [
                        "en:eggs",
                        "en:gluten",
                        "en:milk",
                        "en:soybeans"
                    ],
                    "amino_acids_prev_tags": [],
                    "amino_acids_tags": [],
                    "brands": "Lu",
                    "brands_tags": [
                        "lu"
                    ],
                    "carbon_footprint_from_known_ingredients_debug": "en:cereal 50.7% x 0.3 = 15.21 g - ",
                    "carbon_footprint_percent_of_known_ingredients": 50.7,
                    "categories": "Snacks,Snacks sucrés,Biscuits et gâteaux,Biscuits,Biscuits au chocolat",
                    "categories_hierarchy": [
                        "en:snacks",
                        "en:sweet-snacks",
                        "en:biscuits-and-cakes",
                        "en:biscuits",
                        "en:chocolate-biscuits"
                    ],
                    "categories_lc": "fr",
                    "categories_old": "Botanas,Snacks dulces,Galletas y pasteles,Galletas,Galletas de chocolate",
                    "categories_properties": {
                        "agribalyse_proxy_food_code:en": "24036"
                    },
                    "categories_properties_tags": [
                        "all-products",
                        "categories-known",
                        "agribalyse-food-code-unknown",
                        "agribalyse-proxy-food-code-24036",
                        "agribalyse-proxy-food-code-known",
                        "ciqual-food-code-unknown",
                        "agribalyse-known",
                        "agribalyse-24036"
                    ],
                    "categories_tags": [
                        "en:snacks",
                        "en:sweet-snacks",
                        "en:biscuits-and-cakes",
                        "en:biscuits",
                        "en:chocolate-biscuits"
                    ],
                    "category_properties": {},
                    "checked": "on",
                    "checkers_tags": [
                        "beniben"
                    ],
                    "ciqual_food_name_tags": [
                        "unknown"
                    ],
                    "cities_tags": [],
                    "code": "7622210449283",
                    "codes_tags": [
                        "code-13",
                        "7622210449xxx",
                        "7xxxxxxxxxxxx"
                    ],
                    "compared_to_category": "en:chocolate-biscuits",
                    "complete": 0,
                    "completeness": 0.9,
                    "correctors_tags": [
                        "tacite",
                        "quentinbrd"
                    ],
                    "countries": "Algérie,Belgique,France,Polynésie française,Allemagne,Guadeloupe,Hongrie,Luxembourg,Martinique,Maroc,Nouvelle-Calédonie,Portugal,La Réunion,Espagne,Suisse,États-Unis",
                    "countries_beforescanbot": "Belgique,France,Polynésie française,Guadeloupe,Luxembourg,Portugal,La Réunion",
                    "countries_hierarchy": [
                        "en:algeria",
                        "en:belgium",
                        "en:france",
                        "en:french-polynesia",
                        "en:germany",
                        "en:guadeloupe",
                        "en:hungary",
                        "en:luxembourg",
                        "en:martinique",
                        "en:morocco",
                        "en:new-caledonia",
                        "en:portugal",
                        "en:reunion",
                        "en:spain",
                        "en:switzerland",
                        "en:united-states"
                    ],
                    "countries_lc": "fr",
                    "countries_tags": [
                        "en:algeria",
                        "en:belgium",
                        "en:france",
                        "en:french-polynesia",
                        "en:germany",
                        "en:guadeloupe",
                        "en:hungary",
                        "en:luxembourg",
                        "en:martinique",
                        "en:morocco",
                        "en:new-caledonia",
                        "en:portugal",
                        "en:reunion",
                        "en:spain",
                        "en:switzerland",
                        "en:united-states"
                    ],
                    "created_t": 1443988064,
                    "creator": "openfoodfacts-contributors",
                    "data_quality_bugs_tags": [],
                    "data_quality_errors_tags": [],
                    "data_quality_info_tags": [
                        "en:packaging-data-complete",
                        "en:ingredients-percent-analysis-ok",
                        "en:nutrition-data-prepared",
                        "en:carbon-footprint-from-known-ingredients-but-not-from-meat-or-fish"
                    ],
                    "data_quality_tags": [
                        "en:packaging-data-complete",
                        "en:ingredients-percent-analysis-ok",
                        "en:nutrition-data-prepared",
                        "en:carbon-footprint-from-known-ingredients-but-not-from-meat-or-fish",
                        "en:ingredients-fr-5-consonants",
                        "en:ingredients-en-ending-comma",
                        "en:nutrition-data-prepared-without-category-dried-products-to-be-rehydrated",
                        "en:ecoscore-origins-of-ingredients-origins-are-100-percent-unknown",
                        "en:ecoscore-production-system-no-label"
                    ],
                    "data_quality_warnings_tags": [
                        "en:ingredients-fr-5-consonants",
                        "en:ingredients-en-ending-comma",
                        "en:nutrition-data-prepared-without-category-dried-products-to-be-rehydrated",
                        "en:ecoscore-origins-of-ingredients-origins-are-100-percent-unknown",
                        "en:ecoscore-production-system-no-label"
                    ],
                    "data_sources": "App - yuka, Apps",
                    "data_sources_tags": [
                        "app-yuka",
                        "apps"
                    ],
                    "debug_param_sorted_langs": [
                        "fr",
                        "en"
                    ],
                    "ecoscore_data": {
                        "adjustments": {
                            "origins_of_ingredients": {
                                "aggregated_origins": [
                                    {
                                        "origin": "en:unknown",
                                        "percent": 100
                                    }
                                ],
                                "epi_score": 0,
                                "epi_value": -5,
                                "origins_from_origins_field": [
                                    "en:unknown"
                                ],
                                "transportation_score_be": 0,
                                "warning": "origins_are_100_percent_unknown"
                            },
                            "production_system": {
                                "warning": "no_label"
                            },
                            "threatened_species": {
                                "ingredient": "en:palm-oil",
                                "value": -10
                            }
                        },
                        "grade": "d",
                        "grade_be": "d",
                        "grade_ch": "d",
                        "grade_de": "d",
                        "grade_es": "d",
                        "grade_fr": "d",
                        "grade_ie": "d",
                        "grade_it": "d",
                        "grade_lu": "d",
                        "grade_nl": "d",
                        "missing": {
                            "labels": 1,
                            "origins": 1
                        },
                        "missing_data_warning": 1,
                        "score": 34,
                        "score_be": 29,
                        "score_ch": 29,
                        "score_de": 29,
                        "score_es": 29,
                        "score_fr": 29,
                        "score_ie": 29,
                        "score_it": 29,
                        "score_lu": 29,
                        "score_nl": 29,
                        "status": "known"
                    },
                    "ecoscore_grade": "d",
                    "ecoscore_score": 34,
                    "ecoscore_tags": [
                        "d"
                    ],
                    "editors": [
                        "",
                        "tacite"
                    ],
                    "editors_tags": [
                        "eatshalal",
                        "aleene",
                        "jamesjamesjames",
                        "product-scanner"
                    ],
                    "emb_codes": "",
                    "emb_codes_20141016": "",
                    "emb_codes_orig": "",
                    "emb_codes_tags": [],
                    "entry_dates_tags": [
                        "2015-10-04",
                        "2015-10",
                        "2015"
                    ],
                    "environment_impact_level": "",
                    "environment_impact_level_tags": [],
                    "expiration_date": "31/07/2020",
                    "fruits-vegetables-nuts_100g_estimate": 0,
                    "generic_name": "BISCUITS FOURRÉS (35%) PARFUM CHOCOLAT",
                    "generic_name_en": "",
                    "generic_name_fr": "BISCUITS FOURRÉS (35%) PARFUM CHOCOLAT",
                    "id": "7622210449283",
                    "image_front_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.200.jpg",
                    "image_front_thumb_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.100.jpg",
                    "image_front_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.400.jpg",
                    "image_ingredients_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/ingredients_fr.396.200.jpg",
                    "image_ingredients_thumb_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/ingredients_fr.396.100.jpg",
                    "image_ingredients_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/ingredients_fr.396.400.jpg",
                    "image_nutrition_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/nutrition_fr.406.200.jpg",
                    "image_nutrition_thumb_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/nutrition_fr.406.100.jpg",
                    "image_nutrition_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/nutrition_fr.406.400.jpg",
                    "image_packaging_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/packaging_fr.430.200.jpg",
                    "image_packaging_thumb_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/packaging_fr.430.100.jpg",
                    "image_packaging_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/packaging_fr.430.400.jpg",
                    "image_small_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.200.jpg",
                    "image_thumb_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.100.jpg",
                    "image_url": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.400.jpg",
                    "images": {
                        "1": {
                            "sizes": {
                                "100": {
                                    "h": 100,
                                    "w": 56
                                },
                                "400": {
                                    "h": 400,
                                    "w": 225
                                },
                                "full": {
                                    "h": 2592,
                                    "w": 1456
                                }
                            },
                            "uploaded_t": "1443988064",
                            "uploader": "openfoodfacts-contributors"
                        },
                        "5": {
                            "sizes": {
                                "100": {
                                    "h": 100,
                                    "w": 75
                                },
                                "400": {
                                    "h": 400,
                                    "w": 299
                                },
                                "full": {
                                    "h": 2592,
                                    "w": 1936
                                }
                            },
                            "uploaded_t": "1451475843",
                            "uploader": "teolemon"
                        },
                        "front_en": {
                            "angle": 0,
                            "coordinates_image_size": "full",
                            "geometry": "0x0--1--1",
                            "imgid": "195",
                            "rev": "427",
                            "sizes": {
                                "100": {
                                    "h": 100,
                                    "w": 34
                                },
                                "200": {
                                    "h": 200,
                                    "w": 68
                                },
                                "400": {
                                    "h": 400,
                                    "w": 136
                                },
                                "full": {
                                    "h": 400,
                                    "w": 136
                                }
                            },
                            "x1": "-1",
                            "x2": "-1",
                            "y1": "-1",
                            "y2": "-1"
                        },
                        "front_fr": {
                            "angle": "0",
                            "coordinates_image_size": "full",
                            "geometry": "0x0-0-0",
                            "imgid": "195",
                            "normalize": "false",
                            "rev": "429",
                            "sizes": {
                                "100": {
                                    "h": 100,
                                    "w": 34
                                },
                                "200": {
                                    "h": 200,
                                    "w": 68
                                },
                                "400": {
                                    "h": 400,
                                    "w": 136
                                },
                                "full": {
                                    "h": 400,
                                    "w": 136
                                }
                            },
                            "white_magic": "false",
                            "x1": "0",
                            "x2": "0",
                            "y1": "0",
                            "y2": "0"
                        },
                        "ingredients_fr": {
                            "angle": "0",
                            "coordinates_image_size": "full",
                            "geometry": "1408x1014-528-262",
                            "imgid": "189",
                            "normalize": "false",
                            "rev": "396",
                            "sizes": {
                                "100": {
                                    "h": 72,
                                    "w": 100
                                },
                                "200": {
                                    "h": 144,
                                    "w": 200
                                },
                                "400": {
                                    "h": 288,
                                    "w": 400
                                },
                                "full": {
                                    "h": 1014,
                                    "w": 1408
                                }
                            },
                            "white_magic": "false",
                            "x1": "528.2933025404158",
                            "x2": "1936.4087759815238",
                            "y1": "262.8575346420323",
                            "y2": "1276.1046478060043"
                        },
                        "nutrition_fr": {
                            "angle": 0,
                            "coordinates_image_size": "full",
                            "geometry": "0x0--1--1",
                            "imgid": "193",
                            "rev": "406",
                            "sizes": {
                                "100": {
                                    "h": 66,
                                    "w": 100
                                },
                                "200": {
                                    "h": 132,
                                    "w": 200
                                },
                                "400": {
                                    "h": 265,
                                    "w": 400
                                },
                                "full": {
                                    "h": 1252,
                                    "w": 1893
                                }
                            },
                            "x1": "-1",
                            "x2": "-1",
                            "y1": "-1",
                            "y2": "-1"
                        },
                        "packaging_fr": {
                            "angle": "0",
                            "coordinates_image_size": "full",
                            "geometry": "1925x320-519-1230",
                            "imgid": "173",
                            "normalize": "false",
                            "rev": "430",
                            "sizes": {
                                "100": {
                                    "h": 17,
                                    "w": 100
                                },
                                "200": {
                                    "h": 33,
                                    "w": 200
                                },
                                "400": {
                                    "h": 66,
                                    "w": 400
                                },
                                "full": {
                                    "h": 320,
                                    "w": 1925
                                }
                            },
                            "white_magic": "false",
                            "x1": "519.8568764461834",
                            "x2": "2444.6371496059983",
                            "y1": "1230.1567460841977",
                            "y2": "1550"
                        }
                    },
                    "informers_tags": [
                        "openfoodfacts-contributors",
                        "quentinbrd"
                    ],
                    "ingredients": [
                        {
                            "id": "en:cereal",
                            "ingredients": [
                                {
                                    "id": "en:wheat-flour",
                                    "percent": 35,
                                    "percent_estimate": 35,
                                    "percent_max": 35,
                                    "percent_min": 35,
                                    "text": "farine de blé",
                                    "vegan": "yes",
                                    "vegetarian": "yes"
                                },
                                {
                                    "id": "en:whole-wheat-flour",
                                    "percent": "15.7",
                                    "percent_estimate": 15.7,
                                    "percent_max": 15.7,
                                    "percent_min": 15.7,
                                    "text": "farine de blé complète",
                                    "vegan": "yes",
                                    "vegetarian": "yes"
                                }
                            ],
                            "percent": 50.7,
                            "percent_estimate": 50.7,
                            "percent_max": 50.7,
                            "percent_min": 50.7,
                            "text": "céréales",
                            "vegan": "yes",
                            "vegetarian": "yes"
                        },
                        {
                            "id": "en:sugar",
                            "percent_estimate": 23.875,
                            "percent_max": 43.25,
                            "percent_min": 4.5,
                            "text": "sucre",
                            "vegan": "yes",
                            "vegetarian": "yes"
                        },
                        {
                            "from_palm_oil": "yes",
                            "id": "en:palm-oil",
                            "percent_estimate": 14.9625,
                            "percent_max": 30.3333333333333,
                            "percent_min": 4.5,
                            "text": "huiles végétales de palme",
                            "vegan": "yes",
                            "vegetarian": "yes"
                        },
                        {
                            "from_palm_oil": "no",
                            "id": "en:colza-oil",
                            "percent_estimate": 7.48125,
                            "percent_max": 22.4,
                            "percent_min": 4.5,
                            "text": "huiles végétales de colza",
                            "vegan": "yes",
                            "vegetarian": "yes"
                        },
                        {
                            "id": "en:fat-reduced-cocoa-powder",
                            "percent": 4.5,
                            "percent_estimate": 2.98125,
                            "percent_max": 4.5,
                            "percent_min": 4.5,
                            "text": "cacao maigre en poudre",
                            "vegan": "yes",
                            "vegetarian": "yes"
                        },
                        {
                            "id": "en:glucose-syrup",
                            "percent_estimate": 0,
                            "percent_max": 4.5,
                            "percent_min": 0,
                            "text": "sirop de glucose",
                            "vegan": "yes",
                            "vegetarian": "yes"
                        },
                        {
                            "id": "en:wheat-starch",
                            "percent_estimate": 0,
                            "percent_max": 4.5,
                            "percent_min": 0,
                            "text": "amidon de blé",
                            "vegan": "yes",
                            "vegetarian": "yes"
                        },
                        {
                            "id": "en:raising-agent",
                            "ingredients": [
                                {
                                    "id": "en:e503ii",
                                    "percent_estimate": 0,
                                    "percent_max": 4.5,
                                    "percent_min": 0,
                                    "text": "carbonate acide d'ammonium",
                                    "vegan": "yes",
                                    "vegetarian": "yes"
                                },
                                {
                                    "id": "en:e500ii",
                                    "percent_estimate": 0,
                                    "percent_max": 2.25,
                                    "percent_min": 0,
                                    "text": "carbonate acide de sodium",
                                    "vegan": "yes",
                                    "vegetarian": "yes"
                                },
                                {
                                    "id": "fr:diphpsphate disodique",
                                    "percent_estimate": 0,
                                    "percent_max": 1.5,
                                    "percent_min": 0,
                                    "text": "diphpsphate disodique"
                                }
                            ],
                            "percent_estimate": 0,
                            "percent_max": 4.5,
                            "percent_min": 0,
                            "text": "poudre à lever"
                        },
                        {
                            "id": "en:emulsifier",
                            "ingredients": [
                                {
                                    "id": "en:soya-lecithin",
                                    "percent_estimate": 0,
                                    "percent_max": 4.5,
                                    "percent_min": 0,
                                    "text": "lécithine de soja",
                                    "vegan": "yes",
                                    "vegetarian": "yes"
                                },
                                {
                                    "id": "en:sunflower-lecithin",
                                    "percent_estimate": 0,
                                    "percent_max": 2.25,
                                    "percent_min": 0,
                                    "text": "lécithine de tournesol",
                                    "vegan": "yes",
                                    "vegetarian": "yes"
                                }
                            ],
                            "percent_estimate": 0,
                            "percent_max": 4.5,
                            "percent_min": 0,
                            "text": "émulsifiant"
                        },
                        {
                            "id": "en:salt",
                            "percent_estimate": 0,
                            "percent_max": 4.5,
                            "percent_min": 0,
                            "text": "sel",
                            "vegan": "yes",
                            "vegetarian": "yes"
                        },
                        {
                            "id": "en:skimmed-milk-powder",
                            "percent_estimate": 0,
                            "percent_max": 3.97777777777778,
                            "percent_min": 0,
                            "text": "lait écrémé en poudre",
                            "vegan": "no",
                            "vegetarian": "yes"
                        },
                        {
                            "id": "en:lactose-and-milk-proteins",
                            "percent_estimate": 0,
                            "percent_max": 3.58,
                            "percent_min": 0,
                            "text": "lactose et protéines de lait",
                            "vegan": "no",
                            "vegetarian": "yes"
                        },
                        {
                            "id": "en:flavouring",
                            "percent_estimate": 0,
                            "percent_max": 3.25454545454545,
                            "percent_min": 0,
                            "text": "arômes",
                            "vegan": "maybe",
                            "vegetarian": "maybe"
                        }
                    ],
                    "ingredients_analysis_tags": [
                        "en:palm-oil",
                        "en:non-vegan",
                        "en:vegetarian-status-unknown"
                    ],
                    "ingredients_from_or_that_may_be_from_palm_oil_n": 1,
                    "ingredients_from_palm_oil_n": 1,
                    "ingredients_from_palm_oil_tags": [
                        "huile-de-palme"
                    ],
                    "labels_lc": "fr",
                    "labels_old": "Sans conservateurs",
                    "labels_tags": [
                        "en:no-preservatives"
                    ],
                    "lang": "fr",
                    "languages": {
                        "en:english": 2,
                        "en:french": 7
                    },
                    "languages_codes": {
                        "en": 2,
                        "fr": 7
                    },
                    "languages_hierarchy": [
                        "en:french",
                        "en:english"
                    ],
                    "languages_tags": [
                        "en:french",
                        "en:english",
                        "en:2",
                        "en:multilingual"
                    ],
                    "last_check_dates_tags": [
                        "2018-10-30",
                        "2018-10",
                        "2018"
                    ],
                    "last_checked_t": 1540933974,
                    "last_checker": "beniben",
                    "last_edit_dates_tags": [
                        "2021-05-11",
                        "2021-05",
                        "2021"
                    ],
                    "last_editor": "quentinbrd",
                    "last_image_dates_tags": [
                        "2021-05-03",
                        "2021-05",
                        "2021"
                    ],
                    "last_image_t": 1620055369,
                    "last_modified_by": "quentinbrd",
                    "last_modified_t": 1620707768,
                    "lc": "fr",
                    "link": "https://www.lu.fr/prince",
                    "main_countries_tags": [],
                    "manufacturing_places": "",
                    "manufacturing_places_tags": [],
                    "max_imgid": "195",
                    "minerals_prev_tags": [],
                    "minerals_tags": [],
                    "misc_tags": [
                        "en:nutrition-fruits-vegetables-nuts-estimate-from-ingredients",
                        "en:nutrition-all-nutriscore-values-known",
                        "en:nutriscore-computed",
                        "en:ecoscore-missing-data-warning",
                        "en:ecoscore-computed",
                        "en:main-countries-be-unexpectedly-low-scans",
                        "en:main-countries-be-unexpectedly-low-scans-10-20-percent-of-expected",
                        "en:main-countries-de-unexpectedly-low-scans",
                        "en:main-countries-de-unexpectedly-low-scans-0-10-percent-of-expected",
                        "en:main-countries-de-unexpectedly-low-scans-and-no-data-in-country-language",
                        "en:main-countries-de-product-name-not-in-country-language",
                        "en:main-countries-de-ingredients-not-in-country-language",
                        "en:main-countries-de-no-data-in-country-language",
                        "en:main-countries-hu-unexpectedly-low-scans",
                        "en:main-countries-hu-unexpectedly-low-scans-0-10-percent-of-expected",
                        "en:main-countries-hu-unexpectedly-low-scans-and-no-data-in-country-language",
                        "en:main-countries-hu-product-name-not-in-country-language",
                        "en:main-countries-hu-ingredients-not-in-country-language",
                        "en:main-countries-hu-no-data-in-country-language",
                        "en:main-countries-pt-unexpectedly-low-scans",
                        "en:main-countries-pt-unexpectedly-low-scans-10-20-percent-of-expected",
                        "en:main-countries-pt-unexpectedly-low-scans-and-no-data-in-country-language",
                        "en:main-countries-pt-product-name-not-in-country-language",
                        "en:main-countries-pt-ingredients-not-in-country-language",
                        "en:main-countries-pt-no-data-in-country-language",
                        "en:main-countries-es-unexpectedly-low-scans",
                        "en:main-countries-es-unexpectedly-low-scans-0-10-percent-of-expected",
                        "en:main-countries-es-unexpectedly-low-scans-and-no-data-in-country-language",
                        "en:main-countries-es-product-name-not-in-country-language",
                        "en:main-countries-es-ingredients-not-in-country-language",
                        "en:main-countries-es-no-data-in-country-language",
                        "en:main-countries-ch-unexpectedly-low-scans",
                        "en:main-countries-ch-unexpectedly-low-scans-10-20-percent-of-expected",
                        "en:main-countries-us-product-name-not-in-country-language",
                        "en:main-countries-us-only-1-field-in-country-language"
                    ],
                    "no_nutrition_data": "",
                    "nova_group": 4,
                    "nova_group_debug": " -- ingredients/en:salt : 3 -- ingredients/en:emulsifier : 4",
                    "nova_group_tags": [
                        "not-applicable"
                    ],
                    "nova_groups": "4",
                    "nova_groups_tags": [
                        "en:4-ultra-processed-food-and-drink-products"
                    ],
                    "nucleotides_prev_tags": [],
                    "nucleotides_tags": [],
                    "nutrient_levels": {
                        "fat": "moderate",
                        "salt": "moderate",
                        "saturated-fat": "high",
                        "sugars": "high"
                    },
                    "nutrient_levels_tags": [
                        "en:fat-in-moderate-quantity",
                        "en:saturated-fat-in-high-quantity",
                        "en:sugars-in-high-quantity",
                        "en:salt-in-moderate-quantity"
                    ],
                    "nutriments": {
                        "carbohydrates": 69,
                        "carbohydrates_100g": 69,
                        "carbohydrates_prepared_unit": "g",
                        "carbohydrates_serving": 13.8,
                        "carbohydrates_unit": "g",
                        "carbohydrates_value": 69,
                        "carbon-footprint-from-known-ingredients_100g": 15.21,
                        "carbon-footprint-from-known-ingredients_product": 45.6,
                        "carbon-footprint-from-known-ingredients_serving": 3.04,
                        "energy": 1955,
                        "energy-kcal": 465,
                        "energy-kcal_100g": 465,
                        "energy-kcal_prepared_unit": "kcal",
                        "energy-kcal_serving": 93,
                        "energy-kcal_unit": "kcal",
                        "energy-kcal_value": 465,
                        "energy-kj": 1955,
                        "energy-kj_100g": 1955,
                        "energy-kj_prepared_unit": "kJ",
                        "energy-kj_serving": 391,
                        "energy-kj_unit": "kJ",
                        "energy-kj_value": 1955,
                        "energy_100g": 1955,
                        "energy_prepared": 391,
                        "energy_prepared_100g": 391,
                        "energy_prepared_serving": 78.2,
                        "energy_prepared_unit": "kJ",
                        "energy_serving": 391,
                        "energy_unit": "kJ",
                        "energy_value": 1955,
                        "fat": 17,
                        "fat_100g": 17,
                        "fat_prepared_unit": "mg",
                        "fat_serving": 3.4,
                        "fat_unit": "g",
                        "fat_value": 17,
                        "fiber": 4,
                        "fiber_100g": 4,
                        "fiber_prepared_unit": "mg",
                        "fiber_serving": 0.8,
                        "fiber_unit": "g",
                        "fiber_value": 4,
                        "fruits-vegetables-nuts-estimate-from-ingredients_100g": 4.5,
                        "nova-group": 4,
                        "nova-group_100g": 4,
                        "nova-group_serving": 4,
                        "nutrition-score-fr": 15,
                        "nutrition-score-fr_100g": 15,
                        "proteins": 6.4,
                        "proteins_100g": 6.4,
                        "proteins_prepared_unit": "mg",
                        "proteins_serving": 1.28,
                        "proteins_unit": "g",
                        "proteins_value": 6.4,
                        "salt": 0.58,
                        "salt_100g": 0.58,
                        "salt_prepared_unit": "mg",
                        "salt_serving": 0.116,
                        "salt_unit": "g",
                        "salt_value": 0.58,
                        "saturated-fat": 5.6,
                        "saturated-fat_100g": 5.6,
                        "saturated-fat_prepared_unit": "mg",
                        "saturated-fat_serving": 1.12,
                        "saturated-fat_unit": "g",
                        "saturated-fat_value": 5.6,
                        "sodium": 0.232,
                        "sodium_100g": 0.232,
                        "sodium_prepared_unit": "mg",
                        "sodium_serving": 0.0464,
                        "sodium_unit": "g",
                        "sodium_value": 0.232,
                        "sugars": 32,
                        "sugars_100g": 32,
                        "sugars_prepared_unit": "mg",
                        "sugars_serving": 6.4,
                        "sugars_unit": "g",
                        "sugars_value": 32
                    },
                    "nutriscore_data": {
                        "energy": 1955,
                        "energy_points": 5,
                        "energy_value": 1955,
                        "fiber": 4,
                        "fiber_points": 4,
                        "fiber_value": 4,
                        "fruits_vegetables_nuts_colza_walnut_olive_oils": 4.5,
                        "fruits_vegetables_nuts_colza_walnut_olive_oils_points": 0,
                        "fruits_vegetables_nuts_colza_walnut_olive_oils_value": 4.5,
                        "grade": "d",
                        "is_beverage": 0,
                        "is_cheese": 0,
                        "is_fat": 0,
                        "is_water": 0,
                        "negative_points": 19,
                        "positive_points": 4,
                        "proteins": 6.4,
                        "proteins_points": 3,
                        "proteins_value": 6.4,
                        "saturated_fat": 5.6,
                        "saturated_fat_points": 5,
                        "saturated_fat_ratio": 32.9411764705882,
                        "saturated_fat_ratio_points": 4,
                        "saturated_fat_ratio_value": 32.9,
                        "saturated_fat_value": 5.6,
                        "score": 15,
                        "sodium": 232,
                        "sodium_points": 2,
                        "sodium_value": 232,
                        "sugars": 32,
                        "sugars_points": 7,
                        "sugars_value": 32
                    },
                    "nutriscore_grade": "d",
                    "nutriscore_score": 15,
                    "nutriscore_score_opposite": -15,
                    "nutrition_data": "on",
                    "nutrition_data_per": "100g",
                    "nutrition_data_prepared": "on",
                    "nutrition_data_prepared_per": "100g",
                    "nutrition_grade_fr": "d",
                    "nutrition_grades": "d",
                    "nutrition_grades_tags": [
                        "d"
                    ],
                    "nutrition_score_beverage": 0,
                    "nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients": 1,
                    "nutrition_score_warning_fruits_vegetables_nuts_estimate_from_ingredients_value": 4.5,
                    "obsolete": "",
                    "obsolete_since_date": "",
                    "origins": "",
                    "origins_hierarchy": [],
                    "origins_lc": "fr",
                    "origins_old": "",
                    "origins_tags": [],
                    "other_nutritional_substances_prev_tags": [],
                    "other_nutritional_substances_tags": [],
                    "packaging": "plastique,fr:Film en plastique,paquet,mondelez,fr:Etui en carton",
                    "packaging_tags": [
                        "plastique",
                        "fr-film-en-plastique",
                        "paquet",
                        "mondelez",
                        "fr-etui-en-carton"
                    ],
                    "packaging_text": "1 Film plastique à jeter, 1 étui carton à recycler",
                    "packaging_text_en": "",
                    "packaging_text_fr": "1 Film plastique à jeter, 1 étui carton à recycler",
                    "packagings": [
                        {
                            "material": "en:plastic",
                            "number": "1",
                            "recycling": "en:discard",
                            "shape": "en:film"
                        },
                        {
                            "material": "en:cardboard",
                            "number": "1",
                            "recycling": "en:recycle",
                            "shape": "en:sleeve"
                        }
                    ],
                    "photographers_tags": [
                        "openfoodfacts-contributors",
                        "teolemon",
                        "jeremywolf",
                        "mkl159",
                        "martialc57",
                        "kiliweb",
                        "l-instant-convivial",
                        "eatshalal",
                        "kick-ha-farce",
                        "fischer",
                        "asmoth",
                        "kch",
                        "date-limite-app",
                        "vincequertier-live-fr",
                        "nelathylanno42",
                        "samoth47",
                        "foodvisor"
                    ],
                    "pnns_groups_1": "Sugary snacks",
                    "pnns_groups_1_tags": [
                        "sugary-snacks",
                        "known"
                    ],
                    "pnns_groups_2": "Biscuits and cakes",
                    "pnns_groups_2_tags": [
                        "biscuits-and-cakes",
                        "known"
                    ],
                    "popularity_key": 19999993087,
                    "popularity_tags": [
                        "top-10-scans-2019",
                        "top-50-scans-2019",
                        "top-100-scans-2019",
                        "top-100000-ci-scans-2020"
                    ],
                    "product_name": "Prince Chocolat",
                    "product_name_en": "",
                    "product_name_fr": "Prince Chocolat",
                    "product_quantity": 300,
                    "purchase_places": "F-77480 Mousseaux-les-Bray,FRANCE",
                    "purchase_places_tags": [
                        "f-77480-mousseaux-les-bray",
                        "france"
                    ],
                    "quantity": "300 g",
                    "removed_countries_tags": [],
                    "rev": 431,
                    "scans_n": 4908,
                    "selected_images": {
                        "front": {
                            "display": {
                                "en": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_en.427.400.jpg",
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.400.jpg"
                            },
                            "small": {
                                "en": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_en.427.200.jpg",
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.200.jpg"
                            },
                            "thumb": {
                                "en": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_en.427.100.jpg",
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/front_fr.429.100.jpg"
                            }
                        },
                        "ingredients": {
                            "display": {
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/ingredients_fr.396.400.jpg"
                            },
                            "small": {
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/ingredients_fr.396.200.jpg"
                            },
                            "thumb": {
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/ingredients_fr.396.100.jpg"
                            }
                        },
                        "nutrition": {
                            "display": {
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/nutrition_fr.406.400.jpg"
                            },
                            "small": {
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/nutrition_fr.406.200.jpg"
                            },
                            "thumb": {
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/nutrition_fr.406.100.jpg"
                            }
                        },
                        "packaging": {
                            "display": {
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/packaging_fr.430.400.jpg"
                            },
                            "small": {
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/packaging_fr.430.200.jpg"
                            },
                            "thumb": {
                                "fr": "https://static.openfoodfacts.org/images/products/762/221/044/9283/packaging_fr.430.100.jpg"
                            }
                        }
                    },
                    "serving_quantity": 20,
                    "serving_size": "20g",
                    "sortkey": 1610831524,
                    "states": "en:to-be-completed, en:nutrition-facts-completed, en:ingredients-completed, en:expiration-date-completed, en:packaging-code-to-be-completed, en:characteristics-to-be-completed, en:origins-to-be-completed, en:categories-completed, en:brands-completed, en:packaging-completed, en:quantity-completed, en:product-name-completed, en:photos-validated, en:packaging-photo-selected, en:nutrition-photo-selected, en:ingredients-photo-selected, en:front-photo-selected, en:photos-uploaded",
                    "states_hierarchy": [
                        "en:to-be-completed",
                        "en:nutrition-facts-completed",
                        "en:ingredients-completed",
                        "en:expiration-date-completed",
                        "en:packaging-code-to-be-completed",
                        "en:characteristics-to-be-completed",
                        "en:origins-to-be-completed",
                        "en:categories-completed",
                        "en:brands-completed",
                        "en:packaging-completed",
                        "en:quantity-completed",
                        "en:product-name-completed",
                        "en:photos-validated",
                        "en:packaging-photo-selected",
                        "en:nutrition-photo-selected",
                        "en:ingredients-photo-selected",
                        "en:front-photo-selected",
                        "en:photos-uploaded"
                    ],
                    "states_tags": [
                        "en:to-be-completed",
                        "en:photos-uploaded"
                    ],
                    "stores": "Carrefour Market,Magasins U,Auchan,Intermarché,Carrefour,Casino,Leclerc,Cora,Bi1",
                    "stores_tags": [
                        "carrefour-market",
                        "cora",
                        "bi1"
                    ],
                    "teams": "pain-au-chocolat,shark-attack,chocolatine,la-robe-est-bleue,stakano,dietreflux",
                    "teams_tags": [
                        "pain-au-chocolat",
                        "shark-attack",
                        "chocolatine",
                        "la-robe-est-bleue",
                        "stakano",
                        "dietreflux"
                    ],
                    "traces": "en:eggs",
                    "traces_from_ingredients": "",
                    "traces_from_user": "(fr) Œufs",
                    "traces_hierarchy": [
                        "en:eggs"
                    ],
                    "traces_lc": "fr",
                    "traces_tags": [
                        "en:eggs"
                    ],
                    "unique_scans_n": 3075,
                    "unknown_ingredients_n": 1,
                    "unknown_nutrients_tags": [],
                    "update_key": "main-countries",
                    "url": "https://fr.openfoodfacts.org/produit/7622210449283/prince-chocolat-lu",
                    "vitamins_prev_tags": [],
                    "vitamins_tags": []
                }
            ],
            "skip": 0
        }