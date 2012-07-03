# A Dragon Appears

A Dragon Appears (ADA) is a gaming framework intended for the rapid prototyping of roleplaying games and the tools to learn and play them quickly and easily. ADA borrows many lessons from software development, like how to separate concerns and share or re-use material, so that ADA games can be remixed into whole new gaming experiences with a minimum of effort. 

The tools to play ADA games perform the arithmetic posed in game rules, and in turn, contain the game rules themselves. In essence, the tools *are* the game rules. If you've ever played Dungeons and Dragons, you're probably fimiliar with the amount of mathematical computation necessary. These tools are meant to get the arithmetic out of your way, so you can get back to adventuring with your friends.

Game development using ADA resembles what is called "Readme-Driven Development" (RDD), where in you write up the game experience, and derive tools that satisfy the written description. Ultimately, ADA will derive these tools automatically, either totally or in part, so you can get to gaming faster. Currently, ADA uses these written descriptions for testing, to make sure all the tools work as intended.

## Design Philosophy

ADA seeks to embody the following principles in its design:

1. Modularity: Regardless of flavor or setting, game mechanics should be easy to re-use and re-purpose.
2. Consistency: Even as rules between games differ, the interfaces that allow their use shouldn't.

Why? To obliterate the time required both to design games and to learn to play them. Rather than spend time flipping through your games' rules compendium, spend that time playing the game. ADA handles the grit and mess, so you can get back to traveling through time / adventuring across medieval landscapes / destroying Zombie Hitler / searching for lost artifacts / becoming the greatest wizard who ever lived / getting sick and tired of these monkey-fightin' snakes on this Monday to Friday plane, or whatever else your imagination can conjure.

## Parts and Mechanics

ADA's core mechanics are based on a traditional MVC (model-view-controller) separation of concerns: models store data, controllers manipulate data, and views show data. In ADA, these parts are called Entities (Models), Interactions (Controllers), and Flavor (Views). By assigning responsibility in this way, we improve modularity. A whole new game can be spun up just by replacing the Flavor of one game with another; or a game experience can change completely just by altering the way an Interaction resolves conflict.

Now let's talk about each of these mechanics in more detail:

### Entities (AKA Models)

Entities are objects, items, characters, monsters, etc. Most nouns can be characterized as an entity. They consist of attributes, which describe their skills, nature, abilities, and other statistics like health or stamina -- whatever applies to the entity. A character and a lamp will have very different attributes, but they're both entities. Entities do not compute or change values on their own. Interactions call on them, and the Entities morph accordingly. For example, the ability for a character to attack something is an interaction, not a part of the entity: it's the character interacting with other entities.

**Summary**: Entities store and validate attributes. Entities interact with other entities and their environment through interactions.

#### Attributes (AKA Fields)

Attributes represent aspects of entities, like health or strength or durability. They grow, diminish, change, and morph in a variety of ways, but their interface is consistent: all attributes have a way of reading their values without changing them, of changing their values, and of using the attribute (which may change the attribute's values).

**Summary**: Attributes store and validate values, and allow other mechanics to access and use them uniformly.

### Interactions

Interactions are verbs, like attacking, competing, attempting, and the like. Whenever an entity is trying to affect other entities, its environment, or often itself, it does so through interactions. They take the entity, or some part of the entity, manipulate it, and return the result of the interaction. For example, an entity attacking another might change the stamina of the attacker, and the health of the defender. The result is like a bunch of logging information, which flavor parses into the story of the interaction.

**Summary**: Interactions manipulate entities as they try to interact with themselves, other entities, and their environment. Interaction results are used by flavor to tell the story of the interaction.

### Flavor

Flavor tells the story of entities, attributes, and interactions. When two characters get in a brawl, flavor parses who hit who, how hard, and any other information into a coherent, human-readable summary, like this:

"Gargak struck the wayward bard Florbid with his tankard. Florbid touched his cracked lip before aggressing in turn, slamming his mandolin into the side of Gargak's head, sending him to the floor."

Flavor can also describe entities based on their attributes:

"Gargak, the insolent barbarian, stands strong and tall. A fit orc, he holds true to his mantra: 'Smash now, talk later!'"

Because of how much flavor needs to know about the entities and interactions in your game, ADA uses flavor to test other game mechanics, to make sure the rules as written match up to the game as expected. That way, flavor not only fleshes out the game world, it also helps weed out kinks in the rest of the game.

**Summary**: Flavor yields human-readable descriptions of entities or interaction results, fleshing out the game world and its narrative tone.

## Stories

Like a video game has saves, ADA games have stories, with a log of everything that's happened, a list of game entities and their current states, and everything else needed to run the game. Where traditional game masters need to keep notes on game events, ADA tries to log all this information for you, so you can spend more time playing and less time doing bookkeeping.

### Logs

#### Interaction logs

These are diagnostic logs generated by interactions in the game. Not meant for human consumption, they can be used to restore game entities to any point in the game's history, or undo changes after some point.

#### Flavor logs

Human-readable logs of game events generated by flavor. These exist for players to read, though have enough identifying data to facilitate the use of the restorative powers of the interaction logs.

### Game Entities

Saved game entities are pickled python objects, restorable by console. They're restored automatically when you load up the story.

### Game Master Notes

Notes about the game that are secret to the players, whether because they haven't happened yet or just because the players shouldn't know. These are human-written notes, but bound to each story.

## Game Structure

Games are made from a body of folders and files, as follows:

    / README
    / setup.py
    / game/
        / attributes.py
        / entities.py
        / interactions.py
        / flavor.py
    / stories/
        / [story name]/
            / logs/
                / interactions.log
                / flavor.log
            / entities/
            / notes/
    / manage.py
    / venv/

The README describes the game, its mechanics, and how to use it. It can be automatically constructed based on the documentation of the game's mechanics, whereupon the author may further edit the file to their liking.

`setup.py` is a python setup script, which other ADA games will use to install this game with, should they want to make use of its parts.

`game` contains all the game's parts in its constituent files: `attributes.py`, `entities.py`, `interactions.py`, and `flavor.py`.

`stories` contain folders for each story being run with this game. Each story folder has folders for logs, saved entities, and game master notes.

`manage.py` performs various administrative tasks, like running tests; starting the gaming environment; or creating, loading, and otherwise managing stories.

`venv/` is a python virtual environment, which stores installed modules.

## Managing games

Directions for various administrative tasks.

### Installing a game

    git clone [game repository] [game name]
    cd [game name]
    virtualenv venv
    source venv/bin/activate
    python setup.py install
    
### `manage.py` actions

#### `test`

Use the game's `flavor` to test its mechanics for bugs, completeness, and coverage.

#### `story`

**`create [name]`**

Create a story named [name] and start the game.


**`load [name]`**

Load saved entities from story [name] and start the game.

**`clone [name] [new_name] [timestamp]`**

Creates a copy of story [name] as of [timestamp] called [new_name]. Useful for creating divergent histories. If [timestamp] is not given, the story is cloned from its most recent state.

**`destroy [name]`**

Delete all trace of story [name].

### Actions inside the game client

The game client is a pre-loaded python shell, with access to all the game's attribute, entity, interaction, and flavor classes, plus some extra goodies.

#### `restore` [entity] [timestamp]

Restore [entity] to its state as of [timestamp]

#### `save`

Save the game's current state to its current story.

## TODO

These are items yet to be implemented in ADA, but which are nonetheless intended:

### Turns

A way of yielding control from entity to entity, as in turns from traditional games like Dungeons and Dragons.

### Sinatra-like DSL

Game design and usage, particularly as ADA envisions it, is well worth the power offered by a domain-specific language.
