import pytest
from models.user import UserModel, RoleEnum

@pytest.fixture
def create_property_manager():
    def _create_property_manager():
        pm = UserModel(
                email="manager@domain.com",
                password=b'asdf',
                firstName="Leslie",
                lastName="Knope",
                phone="505-503-4455",
                role=RoleEnum.PROPERTY_MANAGER,
                archived=False
            )
        pm.save_to_db()
        return pm
    yield _create_property_manager

@pytest.fixture
def create_join_staff():
    def _create_join_staff():
        staff = UserModel(
                email="staffer@example.com",
                password=b'asdf',
                firstName="File",
                lastName="Last",
                phone="503-555-hello",
                role=RoleEnum.STAFF,
                archived=False
            )
        staff.save_to_db()
        return staff
    yield _create_join_staff
