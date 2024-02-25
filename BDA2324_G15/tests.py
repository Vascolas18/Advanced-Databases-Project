import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statistics import mean

def get_benchmark_times(filename) :
    df = pd.read_csv(filename)

    return df

def plot(mysql_no_optimizations, mysql_with_optimizations, mongo_no_optimizations, mongo_with_optimizations):
    t = np.array(range(1,31))

    # MySQL
    plt.plot(t, mysql_no_optimizations['loudness_in_range_query'], color='black',label='no optimizations')
    plt.plot(t, mysql_with_optimizations['loudness_in_range_query'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("MySQL - Loudness in range query")
    plt.legend()
    plt.show()

    plt.plot(t, mysql_no_optimizations['popular_songs_query'], color='black',label='no optimizations')
    plt.plot(t, mysql_with_optimizations['popular_songs_query'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("MySQL - Popular songs query")
    plt.legend()
    plt.show()

    plt.plot(t, mysql_no_optimizations['artist_albums_query'], color='black',label='no optimizations')
    plt.plot(t, mysql_with_optimizations['artist_albums_query'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("MySQL - Artist albums query")
    plt.legend()
    plt.show()

    plt.plot(t, mysql_no_optimizations['popular_featured_track_query'], color='black',label='no optimizations')
    plt.plot(t, mysql_with_optimizations['popular_featured_track_query'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("MySQL - Popular featured track query")
    plt.legend()
    plt.show()

    plt.plot(t, mysql_no_optimizations['update'], color='black',label='no optimizations')
    plt.plot(t, mysql_with_optimizations['update'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("MySQL - Update query")
    plt.legend()
    plt.show()

    plt.plot(t, mysql_no_optimizations['insert'], color='black',label='no optimizations')
    plt.plot(t, mysql_with_optimizations['insert'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("MySQL - Insert query")
    plt.legend()
    plt.show()

    # Mongo
    plt.plot(t, mongo_no_optimizations['loudness_in_range_query'], color='black',label='no optimizations')
    plt.plot(t, mongo_with_optimizations['loudness_in_range_query'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("Mongo - Loudness in range query")
    plt.legend()
    plt.show()

    plt.plot(t, mongo_no_optimizations['popular_songs_query'], color='black',label='no optimizations')
    plt.plot(t, mongo_with_optimizations['popular_songs_query'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("Mongo - Popular songs query")
    plt.legend()
    plt.show()

    plt.plot(t, mongo_no_optimizations['artist_albums_query'], color='black',label='no optimizations')
    plt.plot(t, mongo_with_optimizations['artist_albums_query'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("Mongo - Artist albums query")
    plt.legend()
    plt.show()

    plt.plot(t, mongo_no_optimizations['popular_featured_track_query'], color='black',label='no optimizations')
    plt.plot(t, mongo_with_optimizations['popular_featured_track_query'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("Mongo - Popular featured track query")
    plt.legend()
    plt.show()

    plt.plot(t, mongo_no_optimizations['update'], color='black',label='no optimizations')
    plt.plot(t, mongo_with_optimizations['update'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("Mongo - Update query")
    plt.legend()
    plt.show()

    plt.plot(t, mongo_no_optimizations['insert'], color='black',label='no optimizations')
    plt.plot(t, mongo_with_optimizations['insert'], color='red',label='with optimizations')

    plt.xlabel("Iterations")
    plt.ylabel("Time (seconds)")
    plt.title("Mongo - Insert query")
    plt.legend()
    plt.show()

mysql_no_optimizations = get_benchmark_times("mysql_no_optimizations_times.csv")
mysql_with_optimizations = get_benchmark_times("mysql_with_optimizations_times.csv")
mongo_no_optimizations = get_benchmark_times("mongo_no_optimizations_times.csv")
mongo_with_optimizations = get_benchmark_times("mongo_with_optimizations_times.csv")

plot(mysql_no_optimizations, mysql_with_optimizations, mongo_no_optimizations, mongo_with_optimizations)