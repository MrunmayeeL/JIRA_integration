Monte Carlo Simulations for Probability Estimation

Overview

This repository contains Python programs that use Monte Carlo simulations to estimate probabilities and averages for various random events. The project was developed as part of Academic coursework Assignment.

The purpose of this assignment is to perform project management using 

Jira and implement the given Python programs, while also tracking issues and tasks within Jira. The project demonstrates the use of a Scrum framework, with tasks broken down into sub-tasks and managed in a backlog and sprints.

Project Tasks

The following problems were solved using Monte Carlo simulations:

1. Yahtzee Probability

    Problem: Estimate the probability of rolling a Yahtzee in a single roll of five dice.

    Solution: A Python script simulates 100,000 rolls of five dice, checking for a Yahtzee in each trial. The probability is calculated by dividing the number of successful outcomes by the total number of trials.

2. Large Straight Probability

    Problem: Estimate the probability of rolling a large straight (1-2-3-4-5 or 2-3-4-5-6) in a single roll of five dice.

    Solution: A Python script simulates 100,000 rolls, checking for either a 1-2-3-4-5 or 2-3-4-5-6 sequence in the sorted results of each trial.

3. Longest Run of Heads or Tails

    Problem: Estimate the average longest run of heads or tails when flipping a coin 200 times.

    Solution: The simulation runs 10,000 times. In each trial, it simulates 200 coin flips and identifies the longest streak of consecutive heads or tails. The average of these longest runs is then calculated.

4. Five Heads in a Row

    Problem: Estimate the average number of coin flips it takes before five heads in a row come up.

    Solution: The simulation tracks the number of flips needed to achieve five consecutive heads. This process is repeated 10,000 times, and the average number of flips is determined.

5. Specific String s Occurrence

    Problem: Estimate the average number of coin flips it takes before a specific string of heads and tails (e.g., "HHTTH") comes up.

    Solution: The simulation continuously flips a coin and appends the result to a string. It stops when the target string is found at the end of the sequence, and the total number of flips is recorded. The simulation is run 10,000 times to calculate the average.

Project Management

This project was managed using 

Jira.

    Jira Project: The project, named "Monte Carlo Simulations," was set up using a Scrum template.

    Issue Tracking: Each problem statement was created as a separate issue in the Jira backlog. Each issue was broken down into manageable sub-tasks for a clear workflow.

Workflow: Tasks were moved through the project board (e.g., from "To Do" to "In Progress" to "Done") to track progress.

Jira-GitHub Integration: The Jira project was connected to this GitHub repository. Commit messages containing the Jira issue key automatically linked code changes to the relevant tasks, providing a seamless audit trail of development.

How to Run the Codes

The Python programs require no external libraries beyond the standard library.

    Clone this repository:
    Bash

git clone https://github.com/your-username/Monte-Carlo-Simulations-Project.git

Navigate to the project directory:
Bash

cd Monte-Carlo-Simulations-Project

Run any of the Python scripts from your terminal. For example:
Bash

    python yahtzee_probability.py

Deliverables

This project fulfills the deliverables specified in the assignment, including a completely working demonstration of the problem statements, a project created in Jira, the use of various Jira features, a connection to GitHub, and a short summary of the workflow.
