import os
from scripts.take_pictures import take_pictures


def main():
    data_dir = "../data/hand_localization_data"
    take_pictures(data_dir, 10)

if __name__ == "__main__":
    main()

