# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

## Audio #######################################################################

init python:
    ##_game_menu_screen = "preferences"

    renpy.music.register_channel("musicb", mixer="music", loop=True, stop_on_mute=False, tight=True, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)

define config.main_menu_music = "audio/campfire.mp3"
## define config.game_menu_music = "audio/campfire.mp3"

define audio.campfire = "audio/campfire.mp3"
define audio.chewgum = "audio/chewgum.mp3"
define audio.spooky = "audio/spooky.mp3"
define audio.guitar = "audio/guitar.mp3"

## story start

# play music spooky loop fadein 1.0

## on first play of chewgum

# play musicb chewgum loop fadein 1.0

## spooky fadeout
# renpy.music.set_volume(0.0, delay=2, channel='music')
## spooky fadein
# renpy.music.set_volume(1.0, delay=2, channel='music')

## chewgum fadeout
# renpy.music.set_volume(0.0, delay=2, channel='musicb')
## chewgum fadein
# renpy.music.set_volume(1.0, delay=2, channel='musicb')


## Characters ##################################################################

define P = Character(None, kind=nvl, what_color="#4dd0e1", image="emily")
define E = Character(None, kind=nvl, what_color="#f48fb1", image="ellie")
define R = Character(None, kind=nvl, what_color="#ffa726", image="rosie")
define C = Character(None, kind=nvl, what_color="#ba68c8", image="caz")

default caz_score = 0
default rosie_score = 0
default ellie_score = 0
default death = False
default stoned = False
default pizza = False
default kitty = False

define menu = nvl_menu
define narrator = Character(None, kind=nvl, what_prefix="{i}")


## Sprites #####################################################################

# Backgrounds
image bg black = "#000000"
image bg white = "#FFFFFF"

image bg campfire = "images/fire.png"
image bg kitchen = "images/kitchen.png"
image bg sofa = "images/sofa.png"
image bg street = "images/street.png"
image bg tree = "images/tree.png"

# Emily
image emily = "sprite/emily.png"
image emily sheepish = "sprite/emily_sheepish.png"
image emily gendo = "sprite/emily_gendo.png"
image emily interrupted = "sprite/emily_interrupted.png"
image emily satisfied = "sprite/emily_satisfied.png"
image emily relieved = "sprite/emily_relieved.png"

# Ellie
image ellie = "sprite/ellie.png"
image ellie scared = "sprite/ellie_scared.png"
image ellie excited = "sprite/ellie_excited.png"
image ellie pouting = "sprite/ellie_pouting.png"
image ellie hiding = "sprite/ellie_hiding.png"
image ellie flip = im.Flip("sprite/ellie.png", horizontal=True)
image ellie scared flip = im.Flip("sprite/ellie_scared.png", horizontal=True)
image ellie excited flip = im.Flip("sprite/ellie_excited.png", horizontal=True)
image ellie pouting flip = im.Flip("sprite/ellie_pouting.png", horizontal=True)
image ellie hiding flip = im.Flip("sprite/ellie_hiding.png", horizontal=True)

# Rosie
image rosie = "sprite/rosie.png"
image rosie skeptical = "sprite/rosie_skeptical.png"
image rosie gremlin = "sprite/rosie_gremlin.png"
image rosie laughing = "sprite/rosie_laughing.png"
image rosie stoned = "sprite/rosie_stoned.png"
image rosie flip = im.Flip("sprite/rosie.png", horizontal=True)
image rosie skeptical flip = im.Flip("sprite/rosie_skeptical.png", horizontal=True)
image rosie gremlin flip = im.Flip("sprite/rosie_gremlin.png", horizontal=True)
image rosie laughing flip = im.Flip("sprite/rosie_laughing.png", horizontal=True)
image rosie stoned flip = im.Flip("sprite/rosie_stoned.png", horizontal=True)

# Caroline
image caz = "sprite/caz.png"
image caz smirking = "sprite/caz_smirking.png"
image caz eyeroll = "sprite/caz_eyeroll.png"
image caz annoyed = "sprite/caz_annoyed.png"
image caz sinister = "sprite/caz_sinister.png"
image caz reassuring = "sprite/caz_reassure.png"
image caz flip = im.Flip("sprite/caz.png", horizontal=True)
image caz smirking flip = im.Flip("sprite/caz_smirking.png", horizontal=True)
image caz eyeroll flip = im.Flip("sprite/caz_eyeroll.png", horizontal=True)
image caz annoyed flip = im.Flip("sprite/caz_annoyed.png", horizontal=True)
image caz sinister flip = im.Flip("sprite/caz_sinister.png", horizontal=True)
image caz reassuring flip = im.Flip("sprite/caz_reassure.png", horizontal=True)


## Animations #################################################################

transform bob_A:
    easein_bounce 1.3 yanchor 0.0
    easein 1.0 yanchor 0.05
    repeat

transform bob_B:
    easein_bounce 1.5 yanchor 0.0
    easein 1.0 yanchor 0.05
    repeat

transform bob_C:
    easein_bounce 1.7 yanchor 0.0
    easein 1.0 yanchor 0.05
    repeat

transform shake:
    ease 0.08333 xanchor 0.51
    ease 0.08333 xanchor 0.49
    ease 0.1 xanchor 0.51
    ease 0.1 xanchor 0.49
    repeat


## Positions ###################################################################

transform opaque:
    easein 1.0 alpha 1.0

transform faded:
    easein 1.0 alpha 0.2

transform invisible:
    easein 2.0 alpha 0.0

transform hidden:
    alpha 0.0

transform shown:
    alpha 1.0

transform left:
    xcenter 0.125
    ycenter 0.5
    xanchor 0.5
    yanchor 0.46666667

transform audience_left:
    xcenter 0.375
    ycenter 0.66666667
    xanchor 0.5
    yanchor 0.4

transform audience_mid:
    xcenter 0.625
    ycenter 0.66666667
    xanchor 0.5
    yanchor 0.4

transform audience_right:
    xcenter 0.875
    ycenter 0.66666667
    xanchor 0.5
    yanchor 0.4

transform scoot_up:
    easein 0.4 yanchor 0.46666667 alpha 1.0

transform scoot_mid:
    easein 0.4 yanchor 0.4 xanchor 0.5

transform scoot_mid_y:
    easein 0.4 yanchor 0.4

transform scoot_mid_x:
    easein 0.4 xanchor 0.5

transform scoot_down:
    easein 0.4 yanchor 0.33333333

transform scoot_away:
    easein 2 yanchor -0.2 xanchor 0.5

transform scoot_away_left:
    easein 2 yanchor -0.2 xanchor 0.7

transform scoot_away_right:
    easein 2 yanchor -0.2 xanchor 0.2

transform scoot_back:
    easein 1 yanchor 0.46666667

transform scoot_left:
    easein 0.4 xanchor 0.66666667 alpha 1.0

transform scoot_right:
    easein 0.4 xanchor 0.33333333 alpha 1.0

# START ########################################################################

label start:

#stop music
#play sound "audio/Slasher Campfire.mp3" loop

show bg black onlayer background

$ Emily = renpy.input("Content Warnings:\nMild drug use\nSwearing\nDescription of murder\n\n\n\nIf you would like a different name, enter it here. The game will use she/her pronouns for you.\n\n", default='Emily')
$ Emily = Emily.strip()

# PART A #######################################################################

show bg street onlayer background with dissolve

show emily onlayer screens at hidden, left
show rosie onlayer screens at hidden, audience_mid
show ellie onlayer screens at hidden, audience_left
show caz onlayer screens at hidden, audience_right
play music spooky loop fadein 2.0

"...everything feels smothered in darkness, just the faintest glow from the moon lighting up the edges of shapes."

show ellie onlayer screens at hidden, scoot_right
show rosie onlayer screens at hidden, scoot_left

"Streetlights flicker and fail as you walk, and the sound of your footsteps echoes in the silence."

"Your phone struggles to cling on to life as you use it to light your way, but as you reach the end of the road the battery gives out."

"It takes a moment for your eyes to adjust. Swaying on your feet, hesitating before soldiering on, you see something out the corner of your eye - "

show ellie hiding onlayer screens at opaque, scoot_up

E "Eeek!"

show bg campfire onlayer background with dissolve
show rosie laughing onlayer screens at opaque, scoot_up
show ellie scared onlayer screens

$ renpy.music.set_volume(0.0, delay=1, channel='music')
play musicb chewgum loop fadein 1.0

R "IT'S A MONSTER, ELLIE! IT'S COMING TO GET YOU!"

show rosie gremlin onlayer screens at scoot_left
show ellie hiding flip onlayer screens at scoot_mid_x

E "Stop ittttt! You made me jump!"

show ellie pouting flip onlayer screens
show rosie stoned onlayer screens at scoot_mid_x

"Rosie laughs and retrieves her hand after making Ellie jump."

show caz smirking onlayer screens at opaque, scoot_up

"Caroline smirks briefly, then waves a hand to shush them."

C "Quiet, girls. Let [Emily] continue, I want to hear what happens."

nvl clear

show emily interrupted onlayer screens at opaque, left
show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

"The three of them settle down, Rosie and Ellie on a blanket and Caroline in the campchair next to it."

show emily onlayer screens

"The campfire illuminates their faces with flickering orange light, shadows stark and sinister on otherwise cheerful expressions."

"You clear your throat and continue where you left off."

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

nvl clear

show emily gendo onlayer screens
show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

P "Okay... so, you see something out the corner of your eye..."

show bg street onlayer background with dissolve

P "Whatever it is, you can't make it out before it disappears."

P "Squinting at the darkness, you make your way down the street to the house."

P "The wind whines through the trees, plaintive and warning, sending a chill up your spine."

show bg tree onlayer background with dissolve

P "When you reach the gate, the outdoor light triggers and illuminates the garden."

P "Disappearing behind a tree, you see..."

$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

show ellie excited onlayer screens at shown, scoot_up with vpunch

show bg campfire onlayer background with dissolve

show emily interrupted onlayer screens at opaque
show rosie onlayer screens at opaque
show caz eyeroll onlayer screens at opaque

E "A kitty!"

show rosie skeptical onlayer screens

R "Hahahah, what? It's not gonna be a cat!"

show emily onlayer screens at opaque
show ellie pouting flip onlayer screens at scoot_right
show rosie onlayer screens
show caz onlayer screens at opaque

E "Well, what do YOU think it is?"

show rosie stoned onlayer screens

R "If it were me it'd be, like, an old halloween decoration that makes you jump."

show ellie excited flip onlayer screens

E "That's so lame!"

show ellie flip onlayer screens at scoot_mid_y
show rosie onlayer screens
show caz eyeroll onlayer screens at scoot_up

C "You're both lame. Clearly this is a horror story."

show ellie flip onlayer screens
show caz onlayer screens

C "She's going to say 'A wicked blade flashes in the dark', or something."

show emily sheepish onlayer screens
show ellie scared onlayer screens at scoot_mid
show rosie stoned onlayer screens
show caz sinister onlayer screens

P "..."

nvl clear

show emily sheepish onlayer screens at scoot_mid
show ellie pouting onlayer screens at scoot_up
show rosie stoned onlayer screens at scoot_up
show caz sinister onlayer screens at scoot_up

show screen choice_A
"""It feels like the girls are trying to lead you towards three different stories...\n
(Click a character's speech bubble to continue)"""

# CHOICE A ELLIE ###############################################################

label choice_A_Ellie:

hide screen choice_A
nvl clear

show emily gendo onlayer screens at scoot_up
show ellie onlayer screens at scoot_mid 
show rosie onlayer screens at scoot_mid 
show caz onlayer screens at scoot_mid 

$ kitty = True

$ ellie_score += 1

P "A tail flicks out from the tree..."

show ellie excited onlayer screens with vpunch
show emily interrupted onlayer screens
show caz eyeroll onlayer screens

E "Yay! Kitty!"

show rosie stoned onlayer screens

R "Oh my god..."

show emily gendo onlayer screens
show ellie excited onlayer screens at faded
show rosie stoned onlayer screens at faded
show caz eyeroll onlayer screens at faded

P "..."

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show bg tree onlayer background with dissolve

show ellie onlayer screens
show rosie onlayer screens

P "You carefully cross the garden to the tree, and try to coax the cat back out."

P "Pspspspspspsps..."

P "The flick of a tail appears again, cautious and quick, then a small face peeks out."

show ellie onlayer screens at opaque

E "Kitty...."

show caz onlayer screens
show ellie onlayer screens at faded

