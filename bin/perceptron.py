"""
Perceptron code here 

Aishwarya Pradhan xaz3kw

"""

class Perceptron:
    """ class docstring for perceptron """
    def __init__(self):
        self._weights = None
    def train(self, inputs, labels):
        """ train function """
        dummied_inputs = [x + [-1] for x in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])
        for _ in range(5000):
            for input_, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(input_)
                for index, x in enumerate(input_):
                    self._weights[index] += .1 * x * label_delta
    def predict(self, input_):
        """ predict function """
        if len(input_) == 0:
            return None
        input_ = input_ + [-1]
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights, input_)]))# pylint: disable=R1728
        