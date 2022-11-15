import random
from matplotlib import pyplot as plt
plt.style.use("ggplot")


def roll_dice() -> int:
    """
    Function that simulates rolling two fair die with an equal
    probability of returning 1-6 and sums the value

    Returns:
        int: the sum of rolling two fair die
    """

    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    return die_1 + die_2


def check_if_won(total_die_roll: int, win_cut_off: int = 9) -> bool:
    """
    Function that checks whether the total of the die rolled is greater
    than the win probability

    Args:
        total_die_roll (int): the summed amount of the die rolled

    Returns:
        bool: True if the total is greater than the win cut off
        (indicating you win), False otherwise (indicating you lose)
    """

    return total_die_roll > win_cut_off


def perform_simulation(initial_balance: float, wager_per_roll: float,
                       amount_per_win: float, win_cut_off: float,
                       number_of_rolls: int) -> float:
    """
    Function to simulate single game of dice roulette

    Args:
        initial_balance (float): starting balance of our account
        wager_per_roll (float): amount bet per roll of the dice
        amount_per_win (float): amount you could win per roll
        win_cut_off (float): the total dice number above which you win
        number_of_rolls (int): total number of rolls in the game

    Returns:
        float: the total profit (or loss, if negative) from the game
    """
    # Current balance at the start must be our initial balance
    current_balance = initial_balance

    # Iterate over each die roll
    for _ in range(number_of_rolls):
        total_rolled = roll_dice()
        won = check_if_won(total_rolled, win_cut_off=win_cut_off)
        if won:
            # If our total rolled is above the cut-off, increment balance
            current_balance += (amount_per_win * wager_per_roll)
        else:
            # If our total rolled is less than the cut-off, decrement balance
            current_balance -= wager_per_roll

        number_of_rolls += 1

    # Deduct our initial balance from the initial balance to calculate "profit"
    ending_profit = current_balance - initial_balance

    return ending_profit


if __name__ == "__main__":
    number_of_simulations = 10000
    number_of_rolls = 1000
    profits = []

    for _ in range(number_of_simulations):
        # Calculate the profit of a single simulation
        profit = perform_simulation(initial_balance=1000, wager_per_roll=1,
                                    amount_per_win=3.75, win_cut_off=9,
                                    number_of_rolls=100)

        # Append the single profit to all those calculated in our simulation
        profits.append(profit)

    # Plot histogram of results
    plt.hist(profits, bins=30, rwidth=0.9)
    plt.title("Simulated Profits from Dice Roulette")
    plt.xlabel("Total Profit")
    plt.ylabel("Number of Simulations in bucket")
