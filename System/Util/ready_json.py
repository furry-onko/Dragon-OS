import json

def openJson(file: str) -> dict | list | None:
    try:
        with open(file, 'r') as f:
            data = json.load(f)
            return data

    except Exception as x:
        print(f"ERROR LOADING FILE: {x}")
        print("RESTORING...")
        with open(file, 'w') as f:
            f.write("")
        return None

def addKeyValue(file: str, key: str, value: str) -> None:
    file: dict = openJson(file)

    if isinstance(file, dict):
        file[key] = value
        try:
            with open(file, 'w') as f:
                json.dump(data, f, indent=4)
        except Exception as x:
            print(f"ERROR ADDING KEY")