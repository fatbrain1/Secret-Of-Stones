
import hashlib
import json
import time

def hash_stone_entry(entry: dict) -> str:
    base_string = f"{entry['type']}|{entry['content']}|{entry['emotion']}|{entry['culture']}|{entry['timestamp']}"
    hash_object = hashlib.sha256(base_string.encode())
    return hash_object.hexdigest()

def create_stone(type: str, content: str, emotion: str, culture: str):
    entry = {
        "type": type,
        "content": content,
        "emotion": emotion,
        "culture": culture,
        "timestamp": time.time()
    }
    entry["stone_hash"] = hash_stone_entry(entry)
    return entry

# Example usage
if __name__ == "__main__":
    stone = create_stone(
        type="silence",
        content="4.3s pause after his name was spoken",
        emotion="longing",
        culture="Bedouin"
    )
    print(json.dumps(stone, indent=2))