P "The cat is sleek and black, except for a little smudge of white on its nose."

P "It sniffs the air before gingerly stepping forward to let you stroke it."

P "Another gust of wind whistles through the tree, shaking the leaves, and the cat hesitates."

P "It seems apprehensive of the house, and glances at the windows as you scratch behind its ears."

P "Then, there's a noise, and it shrinks back hissing at something over your shoulder."

P "When you turn to look, there's nothing there, and the cat scarpers."

show ellie pouting onlayer screens
show caz onlayer screens

P "You feel a chill run up your spine, and you stand up, alone in the garden, but for the feeling of being watched..."

jump choice_B

# CHOICE A ROSIE ###############################################################

label choice_A_Rosie:

hide screen choice_A
nvl clear

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show bg tree onlayer background with dissolve

show emily gendo onlayer screens at scoot_up
show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ rosie_score += 1

P "A shape sways in the wind..."

show ellie onlayer screens at faded
show caz onlayer screens at faded
show rosie onlayer screens at faded

P "Dangling from a tree, the light catches the edge of plastic bones and wires."

show rosie stoned onlayer screens at shown

R "Yesssss."

show rosie stoned onlayer screens at faded

P "Facing you is the grinning face of a skeleton, hung up for the long month of October."

P "It sways back and forth gently in the wind, arms rattling quietly as the joints click."

P "For a plastic corpse, it's unsettling at first, but then you spot something dangling from its mouth."

P "Someone has taped a joint to its lower jaw."

show rosie gremlin onlayer screens at shown
show caz eyeroll onlayer screens

R "Wack. Get it."

show rosie stoned onlayer screens at faded

P "...you go to reach up for it - and hear a noise behind you!"

show rosie laughing onlayer screens at scoot_up

R "It's a prank!"

show rosie stoned onlayer screens at faded, scoot_mid

P "...you jump as a second skeleton, unseen, starts cackling at you."

show caz onlayer screens

P "The sound is cheap and tinny, coming from a tiny speaker, the distortion creepy and manic."

P "It turns off after a second, as you move your hand away from whatever infrared beam triggered it, but the eye sockets still seem to bore into you."

P "Between the two plastic skeletons, you feel unnerved; the feeling of being watched remains."

P "You feel a chill run up your spine, and the humour of the moment doesn't quite take the edge off the adrenaline."

P "Something makes you feel like you're not alone in the garden..."

jump choice_B

# CHOICE A CAZ #################################################################

label choice_A_Caz:

hide screen choice_A
nvl clear

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show bg tree onlayer background with dissolve

show emily gendo onlayer screens at scoot_up
show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ caz_score += 1

P "A wicked blade flashes in the dark..."

show ellie pouting onlayer screens at faded
show rosie onlayer screens at faded
show caz sinister onlayer screens

C "Nice."

show caz sinister onlayer screens at faded

P "The glimmer of metal sets your heart beating, and you freeze on the spot as the knife disappears out of sight."

P "When you can bring yourself to take more steps into the garden, there's nothing to be seen behind the tree."

P "Shapes move in the corners of your vision, and you look around frantically for whatever lurks in the shadows."

P "You shout at the darkness, challenging whoever's there to show themselves."

P "The only reply is the wind brushing through the trees, and the faintest hint of a laugh..."

show caz sinister onlayer screens at shown

C "Heh heh heh..."

show caz sinister onlayer screens at faded

P "The laughter seems to come from different directions, and you feel small and vulnerable stood there in the garden."

P "Clutching your dead phone to your chest, you try and make out anything in the hedges."

P "The laughter stops, and you can't see anything but trees and bushes."

P "The feeling of being watched and taunted sends a shiver up your spine..."

jump choice_B

# PART B #######################################################################

label choice_B:

hide screen choice_B
nvl clear

P "You don't waste any time heading indoors."

P "Hopefully it'll feel safer inside; familiar, warm, lockable doors."

show ellie onlayer screens
show caz onlayer screens

P "With a last quick check over your shoulder, you open the front door and let yourself in."

P "The door closes with a creak - "

show rosie stoned onlayer screens at opaque

$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

R "Oh come on, our door doesn't creak!"

show bg campfire onlayer background with dissolve

show emily interrupted onlayer screens at opaque
show caz eyeroll onlayer screens at opaque

C "It does in winter. I have to put wd40 on the hinges."

show ellie flip onlayer screens at opaque
show rosie skeptical flip onlayer screens at scoot_left

R "You do?!"

show emily sheepish onlayer screens
show ellie hiding flip onlayer screens
show caz annoyed onlayer screens at scoot_up with vpunch

C "Just because you don't notice, doesn't mean it doesn't get done."

show ellie flip onlayer screens at scoot_right

E "The windows stick when it gets cold, too..."

show emily sheepish onlayer screens at scoot_right

P "Ahem..."

show ellie onlayer screens at scoot_mid
show rosie skeptical onlayer screens at scoot_mid
show caz eyeroll onlayer screens at scoot_mid

"The three trail off quickly and let you keep talking."

P "I didn't say it was our house... it's A house."

show emily sheepish onlayer screens at scoot_mid_x
show rosie onlayer screens
show caz onlayer screens

"It totally is your house you're narrating, though. You keep that quiet."

show emily gendo onlayer screens

P "Anyway..."

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show bg tree onlayer background with dissolve

show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

P "The door opens with a creak; the only sound in the darkness."

P "You close and lock it against the outdoors, taking a deep breath of relief."

P "But inside, it's weirdly quiet. You call out Hello? and nobody responds."

P "You creep down the corridor and peek into the living room."

show bg sofa onlayer background with dissolve

P "The light is on low, with quiet music playing from the stereo."

P "Over the top of the sofa you can see the backs of two people's heads, unmoving."

P "A sense of dread washes over you as you step closer to the sofa to see..."

show ellie pouting onlayer screens
show caz sinister onlayer screens at opaque

C "They're dead..."

$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

show bg campfire onlayer background with dissolve

show emily interrupted onlayer screens at opaque
show rosie stoned onlayer screens at opaque

R "Nah, they're super stoned."

show ellie hiding onlayer screens at opaque

E "No! They just fell asleep cuddling."

nvl clear

show emily interrupted onlayer screens at scoot_mid
show ellie onlayer screens at scoot_up
show rosie gremlin onlayer screens at scoot_up
show caz sinister onlayer screens at scoot_up

show screen choice_B
"""You start to wonder who's telling this story...\n
{i}(Click a character's speech bubble to continue){/i}"""

# CHOICE B ELLIE ###############################################################

label choice_B_Ellie:

hide screen choice_B
nvl clear

show emily onlayer screens at scoot_up
show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ ellie_score += 1

if ellie_score > 1:
    "You glance at Ellie and veer the story towards her tastes again."
else:
    "You glance at Ellie and throw in a scene for her."

show emily gendo onlayer screens
show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show bg sofa onlayer background with dissolve

P "As you get closer to check the bodies, one of them gently snores."

P "Moving around the side of the sofa, you realise it's Jake and Amy - "

show caz eyeroll onlayer screens at opaque

C "Ugh, them again."

show caz onlayer screens at faded

P "...they're both asleep, arms wrapped around each other."

show ellie excited onlayer screens at opaque

E "Awwwh..."

show ellie pouting onlayer screens

E "I want that..."

show emily interrupted onlayer screens at opaque
show rosie gremlin onlayer screens at opaque
show caz smirking onlayer screens

R "Lol, gay."

show ellie onlayer screens
show rosie stoned onlayer screens
show caz smirking onlayer screens at opaque

C "I can't believe you say actually 'lol' out loud like that."

P "..."

show caz onlayer screens

"Eventually, everyone shuts up again and listens."

show emily gendo onlayer screens

P "You keep quiet so as not to disturb them."

show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

P "The remains of cups of tea sit on the table, getting cold."

P "The quiet music playing only makes the room feel more still, like a film paused mid-scene."

P "You think about turning the music off, but it's not disrupting anything to leave it as it is."

P "As you stand there, one of them sniffs in their sleep and fidgets."

P "It's kinda cute to watch, but you start to feel a bit voyeuristic."

P "Then you hear another noise."

show ellie scared onlayer screens at shown

E "Oh no..."

show ellie hiding onlayer screens
show caz sinister onlayer screens at shown

C "Oh yes."

show ellie hiding onlayer screens at faded
show rosie stoned onlayer screens
show caz sinister onlayer screens at faded

P "A wet sound comes from the kitchen, behind the closed door."

P "The two on the sofa don't react, but that feeling you had outside is back."

P "Like you're not alone - sleeping couple aside, it feels like there's something else."

P "Something waits."

jump choice_C

# CHOICE B ROSIE ###############################################################

label choice_B_Rosie:

hide screen choice_B
nvl clear

show emily onlayer screens at scoot_up
show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ stoned = True

$ rosie_score += 1

if rosie_score > 1:
    "You look at Rosie, and play along with her ideas again."
else:
    "You look at Rosie, and pick her idea to run with this time."

$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

show bg sofa onlayer background with dissolve

show emily gendo onlayer screens

P "As you get closer to check the bodies, one of them groans."

show ellie onlayer screens at faded
show rosie stoned onlayer screens at faded
show caz onlayer screens at faded

P "You spot a bong sat on the floor next to the sofa, and you realise the two prone shapes on the sofa are Jake and Amy, too stoned to function."

show rosie stoned onlayer screens at scoot_up
show caz eyeroll onlayer screens

R "Ayyy, fuckin... that's the life."

show emily interrupted onlayer screens
show caz eyeroll onlayer screens at scoot_up
show rosie skeptical onlayer screens

C "If they stay on the SOFA, anyway."

show ellie pouting flip onlayer screens at opaque
show rosie stoned flip onlayer screens at scoot_left

"Rosie sparks up her own joint and laughs."

R "You're not still mad, Caz?"

show emily sheepish onlayer screens
show ellie hiding flip onlayer screens
show rosie skeptical flip onlayer screens at scoot_mid_y
show caz annoyed onlayer screens at scoot_left with vpunch

C "Yes! It was only three weeks ago! When your band friends come over and get trashed they can pass out in YOUR room next time."

show ellie pouting flip onlayer screens
show rosie skeptical flip onlayer screens

R "They weren't trashed, they were just stoned is all. Jake doesn't drink."

show caz eyeroll onlayer screens

C "They were passed out IN MY BED. NAKED. I don't care what it was from."

show caz annoyed flip onlayer screens at scoot_mid_x

P "..."

show ellie pouting flip onlayer screens at scoot_right
show caz eyeroll flip onlayer screens

E "I've done that too..."

show caz reassuring onlayer screens at scoot_up

C "Ellie, dear, you're different, I'm not mad at you."

show emily relieved onlayer screens
show ellie flip onlayer screens
show rosie stoned flip onlayer screens at scoot_up

R "Dya wanna toke? You'll be less mad."

show emily interrupted onlayer screens at scoot_right
show caz eyeroll onlayer screens

P "Ahem."

show emily interrupted onlayer screens at scoot_mid_x
show rosie onlayer screens
show ellie onlayer screens
show caz onlayer screens

"The three of them look at you, and Rosie rubs her neck sheepishly."

show ellie onlayer screens at scoot_mid
show rosie stoned onlayer screens at scoot_mid_x

R "Sorry, [Emily]. Uhhhhh Jake and Amy are stoned on the sofa, then what."

show emily relieved onlayer screens
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

P "..."

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show emily gendo onlayer screens

P "You keep quiet so as not to disturb them."

show rosie onlayer screens at faded
show ellie onlayer screens at faded
show caz onlayer screens at faded

P "Jake lifts a hand slightly, only just registering your presence, then lets it flop back down."

P "The quiet reggae playing only makes the room feel more still, like a film paused mid-scene."

P "You think about turning the music off, but they're probably enjoying it, even if it's not to your taste."

show caz smirking onlayer screens at shown

C "Hah."

show caz smirking onlayer screens at faded

P "...as you hesitate, you hear another noise behind you."

show ellie scared onlayer screens at shown

E "Oh no..."

show ellie hiding onlayer screens
show caz sinister onlayer screens at shown

C "Oh yes. Slasher time."

show ellie hiding onlayer screens at faded
show rosie stoned onlayer screens
show caz sinister onlayer screens at faded

P "...a wet sound comes from the kitchen, behind the closed door."

P "The two on the sofa don't react, but that feeling you had outside is back."

P "Like you're not alone - stoned couple aside, it feels like there's something else."

