# RD11 Development of Optuna

## Coding Task
Please proceed to the following URL to access the coding task: (URL omitted)

The exam consists of three problems.
- Problem 1: (Undisclosed problem)
- Problem 2: Block Floating Point Numbers
- Problem 3: Noise Removal of Rectangle Images

Please provide the solutions using Python3.

## Thematic Task
### Your Tasks

Please answer each question about the `GPSampler` in Optuna.
Note that you may use the following notations in each question if necessary.

- $x \in \mathbb{R}^D$: A parameter. The $D$-dimensional variables that we would like to optimize. In Optuna, it is called params conventionally.
- $y \in \mathbb{R}$: The objective function value. In Optuna, it is called value.
- $\{(x_n, y_n)\}_{n=1}^N$: Observations. A set of observed parameters and the corresponding values during an optimization. In the Optuna convention, it is represented as `[(t.params, t.value) for t in study.trials]`.
- $k(x, x^\prime; \theta)$: A kernel function with hyperparameters  $\theta$.

#### Q1

Please create a code shorter than 10 lines that optimizes a function by [`GPSampler`](https://optuna.readthedocs.io/en/stable/reference/samplers/generated/optuna.samplers.GPSampler.html) and submit it along with the log file. Note that an arbitrary objective function can be used in this task.

#### Q2

GP in `GPSampler` stands for Gaussian process and `GPSampler` trains Gaussian process for each trial suggestion. What is the training procedure of Gaussian process? More specifically, please fill out A to C in the following sentence. “Using A as a dataset, train a model that takes B as an input and returns C.”

#### Q3

Gaussian process outputs C in Q2 using a kernel function at a new input $x^\star$. Write down the formulation of the output at a new input $x^\star$ given the training dataset, i.e., A in Q2.

#### Q4

`GPSampler` utilizes the Gaussian process trained on the training dataset, i.e., A in Q2, to calculate an acquisition function, and suggests the parameter that achieves the optimality given the acquisition function. Provide an example of an acquisition function (its name and its formulation) for the single-objective optimization problem and explain how the behavior may differ between parameter selection by the maximization of the acquisition function and by that of the posterior mean of the Gaussian process.

#### Q5

If the search space contains only continuous parameters, what method does `GPSampler` use to optimize the acquisition function? Please specify the corresponding function name from [Optuna v4.2.1](https://github.com/optuna/optuna/tree/v4.2.1) and write it down along with the optimization method.

#### Q6

Gaussian process adjusts the hyperparameters of the kernel function $\theta$ so that the likelihood of the observations achieves the maxima. During this adjustment, we do not perform a dataset split such as cross-validation that prevents machine learning models from overfitting. Please specify what Optuna’s `GPSampler` does to avoid overfitting instead of simply maximizing the likelihood, and summarize how it works in 200 words. Note that we count any URL length as one word.

### Submission

Submit your answers as a PDF file named `survey.pdf` shorter than 2 Pages (inclusive). Please notice that the submission for Q1 must be created separately.
