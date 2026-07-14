# Assignment 1: Regression

**Deadline:** Aug 16, 2026 23:59 CEST

In this assignment, 
we are interested in predicting ages of children from the poems they wrote.
This is an example of a regression task,
where the outcome variable is a continuous variable.
The data comes from a corpus of poems by children 
[(Hipson and Mohammad, 2020)](https://arxiv.org/abs/2004.06188v3).
However, the version we will work on has been sub-sampled
and includes some numeric features to allow a quick start.
For this exercise,
**you are not allowed to use the original data**.

You can find the data in your repository as two separate files.
The file [nlp2-a1.train](nlp2-a1.train) contains the training instances,
and the file [nlp2-a1.test](nlp2-a1.test) contains the test instances.
Data is formatted as tab-separated files in both cases.
The columns include:

- column **1** the `id` of the instance (unique across train/test data)
- column **2** the outcome variable, `age` of the child.
    The age column in the test file is arbitrarily set to 0
- columns **3-52** numeric features extracted from each poem
- column **53** the title of the poem
- column **54** the poem text with some preprocessing

Your task is to predict ages of the children
who wrote the poems in the test file,
and write your predictions to a file formatted as a tab-separated file
with two columns. The first column should be the id of the test instance
and the second should be the prediction. The following is an example
of the expected format.

```
id      age
36955	10.120152980997084
24192	11.658632919846077
17322	9.620842721977718
49182	10.388876890831183
59294	10.365936803375702
29233	10.303503920638938
31817	11.349653647283414
10817	10.654137200311414
...
```
The filename for the predictions file should be formatted like
`a1-<method>.predictions`.
Here, `<method>` is a (short) string that identifies your approach.
The method name you use for the file will be visible on the scoreboard
(see below).
You are recommended to use understandable method names.
For example, if your method is based on a recurrent network,
`rnn`  may be a good choice.
You are encouraged to submit multiple sets of predictions
(e.g., one with a traditional method, one with a neural method).

For each approach, the main Python script should be named `a1-<method>.py`.
You are free to structure your code as multiple files
(and share code across different approaches).
However, the main file for each approach should be named as instructed above.

You are also provided with [a baseline](baseline.py) that predicts
a random number within the age range in the training set.
The example mainly demonstrates the correct output format.
**Do not** modify the baseline,
even if you decide to improve on it, copy it to `a1-<method>.py`,
and modify the new file.

You are welcome to use any method, tool or library of your choice.
You can make use of additional resources, except the PoKi data set cited above.

## Submissions and scoreboard

All assignments will be released through GitHub (using Clasroom50).
The assignment link will be provided on [the private course
repository](https://github.com/snlp2-2026/snlp2).

For each assignment we will keep a scoreboard
at [the private course repository](https://github.com/snlp2-2025/snlp2).
Each team is required to submit at least one prediction before the deadline.
You are welcome to submit new predictions as you improve your system
(the scoreboard will be updated once a day).
The scoreboard will show at most three (best) approaches from each team.

All code you use for the assignments should be pushed to your 
assignment repository.
