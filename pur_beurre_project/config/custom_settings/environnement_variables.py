"""Environnment variable module
"""
import os


class EnvironnementVariables:
    """Environnement variable class
    """

    # DESCRIPTION: Variable defining if environnement is prod or dev.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: os.environ.get("APP_ENV")
    # CUSTOM SETTINGS: You need to create environnment variable of that name,
    # i.e.APP_ENV, with your values (prod or dev).
    APP_ENV = os.environ.get("APP_ENV")

    # DESCRIPTION: Secret key required for proper Django usage.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: os.environ.get("DJANGO_PURBEURRE_SECRET_KEY")
    # CUSTOM SETTINGS: You need to create environnment variable of that name,
    # i.e.SECRET_KEY, with your a secret value(only known to you).
    APP_SECRET_KEY = os.environ.get("APP_SECRET_KEY")

    # DESCRIPTION: USernzame for Postgres DB access.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: os.environ.get("POSTGRES_USER")
    # CUSTOM SETTINGS: You need to create environnment variable of that name,
    # i.e.POSTGRES_USER, with your username.
    POSTGRES_USER = os.environ.get("POSTGRES_USER")

    # DESCRIPTION: Password for  Postgres DB access.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: os.environ.get("POSTGRES_PWD")
    # CUSTOM SETTINGS: You need to create environnment variable of that name,
    # i.e.POSTGRES_PWD, with your a secret pwd(only known to you).
    POSTGRES_PWD = os.environ.get("POSTGRES_PWD")