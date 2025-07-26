from enum import Enum


class RestaurantApprovalStatus(Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"

    def __str__(self):
        return self.value
