import sys
sys.path.append(".")

from bin.perceptron import Perceptron

def test_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,1]) ==  1, "([1,1]) ==  1"
    assert the_perceptron.predict([1,0]) ==  1, "assert comment"
    assert the_perceptron.predict([0,1]) ==  1, "assert comment"
    assert the_perceptron.predict([0,0]) ==  0, "assert comment"

import pytest

@pytest.mark.xfail
def test_negative_perceptron():
    the_perceptron = Perceptron()
    the_perceptron.train([
        [1,1],
        [1,0],
        [0,1],
        [0,0],
    ], [1,1,1,0])

    assert the_perceptron.predict([1,1]) ==  1, "([1,1]) ==  1"
    assert the_perceptron.predict([1,0]) ==  1, "assert comment"
    assert the_perceptron.predict([0,1]) ==  1, "assert comment"
    assert the_perceptron.predict([0,0]) ==  1, "Intentionally failing assertion"


import os

@pytest.mark.skipif(not sys.platform.startswith('linux'), reason="Test runs only on Linux")
def test_memory_check():
    # Getting all memory using os.popen()
    total_memory, used_memory, free_memory = map(
        int, os.popen('free -t -m').readlines()[-1].split()[1:])
    
    # Add assertions for minimum free memory
    min_free_memory = 100  # Define the minimum free memory threshold
    
    assert free_memory > min_free_memory, f"Free memory below minimum threshold: {free_memory} MB"


@pytest.mark.skip(reason="This test is not yet ready for prime time")
def test_always_skipped():
    # Placeholder content (silly Python content)
    assert 1 == 1
    print("This test is always skipped due to the decorator.")


datasets = [
    ([[1, 1], [1, 0], [0, 1], [0, 0]], [1, 1, 1, 0], [1, 1, 1, 0]),
    # Define more datasets as needed
    # Example: (training_set, labels, expected_predictions)
    # Add more datasets here
]

@pytest.mark.parametrize("training_set, labels, expected", datasets)
def test_perceptron(training_set, labels, expected):
    the_perceptron = Perceptron()
    the_perceptron.train(training_set, labels)

    for data, predict in zip(training_set, expected):
        assert the_perceptron.predict(data) == predict, f"Prediction mismatch for {data}. Expected: {predict}"

@pytest.fixture(scope="module")
def trained_perceptron():
    the_perceptron = Perceptron()
    training_set = [
        [1, 1],
        [1, 0],
        [0, 1],
        [0, 0],
    ]
    labels = [1, 1, 1, 0]
    
    the_perceptron.train(training_set, labels)
    return the_perceptron

def test_predict_1(trained_perceptron):
    assert trained_perceptron.predict([1, 1]) == 1, "([1,1]) == 1"

def test_predict_2(trained_perceptron):
    assert trained_perceptron.predict([1, 0]) == 1, "([1,0]) == 1"

def test_predict_3(trained_perceptron):
    assert trained_perceptron.predict([0, 1]) == 1, "([0,1]) == 1"

def test_predict_4(trained_perceptron):
    assert trained_perceptron.predict([0, 0]) == 0, "([0,0]) == 0"