P "Something waits."

jump choice_C

# CHOICE B CAZ #################################################################

label choice_B_Caz:

hide screen choice_B
nvl clear

show emily onlayer screens at scoot_up
show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ death = True

$ caz_score += 1

if caz_score > 1:
    "You glance up at Caroline, and keep following the horror vibe you'd intended."
else:
    "You glance up at Caroline, and decide to pivot back to proper horror."

show ellie onlayer screens at faded
show rosie stoned onlayer screens at faded
show caz onlayer screens at faded
show emily gendo onlayer screens

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show bg sofa onlayer background with dissolve

P "You step closer to the sofa, and every step causes a sick feeling in your stomach to rise."

show ellie pouting onlayer screens

P "When you can see the figures closer, you gasp and take a step back in shock."

show caz sinister onlayer screens

P "Sprawled out on the sofa are the bodies of - "

"You hesitate for a moment, unsure if naming actual people is too weird."

P " - of two friends, their clothes torn and bloodstained, cut up by some vicious knife."

show ellie hiding onlayer screens at shown

E "Eeeek..."

show ellie hiding onlayer screens
show caz onlayer screens at scoot_up

$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

C "Who's 'two friends' meant to be?"

show emily sheepish onlayer screens

P "Like, just two friends of yours - "

show rosie stoned onlayer screens at scoot_up

R "Is it me and Ellie?"

show ellie pouting onlayer screens at scoot_up
show caz reassuring onlayer screens

E "I don't wanna be stabbed!"

show emily relieved onlayer screens

P "Fine, it's Jake and Amy, they came over for band practice and now they're DEAD."

show emily onlayer screens
show ellie hiding onlayer screens at scoot_mid
show rosie skeptical onlayer screens
show caz onlayer screens

R "...{nw}" 
pause (1.0) 
show rosie stoned onlayer screens 
extend "Grody."

show caz smirking onlayer screens
show rosie stoned onlayer screens

C "Oh, no, Jake and Amy are dead."

show emily interrupted onlayer screens
show ellie pouting flip onlayer screens
show rosie skeptical flip onlayer screens at scoot_left
show caz smirking onlayer screens

R "Hey, I know you don't like them, but chill with the sarcasm."

show caz annoyed onlayer screens at scoot_left
show rosie skeptical flip onlayer screens

C "I don't actually want them dead! But stakes are higher if they're named, right?"

show caz smirking onlayer screens at scoot_mid_x

C "It's not 'oh no generic friend is dead' anymore, it's visceral."

show caz smirking onlayer screens 
show ellie pouting flip onlayer screens at scoot_right

E "I'd be sad if they got stabbed."

show emily sheepish onlayer screens
show rosie stoned flip onlayer screens
show caz eyeroll onlayer screens

P "..."

show emily relieved onlayer screens at scoot_right
show caz onlayer screens

P "So, your two named friends are dead on the sofa - "

show rosie gremlin onlayer screens at scoot_mid_x

R "That's classic Jake and Amy - "

show emily interrupted onlayer screens
show ellie onlayer screens at scoot_mid
show caz eyeroll onlayer screens
show rosie stoned onlayer screens

P "..."

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show emily gendo onlayer screens at scoot_mid_x
show caz onlayer screens at scoot_mid
show rosie stoned onlayer screens at scoot_mid

P "You turn away from the grisly scene, horrified, your stomach turning at the sight."

show ellie pouting onlayer screens at faded
show rosie stoned onlayer screens at faded
show caz onlayer screens at faded
show emily gendo onlayer screens at faded

P "Anywhere here, the killer could be waiting, ready to strike again."

P "The stereo plays on in the corner, ignorant of the death in the room as the next dub track queues up."

P "You go to switch it off, but a sound in the kitchen stops you, and you freeze."

P "Something waits."

jump choice_C

# PART C #######################################################################

label choice_C:

hide screen choice_C
nvl clear

show emily gendo onlayer screens
show ellie scared onlayer screens at faded
show rosie stoned onlayer screens at faded
show caz sinister onlayer screens at faded

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show bg sofa onlayer background with dissolve

P "You stare at the kitchen door, a grim sense of foreboding rooting you to the spot."

P "It feels inevitable that you'll have to open it - "

show ellie hiding onlayer screens at opaque

E "Noo! Run away!"

show emily interrupted onlayer screens at opaque
show ellie hiding onlayer screens at scoot_down
show caz sinister onlayer screens at scoot_up

C "Grab a weapon!"

show rosie laughing onlayer screens at scoot_up

R "Fuck it, open the door."

show emily gendo onlayer screens
show rosie gremlin onlayer screens at scoot_mid
show ellie pouting onlayer screens at scoot_mid
show caz sinister onlayer screens at scoot_mid

P "You take a few deep breaths to try and steel yourself."

show ellie pouting onlayer screens at faded
show rosie stoned onlayer screens at faded
show caz onlayer screens at faded

P "Looking around, all you can find for a weapon is an umbrella in the corner."

P "You pick it up and weigh it in your hands."

P "It's flimsy, but it's something."

P "You creep closer to the door, and press your ear against it for a moment to listen."

P "It's silent on the other side of the door. Sinisterly so."

P "One hand on the handle, you glance back at the sofa, and swallow."

P "Whatever's in the kitchen, you're facing it on your own."

P "With one quick movement, you snap the handle down and push the door open, to see - "

$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

show bg campfire onlayer background with dissolve

show caz sinister onlayer screens at scoot_up

C "The killer!"

show caz sinister onlayer screens at scoot_mid
show ellie onlayer screens at scoot_up

E "No! A surprise birthday party!"

show ellie onlayer screens at scoot_mid
show rosie laughing onlayer screens at scoot_up
show caz eyeroll onlayer screens

R "Nah, a, a, a pizza's on fire!"

show emily interrupted onlayer screens
show ellie excited onlayer screens at scoot_mid
show rosie gremlin onlayer screens at scoot_mid
show caz annoyed onlayer screens

P "..."

nvl clear

show emily onlayer screens at scoot_mid
show ellie onlayer screens at scoot_up
show rosie stoned onlayer screens at scoot_up
show caz onlayer screens at scoot_up

show screen choice_C
"""This is it. Which finale do you go with?\n
(Click a character's speech bubble to continue)"""

# CHOICE C ELLIE ###############################################################

label choice_C_Ellie:

hide screen choice_C
nvl clear

show emily onlayer screens at scoot_up
show ellie onlayer screens at scoot_mid
show rosie stoned onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ ellie_score += 1

if ellie_score > 2:
    "Well, you've committed to Ellie's ideas already."

    "Time to follow through with a cute ending."
elif ellie_score > 1:
    "You veer the story towards Ellie's idea for a second time."

    if death:
        show emily sheepish onlayer screens
        "Guess it's kinda weird after literally killing two people, but whatever."

        "We're off the rails now."
else:
    "At the last minute, you chicken out from a different ending, and go with Ellie's idea."

    if death:
        show emily sheepish onlayer screens
        "It feels kinda jarring, but whatever."

        "This story is a lost cause by now."

show emily gendo onlayer screens

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show bg kitchen onlayer background with dissolve

P "As you open the door, there's a bang, and you close your eyes in shock."

show ellie onlayer screens at faded
show caz onlayer screens at faded
show rosie stoned onlayer screens at faded

P "You raise the umbrella, and feel something light patter against it."

P "Letting your eyes open again, a shower of confetti falls on you."

show ellie excited onlayer screens at scoot_up with vpunch

E "...!"

show ellie onlayer screens
$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

P "Rosie yells {i}Surprise! It's your birthday!{/i}"

show rosie laughing onlayer screens at scoot_up

R "Uhhhhh surprise! It's your birthday!"

show emily onlayer screens
show ellie excited flip onlayer screens at scoot_right
show rosie stoned onlayer screens

E "It's my birthday! Yay!"

show ellie flip onlayer screens

if death:
    show caz eyeroll onlayer screens at scoot_up

    C "..."

    show caz annoyed onlayer screens 

    C "People are DEAD out there."

    show emily interrupted onlayer screens
    show ellie pouting flip onlayer screens at scoot_mid_y
    show rosie laughing onlayer screens at scoot_mid
    show caz annoyed onlayer screens at scoot_mid

    "You hesitate for a moment, keenly aware of how shambolic this story is getting."

    show emily sheepish onlayer screens
    show rosie stoned onlayer screens

    P "Uhhhhhhhhhh Jake and Amy come up behind you and say {i}Happy birthday!{/i} The blood was fake!"

    show ellie excited onlayer screens at scoot_mid_x

    E "Yay they're not dead!"

else:
    show caz smirking onlayer screens at scoot_up

    C "So Jake and Amy are just sleeping through the party, huh?"

    show emily interrupted onlayer screens
    show ellie excited flip onlayer screens at scoot_mid_y
    show rosie gremlin onlayer screens at scoot_mid
    show caz smirking onlayer screens at scoot_mid

    "You hesitate for a moment, trying to retcon it in your head."

    show emily sheepish onlayer screens
    show ellie excited flip onlayer screens
    show rosie stoned onlayer screens

    P "Uhhhh they were just lulling you into a false sense of security!"

    show ellie onlayer screens at scoot_mid_x
    show caz onlayer screens

    P "The two of them emerge behind you and say {i}Happy birthday!{/i}"

show ellie onlayer screens
show rosie stoned onlayer screens
show caz eyeroll onlayer screens

"Caroline rolls her eyes."

show caz smirking onlayer screens

C "Happy birthday~"

show emily onlayer screens
show ellie excited onlayer screens at shake

"Ellie smiles and does a little wiggle whilst sat on the blanket."

show ellie onlayer screens at scoot_up

E "Is there a birthday cake?"

P "Uhhhh yeah there's a strawberry topped birthday cake for you."

P "And you've got presents, too!"

show emily sheepish onlayer screens

"You look imploringly at Rosie and Caz to help you out."

show ellie flip onlayer screens at scoot_right

E "Yay! What have you got me?"

show rosie stoned onlayer screens at scoot_up

R "Uhhhhh..."

"Rosie holds out her half-smoked joint."

show rosie gremlin onlayer screens at scoot_left

R "Here's your present, kiddo."

show emily relieved onlayer screens
show ellie excited flip onlayer screens
show rosie stoned onlayer screens at scoot_mid_x

"Ellie doesn't miss a beat, and takes it from her with a grin."

show emily onlayer screens

E "Yay! Thank you Rosie, you're so kind."

show ellie onlayer screens at scoot_mid_x

E "A surprise birthday! I'm so glad. It's not even my birthday for a week yet..."

jump pre_ending

# CHOICE C ROSIE ###############################################################

label choice_C_Rosie:

hide screen choice_C
nvl clear

show emily onlayer screens at scoot_up
show ellie onlayer screens at scoot_mid
show rosie stoned onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ rosie_score += 1

$ pizza = True

if rosie_score > 2:
    "Let's be honest, it's been shaping up to be a stoner comedy by now."

    "Might as well commit to an appropriate punchline."
elif rosie_score > 1:
    "You lean the story towards Rosie's stoner comedy tastes again."

    if death:
        show emily sheepish onlayer screens
        "Guess it's kinda weird after literally killing two people, but whatever."

        "We're off the rails now."
else:
    "At the last minute, you chicken out from a different ending, and go with Rosie's idea."

    if death:
        show emily sheepish onlayer screens
        "It feels kinda jarring, but whatever."

        "This story is a lost cause by now."

show emily gendo onlayer screens

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show bg kitchen onlayer background with dissolve

show ellie onlayer screens at faded
show caz onlayer screens at faded
show rosie stoned onlayer screens at faded

P "As you open the door, a bad smell hits your nose and you reel backwards a step."

P "The kitchen is filled with black smoke, spilling out in clouds from the edge of the oven door."

show rosie stoned onlayer screens at shown

R "Awh dang."

show rosie stoned onlayer screens at faded

P "You cross the kitchen, wafting smoke away from your face, and pull open the oven door."

P "Inside is a gory mess; the blackened remains of what was once a pizza, now charred to a crisp."

show rosie skeptical onlayer screens at shown

R "Nooo..."

show ellie pouting flip onlayer screens at scoot_right
show emily onlayer screens

$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

E "F in the chat..."

show ellie flip onlayer screens
show rosie stoned onlayer screens at scoot_left
show caz eyeroll onlayer screens at opaque

C "What does that even {i}mean{/i}?"

