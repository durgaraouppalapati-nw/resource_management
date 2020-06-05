import pytest

from unittest.mock import create_autospec
from django_swagger_utils.drf_server.exceptions import BadRequest

from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from resource_management.interactors.signin_interactor import \
    SignInInteractor
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


def test_signin_interactor_with_valid_details_return_access_token(
        oauth_tokens_dto, access_token_dto, refresh_token_dto,
        application_dto
    ):
    # Arrange
    username = "durgarao"
    password = "Durga@123"
    user_id = 1
    application_id = 1
    scopes = "write read"
    access_token_id = 1
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    interactor = SignInInteractor(
        user_storage=user_storage,
        oauth_storage=oauth_storage,
        presenter=presenter    
    )
    user_storage.validate_username_and_password_get_user_id.return_value = user_id
    oauth_storage.get_or_create_default_application.return_value = \
        application_dto, True
    oauth_storage.create_access_token.return_value = access_token_dto
    oauth_storage.create_refresh_token.return_value = refresh_token_dto
    
    # Act
    interactor.login_with_credentials(
        username=username,
        password=password
    )

    # Assert
    user_storage.validate_username_and_password_get_user_id.assert_called_once_with(
        username=username, password=password
    )
    oauth_storage.get_or_create_default_application.assert_called_once_with(
        user_id=user_id    
    )
    oauth_storage.create_access_token.assert_called_once_with(
        user_id=user_id,
        application_id=application_id,
        scopes=scopes,
        expiry_in_seconds=1000000000   
    )
    oauth_storage.create_refresh_token.assert_called_once_with(
        user_id=user_id,
        application_id=application_id,
        access_token_id=access_token_id    
    )
    presenter.get_response_for_user_signin.assert_called_once_with(
        oauth_tokens_dto=oauth_tokens_dto
    )


def test_signin_interactor_with_invalid_details_raises_exception():
    # Arrange
    username = "durgarao"
    password = "Durga@123"
    user_storage = create_autospec(UserInterface)
    presenter = create_autospec(PresenterInterface)
    oauth_storage = create_autospec(OAuth2SQLStorage)
    interactor = SignInInteractor(
        user_storage=user_storage,
        oauth_storage=oauth_storage,
        presenter=presenter    
    )
    user_storage.validate_username_and_password_get_user_id.return_value = None
    presenter.raise_exception_for_invalid_credentials.side_effect = BadRequest

    # Act
    with pytest.raises(BadRequest):
        interactor.login_with_credentials(
            username=username,
            password=password
        )
