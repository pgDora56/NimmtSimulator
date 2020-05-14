# NimmtSimulator

## Files
* main.py : executable file
* player.py : parent class & examples
* simple.py : template class(player)

## Usage
1. Make your own intelligence by editing `simple.py`.
2. Set using players by editing `main.py`.
```
# main.py:line 146-153
if __name__ == "__main__":
    players = [ # Set using players list
                BiggerPlayer(),
                BiggerPlayer(),
                SmallerPlayer(),
                SmallerPlayer(),
            ]
    board = Board(players) # Play!!
```

3. Run the following command:
```
python main.py
```

## LICENSE 
[MIT](LICENSE)

