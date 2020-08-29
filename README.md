# aram-pred

to run:

place under ./_private/env.sh
```bash
export MONGO_USERNAME="XXX"
export MONGO_PASSWORD="XXX"
export RIOT_API_KEY="XXX"
source venv/bin/activate
```

run mongo:

```bash
cd ./infrastructure
./mongo.sh
```


run notebooks:

````bash
# linux
jupyter notebook

# wsl
jupyter notebook --port=8889 --no-browser
```
## todos:

### functions

~~get matchlist for a player~~

~~get match details for a matchid~~

~~get players from matchdetail~~

~~write a player into db (if not exist)~~

~~write a matchdetail to db (if not exist)~~

~~write processor that reads 1 player and saves whole match history~~
~~--> start 0,99~~
~~--> 100, 199~~
~~--> 200, 299~~
~~stop @ end index = totalGames~~

~~write match history to database~~

~~query every match from match history~~

~~write every match to db~~

~~crawl to next 10 players~~



### utility

~~logging~~

~~retry if throttled~~

~~player as json see why not in db~~

