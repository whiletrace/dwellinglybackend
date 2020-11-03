import pytest
from tests.unit.base_interface_test import BaseInterfaceTest
from models.tickets import TicketModel
from schemas.tickets import TicketSchema

lass TestBaseTicketModel(BaseInterfaceTest):
    def setup(self):
        self.object = TicketModel()
        self.custom_404_msg = 'Ticket not found'

        # TODO: Looks like we also don't have a schema - we need to add one
        self.schema = TicketSchema

@pytest.mark.usefixtures('empty_test_db')
class TestTicketModel():
    def test_json(self, create_ticket):
        ticket = create_ticket()
        
        # TODO: Set up necessary relationships - look at tickets.py
        # Set up the tenant,assignedUser, and sender fields which map to the tenant and users models
        # Also look at the notes relationship

        # assert ticket.json() == {
        #         'id': ticket.id,
        #         'issue': ticket.issue,
        #         'sender': ticket.sender,
        #         'tenant': ticket.tenant,
        #         'status': ticket.status,
        #         'urgency': ticket.urgency,
        #         'assignedUser': ticket.assignedUser,
        #     }
