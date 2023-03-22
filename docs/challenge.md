# Challenge

## Introduction

This is an example task to give a brief impression of when a trusted research environment may be used and the flow of working with Data Safe Haven.

There is a dummy data set containing personal information.
This data is synthetic, it does not represent, nor was it built based upon real people.

Your challenge is to calculate the **mean height** of the sample and prepare that result to be extracted from the environment.

Along the way you might notice some of the restrictions of working in a trusted research environment.
You may also need to solve some common problems data scientists frequently encounter.

## Guide

Here are some instructions to point you in the right direction and prompts for things to consider as you work.

### Find the data

- In a Data Safe Haven environment the input data is located at `/data`.
- Can you modify the input data in-place?
- Can you remove the data from the environment?

### Inspect the data

- What tools do you want to use?
- Can you install any packages you want to use?
- What units do you think the height values are in?
- Is there anything usual about the heights?

### Determine the mean height

- What tools do you want to use?
- Can you install any packages you want to use?
- Can you make a modifiable, working copy of the data?
- Will you write your analysis as a script or work interactively?
- Can you make your analysis reproducible?

### Prepare your result for extraction

- In a Data Safe Haven environment data in `/output` can be considered for removing from the environment.
- How will store your result so it can be removed?
- What if you wanted to also remove your analysis?
- Does your analysis reveal any sensitive information about the input data?
