from client.models import *

tables = {
    'access_level': {
        'model': AccessLevel,
        'admin_section': 'accesslevel',
        'view': '_AccessLevel',
        'table': '_AccessLevel',
        'title': 'Уровни доступа',
        'fields': ['id', 'tag', 'lvl'],
        'uid': ['Идентификатор уровня', 'Название', 'Уровень доступа']
    },
    'member': {
        'model': Member,
        'admin_section': 'member',
        'view': '_Member',
        'table': '_Member',
        'title': 'Участники фильмов',
        'fields': ['id', 'first_name', 'last_name', 'portrait', 'role_in_movie'],
        'uid': ['Идентификатор участника', 'Имя', 'Фамилия', 'Путь к файлу изображения', 'Роль в фильме']
    },
    'genre': {
        'model': Genre,
        'admin_section': 'genre',
        'view': '_Genre',
        'table': '_Genre',
        'title': 'Жанры',
        'fields': ['id', 'tag'],
        'uid': ['Идентификатор жанра', 'Название']
    },
    'movie': {
        'model': Movie,
        'admin_section': 'movie',
        'view': '_MovieReport',
        'table': '_Movie',
        'title': 'Фильмы',
        'fields': ['id', 'title', 'duration', 'movie_description', 'release_date',
                   'poster', 'trailer_url', 'suggested', 'access_lvl_id'],
        'uid': ['Идентификатор фильма', 'Название', 'Продолжительность', 'Описание', 'Дата выхода',
                'Путь к файлу изображения', 'ID трейлера на YouTube', 'В предложенном', 'Уровень доступа (тег)']
    },
    'movie_member': {
        'model': MovieMember,
        'admin_section': 'moviemember',
        'view': '_MovieMemberReport',
        'table': '_MovieMember',
        'title': 'Участник/Фильм',
        'fields': ['id', 'movie_id', 'member_id'],
        'uid': ['Идентификатор записи', 'Фильм', 'Участник']
    },
    'movie_genre': {
        'model': MovieGenre,
        'admin_section': 'moviegenre',
        'view': '_MovieGenreReport',
        'table': '_MovieGenre',
        'title': 'Жанр/Фильм',
        'fields': ['id', 'movie_id', 'genre_id'],
        'uid': ['Идентификтаор записи', 'Фильм', 'Жанр']
    },
    'image': {
        'model': Image,
        'admin_section': 'image',
        'view': '_ImageReport',
        'table': '_Image',
        'title': 'Изображение',
        'fields': ['id', 'movie_id', '[file]'],
        'uid': ['Идентификатор изображения', 'Фильм', 'Путь к файлу изображения']
    },
    'subscription': {
        'model': Subscription,
        'admin_section': 'subscription',
        'view': '_SubscriptionReport',
        'table': '_Subscription',
        'title': 'Подписка',
        'fields': ['id', 'access_level_id', 'duration', 'price', 'visible'],
        'uid': ['Идентификатор подписки', 'Уровень доступа', 'Длительность', 'Цена', 'Видна всем']
    },
    'user': {
        'model': User,
        'admin_section': 'user',
        'view': '_UserReport',
        'table': '_User',
        'title': 'Пользователь',
        'fields': ['id', 'email', 'first_name', 'last_name', 'activated',
                   'is_staff', 'subscribed_date', 'subscription_id'],
        'uid': ['Идентификатор пользователя', 'Email', 'Имя', 'Фамилия',
                'Почта подтверждена', 'Админимстратор', 'Дата подписки', 'Подписка']
    },
    'movie_card': {
        'model': MovieCard,
        'admin_section': 'moviecard',
        'view': '_MovieCardReport',
        'table': '_MovieCard',
        'title': 'Карточка фильма',
        'fields': ['id', 'user_id', 'movie_id', 'watched', 'want_to_watch', 'is_favorite', 'liked'],
        'uid': ['Идентификатор карточки', 'Пользователь', 'Фильм',
                'Просмотрен', 'Хочет посмотреть', 'Любимый', 'Понравился']
    },
    'promo_code': {
        'model': PromoCode,
        'admin_section': 'promocode',
        'view': '_PromoCodeReport',
        'table': '_PromoCode',
        'title': 'Промо код',
        'fields': ['id', 'code', 'quantity', 'subscription_id'],
        'uid': ['Идентификатор промо кода', 'Код', 'Количество', 'Подписка']
    },
    'user_promo_code': {
        'model': UserPromoCode,
        'admin_section': 'userpromocode',
        'view': '_UserPromoCodeReport',
        'table': '_UserPromoCode',
        'title': 'Промо коды пользователей',
        'fields': ['id', 'user_id', 'promo_code_id', 'is_active'],
        'uid': ['Идентификатор записи', 'Пользователь', 'Промо код', 'Активный']
    },
}
