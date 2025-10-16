from models import MathUtils
import pytest

# from unittest import TestCase

# def sample_user():
#     return User()

# def test_change_pass(sample_user):
#     sample_user.change_pass()


# def test_forget_pass(sample_user):
#     sample_user.forgot_pass()

# # ------------------------------------------------------------------------
# class TestUser(TestCase):
#     def setup(self):
#         self.sample_user = User
#     def test_change_pass(self):
#         pass


#     def test_forget_pass(self):
#         pass

#     def teardown(self):
#         pass


# # ------------------------------------------------------------------------
@pytest.fixture
def sample_mathutils():
    return MathUtils()


def test_add(sample_mathutils):
    assert sample_mathutils.add(2, 3) == 5
    assert sample_mathutils.add(10, 20) == 30
    assert sample_mathutils.add(-1, -1) == -2
    assert sample_mathutils.add(-1, 1) == 0
    assert sample_mathutils.add(1.5, 1.5) == 3
    assert sample_mathutils.add(-1.5, 1.5) == 0


def test_devide(sample_mathutils):
    assert sample_mathutils.divide(1, 1) == 1
    assert sample_mathutils.divide(4, 2) == 2
    assert sample_mathutils.divide(3, 2) == 1.5
    assert sample_mathutils.divide(2.5, 5) == 0.5
    assert sample_mathutils.divide(5.5, 2.5) == 2.2
    with pytest.raises(ZeroDivisionError):
        sample_mathutils.divide(10, 0)


def test_is_even(sample_mathutils):
    assert sample_mathutils.is_even(3) == False
    assert sample_mathutils.is_even(10) == True
    assert sample_mathutils.is_even(1.2) == False
    assert sample_mathutils.is_even(1.3) == False
    assert sample_mathutils.is_even(-1.3) == False
    assert sample_mathutils.is_even(-1.2) == False
    assert sample_mathutils.is_even(0) == True
    assert sample_mathutils.is_even(-2) == True
