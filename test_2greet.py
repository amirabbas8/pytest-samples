def greet(person):
    return 'Hi {name}'.format(**person)

def test_greet():
    alice = {'name': 'Alice'} # Arrange
    greeting = greet(alice) # Act
    assert greeting == "Hi Alice" # Assert

"""
Arrange: Setup any variables or conditions your test needs.
Act: Execute the code you want to test.
Assert: Check that the code behaviours in a way that you would expect
"""