if death:

    show caz annoyed onlayer screens at scoot_left

    C "Aren't there two people DEAD?"

    show rosie gremlin onlayer screens at scoot_up

    R "They - they - they died before they could eat their pizza!"

    R "This is so sad!"

    show ellie flip onlayer screens at scoot_up
    show rosie stoned onlayer screens

    E "It's so sad!"

show rosie laughing onlayer screens at scoot_mid_y
show ellie flip excited onlayer screens at scoot_mid_y
show emily satisfied onlayer screens
show caz eyeroll onlayer screens

"Rosie breaks down into laughter, passing the joint to Ellie to hold as she cackles."

show caz smirking onlayer screens

"Caroline rolls her eyes, but you catch a glimpse of her smiling." 

show emily relieved onlayer screens
$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

P "..."

show emily gendo onlayer screens
show rosie onlayer screens
show ellie flip onlayer screens

P "You cough at the pizza smoke, and hunt around for gloves to take it out."

show caz onlayer screens at scoot_mid

P "With the blackened disk now sat on the counter, the kitchen feels like a crime scene."

$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

if death: 

    show caz eyeroll onlayer screens

    C "The {i}kitchen{/i} feels like a crime scene?"

    show emily sheepish onlayer screens
    show rosie flip gremlin onlayer screens at scoot_mid

    R "Hey, my dead friends are sad, but a pizza is TRAGIC."

    show caz onlayer screens 

    C "You told me off for being sarcastic about them like, two minutes ago."

    show rosie stoned flip onlayer screens

    R "...yeah, well."

elif stoned:
    
    show caz eyeroll onlayer screens

    C "This is why we don't let Jake and Amy come over unattended."

    show emily onlayer screens
    show ellie pouting flip onlayer screens
    show rosie skeptical flip onlayer screens at scoot_mid

    R "Oh like you've never burned food."

    show caz onlayer screens at scoot_left

    C "Not after smoking too much and passing out at someone {i}else's{/i} house, no!"

    show rosie stoned flip onlayer screens
    show caz onlayer screens at scoot_mid

    R "Well, y'know..."

else:

    show caz eyeroll onlayer screens

    C "This is why we don't let Jake and Amy come over unattended."

    show emily onlayer screens
    show ellie pouting flip onlayer screens
    show rosie skeptical flip onlayer screens at scoot_mid

    R "Oh like you've never burned food."

    show ellie flip onlayer screens
    show caz smirking onlayer screens at scoot_left
 
    C "Not after getting distracted cuddling at someone {i}else's{/i} house, no!"

    show rosie stoned flip onlayer screens
    show caz smirking onlayer screens at scoot_mid

    R "Well, y'know..."

show ellie flip onlayer screens
show rosie stoned onlayer screens at scoot_mid
show caz smirking onlayer screens

"Rosie shrugs, and Caroline rolls her eyes."

jump pre_ending

# CHOICE C CAZ #################################################################

label choice_C_Caz:

hide screen choice_C
nvl clear

show emily onlayer screens at scoot_up
show ellie onlayer screens at scoot_mid
show rosie stoned onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ caz_score += 1

if caz_score > 2:
    "Alright, stick to your horror guns."

    "Time for an appropriately slasher-y ending."
elif caz_score > 1:
    "Okay, it was always meant to be a horror, even if you got slightly distracted."

    if death:
        "This is just the logical continuation of the last scene, really."

        "Be a bit weird to veer off after literally killing people."
else:
    "Well, it was always meant to be a horror, so... you drag the story back to its original ending."

    "Feels a bit jarring, but whatever. Here goes a swerve back onto the rails."

show emily gendo onlayer screens

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show bg kitchen onlayer background with dissolve

show ellie onlayer screens at faded
show rosie stoned onlayer screens at faded
show caz onlayer screens at faded

P "As you open the door, you peek around it, umbrella at the ready."

P "There, hunched over another body, a dark shape looms."

show ellie scared onlayer screens at shown

E "Oh no..."

show emily interrupted onlayer screens
show caz sinister onlayer screens at shown

C "Oh yes..."

show ellie hiding onlayer screens at faded
show caz sinister onlayer screens at faded
show emily gendo onlayer screens

P "You only have a moment to take in the body on the floor, the blood seeping out of them - "

show rosie gremlin onlayer screens at scoot_up

$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

R "Who is it? Who's dead??"

show emily interrupted onlayer screens
show rosie stoned onlayer screens
show caz sinister onlayer screens at scoot_up

C "Maybe it's YOU!"

show emily onlayer screens
show ellie flip onlayer screens at opaque
show rosie laughing onlayer screens at scoot_right with vpunch

"Rosie clutches her hands to her chest in mock pain."

show emily relieved onlayer screens
show rosie laughing flip onlayer screens at scoot_mid_y
show caz onlayer screens

R "No! It can't be! Avenge, me, Caz!"

show rosie laughing flip onlayer screens at scoot_away_right
show caz smirking onlayer screens

if death:

    show ellie pouting flip onlayer screens

    E "There's so many people dying..."

    show emily onlayer screens
    show caz reassuring onlayer screens at scoot_left

    C "It {i}is{/i} a horror story."

show emily relieved onlayer screens
show ellie pouting onlayer screens
show caz smirking onlayer screens at scoot_mid

P "..."

show emily gendo onlayer screens
show rosie stoned onlayer screens at scoot_mid_x

$ renpy.music.set_volume(0.0, delay=1, channel='musicb')
$ renpy.music.set_volume(1.0, delay=2, channel='music')

show ellie pouting onlayer screens at faded
show caz onlayer screens at faded

P "The figure looks up from Rosie's bleeding corpse - "

show rosie gremlin onlayer screens at scoot_down

R "Wack."

show rosie stoned onlayer screens at scoot_away

P "-and straightens up with a dark laugh."

P "Their long blade flicks out from their coat, the muddy fabric shapeless and hooded, hiding their face."

P "You brandish your umbrella in front of you, desperately stepping back as they swipe through the air."

show caz sinister onlayer screens at shown

C "Go for the eyes!"

show ellie hiding onlayer screens at shown

E "Run away!"

show ellie hiding onlayer screens at faded
show caz sinister onlayer screens at faded

P "... you jab the umbrella forward, aiming underneath their hood."

show ellie hiding onlayer screens at faded
show caz sinister onlayer screens at faded

P "They bat it away with ease, and approach you one heavy step at a time."

P "You swing your umbrella at them, trying to knock the knife out of their hand."

P "They slash at it and the flimsy end snaps off, half the umbrella dangling in a spidery mess."

show rosie laughing onlayer screens at scoot_down with vpunch

R "Chuck it and run!"

show rosie stoned onlayer screens at scoot_away
show caz smirking onlayer screens at opaque

C "No! Throw it at them and kick their feet out."

show caz onlayer screens at faded

P "You throw the broken umbrella at the attacker, and try to kick their feet."

P "They stumble, and stagger towards you with an outstretched hand."

P "Stepping backwards to avoid them, you back into the sofa and lose your balance."

if death:

    P "Your foot slips on the blood trickling onto the floor."

elif stoned:

    P "Amy briefly reacts in her stupor, letting out a muffled scream."

else:

    P "Jake jerks awake and yells, throwing a cushion at the attacker."

P "You fall backwards and your head hits the floor with a slam."

P "Everything goes black for a second, then you wrench your eyes open again, just in time to see the glint of the knife - "

show ellie hiding onlayer screens at scoot_up

E "Eeeeek okay we're dead let's stop there please..."

$ renpy.music.set_volume(0.0, delay=1, channel='music')
$ renpy.music.set_volume(1.0, delay=2, channel='musicb')

show emily onlayer screens
show rosie stoned onlayer screens at scoot_down
show caz reassuring onlayer screens at scoot_up

C "Awh, it was just getting good."

jump pre_ending

# PRE-ENDING ###################################################################

label pre_ending:

show emily relieved onlayer screens at scoot_mid_y
show caz onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show ellie onlayer screens at scoot_mid

"Your shoulders sag as you reach the end of the story."

show bg campfire onlayer background with dissolve

show emily onlayer screens

$ renpy.music.set_volume(0.0, delay=2, channel='musicb')
play music guitar loop
$ renpy.music.set_volume(1.0, delay=1, channel='music')


show emily onlayer screens

"In front of you, the campfire has dimmed a little whilst you narrated, and you nudge a log further in with your foot."

show emily satisfied onlayer screens

P "Well, that's it. The end."

show ellie excited onlayer screens at scoot_up

"Ellie claps excitedly for a few seconds, beaming at you."

play musicb campfire loop fadein 0.5
$ renpy.music.set_volume(1.0, delay=1, channel='musicb')

show rosie stoned onlayer screens at scoot_up

"Rosie raises her joint in applause."

show caz smirking onlayer screens at scoot_up

"Caz raises her mug of tea in appreciation."

if ellie_score == 3:

    jump ending_Ellie

elif rosie_score == 3:

    jump ending_Rosie

elif caz_score == 3:

    jump ending_Caz

else:

    jump ending_mix

# ELLIE ENDING #################################################################

label ending_Ellie:

show ellie onlayer screens

E "That was fun! I'm glad you put in a load of cute things for me."

show caz onlayer screens

C "It was a bit... out of place, amongst all the narration."

show emily onlayer screens
show caz onlayer screens
show rosie stoned onlayer screens

"Rosie shrugs, not really agreeing with either of them."

R "It was alright. Who's got the snacks?"

show caz smirking onlayer screens
show emily sheepish onlayer screens

C "They're in the tent, away from the ants."

show caz smirking onlayer screens
show rosie gremlin flip onlayer screens

R "Sick."

show emily onlayer screens
show rosie gremlin flip onlayer screens at scoot_away_right

"Rosie starts to crawl over to the tent to fetch her biscuits."

show caz onlayer screens

"Caz rubs her hands together to warm them up."

show emily satisfied onlayer screens
show ellie onlayer screens at scoot_up

E "Well, I liked it, [Emily]. It was sweet."

show ellie pouting onlayer screens at scoot_mid
show caz reassuring onlayer screens

E "I didn't want to hear a scary story before we go to sleep, it's so... spooky out here."

show emily onlayer screens
show rosie gremlin onlayer screens at scoot_mid_x

"She gestures around to the mostly-empty campsite, the wind making only slightly less noise than in the story."

show emily onlayer screens at scoot_right

P "It is a bit creepy, huh."

show rosie gremlin onlayer screens at scoot_up

R "Yeah. Shomething'sh gonna getcha inna night, Elsh."

show emily interrupted onlayer screens
show ellie hiding flip onlayer screens at scoot_left
show caz onlayer screens at scoot_up

C "Don't speak with your mouth full, dear."

show emily onlayer screens
show ellie pouting flip onlayer screens
show rosie stoned onlayer screens at scoot_mid
show caz smirking onlayer screens at scoot_mid

"Rosie rolls her eyes and lays back down on the blanket, looking up at the stars."

show rosie gremlin flip onlayer screens at scoot_right
show caz onlayer screens

R "Whatever, mom."

show emily satisfied onlayer screens
show ellie flip onlayer screens
show rosie stoned flip onlayer screens
show caz annoyed onlayer screens

C "Don't call me - "

show emily onlayer screens
show rosie onlayer screens at scoot_mid
show caz eyeroll onlayer screens

R "Hey, [Emily], you wanna put more jokes in the next story?"

show rosie gremlin onlayer screens

R "Gotta balance out sourpuss here."

show rosie stoned onlayer screens at scoot_mid
show caz annoyed onlayer screens at scoot_left with vpunch

C "Oh! You - I'm not sharing the tent with you tonight."

show caz onlayer screens at scoot_up

C "[Emily], you're in the tent. If you want, anyway."

"You can stretch your legs out better in the tent, so that's a plus."

show emily satisfied onlayer screens at scoot_up

P "Yeah, I'm in."

show emily onlayer screens at scoot_mid_y
show rosie gremlin onlayer screens at scoot_up

R "Whatever. I can sleep anywhere. I'll sleep outside."

show ellie pouting flip onlayer screens at scoot_right
show rosie stoned onlayer screens
show caz eyeroll onlayer screens

E "Noooo you'll get cold!"

show ellie flip onlayer screens
show rosie laughing onlayer screens
show caz smirking onlayer screens

R "Nah, I'm {i}warmed{/i} by the cute story birthday party... antics."

show rosie stoned onlayer screens at scoot_left

R "What was with that?"

show rosie stoned onlayer screens
show ellie pouting flip onlayer screens
show caz onlayer screens

