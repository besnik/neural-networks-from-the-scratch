# Should I marry her?

This is example we will build simple percepton (aka linear binary classifier) that answers a question: Is it [THIS] or [THAT]? For example, is number higher than 10? Are pixels light or dark? Should I marry her? Sounds fun? :-)

Neural networks try in a way to simulate how human brain works and learns. Instead of solving a problem with bunch of IF-ELSE statements we create neurons that will learn to detect a property of given input. Is it ear or not? Is it nose or not? Is it eye or not? Is eye close enough to nose? By combining neurons that are sensitive to various properties we can answer more complex and interesting questions.

# How to run the program?

```
python should-i-marry-her.py
```

# Our first neuron

Let's build our first neuron. It consists of four parts:

1. Input values (the question)
2. Weights and bias (the knowledge or quality of the neuron)
3. Sum (transforms knowledge into single value)
4. Activation function (transforms value into probability or decision 0/1)

![Image by https://www.hackevolve.com/perceptron/](https://i1.wp.com/www.hackevolve.com/wp-content/uploads/2016/12/perceptron2.png?w=529&ssl=1)


Actually this architecture is called `Perceptron` in machine learning world.

What the neuron will try to do once it learns the knowledge is to lineary separate input (problem) space into two (binary) categories:

![Image by https://stanford.edu/~shervine/teaching/cs-221/cheatsheet-reflex-models](https://stanford.edu/~shervine/teaching/cs-221/illustrations/linear-classifier.png)

