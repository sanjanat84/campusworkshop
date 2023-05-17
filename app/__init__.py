"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="https://github.com/sanjanat84/campusworkshop.git",
        database="todo_056n",
        user="todo_056n_user",
        password="szxvX8ZpQfdUNqqghzmEuUN8yTLYVmYU")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