E "They were nice!"

show ellie onlayer screens
show rosie onlayer screens

E "I like happy endings..."

show emily satisfied onlayer screens

"You're glad that Ellie liked the story."

show ellie flip onlayer screens
show rosie stoned onlayer screens

"It's nice to see her more cheerful, after being initially nervous about the isolated campsite." 

show ellie excited flip onlayer screens at scoot_up
show rosie gremlin onlayer screens

"As you watch, she beams and shushes Rosie by feeding her another biscuit."

show emily onlayer screens
show ellie excited flip onlayer screens at scoot_away_right
show rosie stoned flip onlayer screens at scoot_away
show caz smirking onlayer screens

"Maybe you could've told the story differently, but it's nice seeing someone get what they wanted."

show emily onlayer screens at scoot_away_right
show caz smirking flip onlayer screens at scoot_away

"..."

show bg black onlayer background with dissolve

E "Ellie ending."

show bg black onlayer overlay with dissolve

return

# ROSIE ENDING #################################################################

label ending_Rosie:

show ellie onlayer screens
show caz onlayer screens

E "That was... funny? It kinda felt just like... average real life..."

show ellie onlayer screens
show caz smirking onlayer screens

C "If you narrated real life like a horror story, maybe."

show rosie laughing onlayer screens
show caz onlayer screens

R "Hey, I thought it was fun! It was like, believeable, innit."

show ellie flip onlayer screens at scoot_right
show rosie stoned onlayer screens

R "Relatable antics. Relatable cast - "

show caz smirking onlayer screens at scoot_left

C "Relatable for some of us, anyway."

show emily relieved onlayer screens
show ellie excited flip onlayer screens
show rosie gremlin flip onlayer screens at scoot_right
show caz eyeroll onlayer screens at scoot_mid_x

"Rosie sticks her tongue out at Caz, and looks around on the ground."

show emily onlayer screens
show ellie flip onlayer screens
show rosie stoned onlayer screens
show caz onlayer screens

R "Hey, who's got the snacks?"

E "They're in the tent."

show rosie gremlin onlayer screens

R "Oh, sick. Snack time."

show rosie gremlin onlayer screens at scoot_away
show caz smirking onlayer screens

"Rosie starts to crawl over to the tent to fetch her biscuits."

"Caz watches her go, then rubs her hands together to warm them up."

show ellie pouting flip onlayer screens at scoot_mid_y
show caz onlayer screens

E "I'm kinda sad about the pizza now."

show ellie pouting flip onlayer screens at scoot_right
show caz smirking onlayer screens at scoot_left

C "It's not that tragic. It's just a fictional pizza."

show ellie flip onlayer screens
show caz reassuring onlayer screens

E "I know... I just like happy endings."

show emily relieved onlayer screens at scoot_right
show caz onlayer screens

P "I'll do a happier story next time for you."

show emily onlayer screens
show ellie onlayer screens at scoot_up

"Ellie beams, then brings her knees up to her chest to hug."

show emily satisfied onlayer screens

E "At least it made me laugh."

show emily onlayer screens
show ellie pouting onlayer screens
show caz reassuring onlayer screens
show rosie gremlin onlayer screens at scoot_left

E "I didn't really want to hear a scary story, it's so... spooky out here."

show ellie pouting onlayer screens at scoot_mid_y

"She gestures around to the mostly-empty campsite, the wind making only slightly less noise than in the story."

show emily relieved onlayer screens

P "It is a bit creepy, huh."

show emily onlayer screens
show caz smirking onlayer screens

C "It's only a campsite. We're basically the only ones here."

show caz reassuring onlayer screens
show ellie hiding onlayer screens

E "That's why it's so creepy! We're all alone..."

show rosie stoned onlayer screens at scoot_mid_y

R "It'sh alright, Elsh. I'll protectch you from monshtersh."

show ellie flip onlayer screens
show rosie gremlin onlayer screens
show caz smirking onlayer screens

C "Don't talk with your mouth full, dear."

show caz onlayer screens

"Rosie rolls her eyes and lays back down on the blanket, patting Ellie on the back."

show ellie onlayer screens at scoot_up
show rosie stoned onlayer screens at scoot_up

R "Hey, [Emily], I liked the jokes. S'good."

show rosie stoned onlayer screens
show emily satisfied onlayer screens

P "Thanks."

show emily onlayer screens
show ellie flip onlayer screens
show rosie gremlin flip onlayer screens at scoot_mid_x
show caz onlayer screens

R "Shame it didn't rub off on Caz, huh."

show emily sheepish onlayer screens
show caz annoyed onlayer screens

C "Oh! You - I'm not sharing the tent with you tonight."

show emily onlayer screens
show ellie onlayer screens
show rosie onlayer screens at scoot_left
show caz eyeroll onlayer screens

R "Whatever. You share with Ellie, I'll take the car with [Emily]."

show emily satisfied onlayer screens
show rosie stoned onlayer screens

R "She likes funny stuff, at least. The skeletons were fun."

show emily onlayer screens

R "Like..."

show rosie skeptical onlayer screens at scoot_mid_x
show ellie flip onlayer screens
show caz onlayer screens

"Her face contorts as she tries to suppress a laugh."

show rosie gremlin onlayer screens

R "Like... humerus..."

show emily relieved onlayer screens
show ellie excited flip onlayer screens
show caz smirking onlayer screens

"Caz groans and Ellie giggles. You can't help but grin at the half-formed joke."

show emily onlayer screens
show ellie flip onlayer screens
show rosie stoned onlayer screens

"However the story went down with the others, Rosie appreciated the stoner comedy, at least."

show caz smirking flip onlayer screens at scoot_away
show ellie flip onlayer screens at scoot_away_right

"It's nice to see her laugh - not that that's difficult usually."

show emily satisfied onlayer screens
show rosie onlayer screens

"Maybe you could've told the story differently, but it's nice seeing someone get what they wanted."

show emily satisfied onlayer screens at scoot_away_right
show rosie onlayer screens at scoot_away_left

"..."

show bg black onlayer background with dissolve

R "Rosie ending."

show bg black onlayer overlay with dissolve

return

# CAZ ENDING ###################################################################

label ending_Caz:

show ellie pouting onlayer screens
show caz onlayer screens

E "That was scary..."

show emily onlayer screens
show ellie pouting onlayer screens
show caz smirking onlayer screens

C "That was great."

show ellie hiding flip onlayer screens at scoot_right

E "But we died! Rosie died!"

show ellie pouting flip onlayer screens
show rosie skeptical flip onlayer screens at scoot_right

R "Harsh, bruh."

show rosie stoned flip onlayer screens at scoot_mid_x
show caz annoyed onlayer screens at scoot_left

C "Don't bruh me. This is why you died."

show ellie scared onlayer screens at scoot_down
show caz eyeroll onlayer screens at scoot_mid_x

"A twig snapping noise comes from the trees nearby, and Ellie jumps."

show ellie hiding onlayer screens at shake

E "Eeek! What was that?!"

show emily gendo onlayer screens at scoot_right

P "It's the slasher. They're {i}real{/i}."

show ellie pouting onlayer screens at scoot_mid_y
show caz reassuring onlayer screens

E "Doooooon't I won't sleep!"

show emily relieved onlayer screens
show rosie gremlin onlayer screens at scoot_left

"Rosie subtly reaches around Ellie's back, and taps her on the shoulder."

show emily interrupted onlayer screens
show rosie laughing onlayer screens at scoot_mid_x
show caz eyeroll onlayer screens
show ellie hiding flip onlayer screens at scoot_left with vpunch

"She shrieks and flails away, then bats Rosie's hand away with a pout."

show rosie stoned onlayer screens at scoot_mid_x
show ellie pouting flip onlayer screens at scoot_mid_y
show caz annoyed onlayer screens at scoot_left

C "Alright, let's not be too mean..."

show rosie skeptical onlayer screens
show caz reassuring onlayer screens

C "We said at the start that campfire stories have to be horror, right?"

show emily onlayer screens
show ellie hiding flip onlayer screens at scoot_right

E "{i}I{/i} said what if they were cute instead..."

show emily relieved onlayer screens
show rosie gremlin onlayer screens at scoot_left
show caz smirking onlayer screens

R "You're cute."

show rosie stoned onlayer screens
show ellie pouting flip onlayer screens at scoot_up

E "Shush. Go get me a biscuit for being mean."

show rosie gremlin onlayer screens

R "Now THAT'S an idea."

show emily onlayer screens
show rosie stoned flip onlayer screens at scoot_mid_x
show caz onlayer screens

R "...where are they?"

show ellie pouting flip onlayer screens at scoot_mid_x
show caz smirking onlayer screens

C "They're in the tent."

show rosie stoned onlayer screens at scoot_away_left

"Rosie crawls away from Ellie, who shrinks into a ball and hugs her legs."

show ellie hiding flip onlayer screens at scoot_mid_y

E "I'm all scared now..."

show emily relieved onlayer screens
show ellie hiding flip onlayer screens at scoot_left

P "Sorry, Ellie. There's no slasher really."

show emily onlayer screens
show ellie onlayer screens
show rosie stoned onlayer screens at scoot_mid_x

"She sniffs and smiles thinly at you."

show emily satisfied onlayer screens
show ellie flip onlayer screens
show caz reassuring onlayer screens

C "Well, I enjoyed the story."

show emily satisfied onlayer screens

C "Could've used less interruptions to really build the mood, but it was fun."

show rosie gremlin flip onlayer screens at scoot_down

R "Could've ushed more jokesh."

show emily onlayer screens
show rosie gremlin flip onlayer screens at scoot_up
show caz annoyed onlayer screens

C "Don't talk with your mouth full, dear."

show ellie pouting flip onlayer screens at scoot_right
show rosie onlayer screens at scoot_left
show caz eyeroll onlayer screens

"Rosie sticks her biscuit-coated tongue out at Caz, and passes the pack to Ellie."

show ellie flip onlayer screens at scoot_left
show rosie skeptical onlayer screens

R "Whatever. [Emily], you gotta throw in more jokes next time, they're like, the best bit in horror."

show emily relieved onlayer screens
show rosie stoned onlayer screens
show caz annoyed onlayer screens

C "They're not. The {i}horror{/i} bit is."

show emily onlayer screens
show rosie gremlin flip onlayer screens at scoot_right
show caz eyeroll onlayer screens at scoot_mid_x

"The two of them start to bicker, whilst Ellie eats biscuits quietly and watches them."

show rosie laughing flip onlayer screens at scoot_mid_x
show caz annoyed onlayer screens at scoot_left

"It's nice to see Caroline animated about the story."

show emily relieved onlayer screens at scoot_mid_x
show ellie onlayer screens
show caz eyeroll flip onlayer screens at scoot_away
show rosie gremlin flip onlayer screens at scoot_away_right

"Secretly, you're glad you had the chance to tell a slasher story; the campfire setting just feels right."

show emily satisfied onlayer screens
show ellie onlayer screens at scoot_up

"Maybe you could've told the story differently, but at least you and Caroline enjoyed it."

show emily onlayer screens at scoot_away_right
show ellie flip onlayer screens at scoot_away

"..."

show bg black onlayer background with dissolve

C "Caroline ending"

show bg black onlayer overlay with dissolve

return

# MIXED ENDING #################################################################

label ending_mix:

show ellie pouting onlayer screens

E "That was... ummm..."

show emily onlayer screens
show rosie skeptical onlayer screens

R "Bit of a change in tone."

show caz reassuring onlayer screens

C "A bit, yes."

