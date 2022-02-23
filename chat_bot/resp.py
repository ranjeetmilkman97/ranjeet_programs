import random

R_EATING = "I don't like eating anything because I'm a bot!"
R_ADVICE = "If I were you, I would do a google search instead!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "What does that mean?"][
        random.randrange(2)]
    return response