import argparse

def main():

    # Create argument parser
    parser = argparse.ArgumentParser(description="Play music based on your mood")


    # Add a "mood argument"
    parser.add_argument("mood", type=str, help="Your current mood(eg. happy, sad, relaxed etc..)")

    arg = parser.parse_args()

    print(f"Your current mood is : {arg.mood}")




if __name__ == "__main__":
    main()