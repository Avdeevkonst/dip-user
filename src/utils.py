from enum import Enum


class UserRole(Enum):
    STUDENT = "student"
    INSTRUCTOR = "instructor"
    ADMIN = "admin"
    SUPERADMIN = "superadmin"
