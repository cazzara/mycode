from Cheater import Cheater_Loaded, Cheater_Swapper

def run_sim():
    swapper = Cheater_Swapper('')
    loaded = Cheater_Loaded('')

    swapper_score = 0
    loaded_score = 0
    num_games = 100000
    curr = 0

    while curr < num_games:
        swapper.roll()
        swapper.cheat()

        loaded.roll()
        loaded.cheat()

        swap_total = sum(swapper.get_dice())
        load_total = sum(loaded.get_dice())

        if swap_total == load_total:
            pass
        elif swap_total > load_total:
            swapper_score += 1
        else:
            loaded_score += 1

        curr += 1

    if swapper_score == loaded_score:
        print("both cheaters scored the same....")
    elif swapper_score > loaded_score:
        print("Swapper wins")
        print("Swapper: {} Loaded {}".format(swapper_score, loaded_score))
    else:
        print("Loaded wins")
        print("Swapper: {} Loaded {}".format(swapper_score, loaded_score))

for i in range(10):
    run_sim()
