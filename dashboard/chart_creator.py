import matplotlib.pyplot as plt
from PIL import Image
import numpy
import random

from django.db import connection
from client.models import *


def top_10_liked_mov():
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, (title + ' (' + CAST(release_date as NVARCHAR) + ')') FROM _Movie ORDER BY id")
    movies = cursor.fetchall()
    chart_data = []
    for i in movies:
        cursor.execute(f"SELECT COUNT(liked) FROM _MovieCard WHERE movie_id = {i[0]} AND liked = 1")
        likes = cursor.fetchall()[0][0]
        if likes > 0:
            chart_data.append((i[1], likes))
    chart_data = sorted(chart_data, key=lambda x: x[1])
    chart_data.reverse()
    if len(chart_data) > 10:
        chart_data = chart_data[:10]
    random.shuffle(chart_data)
    # Create chart
    i = 1
    fig, ax = plt.subplots()
    ax.set_title('Топ 10 фильмов по количеству одобрений')
    plt.xlabel('Фильмы', fontsize=16)
    plt.ylabel('Одобрения', fontsize=16)
    for item in chart_data:
        ax.bar(i,
               item[1],
               width=0.75,
               label=item[0],
               color=generate_color())
        i += 1

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=7,
               ncol=3, mode="expand", borderaxespad=0., fontsize=14)
    fig.set_size_inches(19.2, 10.8)

    plt.savefig('media/charts/top_10_liked_mov.png')
    return None


def top_10_wanted_mov():
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, (title + ' (' + CAST(release_date as NVARCHAR) + ')') FROM _Movie ORDER BY id")
    movies = cursor.fetchall()
    chart_data = []
    for i in movies:
        cursor.execute(f"SELECT COUNT(liked) FROM _MovieCard WHERE movie_id = {i[0]} AND want_to_watch = 1")
        wanted_num = cursor.fetchall()[0][0]
        if wanted_num > 0:
            chart_data.append((i[1], wanted_num))
    chart_data = sorted(chart_data, key=lambda x: x[1])
    chart_data.reverse()
    if len(chart_data) > 10:
        chart_data = chart_data[:10]
    random.shuffle(chart_data)
    # Create chart
    i = 1
    fig, ax = plt.subplots()
    ax.set_title('Топ 10 желаемых фильмов')
    plt.xlabel('Фильмы', fontsize=16)
    plt.ylabel('Отметки "хочу посмотреть"', fontsize=16)
    for item in chart_data:
        ax.bar(i,
               item[1],
               width=0.75,
               label=item[0],
               color=generate_color())
        i += 1

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=7,
               ncol=3, mode="expand", borderaxespad=0., fontsize=14)
    fig.set_size_inches(19.2, 10.8)

    plt.savefig('media/charts/top_10_wanted_mov.png')
    return None


def top_10_watched_mov():
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, (title + ' (' + CAST(release_date as NVARCHAR) + ')') FROM _Movie ORDER BY id")
    movies = cursor.fetchall()
    chart_data = []
    for i in movies:
        cursor.execute(f"SELECT COUNT(liked) FROM _MovieCard WHERE movie_id = {i[0]} AND watched = 1")
        watched_num = cursor.fetchall()[0][0]
        if watched_num > 0:
            chart_data.append((i[1], watched_num))
    chart_data = sorted(chart_data, key=lambda x: x[1])
    chart_data.reverse()
    if len(chart_data) > 10:
        chart_data = chart_data[:10]
    random.shuffle(chart_data)
    # Create chart
    i = 1
    fig, ax = plt.subplots()
    ax.set_title('Топ 10 фильмов по количеству просмотров')
    plt.xlabel('Фильмы', fontsize=16)
    plt.ylabel('Просмотры', fontsize=16)
    for item in chart_data:
        ax.bar(i,
               item[1],
               width=0.75,
               label=item[0],
               color=generate_color())
        i += 1

    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=7,
               ncol=3, mode="expand", borderaxespad=0., fontsize=14)
    fig.set_size_inches(19.2, 10.8)

    plt.savefig('media/charts/top_10_watched_mov.png')
    return None


def generate_color():
    """Вернуть 16-ти битное представление случайного цвета"""
    symbols = '1234567890ABCDEF'
    color = '#' + ''.join([symbols[random.randint(0, len(symbols) - 1)] for i in range(6)])
    return color


chart_list = {
    'top_10_liked_mov': {
        'method': top_10_liked_mov,
        'title': 'Топ 10 фильмов по количеству одобрений',
        'link': '/media/charts/top_10_liked_mov.png'
    },
    'top_10_wanted_mov': {
        'method': top_10_wanted_mov,
        'title': 'Топ 10 желаемых фильмов',
        'link': '/media/charts/top_10_wanted_mov.png'
    },
    'top_10_watched_mov': {
        'method': top_10_watched_mov,
        'title': 'Топ 10 фильмов по количеству просмотров',
        'link': '/media/charts/top_10_watched_mov.png'
    },
}