if ellie_score == caz_score: ####################### equal results

    show ellie onlayer screens
    show rosie stoned onlayer screens
    show caz smirking onlayer screens

    C "Something for each of us, I suppose."

    if death: ##### Caz middle

        show caz smirking onlayer screens

        C "An impressively compromised story."

        show emily sheepish onlayer screens
        show rosie skeptical onlayer screens

        R "Yeah, a cute scene, a funny scene, and a dual fuckin' murder."

        show ellie flip onlayer screens at scoot_right
        show caz onlayer screens

        E "The three elements..."

        show emily relieved onlayer screens
        show rosie stoned onlayer screens at scoot_left

        R "Gasp! Jake and Amy were killed by a knife-bender!"

        show emily onlayer screens

        if pizza:
            #### Ellie -> Caz -> Rosie

            show rosie gremlin onlayer screens

            R "And worse, a pizza was murdered, too..."

            show ellie excited flip onlayer screens

            E "So sad..."

            show rosie laughing onlayer screens

            R "So sad!"

            show ellie flip onlayer screens
            show rosie onlayer screens
            show caz smirking onlayer screens at scoot_left

            C "Sadder than your two friends getting stabbed?"

            show rosie gremlin flip onlayer screens

            R "They'd be sad about the pizza too!"

        else:
            #### Rosie -> Caz -> Ellie

            show ellie pouting onlayer screens at scoot_mid_x

            E "But it wasn't a murder! It was fake blood, right?"

            show emily sheepish onlayer screens
            show caz eyeroll onlayer screens at scoot_left

            C "That was totally a cop-out."

            show emily onlayer screens
            show ellie hiding flip onlayer screens

            E "Noooo it was a surprise so I didn't find out about the party..."

            show emily interrupted onlayer screens
            show caz onlayer screens
            show rosie skeptical onlayer screens

            R "..."

            show rosie gremlin onlayer screens
            show caz smirking onlayer screens

            R "It was definitely a cop-out, lol."

            show emily sheepish onlayer screens

            "Yeah, it definitely was."

    elif stoned: ###### Rosie middle

        show rosie skeptical onlayer screens

        R "Yeah, a cute scene, a funny scene, but then a creepy guy with a knife."

        show ellie pouting flip onlayer screens at scoot_right
        show caz onlayer screens

        E "I mean... I've been afraid of killers when stoned..."

        show rosie stoned onlayer screens at scoot_left
        show caz smirking onlayer screens

        R "Yeah, guess it's accurate."

        show ellie excited onlayer screens at scoot_mid_x
        show rosie onlayer screens

        if kitty:
            #### Ellie -> Rosie -> Caz

            E "I'm glad we saw a kitty though..."

            show ellie excited onlayer screens
            show rosie gremlin onlayer screens

            R "Kinda balanced out by the {i}getting murdered{/i}."

            show caz eyeroll onlayer screens

            C "Oh come on, the tone was setting it up."

            show ellie pouting flip onlayer screens
            show caz eyeroll onlayer screens
            show rosie skeptical flip onlayer screens at scoot_mid_x

            R "See a kitty, see your stoned friends, {i}get killed by a knife guy??!{/i}"

            show emily sheepish onlayer screens

            "You do have to admit, it kinda came out of nowhere."

            show emily relieved onlayer screens at scoot_right 
            show ellie onlayer screens
            show rosie stoned onlayer screens
            show caz onlayer screens

            P "I was trying to get back on track..."

        else:
            #### Caz -> Rosie -> Ellie

            E "But I got a lovely birthday party!"

            show rosie laughing onlayer screens
            show caz onlayer screens

            R "Yeah. A surprise!"

            show rosie skeptical onlayer screens

            R "But what was with that knife guy outside..."

            show caz smirking onlayer screens at scoot_left

            C "This was simply the setup, of course."

            show ellie pouting flip onlayer screens
            show rosie stoned flip onlayer screens
            show caz sinister onlayer screens

            C "For a grisly birthday-party slasher murder..."

            show ellie hiding flip onlayer screens
            
            E "Noooooo they were just..."

            show emily sheepish onlayer screens at scoot_right
            show caz onlayer screens

            P "Bringing the knife to cut the cake?"

            show ellie pouting onlayer screens
            show rosie skeptical onlayer screens at scoot_mid_x
            show caz eyeroll onlayer screens at scoot_mid_x
            
            "Nobody looks convinced by that."

            show ellie excited onlayer screens

            E "...yeah..."

    else: ###### Ellie middle

        show rosie skeptical onlayer screens

        R "Yeah, a cute couple oblivious to the horror around them..."

        show ellie pouting flip onlayer screens at scoot_right
        show caz onlayer screens

        E "Well... I've been like that before..."

        show rosie stoned onlayer screens at scoot_left

        R "You've ignored a {i}creepy guy with a knife{/i} whilst cuddling?"

        show caz smirking onlayer screens at scoot_left

        C "Really sets the mood, doesn't it."

        if pizza:
        ##### Caz -> Ellie -> Rosie

            show caz onlayer screens
            show rosie gremlin onlayer screens

            R "God, what carnage... what horror..."

            show caz eyeroll onlayer screens

            C "You're talking about the pizza, aren't you."

            show caz onlayer screens
            show ellie flip onlayer screens

            E "So sad..."

            show rosie laughing onlayer screens

            R "So sad!"

            show caz annoyed onlayer screens

            C "So what was with the creepy knife guy outside?"

            show emily sheepish onlayer screens at scoot_right
            show ellie onlayer screens
            show rosie stoned onlayer screens
            show caz onlayer screens

            P "Uhhh..."

            show emily sheepish onlayer screens at scoot_mid_x

            R "He murdered the pizza!"

            show emily satisfied onlayer screens
            show ellie hiding flip onlayer screens

            E "Oh no!"

            show ellie onlayer screens
            show rosie laughing onlayer screens

            R "Oh no!"

            show caz eyeroll onlayer screens

            "Caz looks unimpressed."

        else:
        ###### Rosie -> Ellie -> Caz

            show rosie stoned flip onlayer screens at scoot_mid_x
            show caz annoyed onlayer screens

            R "Yeah, well, your ignorance led to my {i}death{/i}."

            show rosie gremlin flip onlayer screens
            show ellie hiding flip onlayer screens
            show caz onlayer screens

            E "And ours!"

            show rosie skeptical onlayer screens

            R "Yeah! So much death outta nowhere! Talk about no foreshadowing!"

            show caz eyeroll onlayer screens

            C "Oh come on, the tone was setting it up."

            show ellie pouting flip onlayer screens
            show rosie stoned flip onlayer screens
            show caz onlayer screens

            R "See a creepy skeleton, see your friends cuddling, {i}get killed by a knife guy??!{/i}"

            show emily sheepish onlayer screens
            show ellie flip onlayer screens

            "You do have to admit, it kinda came out of nowhere."

            show emily sheepish onlayer screens at scoot_right

            P "I was trying to get back on track..."

            show ellie pouting onlayer screens
            show rosie skeptical onlayer screens
            show caz reassuring onlayer screens

            "Everyone looks unimpressed."

elif ellie_score == 2: ####################### ellie majority

    show ellie onlayer screens
    show rosie onlayer screens
    show caz onlayer screens

    E "I liked that it was mostly cute..."

    if not kitty:

        show rosie stoned onlayer screens at scoot_left

        R "Yeah, you got a cute cuddly couple and a birthday."

        show ellie flip onlayer screens

        E "It was nice! I didn't want to hear a scary story before we go to sleep."

        show ellie pouting flip onlayer screens

        E "It's so... spooky out here."

        show caz reassuring onlayer screens

        "She gestures around to the mostly-empty campsite, the wind making only slightly less noise than in the story."

        if rosie_score == 1: ####### Rosie -> Ellie -> Ellie

            show rosie gremlin onlayer screens

            R "Just don't think about those spooooooky plastic skeletons."

            show rosie stoned onlayer screens
            show caz smirking onlayer screens at scoot_left

            C "Who puts them up for {i}birthdays{/i}?"

            show rosie laughing flip onlayer screens at scoot_mid_x

            R "Spooky people! Spooky birthdays!"

            show rosie stoned flip onlayer screens
            show caz annoyed onlayer screens

            C "But it's August!"

            show caz onlayer screens
            show ellie pouting flip onlayer screens

            E "And I'm not spooky, either..."

            show ellie pouting onlayer screens at scoot_mid_x
            show emily sheepish onlayer screens at scoot_right

            P "Yeah, they were... a bit out of place, I guess."

        if caz_score == 1: ####### Caz -> Ellie -> Ellie

            show rosie gremlin onlayer screens

            R "Just don't think about the creepy knife guy outside."

            show rosie stoned onlayer screens
            show ellie hiding flip onlayer screens

            E "...well NOW I'm thinking about them!"

            show emily sheepish onlayer screens at scoot_right
            show ellie hiding flip onlayer screens
            show rosie skeptical onlayer screens

            P "I guess that was... uhhh..."

            show ellie pouting flip onlayer screens
            show caz smirking onlayer screens

            C "It was simply the setup, of course."

            show emily onlayer screens
            show rosie stoned flip onlayer screens
            show caz sinister onlayer screens at scoot_left

            C "For a grisly birthday-party slasher murder!"

            show ellie hiding flip onlayer screens
            show caz sinister onlayer screens

            E "Noooooo they were just... umm..."

            show emily onlayer screens
            show ellie hiding flip onlayer screens
            show rosie gremlin onlayer screens

            R "Bringing the knife to cut the cake?"

            show emily interrupted onlayer screens
            show rosie stoned onlayer screens
            show ellie pouting flip onlayer screens
            show caz eyeroll onlayer screens at scoot_mid_x

            "Nobody looks convinced by that."

            show ellie onlayer screens

            E "...yeah..."

    elif stoned: ##### Ellie -> Rosie -> Ellie 

        show rosie stoned onlayer screens at scoot_left

        R "Yeah, you got a nice kitty and a party."

        show ellie flip onlayer screens

        E "It was nice! I didn't want to hear a scary story before we go to sleep."

        show ellie pouting flip onlayer screens

        E "It's so... spooky out here."

        show caz reassuring onlayer screens

        "She gestures around to the mostly-empty campsite, the wind making only slightly less noise than in the story."

        show caz smirking onlayer screens at scoot_left

        C "And you got two people stoned on your sofa."

        show emily sheepish onlayer screens
        show rosie stoned flip onlayer screens

        "You wince at the reminder."

        show ellie flip onlayer screens

        E "Yeah... I guess that's kinda realistic..."

        show emily relieved onlayer screens
        show rosie gremlin flip onlayer screens at scoot_mid_x

        R "It's real life, innit."

        show emily onlayer screens
        show rosie stoned flip onlayer screens
        show caz onlayer screens

        C "Depressingly so."

        show ellie onlayer screens

        E "...yeah..."

    elif pizza: ##### Ellie -> Ellie -> Rosie

        show rosie stoned onlayer screens at scoot_left

        R "Yeah, you got a nice kitty and a cute couple."
        
        show ellie flip onlayer screens
        show rosie stoned onlayer screens
        show caz eyeroll onlayer screens at scoot_left

        C "Then a burnt pizza and a room full of smoke."

        show rosie laughing onlayer screens
        show caz onlayer screens

        R "So sad..."

        show ellie excited flip onlayer screens at scoot_right

        E "So sad..."

        show emily sheepish onlayer screens
        show ellie flip onlayer screens
        show rosie stoned onlayer screens
        show caz smirking onlayer screens

        "You wince at the disappointing ending."

        show ellie flip onlayer screens

        E "It was nice! I didn't want to hear a scary story before we go to sleep."

        show emily onlayer screens
        show ellie hiding onlayer screens at scoot_mid_x

        E "It's so... spooky out here."

        show rosie stoned flip onlayer screens at scoot_mid_x
        show caz reassuring onlayer screens

        R "But now you're going to be haunted at night...."

        show ellie scared onlayer screens
        show caz onlayer screens
        show rosie laughing onlayer screens at scoot_left with vpunch

        R "by the ghost of the pizza!"

        show emily onlayer screens
        show rosie gremlin onlayer screens
        show ellie pouting flip onlayer screens at scoot_left

        E "..."

        show rosie stoned onlayer screens
        show caz annoyed onlayer screens at scoot_mid_x

        C "..."

        show emily sheepish onlayer screens at scoot_right
        show rosie skeptical onlayer screens

        P "..."

        show emily relieved onlayer screens
        show ellie flip onlayer screens
        show rosie stoned onlayer screens
        show caz smirking flip onlayer screens

        R "Yeah okay that wasn't a great joke, was it."

    elif death: ##### Ellie -> Caz -> Ellie

        show rosie stoned onlayer screens at scoot_left

        R "Yeah, you got a cute kitty and a birthday party."

        show caz sinister onlayer screens at scoot_left

        C "And a double-murder."

        show ellie pouting flip onlayer screens at scoot_right

        E "But it wasn't a murder! It was fake blood, right?"

        show emily sheepish onlayer screens
        show rosie onlayer screens
        show caz eyeroll onlayer screens

        C "That was totally a cop-out."

        show emily onlayer screens
        show ellie hiding onlayer screens at scoot_mid_x

        E "Noooo it was a surprise so I didn't find out about the party..."

        show emily relieved onlayer screens
        show caz reassuring onlayer screens
        show rosie skeptical onlayer screens

        R "..."

        show rosie gremlin flip onlayer screens at scoot_mid_x
        show caz smirking onlayer screens

        R "It was definitely a cop-out, lol."

        show emily interrupted onlayer screens

        "Yeah, it definitely was."

        show rosie stoned onlayer screens
        show caz eyeroll flip onlayer screens at scoot_mid_x

        C "Shame you couldn't commit to the party-slasher-horror setup."

        show ellie scared onlayer screens at scoot_left

        E "Noooo that's not what it was! Don't make me worry about a slasher."

        show emily onlayer screens
        show ellie pouting onlayer screens
        show caz reassuring onlayer screens

        E "That wasn't the story, right?"

        show emily sheepish onlayer screens at scoot_right
        show ellie pouting onlayer screens

        P "..."

        P "...no, the murders were, uh. Pretend."

        show rosie skeptical onlayer screens
        show caz onlayer screens

        "Nobody really looks impressed."

    else: ##### Ellie -> Ellie -> Caz

        show rosie stoned onlayer screens

        R "Yeah, you got to see a cute kitty and a nice cuddle."

        show emily interrupted onlayer screens
        show ellie hiding flip onlayer screens at scoot_left
        show rosie laughing onlayer screens at scoot_left with vpunch

        R "Then I fucking DIED."

        show ellie pouting flip onlayer screens
        show rosie gremlin onlayer screens
        show caz annoyed onlayer screens

        C "Oh come on, the tone was setting it up."

        show rosie skeptical flip onlayer screens at scoot_mid_x

        R "What part of that was setting up to {i}get killed by a knife guy??!{/i}"

        show rosie skeptical flip onlayer screens
        show emily sheepish onlayer screens

        "You do have to admit, it kinda came out of nowhere."

        show emily sheepish onlayer screens at scoot_right

        P "I was trying to get back on track..."

        show ellie hiding flip onlayer screens
        show rosie stoned onlayer screens
        show caz reassuring onlayer screens

        E "I wish you hadn't..."

        show rosie gremlin onlayer screens at scoot_left

        R "No cute story for baby Ellie. Just DEATH."

        show ellie pouting onlayer screens at scoot_mid_x
        show rosie stoned onlayer screens
        show caz smirking onlayer screens
        
        "Ellie pouts and you feel a little bad."

        "Caz just rolls her eyes with a smirk."

