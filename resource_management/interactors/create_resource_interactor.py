from resource_management.interactors.storages.resource_interface import \
    ResourceInterface
from resource_management.interactors.presenters.presenter_interface import \
    PresenterInterface


class CreateResourceInteractor:

    def __init__(self, resource_storage: ResourceInterface,
                 presenter: PresenterInterface):
        self.resource_storage = resource_storage
        self.presenter = presenter

    def create_resource(self, user_id: int,
            name: str, resource_pic: str, link: str,
            description: str):
        is_user_not_admin = \
            not self.resource_storage.check_is_user_admin(user_id=user_id)
        if is_user_not_admin:
            self.presenter.raise_exception_for_unauthorized_user()
            return

        is_resource_name_already_exists = \
            self.resource_storage.check_is_resource_name_already_exists(
                resource_name=name    
            )
        if is_resource_name_already_exists:
            self.presenter.raise_exception_for_resource_name_already_exists()

        self.resource_storage.create_resource(
            name=name, resource_pic=resource_pic,
            link=link, description=description  
        )
        return
