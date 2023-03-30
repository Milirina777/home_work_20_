import pytest
from setup_db import db
from unittest.mock import MagicMock
from dao.director import DirectorDAO
from dao.model.director import Director
from dao.genre import GenreDAO
from dao.model.genre import Genre
from dao.movie import MovieDAO
from dao.model.movie import Movie


@pytest.fixture()
def director_dao():
    """Создаем фикстуру с моком для DirectorDAO."""
    director_dao = DirectorDAO(db.session)

    director_1 = Director(id=1, name="Дэмьен Шазелл")
    director_2 = Director(id=2, name="Дени Вильнёв")
    director_3 = Director(id=3, name="Пит Доктер")

    directors = {1: director_1,
                 2: director_2,
                 3: director_3,
                 }

    director_dao.get_all = MagicMock(return_value=directors.values())
    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.create = MagicMock(return_value=director_1)
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    """Создаем фикстуру с моком для GenreDAO"""
    genre_dao = GenreDAO(db.session)

    genre_1 = Genre(id=1, name='Мюзикл')
    genre_2 = Genre(id=2, name='Фантастика')
    genre_3 = Genre(id=3, name='Мультфильм')

    genres = {
        1: genre_1,
        2: genre_2,
        3: genre_3,
    }

    genre_dao.get_all = MagicMock(return_value=genres.values())
    genre_dao.get_one = MagicMock(return_value=genre_2)
    genre_dao.create = MagicMock(return_value=genre_1)
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock()

    return genre_dao

@pytest.fixture()
def movie_dao():
    """Создаем фикстуру с моком для MovieDAO"""
    movie_dao = MovieDAO(db.session)

    movie_1 = Movie(
        id=1,
        title="Дюна",
        description="Наследник знаменитого дома Атрейдесов Пол отправляется вместе с семьей на одну из самых опасных планет во Вселенной — Арракис. Здесь нет ничего, кроме песка, палящего солнца, гигантских чудовищ и основной причины межгалактических конфликтов — невероятно ценного ресурса, который называется меланж. В результате захвата власти Пол вынужден бежать и скрываться, и это становится началом его эпического путешествия. Враждебный мир Арракиса приготовил для него множество тяжелых испытаний, но только тот, кто готов взглянуть в глаза своему страху, достоин стать избранным.",
        trailer="https://www.youtube.com/watch?v=DOlTmIhEsg0",
        year=2021,
        rating=8.4,
        genre_id=2,
        director_id=2
    )
    movie_2 = Movie(
        id=2,
        title="Ла-Ла Ленд",
        description="Это история любви старлетки, которая между прослушиваниями подает кофе состоявшимся кинозвездам, и фанатичного джазового музыканта, вынужденного подрабатывать в заштатных барах. Но пришедший к влюбленным успех начинает подтачивать их отношения.",
        trailer="https://www.youtube.com/watch?v=lneNCBIXD4I",
        year=2016,
        rating=8.0,
        genre_id=1,
        director_id=1
    )

    movie_3 = Movie(
        id=3,
        title="Душа",
        description="Уже немолодой школьный учитель музыки Джо Гарднер всю жизнь мечтал выступать на сцене в составе джазового ансамбля. Однажды он успешно проходит прослушивание у легендарной саксофонистки и, возвращаясь домой вне себя от счастья, падает в люк и умирает. Теперь у Джо одна дорога — в Великое После, но он сбегает с идущего в вечность эскалатора и случайно попадает в Великое До. Тут новенькие души обретают себя, и у будущих людей зарождаются увлечения, мечты и интересы. Джо становится наставником упрямой души 22, которая уже много веков не может найти свою искру и отправиться на Землю.",
        trailer="https://www.youtube.com/watch?v=vsb8762mE6Q",
        year=2020,
        rating=8.1,
        genre_id=3,
        director_id=3
    )

    movies = {
        1: movie_1,
        2: movie_2,
        3: movie_3,
    }

    movie_dao.get_all = MagicMock(return_value=movies.values())
    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.create = MagicMock(return_value=movie_1)
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
