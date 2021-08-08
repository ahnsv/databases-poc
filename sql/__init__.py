from enum import Enum


class SqlFile(str, Enum):
    ALL_USERS_INNER_JOINED = "sql/fetch_all_users_inner_joined.sql"
