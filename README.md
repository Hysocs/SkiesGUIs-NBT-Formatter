# SkiesGUIs NBT Formatter

**SkiesGUIs NBT Formatter** is a tool designed to format Minecraft `give` commands into a JSON format suitable for use in the SkiesGUIs mod configuration. This tool simplifies the process of converting commands, making it easy to integrate custom heads and items with NBT data into your mod.

## How to Use

1. Go to the website https://minecraft-heads.com.
2. Find a head you want to use.
3. Set the version to 1.20.
4. Set the command version to `server`.
5. Copy the `Give Code` command provided by the site.
6. Paste the command into the input box in the tool.
7. Press 'Convert to JSON' to get the formatted JSON output.

The tool parses the NBT data from the command and converts it into a JSON format that can be used in the SkiesGUIs mod configuration.

## Adding to SkiesGUIs Config

To add the formatted NBT data into your SkiesGUIs configuration, follow these steps:

1. Ensure the item is set to `"item": "minecraft:player_head"` in the mod's config.
2. Place the NBT data inside the config under the appropriate item section.

Here is an example of how to place the NBT data inside the config for the player head to show up in-game:

```json
{
  "title": "<dark_gray>Example GUI",
  "size": 4,
  "alias_commands": ["examplegui", "examplegui"],
  "open_actions": {
    "playsound": {
      "type": "PLAYSOUND",
      "sound": "cobblemon:pc.on"
    }
  },
  "close_actions": {
    "playsound": {
      "type": "PLAYSOUND",
      "sound": "cobblemon:pc.off"
    }
  },
  "items": {
    "background": {
      "item": "minecraft:blue_stained_glass_pane",
      "slots": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 17, 18, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
      "name": ""
    },
    "ExampleGui": {
      "item": "minecraft:player_head",
      "slots": [13],
      "name": "<blue><b>Random Pokemon",
      "lore": ["<gray><italic>Click for a random Pokemon"],
      "priority": 2,
      "nbt": {
          "display": {
            "Name": "{\"text\":\"Mossy Stone Brick Block\",\"color\":\"gold\",\"underlined\":true,\"bold\":true,\"italic\":false}",
            "Lore": [
              "{\"text\":\"Custom Head ID: 57169\",\"color\":\"gray\",\"italic\":false}",
              "{\"text\":\"www.minecraft-heads.com\",\"color\":\"blue\",\"italic\":false}"
            ]
          },
          "SkullOwner": {
            "Id": [
              1697330712,
              527124754,
              -1908941700,
              248141423
            ],
            "Properties": {
              "textures": [
                {
                  "Value": "eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvNzlhMjQxZmZmMzcyMDZlMGRiOTc2Yzc5MmFjMjMzOGIyY2MzOWVhYmFlODNjN2Q0NjczYTFiM2RiYzNmNDBlYiJ9fX0="
                }
              ]
            }
          }
        },
      "click_actions": {
        "pokemon": {
          "type": "COMMAND_CONSOLE",
          "commands": ["pokegiveother %player% random"]
        },
        "message": {
          "type": "MESSAGE",
          "message": ["<blue>You have received a random Pokemon!"]
        }
      }
    }
  }
}
