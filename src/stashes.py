import json
import init_paths


stashes_path = f"{init_paths.game_path}\\data\\stashes.json"


with open(stashes_path, encoding="utf-8") as f:
    stashes = json.load(f)

for stash in stashes.values():
    print(stash["name"])
    for item, amount in stash["contents"].items():
        print(item, amount)
    print("----||----")
