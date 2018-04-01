Crypto Trader Bot project
=========================

This project is a simple crypto currency trader bot to learn and experiment
with different strategies.

This projects does not aim to generate profits but mostly for recreational and
learning purposes. Could be a great platform to test and implement your AI
algorithms.

In order to allow simulations of trading sessions the system is divided in the
following components.

 * Data collector - This component collects the pricing information for the
 currencies selected and sends the information to the crypto bot module at
 specified intervals.
 * Portfolio tracker - This component retrieve and keeps track of the different
 cyrpto currencies owned and the amounts to support the decision making.
 * Crypto bot - This component is a state machine that receives information from
 the data collector module and decides based on the specified logic and current
 portfolio details.

The algorithm to decide the investment strategy is configurable and easily
customizable in order to implement your own strategies and analyze the results.

