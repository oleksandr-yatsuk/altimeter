from os import environ
from unittest import TestCase


class BaseTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()

        boto3_profile()
        boto3_credentials()


def boto3_credentials() -> None:
    environ["AWS_ACCESS_KEY_ID"] = "testing"
    environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    environ["AWS_SECURITY_TOKEN"] = "testing"
    environ["AWS_SESSION_TOKEN"] = "testing"


def boto3_profile() -> None:
    profile_vars = ["AWS_DEFAULT_PROFILE", "AWS_PROFILE"]

    for profile_var in profile_vars:
        if profile_var in environ:
            environ.pop(profile_var)
