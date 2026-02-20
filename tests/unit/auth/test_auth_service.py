from app.settings import Settings
from app.users.auth.schema import UserLoginSchema
from app.users.auth.service import AuthService

import datetime as dt

from jose import jwt


async def test_redirect_google_url__success(auth_service: AuthService, settings: Settings):
    settings_google_redirect_url = settings.google_redirect_url
    auth_service_google_redirect_url = auth_service.get_google_redirect_url()
    assert isinstance(auth_service_google_redirect_url, str)
    assert auth_service_google_redirect_url == settings_google_redirect_url


async def test_redirect_yandex_url__success(auth_service: AuthService, settings: Settings):
    settings_yandex_redirect_url = settings.yandex_redirect_url
    auth_service_yandex_redirect_url = auth_service.get_yandex_redirect_url()
    assert isinstance(auth_service_yandex_redirect_url, str)
    assert auth_service_yandex_redirect_url == settings_yandex_redirect_url

async def test_generate_access_token__success(auth_service: AuthService, settings: Settings):
    user_id = 1
    access_token = auth_service.generate_access_token(user_id)
    decoded_access_token = jwt.decode(access_token, settings.JWT_SECRET_KEY, algorithms=settings.JWT_ENCODE_ALGORITHM)
    decoded_user_id = decoded_access_token.get('user_id')
    decoded_token_expire = dt.datetime.fromtimestamp(decoded_access_token.get('expire'), tz=dt.timezone.utc)

    assert decoded_token_expire - dt.datetime.now(tz=dt.UTC) > dt.timedelta(days=6)
    assert decoded_user_id == user_id

async def test_get_user_id_from_access_token__success(auth_service: AuthService):
    user_id = 1
    access_token = auth_service.generate_access_token(user_id)
    decoded_user_id = auth_service.get_user_id_from_access_token(access_token)

    assert decoded_user_id == user_id

async def test_google_auth__success(auth_service: AuthService):
    user = await auth_service.google_auth(code="fake_code")
    access_token = user.access_token
    decoded_user_id = auth_service.get_user_id_from_access_token(access_token)
    assert user.user_id == decoded_user_id
    assert isinstance(user, UserLoginSchema)

async def test_yandex_auth__success(auth_service: AuthService):
    user = await auth_service.yandex_auth(code="fake_code")
    access_token = user.access_token
    decoded_user_id = auth_service.get_user_id_from_access_token(access_token)
    assert user.user_id == decoded_user_id
    assert isinstance(user, UserLoginSchema)
