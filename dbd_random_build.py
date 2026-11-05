
import random
import requests

BASE_URL = "https://deadbydaylight-api.onrender.com"

PERK_ENDPOINTS = {
    "s": ("Survivor", f"{BASE_URL}/perks/survivor"),
    "k": ("Killer", f"{BASE_URL}/perks/killer"),
}

def fetch_perks(url):
    """Fetch perk names from the alternative DBD API."""
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    data = response.json()

    # Support either a list of perks or a dictionary response.
    if isinstance(data, dict):
        perks_data = data.get("perks", data.get("data", []))
    else:
        perks_data = data

    perks = sorted({
        perk["name"].strip()
        for perk in perks_data
        if isinstance(perk, dict)
        and isinstance(perk.get("name"), str)
        and perk["name"].strip()
    })

    if len(perks) < 4:
        raise ValueError(
            "The API did not return at least four valid perks."
        )

    return perks


def generate_build(role, url):
    """Generate and display a random four-perk build."""
    print(f"\nFetching {role} perks...")

    try:
        perks = fetch_perks(url)
        build = random.sample(perks, 4)

        print("\n" + "=" * 40)
        print(f" YOUR RANDOM {role.upper()} BUILD")
        print("=" * 40)

        for number, perk in enumerate(build, start=1):
            print(f"{number}. {perk}")

        print("=" * 40)

    except requests.exceptions.Timeout:
        print("The API took too long to respond. Try again.")

    except requests.exceptions.HTTPError as error:
        print(f"The API returned an HTTP error: {error}")

    except requests.exceptions.RequestException as error:
        print(f"Could not connect to the API: {error}")

    except (ValueError, KeyError, TypeError) as error:
        print(f"Could not process the perk data: {error}")


def main():
    print("=" * 40)
    print("   DEAD BY DAYLIGHT RANDOMIZER")
    print("=" * 40)

    while True:
        choice = input(
            "\nChoose your build:\n"
            "[S] Survivor\n"
            "[K] Killer\n"
            "Your choice: "
        ).strip().lower()

        if choice in PERK_ENDPOINTS:
            role, url = PERK_ENDPOINTS[choice]
            break

        print("Invalid choice. Please enter S or K.")

    while True:
        generate_build(role, url)

        again = input(
            "\nGenerate another build? (y/n): "
        ).strip().lower()

        if again != "y":
            print("\nThanks for playing. Good luck in the Fog!")
            break


if __name__ == "__main__":
    main()
