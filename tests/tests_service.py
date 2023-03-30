import pytest

from service.director import DirectorService
from service.genre import GenreService
from service.movie import MovieService


# Класс с тестами для DirectorService
class TestsDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert directors is not None
        assert len(directors) > 0

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None
        assert director.name == "Дэмьен Шазелл"

    def test_create(self):
        director_d = {
            "name": "Квентин Тарантино"
        }

        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "Новое имя - Джеки Чан"
        }
        assert self.director_service.update(director_d)

    def test_delete(self):
        assert self.director_service.delete(1) is None


# Класс с тестами для GenreService
class TestsGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao)

    def test_get_all(self):
        all_genres = self.genre_service.get_all()
        assert all_genres is not None
        assert len(all_genres) > 0

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None
        assert genre.name == "Мюзикл"

    def test_create(self):
        genre_d = {
            "name": "Детектив"
        }

        genre = self.genre_service.create(genre_d)
        assert genre.id is not None

    def test_update(self):
        genre_d = {
            "id": 1,
            "name": "Новый жанр - Фэнтези"
        }
        assert self.genre_service.update(genre_d)

    def test_delete(self):
        assert self.genre_service.delete(3) is None


# Класс с тестами для MovieService
class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao)

    def test_get_all(self):
        all_movies = self.movie_service.get_all()
        assert all_movies is not None
        assert len(all_movies) > 0

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None
        assert movie.title == "Дюна"

    def test_create(self):
        movie_d = {
            "title": "Дюна",
            "description": "Наследник знаменитого дома Атрейдесов Пол отправляется вместе с семьей на одну из самых опасных планет во Вселенной — Арракис. Здесь нет ничего, кроме песка, палящего солнца, гигантских чудовищ и основной причины межгалактических конфликтов — невероятно ценного ресурса, который называется меланж. В результате захвата власти Пол вынужден бежать и скрываться, и это становится началом его эпического путешествия. Враждебный мир Арракиса приготовил для него множество тяжелых испытаний, но только тот, кто готов взглянуть в глаза своему страху, достоин стать избранным.",
            "trailer": "https://www.youtube.com/watch?v=DOlTmIhEsg0",
            "year": 2021,
            "rating": 8.4,
            "genre_id": 2,
            "director_id": 2,
        }

        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_update(self):
        movie_d = {
            "id": 1,
            "title": "Название фильма 1 изменено на 'Веном'",
            "description": "Новое описание: Что если в один прекрасный день в тебя вселяется существо-симбиот, которое наделяет тебя сверхчеловеческими способностями? Вот только Веном – симбиот совсем недобрый, и договориться с ним невозможно. Хотя нужно ли договариваться?.. Ведь в какой-то момент ты понимаешь, что быть плохим вовсе не так уж и плохо. Так даже веселее. В мире и так слишком много супергероев! Мы – Веном!",
            "trailer": "https://www.youtube.com/watch?v=n7GlLxV_Igk",
            "year": 2018,
            "rating": 6.7,
            "genre_id": 2,
            "director_id": 2
        }

        assert self.movie_service.update(movie_d) is not None

    def test_delete(self):
        assert self.movie_service.delete(1) is None

