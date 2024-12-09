import pandas as pd
import matplotlib.pyplot as plt

def load_and_clean_data(file_path):
    """Load and preprocess data."""
    data = pd.read_csv(file_path)
    data = data.drop(columns=["Comments"], errors="ignore")
    data["GHI"] = data["GHI"].clip(lower=0)
    data["DNI"] = data["DNI"].clip(lower=0)
    data["DHI"] = data["DHI"].clip(lower=0)
    data["Timestamp"] = pd.to_datetime(data["Timestamp"])
    return data

def summarize_data(data):
    """Summarize solar data."""
    return data[["GHI", "DNI", "DHI"]].describe()

def plot_solar_data(data, region_name):
    """Plot solar data over time."""
    data.set_index("Timestamp", inplace=True)
    data[["GHI", "DNI", "DHI"]].resample("M").mean().plot()
    plt.title(f"Monthly Solar Irradiance - {region_name}")
    plt.xlabel("Date")
    plt.ylabel("Irradiance (W/m²)")
    plt.show()

if __name__ == "__main__":
    data = load_and_clean_data("../data/benin-malanville.csv")
    print(summarize_data(data))
    plot_solar_data(data, "Benin")
