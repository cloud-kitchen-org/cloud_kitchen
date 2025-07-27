from enum import Enum


class UserRole(Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"
    PARTNER = "partner"

    def __str__(self):
        return self.value