elif rosie_score == 2: ################ rosie majority

    show ellie onlayer screens
    show caz onlayer screens
    show rosie onlayer screens
    
    R "I liked that it was mostly kinda funny."

    show caz smirking onlayer screens

    C "A regular stoner comedy."

    show rosie stoned flip onlayer screens at scoot_right
    show ellie flip onlayer screens

    R "Yeah! Right!"

    show rosie skeptical flip onlayer screens

    R "Just..."

    if not stoned:

        show rosie stoned onlayer screens

        R "Without anyone actually getting stoned."

        show emily sheepish onlayer screens
        show caz onlayer screens

        "Woops..."

        show ellie pouting flip onlayer screens

        E "Yeah..."

        if ellie_score == 1: ####### R E R

            show ellie flip onlayer screens at scoot_right
            show rosie onlayer screens

            E "I mean, there was a cute couple!"

            show emily onlayer screens
            show caz eyeroll onlayer screens

            C "If it was Jake and Amy, they probably {i}were{/i} stoned. They usually are."

            show rosie stoned flip onlayer screens
            show caz onlayer screens

            R "Yeah! guess it was just, like... implied..."

            show emily sheepish onlayer screens at scoot_right

            P "Right. Yeah. Implied."

            show ellie pouting onlayer screens
            show rosie skeptical onlayer screens

            R "..."

            C "Actually, it's kind of depressing, isn't it?"

            show emily relieved onlayer screens
            show caz eyeroll onlayer screens
            show rosie flip onlayer screens
            show ellie flip onlayer screens

            C "You run into some halloween decorations outside, in {i}August{/i}..."

            show emily onlayer screens
            show rosie stoned flip onlayer screens
            show caz smirking onlayer screens

            C "Then go in to find your friends made out too much and fell asleep and burned a pizza."

            show ellie pouting onlayer screens

            E "..."

            show rosie skeptical onlayer screens

            R "..."

            show emily sheepish onlayer screens

            P "...I guess that wasn't a super exciting narrative, was it..."

        else: ###### R C R

            show rosie skeptical onlayer screens

            R "Yeah, they just fucking... died..."

            show emily onlayer screens
            show caz eyeroll onlayer screens

            C "If it was Jake and Amy, they probably {i}were{/i} stoned, beforehand. They usually are."

            show ellie flip onlayer screens
            show rosie stoned flip onlayer screens
            show caz onlayer screens

            R "Yeah! guess it was just, like... implied..."

            show rosie gremlin onlayer screens at scoot_mid_x

            R "Impldied."

            show emily interrupted onlayer screens
            show ellie excited flip onlayer screens
            show caz annoyed onlayer screens

            "Ellie giggles at the mashed pronunciation."

            show emily relieved onlayer screens
            show rosie stoned onlayer screens
            show caz smirking onlayer screens

            C "It's like an anti-drugs advert."

            show emily sheepish onlayer screens
            show ellie flip onlayer screens
            show rosie stoned flip onlayer screens
            show caz smirking onlayer screens
            
            "Woops..."

            show caz eyeroll onlayer screens

            C "Don't do drugs, kids! You'll get killed by a knife murderer!"

            show emily relieved onlayer screens
            show rosie gremlin flip onlayer screens
            show caz smirking onlayer screens

            R "And burn your pizza!"

            show ellie excited flip onlayer screens at scoot_right

            E "So sad!"

            show rosie laughing onlayer screens at scoot_left

            R "So sad!"

            P "..."

    elif not pizza:

        show rosie skeptical onlayer screens

        R "With a kinda leftfield ending..."

        show emily sheepish onlayer screens

        "Woops..."

        show ellie pouting flip onlayer screens

        E "Yeah..."

        if ellie_score == 1: ###### R R E

            show emily relieved onlayer screens
            show ellie flip onlayer screens at scoot_right

            E "I mean... it was kinda cute to go from comedy to a fun party..."

            show ellie flip onlayer screens
            show rosie onlayer screens

            E "It was nice! I didn't want to hear a scary story before we go to sleep."

            show emily onlayer screens
            show ellie pouting flip onlayer screens

            E "It's so... spooky out here."

            show caz reassuring onlayer screens

            "She gestures around to the mostly-empty campsite, the wind making only slightly less noise than in the story."

            show caz smirking onlayer screens

            C "So you get a birthday party, that's happening whilst two people are stoned on your sofa."

            show emily sheepish onlayer screens
            show ellie flip onlayer screens
            show rosie stoned onlayer screens

            E "Yeah... I guess that's kinda realistic..."

            show emily relieved onlayer screens
            show rosie gremlin flip onlayer screens at scoot_mid_x

            R "It's real life, innit."

            show rosie stoned flip onlayer screens
            show caz eyeroll onlayer screens

            C "Depressingly so."

            show emily sheepish onlayer screens at scoot_right

            P "..."

        else:  ######## R R C

            show rosie skeptical onlayer screens at scoot_mid_x

            R "Yeah, I just fucking... died..."

            show ellie hiding flip onlayer screens at scoot_right

            E "So did we! Or... whoever's meant to be the character..."

            show emily relieved onlayer screens

            "It was kinda muddled as to who the protagonist was..."

            show caz onlayer screens at scoot_left

            C "I thought it was alright."

            show emily onlayer screens
            show ellie pouting flip onlayer screens
            show rosie laughing flip onlayer screens at scoot_left

            R "It was so out of nowhere!"

            show rosie stoned flip onlayer screens
            show caz annoyed onlayer screens

            C "It was a classic one-two-three misdirection."

            show rosie stoned flip onlayer screens
            show caz onlayer screens

            C "Setup, repeat, twist."

            show emily sheepish onlayer screens at scoot_right

            P "Uhhh yeah that's what - "

            show rosie skeptical flip onlayer screens at scoot_mid_x

            R "Oh come on, it felt like an anti-drugs advert."

            show emily onlayer screens
            show caz smirking onlayer screens at scoot_mid_x

            "Caz laughs suddenly, and pats her thigh in amusement."

            show caz sinister onlayer screens

            C "Don't do drugs, kids! You'll get killed by a knife murderer!"

            show ellie pouting flip onlayer screens
            show rosie stoned flip onlayer screens at scoot_left

            E "But the protagonist didn't, did they? Whoever we were..."

            show caz onlayer screens

            C "...I guess not."

            show caz onlayer screens
            show rosie gremlin flip onlayer screens at scoot_mid_x

            R "Don't be in proximity to drugs?"

            show rosie stoned flip onlayer screens
            show caz smirking onlayer screens

            C "Doesn't really work, does it..."

            show emily sheepish onlayer screens

            P "..."

    else:

        show emily sheepish onlayer screens
        show ellie pouting flip onlayer screens
        show rosie skeptical onlayer screens at scoot_mid_x

        R "Kinda started slightly a bit clunkily..."

        show caz onlayer screens at scoot_left

        C "What, you mean the ominous narration?"

        if ellie_score == 1: ##### E R R

            show emily relieved onlayer screens
            show rosie gremlin flip onlayer screens

            R "No, like, the cat..."

            show ellie hiding flip onlayer screens at scoot_right

            E "The kitty was nice!"

            show emily onlayer screens
            show ellie flip onlayer screens
            show rosie onlayer screens

            E "Don't you like saying hi to a cat?"

            show rosie skeptical onlayer screens

            R "I mean yeah totally. But it's a weird narrative, innit?"

            show ellie pouting flip onlayer screens
            show rosie stoned onlayer screens
            show caz smirking flip onlayer screens at scoot_mid_x

            C "Pet a cat, see your stoned friends, take a burnt pizza out the oven?"

            show emily sheepish onlayer screens at scoot_right

            P "..."

            show ellie flip onlayer screens
            show caz onlayer screens

            E "It just sounds like a generic day..."

            show emily relieved onlayer screens
            show rosie onlayer screens

            R "Yeah, dang."

            "You admit to yourself that it wasn't the most gripping story..."

        else: #C R R

            show emily onlayer screens
            show rosie stoned flip onlayer screens

            R "No, like, the fucking... knife guy hanging around."

            show rosie gremlin onlayer screens at scoot_left
            show caz eyeroll flip onlayer screens

            R "What was with that??"

            show ellie hiding onlayer screens at scoot_right
            show rosie stoned onlayer screens

            E "It was scary..."

            show emily relieved onlayer screens at scoot_right
            show ellie pouting onlayer screens
            show caz reassuring onlayer screens

            "It {i}was{/i} a bit out of place..."

            show ellie onlayer screens
            show caz sinister onlayer screens

            C "It's foreshadowing the death of the pizza."

            show emily interrupted onlayer screens
            show ellie excited onlayer screens
            show rosie skeptical flip onlayer screens at scoot_mid_x

            R "That wasn't {i}stabbed{/i} though."

            show ellie onlayer screens
            show rosie stoned flip onlayer screens
            show caz smirking onlayer screens

            C "Foreshadowing the abstract concept of death."

            show emily onlayer screens
            show ellie onlayer screens at scoot_mid_x
            show caz onlayer screens

            E "Pizza death..."

            show emily relieved onlayer screens
            show ellie onlayer screens
            show rosie onlayer screens
            show caz reassuring onlayer screens

            P "..."

            show ellie excited flip onlayer screens at scoot_right
            show caz smirking onlayer screens

            E "So sad..."

            show rosie laughing onlayer screens at scoot_left

            R "So sad..."

