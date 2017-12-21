from client.models import *

tables = {
    'access_level': {
        'model': AccessLevel,
        'select_from': '_AccessLevel',
        'title': 'Уровни доступа',
        'uid': ['Идентификатор уровня', 'Название', 'Уровень доступа']
    },
    'member': {
        'model': Member,
        'select_from': '_Member',
        'title': 'Участники фильмов',
        'uid': ['Идентификатор участника', 'Имя', 'Фамилия', 'Путь к файлу изображения', 'Роль в фильме']
    },
    'genre': {
        'model': Genre,
        'select_from': '_Genre',
        'title': 'Жанры',
        'uid': ['Идентификатор жанра', 'Название']
    },
    'movie': {
        'model': Movie,
        'select_from': '_MovieReport',
        'title': 'Фильмы',
        'uid': ['Идентификатор фильма', 'Название', 'Продолжительность', 'Описание', 'Дата выхода', 'Путь к файлу изображения', 'ID трейлера на YouTube', 'В предложенном', 'Уровень доступа (тег)']
    },
    'movie_member': {
        'model': MovieMember,
        'select_from': '_MovieMemberReport',
        'title': 'Участник/Фильм',
        'uid': ['Идентификатор записи', 'Фильм', 'Участник']
    },
    'movie_genre': {
        'model': MovieGenre,
        'select_from': '_MovieGenreReport',
        'title': 'Жанр/Фильм',
        'uid': ['Идентификтаор записи', 'Фильм', 'Жанр']
    },
    'image': {
        'model': Image,
        'select_from': '_ImageReport',
        'title': 'Изображение',
        'uid': ['Идентификатор изображения', 'Название фильма', 'Путь к файлу изображения']
    },
    'subscription': {
        'model': Subscription,
        'select_from': '_SubscriptionReport',
        'title': 'Подписка',
        'uid': ['Идентификатор подписки', 'Уровень доступа', 'Длительность', 'Цена', 'Видна всем']
    },
    'user': {
        'model': User,
        'select_from': '_UserReport',
        'title': 'Пользователь',
        'uid': ['Идентификатор пользователя', 'Email', 'Имя', 'Фамилия', 'Почта подтверждена', 'Админимстратор', 'Дата подписки', 'Подписка', 'Длительность подписки']
    },
    'movie_card': {
        'model': MovieCard,
        'select_from': '_MovieCardReport',
        'title': 'Карточка фильма',
        'uid': ['Идентификатор карточки', 'Пользователь', 'Фильм', 'Просмотрен', 'Хочет посмотреть', 'Любимый', 'Понравился']
    },
    'promo_code': {
        'model': PromoCode,
        'select_from': '_PromoCodeReport',
        'title': 'Промо код',
        'uid': ['Идентификатор промо кода', 'Код', 'Количество', 'Подписка']
    },
    'user_promo_code': {
        'model': UserPromoCode,
        'select_from': '_UserPromoCodeReport',
        'title': 'Промо коды пользователей',
        'uid': ['Идентификатор записи', 'Пользователь', 'Промо код', 'Активный']
    },
}
