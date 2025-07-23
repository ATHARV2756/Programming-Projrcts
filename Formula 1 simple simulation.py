import random
import time

# List of tracks
tracks = [
    "Albert Park (Australia)", "Shanghai", "Suzuka", "Bahrain (Sakhir)", "Jeddah", "Miami", "Imola", "Monaco",
    "Barcelona", "Montreal", "Spielberg (Austria)", "Silverstone", "Spa-Francorchamps", "Hungaroring", "Zandvoort",
    "Monza", "Baku", "Marina Bay (Singapore)", "Circuit of the Americas (Austin)", "Mexico City",
    "Interlagos (São Paulo)", "Las Vegas", "Lusail (Qatar)", "Yas Marina (Abu Dhabi)",
    "Sepang", "Nürburgring", "Laguna Seca", "Indianapolis", "Caesars Palace", "Brands Hatch",
    "AVUS", "Boavista", "Nordschleife", "Charade"
]

# Points system for top 10
points_award = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

# Driver data
drivers = [
    {"name": "Max Verstappen", "skill": 10, "car": 8},
    {"name": "Yuki Tsunoda", "skill": 7, "car": 8},
    {"name": "Lando Norris", "skill": 9, "car": 10},
    {"name": "Oscar Piastri", "skill": 9, "car": 10},
    {"name": "Charles Leclerc", "skill": 9, "car": 9},
    {"name": "Lewis Hamilton", "skill": 9, "car": 8},
    {"name": "George Russell", "skill": 9, "car": 9},
    {"name": "Andrea Kimi Antonelli", "skill": 7, "car": 8},
    {"name": "Carlos Sainz", "skill": 9, "car": 7},
    {"name": "Fernando Alonso", "skill": 9, "car": 7},
    {"name": "Pierre Gasly", "skill": 8, "car": 6},
    {"name": "Esteban Ocon", "skill": 7, "car": 7}
]

# Modifiers
def generate_weather():
    roll = random.randint(1, 100)
    if roll <= 60:
        return "Dry"
    elif roll <= 85:
        return "Light Rain"
    else:
        return "Heavy Rain"

def get_weather_modifier(weather):
    if weather == "Dry":
        return 1.0
    elif weather == "Light Rain":
        return 0.95
    elif weather == "Heavy Rain":
        return 0.85

def get_track_modifier(track_name):
    if "Monaco" in track_name or "Singapore" in track_name or "Baku" in track_name:
        return {"skill_weight": 0.7, "car_weight": 0.3}
    elif "Monza" in track_name or "Spa" in track_name or "Las Vegas" in track_name:
        return {"skill_weight": 0.4, "car_weight": 0.6}
    else:
        return {"skill_weight": 0.6, "car_weight": 0.4}

# Season Simulation
def simulate_season():
    standings = {driver["name"]: 0 for driver in drivers}

    for round_num, track in enumerate(tracks, 1):
        print(f"\n===== Round {round_num}: {track} =====")
        weather = generate_weather()
        print(f"Weather: {weather}")

        modifier = get_track_modifier(track)
        weather_mod = get_weather_modifier(weather)

        performance_list = []
        for driver in drivers:
            performance = (
                driver["skill"] * modifier["skill_weight"] +
                driver["car"] * modifier["car_weight"] +
                random.uniform(0, 2)
            ) * weather_mod
            performance_list.append((performance, driver["name"]))

        performance_list.sort(reverse=True)

        print("Results:")
        for pos, (score, name) in enumerate(performance_list, 1):
            print(f"{pos}. {name} ({score:.2f})")
            if pos <= 10:
                standings[name] += points_award[pos - 1]

        time.sleep(1)

    # Final Standings
    print("\n===== FINAL CHAMPIONSHIP STANDINGS =====")
    sorted_standings = sorted(standings.items(), key=lambda x: x[1], reverse=True)
    for pos, (name, pts) in enumerate(sorted_standings, 1):
        print(f"{pos}. {name} - {pts} pts")
    print(f"\n🏆 World Champion: {sorted_standings[0][0]}")

# Run full season
simulate_season()
