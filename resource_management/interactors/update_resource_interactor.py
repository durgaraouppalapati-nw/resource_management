from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class UpdateResourceInteractor:

    def __init__(self, resource_storage: ResourceInterface,
                 presenter: PresenterInterface):
        self.resource_storage = resource_storage
        self.presenter = presenter

    def update_resource(self, user_id: int, resource_id: int,
            name: str, resource_pic: str, link: str,
            description: str):
        is_user_not_admin = \
            not self.resource_storage.check_is_user_admin(user_id=user_id)
        if is_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        is_resource_not_exists = \
            not self.resource_storage.check_is_resource_exists(resource_id)
        if is_resource_not_exists:
            self.presenter.raise_exception_for_resource_not_found()
            return

        resource_dto = self.resource_storage.update_resource_and_get_dto(
            resource_id=resource_id, name=name, resource_pic=resource_pic,
            link=link, description=description  
        )
        return self.presenter.get_response_for_update_resource(
            resource_dto=resource_dto
        )
