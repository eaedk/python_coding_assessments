# Assessment : Cinema ticket pricing
A cinema in Wakanda want you to make a pricing system to automatise the actual process.

Find the price related information bellow:
- Time : Day price = 100P ; Night price = 300P.
- Children : -10P during Day ; -30P Wednesday.
- Teenagers : -30P during Night if it's a Weekday; -15P during Night if it's the Weekend; -35P during Day if it's the Weekend.
- Adults : -40P during Night if it's a Weekday.
- Weekend [Saturday,Sunday] : -15% during Day; -20% during Night.

Fixed value discount are applied before percentages one. Some discount are cumulative according the statements above.

**NB**: Your solution must return a numerical value, the `P` is just the just the symbol of the Wakanda's currency. The operations to compute prices must be in the code.

# Example of price computing
- Children, Wednesday during day will pay : Day price - (10P + 30P) = 60P
- Teenagers, the weekend, during night will pay : (100 - 20)% of ( Night price - 15P )  = 228P

<!-- ```python


``` -->

# TODO
Implement the logic of the solution in the file named `file.py`.

Add a clear and concise documentation to the `solution function` and `main function`. (documentation has been written only for the first argument)

Add logic the `solution function` and `main function`.

**NB**: If you think you need other arguments to better define the `solution function` add these arguments only using `**kwargs`.
