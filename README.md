Simulation 2024 Fall
Homework #1 due on September 25

1. Use the basic Monte Carlo technique from class to integrate = ∫(1,2) (1/√2𝜋)∙ℯ{−𝜒^2/2}. Use n =10 U(0, 1) random variates to produce your answer. Repeat this 5 times to get an idea of what the variance of 110 is. Can you think of any way to calculate an "exact" answer? If you need a uniform generator, refer to Appendix 7A, or any random number generator. If you do not want to do any programming, you can use Excel; or pick a whole bunch of uniforms by yourself.
   Extra Credit: prove that Î, is an unbiased estimator for I.

2. Repeat the example we did in class to estimate via Monte Carlo sampling. Plot your
   estimates for sample sizes of n = 2, 4, 8, ..., 2048. (Use a logarithmic scale for the x-axis.) Does your answer seem to be converging to 3.14159?

3. Simulate in your favorite computer language the single-server queueing system from
   class. That is, suppose that customers arrive at a single-server queue with customer interarrival times i.i.d. discrete uniform {1, 2, ..., 6} minutes. Suppose that customers are served first-in-first-out and that the service times are i.i.d. discrete uniform {1, 2, ..., 6} minutes. For convenience, suppose that the first customer arrives at time zero. Simulate this system for 100 customers. What is the average waiting time for the 100 customers? What is the average number of people waiting in line during the first 200 minutes? What is the average number of people in the system (in line or being served) during the first 200 minutes? If you need a uniform generate, refer to Appendix 7A, or you can use one that is probably supplied by the language that you are using.

4. Consider the same single-server queueing system as that is question 3. above, except that
   now suppose the queue only has room for three customers to wait (i.e., the buffer size is 3.) We want to know the expected time it takes until a customer is turned away. Obviously, you only need to simulate the system until the first turn away occurs. Does this a bunch of times and calculate the sample average

Homework #2

Modify the code for the single-server queue in Sec. 1.4.4 to compute and write in
addition the following measures of performance:
(a) The time-average number in the system (see Prob. 1.3)
(b) The average total time in the system (see Prob. 1.5)
(c) The maximum queue length (see Prob. 1.6)
(d) The maximum delay in queue
(e) The maximum time in the system
(f) The proportion of customers having a delay in queue in excess of 1 minute
