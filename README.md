# Bing Wallpaper Fetch

A simple python script to fetch fancy [Bing Wallpapers](http://www.bing.com/gallery/).

Usage:
```bash
python3 bing_wallpaper_fetch.py --count=8 --output-directory=~/Pictures/Wallpapers
```

The most common usage for the script is to put it into the /etc/crontab to fetch the latest Bing wallpaper every day, e.g:
```bash
# /etc/crontab
# Fetch the new Bing Wallpaper daily at 13:00
0 13    * * *   tim     python3 /home/tim/dev/bing-wallpaper-fetch/bing_wallpaper_fetch.py -c 1 -d ~/Pictures/Wallpapers
```

Please note that due to the Bing's API limitation, only the last 16 images are available for download.
