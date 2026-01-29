import json
import init_django_orm  # noqa: F401
from db.models import Race, Skill, Player, Guild


def main() -> None:

    with open("players.json", "r") as f:
        data = json.load(f)

    for name, info in data.items():
        guild = None
        nickname = name
        email = info["email"]
        bio = info["bio"]
        race_data = info["race"]
        name_race = race_data["name"]
        description_race = race_data["description"]
        skills_race = race_data["skills"]
        guild_inf = info["guild"]

        race, created = Race.objects.get_or_create(
            name=name_race,
            description=description_race
        )

        if skills_race:
            for skill in skills_race:
                Skill.objects.get_or_create(
                    name=skill["name"],
                    bonus=skill["bonus"],
                    race=race
                )

        if guild_inf:
            guild_name = guild_inf["name"]
            guild_description = guild_inf["description"]

            guild, created = Guild.objects.get_or_create(
                name=guild_name,
                description=guild_description
            )

        Player.objects.get_or_create(
            nickname=nickname,
            email=email,
            bio=bio,
            race=race,
            guild=guild
        )


if __name__ == "__main__":
    main()
