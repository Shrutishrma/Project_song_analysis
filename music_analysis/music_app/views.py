# music_analysis/views.py
from django.shortcuts import render
from .forms import RecommendationForm
from .models import Song
import base64
from io import BytesIO
import matplotlib.pyplot as plt
import pandas as pd
import random

def load_data():
    file_path = r'C:\Users\shrut\OneDrive\Desktop\data_analytics_project.xlsx'
    df = pd.read_excel(file_path)
    
    # Iterate over rows and create Song objects
    for _, row in df.iterrows():
        Song.objects.create(
            track_name=row['track_name'],
            artist_names=row['artist_names'],
            popularity = row['popularity'],
            duration_in_min = row['duration_in_min'],
            genres = row["genres"],
            album_name = row["album_name"],
            release_year = row["release_year"],
            danceability = row["danceability"],
            energy = row["energy"],
            key = row["key"],
            loudness = row["loudness"],
            mode = row["mode"],
            speechiness = row['speechiness'],
            acousticness = row["acousticness"],
            instrumentalness = row["instrumentalness"],
            liveness = row["liveness"],
            valence = row["valence"],
            tempo = row["tempo"],
            time_signature = row["time_signature"],

            )

load_data()


def home(request):
    songs = Song.objects.all()
    print(songs) 
    return render(request, 'home.html', {'songs': songs})

def new_page(request):
    return render(request, 'newpage.html')

def create_popularity_chart(popularity_data):
    plt.bar(range(1, len(popularity_data) + 1), popularity_data)
    plt.xlabel('Song')
    plt.ylabel('Popularity')
    plt.title('Popularity Chart')
    
    # Save the chart as a PNG image in memory
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Convert the image stream to base64
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    return f"data:image/png;base64,{image_base64}"



def recommend_songs(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            genres = form.cleaned_data.get('genres')
            duration_in_min = form.cleaned_data.get('duration_in_min')
            release_year = form.cleaned_data.get('release_year')

            # Fetch all songs initially
            all_songs = Song.objects.all()

            # Apply filters based on user input
            filtered_songs = all_songs.filter(
                release_year=release_year,
                genres__icontains=genres.lower(),
            ).order_by('-popularity')

            unique_songs = set()

            # Randomly select 10 unique songs
            while len(unique_songs) < 10 and filtered_songs:
                song = random.choice(filtered_songs)
                unique_songs.add(song)
                filtered_songs = filtered_songs.exclude(pk=song.pk)  # Exclude the selected song from further selection

            # Convert the set to a list for rendering
            unique_songs_list = list(unique_songs)

            popularity_data = [float(song.popularity) for song in unique_songs_list]
            chart_path = create_popularity_chart(popularity_data)

            return render(request, 'recommendations.html', {
                'songs': unique_songs_list,
                'chart_path': chart_path,
            })

        else:
            print("Form Errors:", form.errors)

    form = RecommendationForm()
    return render(request, 'recommend_form.html', {'form': form})