from common.oauth_user_auth_tokens_service import \
    OAuthUserAuthTokensService
from common.oauth2_storage import OAuth2SQLStorage
from resource_management.interactors.storages.user_interface import \
    UserInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class SignInInteractor:

    def __init__(self, user_storage: UserInterface,
                 oauth_storage: OAuth2SQLStorage,
                 presenter: PresenterInterface):
        self.user_storage = user_storage
        self.oauth_storage = oauth_storage
        self.presenter = presenter

    def login_with_credentials(self, username: int, password: str):
        user_id = self.user_storage.validate_username_and_password_get_user_id(
            username=username, password=password
        )

        if not user_id:
            self.presenter.raise_exception_for_invalid_credentials()
        
        oauth_service = OAuthUserAuthTokensService(
            oauth2_storage=self.oauth_storage    
        )
        oauth_tokens_dto = oauth_service.create_user_auth_tokens(
            user_id=user_id
        )
        return self.presenter.get_response_for_user_signin(
            oauth_tokens_dto=oauth_tokens_dto
        )   
