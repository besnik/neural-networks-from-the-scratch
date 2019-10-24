# USAGE: python should-i-marry-her.py
# In code look after main() function
import random


class Perceptron():
    """This is our basic neuron."""

    def __init__(self, input_size):
        # w0 is bias w1..wN are (initally random) weights
        self.weights = [random.randint(-100, +100) for _ in range(0, input_size + 1)]

    def __repr__(self):
        return f"Perceptron({len(self.weights) - 1})"

    def __call__(self, *args, **kwargs):
        # input & validation
        input = kwargs.get("input")
        if len(input) != len(self.weights) - 1:  # minus bias value w0
            raise ValueError(f"Invalid input. Expecting list of numbers with length {len(self.weights) - 1} (capacity of the neutron).")

        # insert constant 1 so the bias won't change later in sum function
        input.insert(0, 1)

        # weighted sum (w0 is bias, w1..wN is knowledge)
        sum = 0.0
        for i in range(0, len(input)):
            sum += input[i] * self.weights[i]

        # activation function. For now just return binary choice.
        # later we will return probability of correct answer.
        return 0 if sum < 0 else 1


def main():
    # 1. Init neuron
    p = Perceptron(4)
    # 2. Train it
    # TBD
    # 3. Test it
    result = p(input=[1, 2, 3, 4])
    print(f"Should I marry her? The answer is {'yes' if result == 1 else 'no'}.")


if __name__ == "__main__":
    main()
    print("Done")