elif caz_score == 2: ################# caz majority

    show rosie onlayer screens
    show caz onlayer screens at scoot_left

    C "I liked most of it."

    show caz sinister onlayer screens

    C "Nearly a solid slasher narrative."

    show caz onlayer screens

    if ellie_score == 1:

        show ellie hiding onlayer screens

        E "Yeah..."

        show ellie onlayer screens

        E "But at least it had a little cute moment!"

        if kitty: ##### E C C

            show rosie stoned onlayer screens at scoot_left

            R "Oh, the cat?"

            show rosie stoned onlayer screens
            show ellie flip onlayer screens

            E "Yeah!"

            show ellie pouting flip onlayer screens

            E "We got to see a cat before everyone died..."

            show rosie gremlin flip onlayer screens at scoot_mid_x

            R "The dreaded black cat... a bad omen..."

            show emily relieved onlayer screens
            show ellie flip onlayer screens

            "Huh, guess that scene kinda worked in context..."

            show emily onlayer screens
            show caz annoyed onlayer screens

            C "They're not bad omens. They're just cats."

            show rosie flip onlayer screens
            show caz eyeroll flip onlayer screens at scoot_mid_x

            C "They get so much shunning for having black fur..."

            show rosie stoned flip onlayer screens at scoot_right

            R "Oh, Caz, I was {i}joking{/i}."

            show caz annoyed onlayer screens

            C "Hmmph."

            show emily sheepish onlayer screens
            show caz onlayer screens

            P "..."

            show ellie pouting onlayer screens

            E "I hope the cat survived..."

            show emily relieved onlayer screens at scoot_right
            show rosie onlayer screens at scoot_mid_x

            P "I wouldn't kill a cat in a story!"

        elif not death: ###### C E C

            show caz eyeroll flip onlayer screens at scoot_mid_x

            C "You mean Jake and Amy passed out on the sofa."

            show ellie flip onlayer screens at scoot_right
            show caz onlayer screens

            E "Yeah! Having a cuddle..."

            show ellie onlayer screens

            E "It sounds nice."

            show ellie pouting onlayer screens
            show rosie gremlin onlayer screens at scoot_left
            
            R "And then a murderer breaks in!"

            show emily interrupted onlayer screens
            show ellie hiding onlayer screens
            show caz sinister onlayer screens at scoot_left

            C "Blood everywhere as they scream."

            show ellie hiding flip onlayer screens at scoot_mid_x

            "Ellie pouts and shakes her head at the two of them."

            show emily onlayer screens at scoot_right
            show ellie pouting flip onlayer screens
            show rosie stoned onlayer screens
            show caz onlayer screens

            E "It's so back and forth..."

            show ellie pouting flip onlayer screens
            show caz smirking onlayer screens

            C "Everyone knows the couple who make out die in a horror film."

            show rosie skeptical flip onlayer screens at scoot_mid_x

            R "Did they die, though? I thought we did? Or like... whoever the protagonist was."

            show emily sheepish onlayer screens
            show ellie pouting onlayer screens
            show caz onlayer screens

            P "..."

            P "I didn't specify if they died."

            show emily onlayer screens
            show ellie hiding flip onlayer screens at scoot_right
            show rosie stoned onlayer screens

            E "I hope they're not dead."

            show ellie pouting flip onlayer screens
            show rosie onlayer screens at scoot_left

            R "I mean, they're not in real life."

            show caz sinister onlayer screens

            C "Who knows? Could be a slasher at our house right now."

            show emily relieved onlayer screens
            show rosie gremlin onlayer screens
            show ellie hiding onlayer screens at scoot_mid_x

            E "Nooo..."

        else: ###### C C E

            show ellie excited flip onlayer screens at scoot_right

            E "I got a nice birthday party!"

            show rosie stoned onlayer screens at scoot_left

            R "You mean the \"Happy birthday! My friends are dead and there's a knife guy outside laughing at us!\" bit?"

            show emily interrupted onlayer screens
            show ellie pouting flip onlayer screens

            E "But it wasn't a murder! It was fake blood, right?"

            show caz smirking onlayer screens at scoot_left

            C "Yeah. That was totally a cop-out."

            show emily sheepish onlayer screens
            show ellie pouting onlayer screens at scoot_mid_x

            "She glances over at you, unimpressed."

            show ellie hiding flip onlayer screens

            E "Noooo it was a surprise so I didn't find out about the party..."

            show ellie pouting flip onlayer screens
            show rosie stoned onlayer screens

            R "..."

            show emily relieved onlayer screens
            show rosie gremlin onlayer screens

            R "It was definitely a cop-out, lol."

            show rosie flip onlayer screens
            show caz smirking flip onlayer screens at scoot_mid_x

            C "Shame you couldn't commit to the party-slasher-horror setup."

            show caz sinister onlayer screens at scoot_left

            C "Or maybe it's a double-bluff, and next the slasher comes in for real."

            show emily onlayer screens
            show rosie stoned flip onlayer screens
            show caz onlayer screens

            C "That'd be fun."

            show ellie hiding flip onlayer screens

            E "Noooo that's not what it was going to be! Don't make me worry about a slasher."

            show ellie pouting onlayer screens at scoot_left
            show rosie stoned onlayer screens
            show caz smirking onlayer screens

            E "That wasn't the story, right?"

            show emily sheepish onlayer screens
            show rosie stoned flip onlayer screens at scoot_mid_x
            show caz reassuring onlayer screens

            P "..."

            show emily sheepish onlayer screens at scoot_right

            P "...no, the murders were, uh. Pretend."

            show rosie skeptical onlayer screens
            show caz onlayer screens

            "Nobody really looks impressed at that compromise."

    else:

        if pizza:  ###### C C R

            show rosie skeptical flip onlayer screens

            R "Yeah, just derailed by the pizza-murder ending."

            show ellie flip onlayer screens at scoot_right

            E "The saddest part..."

            show emily relieved onlayer screens
            show rosie stoned onlayer screens at scoot_left

            R "So sad..."

            show caz annoyed onlayer screens

            C "Sadder than your two friends getting stabbed?"

            show emily onlayer screens
            show ellie pouting flip onlayer screens
            show rosie gremlin flip onlayer screens at scoot_mid_x

            R "They'd be sad about the pizza too!"

            show ellie flip onlayer screens
            show rosie stoned flip onlayer screens
            show caz onlayer screens

            C "Hmmm."

            show caz smirking onlayer screens

            C "I guess it's a good black comedy twist."

            show ellie onlayer screens
            show emily sheepish onlayer screens
            show caz smirking onlayer screens

            "Yeah, that's totally what it was."

            show emily onlayer screens
            show caz reassuring onlayer screens

            C "A bit anticlimatic though."

            show emily sheepish onlayer screens at scoot_right
            show ellie onlayer screens
            show rosie onlayer screens
            show caz reassuring onlayer screens

            P "Yeah, I guess."

        elif stoned: ##### C R C

            show rosie skeptical flip onlayer screens

            R "How was it? You see a creepy guy, see your stoned friends, then I'm dead?"

            show ellie flip onlayer screens
            show caz smirking onlayer screens

            C "Yeah. Setup, distraction, payoff."

            show rosie stoned flip onlayer screens
            show caz onlayer screens

            C "Shame we don't see what happens to Jake and Amy."

            show ellie pouting flip onlayer screens at scoot_right

            E "Or... whoever's meant to be the character..."

            show emily sheepish onlayer screens

            "It was kinda muddled as to who the protagonist was..."

            C "Yeah. I guess it's like an anti-drugs advert."

            show emily onlayer screens at scoot_right

            P "Uhhh... yeah...?"

            show ellie flip onlayer screens
            show rosie flip onlayer screens
            show caz eyeroll flip onlayer screens at scoot_mid_x

            C "Don't do drugs, kids! You'll wake up to your recording engineer dead by knife!"

            show rosie stoned flip onlayer screens at scoot_right

            R "However will they record their EP without me..."

            show caz smirking onlayer screens

            C "They'll be missing a certain spark, that's for sure."

            show ellie pouting flip onlayer screens

            E "But it's not like {i}we{/i} took any - I mean, the protagonist... whoever they are."

            show rosie stoned onlayer screens

            R "I mean, I probably did. It's implied."

            show rosie gremlin onlayer screens at scoot_mid_x

            R "Heh. Impldied, you could say."

            show emily interrupted onlayer screens
            show ellie excited flip onlayer screens
            show caz onlayer screens

            "Ellie snorts at the bad pun."

            show caz annoyed onlayer screens at scoot_left

            C "God, you probably got knife-murdered because of that level of pun."

            show emily relieved onlayer screens
            show ellie flip onlayer screens
            show rosie stoned flip onlayer screens

            R "Hey, you love my jokes!"

            show caz onlayer screens

            "Caz looks unimpressed."

        else: ###### R C C

            show rosie skeptical flip onlayer screens

            R "What do you mean? It was rock solid, even if I {i}died{/i}."

            show ellie flip onlayer screens
            show caz eyeroll flip onlayer screens at scoot_mid_x

            C "I mean, the sofa death comes out of nowhere."

            show caz onlayer screens

            C "Just a few skeleton jumpscares beforehand."

            show caz onlayer screens
            show rosie stoned flip onlayer screens at scoot_right

            R "That's, like, setting up misdirection, innit."

            show emily relieved onlayer screens

            "You're glad that Rosie is covering for your storytelling..."

            show rosie flip onlayer screens

            R "Funny, too..."

            show emily onlayer screens
            show ellie hiding flip onlayer screens at scoot_right

            E "If you put up jumpscare skeletons this halloween, I'll scream..."

            show ellie pouting flip onlayer screens
            show rosie gremlin onlayer screens at scoot_mid_x

            R "Heh heh heh..."

            show ellie flip onlayer screens
            show rosie flip onlayer screens
            show caz smirking onlayer screens at scoot_left

            C "Really, though, if I was going for a misdirection, I'd have {i}two{/i} of them to really sell it."

            show caz sinister onlayer screens

            C "A skeleton jumpscare, then - I don't know, something else, {i}then{/i} knife murder."

            show emily sheepish onlayer screens
            show ellie flip pouting onlayer screens
            show rosie stoned flip onlayer screens
            show caz onlayer screens

            P "..."

            show emily sheepish onlayer screens at scoot_right

            P "Guess I'll remember that for next time..."

            show emily onlayer screens
            show rosie skeptical onlayer screens at scoot_left

            R "Hey, next storytime, maybe me and the band can {i}survive{/i}? Just a thought."

            show ellie flip onlayer screens
            show emily onlayer screens

            E "Once upon a time, Rosie and the band didn't die. The end, happy ever after."

            show emily relieved onlayer screens
            show rosie laughing onlayer screens
            show caz smirking onlayer screens

            R "Thanks, El, that's perfect."

else: ############### i don't think this should come up?

    nvl clear

    show emily sheepish onlayer screens at scoot_mid_x
    show rosie skeptical onlayer screens at scoot_mid_x
    show ellie onlayer screens at scoot_mid_x
    show caz onlayer screens at scoot_mid_x

    R "That was a fucking mess."

    show caz eyeroll onlayer screens

    C "Indeed. So much so you're seeing text the writer didn't forsee you seeing."

    show ellie pouting flip onlayer screens at scoot_right
    show rosie stoned flip onlayer screens

    E "Awh don't make fun of them..."

    show rosie gremlin onlayer screens

    R "Lol."

    "You can't help but wonder why this happened. And if you should let the developers know?"

    "But broken story or no, perhaps a little Easter Egg like this isn't such a bad thing."

nvl clear

show rosie stoned onlayer screens at scoot_mid_x
show ellie onlayer screens at scoot_mid_x
show caz onlayer screens at scoot_mid_x
show emily onlayer screens at scoot_right

"Rosie blows out a breath and laughs briefly, stubbing her roach into the grass."

show rosie gremlin flip onlayer screens at scoot_right

R "Anyway, storytime over. Where's the snacks..."

show rosie stoned flip onlayer screens
show caz smirking onlayer screens

C "They're in the tent."

show ellie excited flip onlayer screens at scoot_right

E "Ooh, get me some too!"

show ellie excited flip onlayer screens at scoot_mid_y
show rosie stoned onlayer screens at scoot_away_left

"Rosie crawls off to fetch them, leaving Ellie to curl up on the blanket."

show caz onlayer screens
show ellie flip onlayer screens at scoot_away_right

"In her camp chair, Caz leans back and looks at the stars."

show emily relieved onlayer screens

"Your story seems to have... well, at least entertained them a bit."

show emily interrupted onlayer screens

"Maybe you could've told it a bit more consistently..."

"But it seemed like a good idea to try and please everyone."

show caz smirking onlayer screens at scoot_left

"Caz seems to notice you staring frustratedly at the fire, and whistles quietly to get your attention."

show emily onlayer screens
show caz reassuring onlayer screens

C "Hey, [Emily], it wasn't that bad. Trying to appeal to everyone is... admirable, at least."

show emily relieved onlayer screens

P "Thanks..."

show emily satisfied onlayer screens
show caz smirking onlayer screens

P "Thought that counts, right?"

show emily satisfied onlayer screens at invisible
show caz smirking onlayer screens at invisible

"..."

show bg black onlayer background with dissolve

P "Mixed Ending"

show bg black onlayer overlay with dissolve

return