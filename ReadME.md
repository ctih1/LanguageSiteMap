# How it works
The script gets your base URL, and loops over every country code in resources/data.json, and replaces %COUNTRY% with that. Then it sends a request to the site, if it responds with a 200, it's green. If it responds with a 404, it's red.

# Examples

```
python3 ./main.py
> https://wwww.apple.com/%COUNTRY%
```
https://ibb.co/nbHFFkT