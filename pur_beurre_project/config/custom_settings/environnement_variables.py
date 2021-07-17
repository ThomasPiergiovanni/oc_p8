"""Environnment variable module
"""
import os


class EnvironnementVariables:
    """Environnement variable class
    """
    # DESCRIPTION: Secret key required for proper Django usage.
    # MANDATORY: Yes.
    # DEFAULT SETTINGS: os.environ.get("DJANGO_PURBEURRE_SECRET_KEY")
    # CUSTOM SETTINGS: You need to create environnment variable of that name,
    # i.e.SECRET_KEY, with your a secret value(only known to you).
    SECRET_KEY = os.environ.get("DJANGO_PURBEURRE_SECRET_KEY")

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