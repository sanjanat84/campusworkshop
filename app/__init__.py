"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="@dpg-chi7u75269vf5qbbngag-a.oregon-postgres.render.com",
        database="todo_056n",
        user="todo_056n_user",
        password="szxvX8ZpQfdUNqqghzmEuUN8yTLYVmYU")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
