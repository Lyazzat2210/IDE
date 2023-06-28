import numpy as np
# The computer guess numbers itself.
def random_predict(number:int=1) -> int:
    """Guess the number random

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Number of attempts
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        
        if number == predict_number:
            break
    return count

print(f"Count of attempts: {random_predict()}")

# mean of trials for quessing number

def score_game(random_predict) -> int:
    """the count of trials for guessing number in 1000 iterations

    Args:
        random_predict (_type_): function of guessing

    Returns:
        int: mean count of trials
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # mean count of trials
    
    print(f"Your algorithm guess the number for:{score} trials in mean.")
    return score

score_game(random_predict)

# RUN
if __name__ == "_main_":
    score_game(random_predict)
    