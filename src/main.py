import pandas as pd


def read_csv(filename):
    """Reads CSV data from a file and returns a Pandas DataFrame."""
    df = pd.read_csv(filename, delimiter=",")
    return df


if __name__ == "__main__":
    filename = "data/books.csv"
    df = read_csv(filename)
