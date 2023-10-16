# Microproject - Billboard 100 Spotify Playlist

This documentation provides an explanation of a Python script that generates a Spotify playlist containing the Billboard Hot 100 songs for a specific date.

## Purpose
The purpose of this script is to fetch the Billboard Hot 100 songs for a user-specified date, find them on Spotify, and create a private Spotify playlist with those songs.

## Dependencies
To run this script, you need the following dependencies:
- `requests`: This library is used to send HTTP requests to fetch the Billboard Hot 100 songs from the Billboard website.
- `BeautifulSoup`: A Python library for web scraping and parsing HTML.
- `spotipy`: A Python library for the Spotify API.
- `confidential` module: This module contains your confidential Spotify client ID and client secret, which are used for authentication.

## Usage
1. The script starts by asking the user for the year they want to travel to, in the format YYYY-MM-DD.

2. It constructs a URL to the Billboard Hot 100 chart for the specified date and uses `requests` and `BeautifulSoup` to scrape the titles of the songs from the Billboard website.

3. It then uses the `spotipy` library to interact with the Spotify API. It initiates a Spotify client with the necessary authentication details and gets the current user's ID.

4. The script searches for each song from the Billboard Hot 100 on Spotify, collects their URIs, and stores them in a list.

5. It creates a private Spotify playlist with the name "YYYY-MM-DD Billboard 100" and adds the songs to the playlist.

6. If any song is not available on Spotify, it prints a message indicating that.

## Security Considerations
Make sure to secure your Spotify client ID and client secret. Storing them in a separate `confidential` module is a good practice to keep them private.

## Limitations
- This script assumes that the user's Spotify account has the necessary permissions to create a private playlist and add songs to it.
- The Spotify API may have limitations on the number of requests you can make within a certain time frame. You should consider this when handling a large number of songs.

## Spotify Authentication
This script uses the Spotify OAuth2 flow for authentication. Ensure that you have a registered Spotify application with the correct client ID and client secret. You can also adjust the scope and other parameters as needed.

## License
This script is provided for educational and personal use. Be aware of any licensing and usage restrictions associated with the dependencies and Spotify API.

Enjoy creating your Billboard Hot 100 playlist on Spotify with this Python tool!
