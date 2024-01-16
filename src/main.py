import pandas as pd
import json


def read_csv(filename):
    """Reads CSV data from a file and returns a Pandas DataFrame."""
    df = pd.read_csv(filename, delimiter=",")
    return df


def write_json(filename, data):
    """Writes JSON data to a file."""
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


if __name__ == "__main__":
    filename = "data/books.csv"
    df = read_csv(filename)
    books_data = df.to_dict(orient='records')
    write_json("data/books.json", books_data)
