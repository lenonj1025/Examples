from app import a
from app import c

# A unit test case will fail if any exception occurs that is not handled
# Otherwise, it will pasee
def test_a(mocker):
    # What is the SUT (System under test)?
    # Answer: function a()

    # AAA
    # Arrange: Set up whatever is necessary for the system under test
    # arrange is not necessary in this case
    mocker.patch('app.b', return_values=10000)

    # Act: invoke the SUT
    actual = a()    # Here we invoke a(), which is what we are testing, which will then invoke b()
    # (which is the dependency that we mock)

    # Assert: failing the test if the assertion is not True
    # An assent, if False, produces an exception that will fail the test
    assert (actual == 99)

def test_c(mocker):
    # Arrange
    def mock_get_all_users(self):
        return [{"username": "bachy21", "age": 24},{"username": "jane_doe", "age": 30}]

    mocker.patch('app.UserDao.get_all_users', mock_get_all_users)

    # Act
    actual = c()

    # Assert
    assert actual == [{"username": "bachy21", "age": 24},{"username": "jane_doe", "age": 30}]
