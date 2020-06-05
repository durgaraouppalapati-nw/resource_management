import pytest

from resource_management.presenters.presenter_implementation import \
    PresenterImplementation


def test_get_response_for_user_signin_return_access_token_dict(
        oauth_tokens_dto):
    # Arrange
    presenter = PresenterImplementation()
    expected_access_token_dict = \
        {'access_token': 'access_token'}

    # Act
    actual_access_token_dict = \
        presenter.get_response_for_user_signin(
            oauth_tokens_dto=oauth_tokens_dto
        )

    # Assert
    assert expected_access_token_dict == actual_access_token_dict
