# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# STYLES - Pick one you like by uncommenting it ################################

# Colored text, no names
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

# Ellie
image ellie = "sprite/ellie.png"
image ellie scared = "sprite/ellie_scared.png"
image ellie excited = "sprite/ellie_excited.png"
image ellie pouting = "sprite/ellie_pouting.png"
image ellie hiding = "sprite/ellie_hiding.png"

# Rosie
image rosie = "sprite/rosie.png"
image rosie skeptical = "sprite/rosie_skeptical.png"
image rosie gremlin = "sprite/rosie_gremlin.png"
image rosie laughing = "sprite/rosie_laughing.png"
image rosie stoned = "sprite/rosie_stoned.png"

# Caroline
image caz = "sprite/caz.png"
image caz smirking = "sprite/caz_smirking.png"
image caz eyeroll = "sprite/caz_eyeroll.png"
image caz annoyed = "sprite/caz_annoyed.png"
image caz sinister = "sprite/caz_sinister.png"


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
    ease 0.1 xanchor 0.5
    repeat


## Positions ###################################################################

#transform flip:
#    xzoom -1

#transform unflip:
#    xzoom 1

transform opaque:
    easein 1.0 alpha 1.0

transform faded:
    easein 2.0 alpha 0.2

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
    yanchor 0.5

transform audience_left:
    #xcenter 0.48
    xcenter 0.375
    ycenter 0.66666667
    xanchor 0.5
    yanchor 0.4

transform audience_mid:
    #xcenter 0.66666667
    xcenter 0.625
    ycenter 0.66666667
    xanchor 0.5
    yanchor 0.4

transform audience_right:
    #xcenter 0.85333333
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
    easein 0.4 yanchor 0.0

transform scoot_left:
    easein 0.4 xanchor 0.66666667

transform scoot_right:
    easein 0.4 xanchor 0.33333333

# The game starts here.

label start:

show bg black onlayer background

$ Emily = renpy.input("Content Warnings:\nMild drug use\nSwearing\nDescription of murder\n\n\n\nIf you would like a different name, enter it here. The game will use she/her pronouns for you.\n\n", default='Emily')
$ Emily = Emily.strip()

show bg street onlayer background with dissolve

#"| || ||| |||| ||||| 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0"

show emily onlayer screens at hidden, left
show rosie onlayer screens at hidden, audience_mid
show ellie onlayer screens at hidden, audience_left
show caz onlayer screens at hidden, audience_right

"...everything feels smothered in darkness, just the faintest glow from the moon lighting up the edges of shapes."

"Streetlights flicker and fail as you walk, and the sound of your footsteps echoes in the silence."

"Your phone struggles to cling on to life as you use it to light your way, but as you reach the end of the road the battery gives out."

"It takes a moment for your eyes to adjust. Swaying on your feet, hesitating before soldiering on, you see something out the corner of your eye - "

show ellie scared onlayer screens at opaque, scoot_up

E "Eeek!"

show bg campfire onlayer background with dissolve
show rosie gremlin onlayer screens at opaque, scoot_up
show ellie scared onlayer screens at scoot_mid

R "IT'S A MONSTER, ELLIE! IT'S COMING TO GET YOU!"

show rosie gremlin onlayer screens at scoot_left
show ellie hiding onlayer screens at scoot_down

E "Stop ittttt! You made me jump!"

"Rosie laughs and retrieves her hand after making Ellie jump."

show caz smirking onlayer screens at opaque, scoot_up
show rosie onlayer screens at scoot_mid_x

"Caroline smirks briefly, then waves a hand to shush them."

show emily interrupted onlayer screens at opaque, left
show ellie pouting onlayer screens at scoot_mid
show caz onlayer screens

C "Quiet, girls. Let [Emily] continue, I want to hear what happens."

nvl clear

show emily onlayer screens
show ellie onlayer screens
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

"The three of them settle down, Rosie and Ellie on a blanket and Caroline in the campchair next to it."

"The campfire illuminates their faces with flickering orange light, shadows stark and sinister on otherwise cheerful expressions."

"You clear your throat and continue where you left off."

nvl clear

show bg street onlayer background with dissolve

show emily gendo onlayer screens

P "Okay... so, you see something out the corner of your eye..."

show emily gendo onlayer screens at faded
show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

"Whatever it is, you can't make it out before it disappears."

"Squinting at the darkness, you make your way down the street to the house."

"The wind whines through the trees, plaintive and warning, sending a chill up your spine."

show bg tree onlayer background with dissolve

"When you reach the gate, the outdoor light triggers and illuminates the garden."

"Disappearing behind a tree, you see..."

show ellie excited onlayer screens at shown with vpunch
show emily interrupted onlayer screens at opaque
show rosie onlayer screens at opaque
show caz onlayer screens at opaque

E "A kitty!"

show ellie onlayer screens
show rosie skeptical onlayer screens

R "Hahahah what!? It's not gonna be a cat!"

show rosie onlayer screens

E "Well, what do YOU think it is?"

show ellie onlayer screens

R "If it were me it'd be, like, an old halloween decoration that makes you jump."

show ellie pouting onlayer screens

E "That's so lame!"

show caz eyeroll onlayer screens

C "You're both lame. Clearly this is a horror story."

show caz sinister onlayer screens

C "She's going to say 'A wicked blade flashes in the dark', or something."

show ellie scared onlayer screens

P "..."

nvl clear

show emily onlayer screens

show ellie onlayer screens at scoot_up
show rosie onlayer screens at scoot_up
show caz sinister onlayer screens at scoot_up

show screen choice_A
"""It feels like the girls are trying to lead you towards three different stories...\n
{i}(Click a character's speech bubble to continue){/i}"""

label choice_A_Ellie:

hide screen choice_A
nvl clear

show ellie onlayer screens at scoot_mid 
show rosie onlayer screens at scoot_mid 
show caz onlayer screens at scoot_mid 

$ kitty = True

$ ellie_score += 1

show emily gendo onlayer screens

P "A tail flicks out from the tree..."

show ellie excited onlayer screens with vpunch

E "Yay! Kitty!"

show rosie stoned onlayer screens

R "Oh my god..."

show emily interrupted onlayer screens

P "..."

show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

P "You carefully cross the garden to the tree, and try to coax the cat back out."

show emily onlayer screens at faded

P "Pspspspspspsps..."

P "The flick of a tail appears again, cautious and quick, then a small face peeks out."

show ellie onlayer screens at shown

E "Kitty...."

show ellie onlayer screens at faded

P "The cat is sleek and black, except for a little smudge of white on its nose."

P "It sniffs the air before gingerly stepping forward to let you stroke it."

P "Another gust of wind whistles through the tree, shaking the leaves, and the cat hesitates."

P "It seems apprehensive of the house, and glances at the windows as you scratch behind its ears."

P "Then, there's a noise, and it shrinks back hissing at something over your shoulder."

P "When you turn to look, there's nothing there, and the cat scarpers."

P "You feel a chill run up your spine, and you stand up, alone in the garden, but for the feeling of being watched..."

jump choice_B


label choice_A_Rosie:

hide screen choice_A
nvl clear

show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ rosie_score += 1

P "A shape sways in the wind..."

show emily gendo
show ellie onlayer screens at faded
show rosie stoned onlayer screens
show caz onlayer screens at faded

R "Yesssss."

show rosie onlayer screens at faded

P "Dangling from a tree, the light catches the edge of plastic bones and wires;"

P "the grinning face of a skeleton, hung up for the long month of October."

P "It sways back and forth gently in the wind, arms rattling quietly as the joints click."

P "For a plastic corpse, it's unsettling at first, but then you spot something dangling from its mouth."

P "Someone has taped a joint to its lower jaw."

show rosie laughing onlayer screens at shown

R "Wack. Get it."

show rosie onlayer screens at faded

P "...you go to reach up for it - and hear a noise behind you!"

show rosie skeptical onlayer screens at shown

R "It's a prank!"

P "...you jump as a second skeleton, unseen, starts cackling at you."

show rosie onlayer screens at faded

P "The sound is cheap and tinny, coming from a tiny speaker, the distortion creepy and manic."

P "It turns off after a second, as you move your hand away from whatever infrared things triggered it, but the eye sockets still seem to bore into you."

P "Between the two plastic skeletons, you feel unnerved; the feeling of being watched remains."

P "You feel a chill run up your spine, and the humour of the moment doesn't quite take the edge off the adrenaline."

P "Something makes you feel like you're not alone in the garden..."

jump choice_B

label choice_A_Caz:

hide screen choice_A
nvl clear

show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ caz_score += 1

P "A wicked blade flashes in the dark..."

show emily gendo onlayer screens
show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz sinister onlayer screens

C "Nice."

show caz onlayer screens at faded

P "The glimmer of metal sets your heart beating, and you freeze on the spot as the knife disappears out of sight."

show emily gendo onlayer screens at faded

P "When you can bring yourself to take more steps into the garden, there's nothing to be seen behind the tree."

P "Shapes move in the corners of your vision, and you look around frantically for whatever lurks in the shadows."

P "You shout at the darkness, challenging whoever's there to show themselves."

P "The only reply is the wind brushing through the trees, and the faintest hint of a laugh..."

show caz sinister onlayer screens at shown

C "Heh heh heh..."

show caz onlayer screens at faded

P "The laughter seems to come from different directions, and you feel small and vulnerable stood there in the garden."

P "Clutching your dead phone to your chest, you try and make out anything in the hedges."

P "The laughter stops, and you can't see anything but trees and bushes."

P "The feeling of being watched and taunted sends a shiver up your spine..."

jump choice_B


label choice_B:

hide screen choice_B
nvl clear

show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

"You don't waste any time heading indoors."

"Hopefully it'll feel safer inside; familiar, warm, lockable doors."

"With a last quick check over your shoulder, you open the front door and let yourself in."

"The door closes with a creak - "

show rosie skeptical onlayer screens at shown

R "Oh come on, our door doesn't creak!"

show emily interrupted onlayer screens at shown
show rosie skeptical onlayer screens at scoot_mid
show caz annoyed onlayer screens at shown

C "It does in winter. I have to put wd40 on the hinges."

show rosie skeptical onlayer screens at scoot_up

R "You do?!"

show caz annoyed onlayer screens at scoot_up with vpunch

C "Just because you don't notice, doesn't mean it doesn't get done."

show ellie hiding onlayer screens at opaque

E "The windows stick when it gets cold, too..."

show emily interrupted onlayer screens at scoot_right

P "Ahem..."

show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz annoyed onlayer screens at scoot_mid

"The three trail off quickly and let you keep talking."

P "I didn't say it was our house... it's A house."

show emily interrupted onlayer screens at scoot_mid_x

"It totally is your house you're narrating, though. You keep that quiet."

show emily onlayer screens at left

P "Anyway..."

show emily gendo onlayer screens
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

show caz sinister onlayer screens at opaque

C "They're dead..."

show rosie stoned onlayer screens at opaque

R "Nah, they're super stoned."

show ellie hiding onlayer screens at opaque

E "No! They just fell asleep cuddling."

show emily interrupted onlayer screens

"You start to wonder who's telling this story..."

nvl clear

show emily onlayer screens

show ellie onlayer screens at scoot_up
show rosie onlayer screens at scoot_up
show caz sinister onlayer screens at scoot_up

show screen choice_B
"""Whose idea do you choose?\n
{i}(Click a character's speech bubble to continue){/i}"""


label choice_B_Ellie:

hide screen choice_B
nvl clear

show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ ellie_score += 1

if ellie_score > 1:
    "You glance at Ellie and veer the story towards her tastes again."
else:
    "You glance at Ellie and throw in a scene for her."

show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded
show emily gendo onlayer screens

P "As you get closer to check the bodies, one of them gently snores."

P "Moving around the side of the sofa, you realise it's Jake and Amy - "

show caz eyeroll onlayer screens at scoot_up

C "Ugh, them again."

show emily interrupted onlayer screens
show caz onlayer screens at scoot_mid

P "...they're both asleep, arms wrapped around each other."

show ellie excited onlayer screens at scoot_up

E "Awwwh..."

show ellie pouting onlayer screens

E "I want that..."

show rosie gremlin onlayer screens at scoot_up
show ellie onlayer screens at scoot_mid

R "Lol, gay."

show caz eyeroll onlayer screens at scoot_up

C "I can't believe you say actually 'lol' out loud like that."

show caz onlayer screens at scoot_mid
show emily onlayer screens

P "..."

show emily interrupted onlayer screens

P "You keep quiet so as not to disturb them."

"Everyone shuts up again and listens."

show emily gendo onlayer screens
show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

P "The remains of cups of tea sit on the table, getting cold."

P "The quiet music playing only makes the room feel more still, like a film paused mid-scene."

P "You think about turning the music off, but it's not disrupting anything to leave it as it is."

P "As you stand there, one of them sniffs in their sleep and fidgets."

P "It's kinda cute to watch, but you start to feel a bit voyeuristic."

P "Then you hear another noise."

show ellie hiding onlayer screens at scoot_down

E "Oh no..."

show caz sinister onlayer screens at scoot_up

C "Oh yes."

show caz onlayer screens at scoot_mid

P "A wet sound comes from the kitchen, behind the closed door."

show caz onlayer screens at faded
show ellie onlayer screens at faded

P "The two on the sofa don't react, but that feeling you had outside is back."

P "Like you're not alone - sleeping couple aside, it feels like there's something else."

P "Something waits."

jump choice_C


label choice_B_Rosie:

hide screen choice_B
nvl clear

show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ stoned = True

$ rosie_score += 1

if rosie_score > 1:
    "You look at Rosie, and play along with her ideas again."
else:
    "You look at Rosie, and pick her idea to run with this time."

show emily gendo onlayer screens

P "As you get closer to check the bodies, one of them groans."

show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

P "You spot a bong sat on the floor next to the sofa, and you realise the two prone shapes on the sofa are Jake and Amy, too stoned to function."

show rosie stoned onlayer screens at shown

R "Ayyy, fuckin... that's the life."

show caz annoyed onlayer screens at shown

C "If they stay on the SOFA, anyway."

show emily interrupted onlayer screens

"Rosie sparks up her own joint and laughs."

show rosie skeptical onlayer screens at scoot_up

R "You're not still mad, Caz?"

show caz annoyed onlayer screens at scoot_up
show rosie_skeptical onlayer screens at scoot_mid

C "Yes! It was only three weeks ago! When your band friends come over and get trashed they can pass out in YOUR room next time."

show rosie onlayer screens at scoot_up
show ellie hiding onlayer screens

R "They weren't trashed, they were just stoned is all. Jake doesn't drink."

show rosie onlayer screens at scoot_mid
show caz annoyed onlayer screens at scoot_up

C "They were passed out IN MY BED. NAKED. I don't care what it was from."

show caz annoyed onlayer screens at scoot_mid
show emily sheepish onlayer screens

P "..."

show emily onlayer screens
show ellie hiding onlayer screens at scoot_up

E "I've done that too..."

show ellie onlayer screens at scoot_mid
show caz smirking onlayer screens at scoot_up # TODO: replace with reassuring emote

C "Ellie, dear, you're different, I'm not mad at you."

show caz onlayer screens at scoot_mid
show rosie stoned onlayer screens at scoot_up

R "Dya wanna toke? You'll be less mad."

show rosie stoned onlayer screens at scoot_mid
show emily interrupted onlayer screens at scoot_right

P "Ahem."

show emily interrupted onlayer screens at scoot_mid
show rosie grmelin onlayer screens
show ellie onlayer screens
show caz eyeroll onlayer screens

"The three of them look at you, and Rosie rubs her neck sheepishly."

show rosie stoned onlayer screens at scoot_up

R "Sorry, Em. Uhhhhh Jake and Amy are stoned on the sofa, then what."

show rosie onlayer screens at scoot_mid
show caz onlayer screens
show emily onlayer screens

P "..."

show emily gendo onlayer screens

P "You keep quiet so as not to disturb them."

show emily gendo onlayer screens at faded
show rosie onlayer screens at faded
show ellie onlayer screens at faded
show caz onlayer screens at faded

P "Jake lifts a hand slightly, only just registering your presence, then lets it flop back down."

P "The quiet reggae playing only makes the room feel more still, like a film paused mid-scene."

P "You think about turning the music off, but they're probably enjoying it, even if it's not to your taste."

show caz smirking onlayer screens at shown

C "Hah."

show caz onlayer screens at faded

P "...as you hesitate, you hear another noise behind you."

show ellie hiding at shown

E "Oh no..."

show ellie hiding onlayer screens at scoot_down
show caz sinister onlayer screens at shown

C "Oh yes. Slasher time."

show ellie hiding onlayer screens at faded
show caz onlayer screens at faded

P "...a wet sound comes from the kitchen, behind the closed door."

P "The two on the sofa don't react, but that feeling you had outside is back."

P "Like you're not alone - stoned couple aside, it feels like there's something else."

P "Something waits."

jump choice_C


label choice_B_Caz:

hide screen choice_B
nvl clear

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
show rosie onlayer screens at faded
show caz onlayer screens at faded
show emily gendo onlayer screens

P "You step closer to the sofa, and every step causes a sick feeling in your stomach to rise."

show emily gendo onlayer screens at faded

P "When you can see the figures closer, you gasp and take a step back in shock."

P "Sprawled out on the sofa are the bodies of - "

"You hesitate for a moment, unsure if naming actual people is too weird."

P " - of two friends, their clothes torn and bloodstained, cut up by some vicious knife."

show ellie hiding onlayer screens at shown

E "Eeeek..."

show ellie hiding onlayer screens at scoot_down
show caz onlayer screens at scoot_up

C "Who's 'two friends' meant to be?"

show emily sheepish onlayer screens at shown
show caz onlayer screens at scoot_mid

P "Like, just two friends of yours - "

show rosie stoned onlayer screens at scoot_up

R "Is it me and Ellie?"

show ellie hiding onlayer screens at shake

E "I don't wanna be stabbed!"

show ellie hiding onlayer screens at scoot_down
show emily interrupted onlayer screens

P "Fine, it's Jake and Amy, they came over for band practice and now they're DEAD."

show rosie skeptical onlayer screens at scoot_up

R "...{nw}" 
pause (1.0) 
show rosie stoned onlayer screens 
extend "Grody."

show caz eyeroll onlayer screens at scoot_up
show rosie stoned onlayer screens at scoot_mid

C "Oh, no, Jake and Amy are dead."

show caz eyeroll onlayer screens at scoot_mid
show rosie skeptical onlayer screens at scoot_up

R "Hey, I know you don't like them, but chill with the sarcasm."

show caz annoyed onlayer screens at scoot_up
show rosie skeptical onlayer screens at scoot_mid

C "I don't actually want them dead! But stakes are higher if they're named, right?"

show caz smirking onlayer screens

C "It's not 'oh no generic friend is dead' anymore, it's visceral."

show caz smirking onlayer screens at scoot_mid
show ellie pouting onlayer screens at scoot_mid

E "I'd be sad if they got stabbed."

show emily sheepish onlayer screens

P "..."

show emily interrupted onlayer screens at scoot_right

P "So, your two named friends are dead on the sofa - "

show emily onlayer screens at scoot_mid
show rosie gremlin onlayer screens at scoot_up

R "That's classic Jake and Amy - "

show emily interrupted onlayer screens
show caz eyeroll onlayer screens
show rosie gremlin onlayer screens at scoot_mid

P "..."

show emily gendo onlayer screens

P "You turn away from the grisly scene, horrified, your stomach turning at the sight."

show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded
show emily gendo onlayer at faded

P "Anywhere here, the killer could be waiting, ready to strike again."

P "The stereo plays on in the corner, ignorant of the death in the room as the next dub track queues up."

P "You go to switch it off, but a sound in the kitchen stops you, and you freeze."

P "Something waits."

jump choice_C

label choice_C:

hide screen choice_C
nvl clear

show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded
show emily gendo onlayer at faded

P "You stare at the kitchen door, a grim sense of foreboding rooting you to the spot."

P "It feels inevitable that you'll have to open it - "

show ellie scared onlayer screens at shown

E "Noo! Run away!"

show emily interrupted onlayer screens at opaque
show ellie scared onlayer screens at scoot_down
show caz sinister onlayer screens at scoot_up

C "Grab a weapon!"

show caz sinister onlayer screens at scoot_mid
show rosie gremlin onlayer screens at scoot_up

R "Fuck it, open the door."

show rosie gremlin onlayer screens at scoot_mid

P "You take a few deep breaths to try and steel yourself."

show emily gendo onlayer screens
show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

P "Looking around, all you can find for a weapon is an umbrella in the corner."

P "You pick it up and weigh it in your hands."

P "It's flimsy, but it's something."

P "You creep closer to the door, and press your ear against it for a moment to listen."

P "It's silent on the other side of the door. Sinisterly so."

P "One hand on the handle, you glance back at the sofa, and swallow."

P "Whatever's in the kitchen, you're facing it on your own."

P "With one quick movement, you snap the handle down and push the door open, to see - "

show bg kitchen onlayer background with dissolve

show caz sinister onlayer screens at scoot_up

C "The killer!"

show caz sinister onlayer screens at scoot_mid
show ellie excited onlayer screens at scoot_up

E "No! A surprise birthday party!"

show ellie excited onlayer screens at scoot_mid
show rosie stoned onlayer screens at scoot_up

R "Nah, a, a, a pizza's on fire!"

show rosie stoned onlayer screens at scoot_mid
show emily interrupted onlayer screens

P "..."

nvl clear

show emily onlayer screens

show ellie excited onlayer screens at scoot_up
show rosie stoned onlayer screens at scoot_up
show caz sinister onlayer screens at scoot_up

show screen choice_C
"""Whose idea do you choose?\n
{i}(Click a character's speech bubble to continue){/i}"""

label choice_C_Ellie:

hide screen choice_C
nvl clear

show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ ellie_score += 1

if ellie_score > 2:
    "Well, you've committed to Ellie's ideas already."

    "Time to follow through with a cute ending."
elif ellie_score > 1:
    "You veer the story towards Ellie's idea for a second time."

    if death:
        "Guess it's kinda weird after literally killing two people, but whatever."

        "We're off the rails now."
else:
    "At the last minute, you chicken out from a different ending, and go with Ellie's idea."

    if death:
        "It feels kinda jarring, but whatever."

        "This story is a lost cause by now."

show emily gendo onlayer screens

P "As you open the door, there's a bang, and you close your eyes in shock."

show ellie onlayer screens at faded
show caz onlayer screens at faded
show rosie onlayer screens at faded

P "You raise the umbrella, and feel something light patter against it."

P "Letting your eyes open again, a shower of confetti falls on you."

show ellie excited onlayer screens at scoot_up with vpunch

E "...!"

P "Rosie yells {i}Surprise! It's your birthday!{/i}"

show ellie excited onlayer screens at scoot_mid
show rosie stoned onlayer screens at scoot_up

R "Uhhhhh surprise! It's your birthday!"

show ellie excited onlayer screens at scoot_up
show rosie stoned onlayer screens at scoot_mid

E "It's my birthday! Yay!"

show ellie excited onlayer screens at scoot_mid

if death:
    show caz onlayer screens at scoot_up

    C "..."

    show caz annoyed onlayer screens 

    C "People are DEAD out there."

    show caz annoyed onlayer screens at scoot_mid

    "You hesitate for a moment, keenly aware of how shambolic this story is getting."

    show emily sheepish onlayer screens

    P "Uhhhhhhhhhh Jake and Amy come up behind you and say {i}Happy birthday!{/i} The blood was fake!"

    show ellie excited onlayer screens at scoot_up

    E "Yay they're not dead!"

else:

    show caz eyeroll onlayer screens at scoot_up

    C "So Jake and Amy are just sleeping through the party, huh?"

    show emily interrupted onlayer screens

    "You hesitate for a moment, trying to retcon it in your head."

    show caz onlayer screens at scoot_mid
    show emily sheepish onlayer screens

    P "Uhhhh they were just lulling you into a false sense of security!"

    P "The two of them emerge behind you and say {i}Happy birthday!{/i}"

show ellie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid
show caz eyeroll onlayer screens at scoot_mid

"Caroline rolls her eyes."

show caz smirking onlayer screens at scoot_up

C "Happy birthday~"

show caz onlayer screens at scoot_mid
show ellie excited onlayer screens at scoot_mid,shake

"Ellie smiles and does a little wiggle whilst sat on the blanket."

show ellie excited onlayer screens at scoot_up

E "Is there a birthday cake?"

show ellie excited onlayer screens at scoot_mid

P "Uhhhh yeah there's a strawberry topped birthday cake for you."

P "And you've got presents, too!"

show emily sheepish onlayer screens

"You look imploringly at Rosie and Caz to help you out."

show ellie excited onlayer screens at scoot_up

E "Yay! What have you got me?"

show ellie excited onlayer screens at scoot_mid
show rosie stoned onlayer screens at scoot_up

R "Uhhhhh..."

"Rosie holds out her half-smoked joint."

show rosie gremlin onlayer screens at scoot_up

R "Here's your present, kiddo."

show rosie gremlin onlayer scrfeens at scoot_mid

"Ellie doesn't miss a beat, and takes it from her with a grin."

show ellie excited onlayer screens at scoot_up

E "Yay! Thank you Rosie, you're so kind."

show ellie onlayer screens at scoot_up

E "A surprise birthday! I'm so glad. It's not even my birthday for a week yet..."

jump pre_ending


label choice_C_Rosie:

hide screen choice_C
nvl clear

show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

$ rosie_score += 1

$ pizza = True

if rosie_score > 2:
    "Let's be honest, it's been shaping up to be a stoner comedy by now."

    "Might as well commit to an appropriate punchline."
elif rosie_score > 1:
    "You lean the story towards Rosie's stoner comedy tastes again."

    if death:
        "Guess it's kinda weird after literally killing two people, but whatever."

        "We're off the rails now."
else:
    "At the last minute, you chicken out from a different ending, and go with Rosie's idea."

    if death:
        "It feels kinda jarring, but whatever."

        "This story is a lost cause by now."

P "As you open the door, a bad smell hits your nose and you reel backwards a step."

P "The kitchen is filled with black smoke, spilling out in clouds from the edge of the oven door."

show rosie skeptical onlayer screens at scoot_up

R "Awh dang."

show rosie skeptical onlayer screens at scoot_mid

P "You cross the kitchen, wafting smoke away from your face, and pull open the oven door."

P "Inside is a gory mess; the blackened remains of what was once a pizza, now charred to a crisp."

show rosie stoned onlayer screens at scoot_up

R "Nooo..."

show rosie stoned onlayer screens at scoot_mid
show ellie pouting onlayer screens at scoot_up

E "F in the chat..."

show ellie onlayer screens at scoot_mid
show caz annoyed onlayer screens at scoot_up
show emily interrupted onlayer screens

C "What does that even {i}mean{/i}?"

if death:

    C "Aren't there two people DEAD?"

    show caz annoyed onlayer screens at scoot_mid
    show rosie gremlin onlayer screens at scoot_up

    R "They - they - they died before they could eat their pizza!"

    show rosie laughing onlayer screens at scoot_up

    R "This is so sad!"

    show rosie laughing onlayer screens at scoot_mid
    show ellie excited onlayer screens at scoot_up

    E "It's so sad!"

show ellie excited onlayer screens at scoot_mid

"Rosie breaks down into laughter, passing the joint to Ellie to hold as she cackles."

show caz smirking onlayer screens

"Caroline rolls her eyes, but you catch a glimpse of her smiling." 

show emily sheepish onlayer screens

P "..."

show emily onlayer screens

P "You cough at the pizza smoke, and hunt around for gloves to take it out."

show emily gendo onlayer screens

P "With the blackened disk now sat on the counter, the kitchen feels like a crime scene."

if death: 

    show caz smirking onlayer screens at scoot_up

    C "The {i}kitchen{/i} feels like a crime scene?"

    show caz smirking onlayer screens at scoot_mid
    show rosie gremlin onlayer screens at scoot_up

    R "Hey, my dead friends are sad, but a pizza is TRAGIC."

    show rosie gremlin onlayer screens at scoot_mid
    show caz annoyed onlayer screens at scoot_up

    C "You told me off for being sarcastic about them like, two minutes ago."

    show caz annoyed onlayer screens at scoot_mid
    show rosie stoned onlayer screens at scoot_up

    R "...yeah, well."

elif stoned:
    
    show caz eyeroll onlayer screens at scoot_up

    C "This is why we don't let Jake and Amy come over unattended."

    show caz eyeroll onlayer screens at scoot_mid
    show rosie skeptical onlayer screens at scoot_up

    R "Oh like you've never burned food."

    show rosie skeptical onlayer screens at scoot_mid
    show caz annoyed onlayer screens at scoot_up

    C "Not after smoking too much and passing out at someone {i}else's{/i} house, no!"

    show caz onlayer screens at scoot_mid
    show rosie stoned onlayer screens at scoot_up

    R "Well, y'know..."

else:

    show caz eyeroll onlayer screens at scoot_up

    C "This is why we don't let Jake and Amy come over unattended."

     show caz eyeroll onlayer screens at scoot_mid
    show rosie skeptical onlayer screens at scoot_up

    R "Oh like you've never burned food."

    show rosie skeptical onlayer screens at scoot_mid
    show caz annoyed onlayer screens at scoot_up
 
    C "Not after getting distracted cuddling at someone {i}else's{/i} house, no!"

    show caz onlayer screens at scoot_mid
    show rosie stoned onlayer screens at scoot_up

    R "Well, y'know..."

show rosie stoned onlayer screens at scoot_mid

"Rosie shrugs, and Caroline rolls her eyes."

jump pre_ending


label choice_C_Caz:

hide screen choice_C
nvl clear

show ellie onlayer screens at scoot_mid
show rosie onlayer screens at scoot_mid
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
show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

P "As you open the door, you peek around it, umbrella at the ready."

P "There, hunched over another body, a dark shape looms."

show ellie scared onlayer screens at opaque

E "Oh no..."

show emily interrupted onlayer screens
show caz sinister onlayer screens at scoot_up

C "Oh yes..."

show caz sinister onlayer screens at scoot_mid
show emily gendo onlayer screens

P "You only have a moment to take in the body on the floor, the blood seeping out of them - "

show rosie gremlin onlayer screens at scoot_up

R "Who is it? Who's dead??"

show rosie gremlin onlayer screens at scoot_mid
show caz smirking onlayer screens at scoot_up
show emily interrupted onlayer screens

C "Maybe it's YOU!"

show caz smirking onlayer screens at scoot_mid

"Rosie clutches her hands to her chest in mock pain."

show rosie laughing onlayer screens at scoot_up with vpunch

R "No! It can't be! Avenge, me, Caz!"

if death:

    show rosie laughing onlayer screens at scoot_mid
    show ellie scared onlayer screens at scoot_up

    E "There's so many people dying..."

    show ellie pouting onlayer screens at scoot_mid
    show caz eyeroll onlayer screens at scoot_up

    C "It {i}is{/i} a horror story."

show rosie stoned onlayer screens at scoot_mid
show ellie onlayer screens at scoot_mid
show caz onlayer screens at scoot_mid

P "..."

show emily gendo onlayer screens
show rosie stoned onlayer screens at faded
show ellie onlayer screens at faded
show caz onlayer screens at faded

P "The figure looks up from Rosie's bleeding corpse - "

show rosie gremlin onlayer screens at shown

R "Wack."

show rosie gremlin onlayer screens at faded

P "-and straightens up with a dark laugh."

P "Their long blade flicks out from their coat, the muddy fabric shapeless and hooded, hiding their face."

P "You brandish your umbrella in front of you, desperately stepping back as they swipe through the air."

show caz sinister onlayer screens at scoot_up

C "Go for the eyes!"

show caz sinister Os at scoot_mid
show ellie hiding onlayer screens at scoot_up

E "Run away!"

show ellie hiding onlayer screens at scoot_mid

P "... you jab the umbrella forward, aiming underneath their hood."

show caz sinister onlayer screens at faded
show ellie hiding onlayer screens at faded

P "They bat it away with ease, and approach you one heavy step at a time."

P "You swing your umbrella at them, trying to knock the knife out of their hand."

P "They slash at it and the flimsy end snaps off, half the umbrella dangling in a spidery mess."

show rosie laughing onlayer screens at scoot_up

R "Chuck it and run!"

show rosie laughing onlayer screens at scoot_mid
show caz smirking onlayer screens at scoot_up

C "No! Throw it at them and kick their feet out."

show caz onlayer screens at scoot_mid

P "You throw the broken umbrella at the attacker, and try to kick their feet."

show rosie onlayer screens at faded
show caz onlayer screens at faded

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

show ellie hiding onlayer screens at scoot_mid
show caz sinister onlayer screens at scoot_up

C "Awh, it was just getting good."

jump pre_ending

label pre_ending:

show caz onlayer screens at faded
show rosie onlayer screens at faded
show ellie onlayer screens at faded

"Your shoulders sag as you reach the end of the story."

show bg campfire onlayer background with dissolve

"In front of you, the campfire has dimmed a little whilst you narrated, and you nudge a log further in with your foot."

show emily satisfied onlayer screens

P "Well, that's it. The end."

show emily onlayer screens
show ellie excited onlayer screens at opaque

"Ellie claps excitedly for a few seconds, beaming at you."

show rosie stoned onlayer screens at opaque

"Rosie raises her joint in applause."

show caz smirking onlayer screens at opaque

"Caz raises her mug of tea in appreciation."

if ellie_score == 3:

    jump ending_Ellie

elif rosie_score == 3:

    jump ending_Rosie

elif caz_score == 3:

    jump ending_Caz

else:

    jump ending_mix

label ending_Ellie:

show ellie onlayer screens at scoot_up

E "That was fun! I'm glad you put in a load of cute things for me."

show emily satisfied onlayer screens
show ellie onlayer screens at scoot_mid
show caz onlayer screens at scoot_up

C "It was a bit... out of place, amongst all the narration."

show caz onlayer screens at scoot_mid
show emily onlayer screens

"Rosie shrugs, not really agreeing with either of them."

show rosie onlayer screens at scoot_up

R "It was alright. Who's got the snacks?"

show rosie onlayer screens at scoot_mid
show caz smirking onlayer screens at scoot_up
show emily sheepish onlayer screens

C "They're in the tent, away from the ants."

show caz smirking onlayer screens at scoot_mid
show rosie stoned onlayer screens at scoot_up

R "Sick."

show rosie stoned onlayer screens at scoot_away

"Rosie starts to crawl over to the tent to fetch her biscuits."

"Caz rubs her hands together to warm them up."

show ellie onlayer screens at scoot_up

E "Well, I liked it, [Emily]. It was sweet."

show ellie pouting onlayer screens
show emily satisfied onlayer screens

E "I didn't want to hear a scary story before we go to sleep, it's so... spooky out here."

"She gestures around to the mostly-empty campsite, the wind making only slightly less noise than in the story."

show ellie pouting onlayer screens at scoot_mid
show emily onlayer screens at scoot_right

P "It is a bit creepy, huh."

show emily onlayer screens at scoot_mid
show rosie gremlin onlayer screens at scoot_left

R "Yeah. Shomething'sh gonna getcha inna night, Elsh."

show caz eyeroll onlayer screens at scoot_up

C "Don't speak with your mouth full, dear."

show rosie skeptical onlayer screens at scoot_mid

"Rosie rolls her eyes and lays back down on the blanket, looking up at the stars."

show rosie skeptical onlayer screens at scoot_up

R "Whatever, mom."

show caz annoyed onlayer screens at scoot_up

C "Don't call me - "

show rosie stoned onlayer screens at scoot_left

R "Hey, [Emily], you wanna put more jokes in the next story?"

show rosie gremlin onlayer screens

R "Gotta balance out sourpuss here."

show rosie gremlin onlayer screens at scoot_mid
show caz annoyed onlayer screens with vpunch

C "Oh! You - I'm not sharing the tent with you tonight."

show caz onlayer screens at scoot_left,scoot_up

C "[Emily], you're in the tent. If you want, anyway."

show caz onlayer screens at scoot_mid

"You can stretch your legs out better in the tent, so that's a plus."

show emily satisfied onlayer screens

P "Yeah, I'm in."

show rosie gremlin onlayer screens at scoot_up

R "Whatever. I can sleep anywhere. I'll sleep outside."

show rosie gremlin onlayer screens at scoot_mid
show ellie pouting onlayer screens at scoot_up

E "Noooo you'll get cold!"

show ellie onlayer screens at scoot_mid
show rosie laughing onlayer screens at scoot_up

R "Nah, I'm {i}warmed{/i} by the cute story birthday party... antics."

show rosie stoned onlayer screens

R "What was with that?"

show rosie stoned onlayer screens at scoot_mid
show ellie pouting onlayer screens at scoot_up

E "They were nice!"

show ellie onlayer screens

E "I like happy endings..."

show ellie onlayer screens at scoot_mid

"You're glad that Ellie liked the story."

show ellie onlayer screens at faded
show rosie onlayer screens at faded
show caz onlayer screens at faded

"It's nice to see her more cheerful, after being initially nervous about the isolated campsite." 

"As you watch, she beams and shushes Rosie by feeding her another biscuit."

"Maybe you could've told the story differently, but it's nice seeing someone get what they wanted."

show emily onlayer screens at faded 

"..."

"Ellie ending."

return

label ending_Rosie:

show ellie 

E "That was... funny? It kinda felt just like... average real life..."

C "If you narrated real life like a horror story, maybe."

R "Hey, I thought it was fun! It was like, believeable, innit."

R "Relatable antics. Relatable cast - "

C "Relatable for some of us, anyway."

"Rosie sticks her tongue out at Caz, and looks around on the ground."

R "Hey, who's got the snacks?"

E "They're in the tent."

R "Oh, sick. Snack time."

"Rosie starts to crawl over to the tent to fetch her biscuits."

"Caz watches her go, then rubs her hands together to warm them up."

E "I'm kinda sad about the pizza now."

C "It's not that tragic. It's just a fictional pizza."

E "I know... I just like happy endings."

P "I'll do a happier story next time for you."

"Ellie beams, then brings her knees up to her chest to hug."

E "At least it made me laugh."

E "I didn't really want to hear a scary story, it's so... spooky out here."

"She gestures around to the mostly-empty campsite, the wind making only slightly less noise than in the story."

P "It is a bit creepy, huh."

C "It's only a campsite. We're basically the only ones here."

E "That's why it's so creepy! We're all alone..."

R "It'sh alright, Elsh. I'll protc you from monshtersh."

C "Don't eat with your mouth full, dear."

"Rosie rolls her eyes and lays back down on the blanket, patting Ellie on the back."

R "Hey, Em, I liked the jokes. S'good."

P "Thanks."

R "Shame it didn't rub off on Caz, huh."

C "Oh! You - I'm not sharing the tent with you tonight."

R "Whatever. You share with Ellie, I'll take the car with Em."

R "She likes funny stuff, at least. The skeletons were fun."

R "Like..."

"Her face contorts as she tries to suppress a laugh."

R "Like... humerus..."

"Caz groans and Ellie giggles. You can't help but grin at the half-formed joke."

"However the story went down with the others, Rosie appreciated the stoner comedy, at least."

"It's nice to see her laugh - not that that's difficult usually."

"Maybe you could've told the story differently, but it's nice seeing someone get what they wanted."

"..."

"Rosie ending."

return

label ending_Caz:

E "That was scary..."

C "That was great."

E "But we died! Rosie died!"

R "Harsh, bruh."

C "Don't bruh me. This is why you died."

"A twig snapping noise comes from the trees nearby, and Ellie jumps."

E "Eeek! What was that?!"

P "It's the slasher. They're {i}real{/i}."

E "Doooooon't I won't sleep!"

"Rosie subtly reaches around Ellie's back, and taps her on the shoulder."

"She shrieks and flails away, then bats Rosie's hand away with a pout."

C "Alright, let's not be too mean..."

C "We said at the start that campfire stories have to be horror, right?"

E "{i}I{/i} said what if they were cute instead..."

R "You're cute."

E "Shush. Go get me a biscuit for being mean."

R "Now THAT'S an idea."

R "...where are they?"

C "They're in the tent."

"Rosie crawls away from Ellie, who shrinks into a ball and hugs her legs."

E "I'm all scared now..."

P "Sorry, Ellie. There's no slasher really."

"She sniffs and smiles thinly at you."

C "Well, I enjoyed the story."

C "Could've used less interruptions to really build the mood, but it was fun."

R "Could've ushed more jokesh."

C "Don't talk with your mouth full, dear."

"Rosie sticks her biscuit-coated tongue out at Caz, and passes the pack to Ellie."

R "Whatever. Em, you gotta throw in more jokes next time, they're like, the best bit in horror."

C "They're not. The {i}horror{/i} bit is."

"The two of them start to bicker, whilst Ellie eats biscuits quietly and watches them."

"It's nice to see Caroline animated about the story."

"Secretly, you're glad you had the chance to tell a slasher story; the campfire setting just feels right."

"Maybe you could've told the story differently, but at least you and Caroline enjoyed it."

"..."

"Caz ending"

return

label ending_mix:

E "That was... ummm..."

R "Bit of a change in tone."

C "A bit, yes."

if ellie_score == caz_score: ####################### equal results

    C "Something for each of us, I suppose."

    if death: ##### Caz middle

        C "An impressively compromised story."

        R "Yeah, a cute scene, a funny scene, and a dual fuckin' murder."

        E "The three elements..."

        R "Gasp! Jake and Amy were killed by a murder-bender!"

        if pizza:

            #### Ellie -> Caz -> Rosie
            R "And worse, a pizza was murdered, too..."

            E "So sad..."

            R "So sad!"

            C "Sadder than your two friends getting stabbed?"

            R "They'd be sad about the pizza too!"

        else:
            #### Rosie -> Caz -> Ellie
            E "But it wasn't a murder! It was fake blood, right?"

            C "That was totally a cop-out."

            E "Noooo it was a surprise so I didn't find out about the party..."

            R "..."

            R "It was definitely a cop-out, lol."

            "Yeah, it definitely was."

    elif stoned: ###### Rosie middle

        R "Yeah, a cute scene, a funny scene, but then a creepy guy with a knife."

        E "I mean... I've been afraid of killers when stoned..."

        R "Yeah, guess it's accurate."

        if kitty:
            #### Ellie -> Rosie -> Caz
            E "I'm glad we saw a kitty though..."

            R "Kinda balanced out by the {i}getting murdered{/i}."

            C "Oh come on, the tone was setting it up."

            R "See a kitty, see your stoned friends, {i}get killed by a knife guy??!{/i}"

            "You do have to admit, it kinda came out of nowhere."

            P "I was trying to get back on track..."

        else:
            #### Caz -> Rosie -> Ellie
            E "But I got a lovely birthday party!"

            R "Yeah. A surprise!"

            R "But what was with that knife guy outside..."

            C "This was simply the setup, of course."

            C "For a grisly birthday-party slasher murder..."

            E "Noooooo they were just..."

            P "Bringing the knife to cut the cake?"

            "Nobody looks convinced by that."

            E "...yeah..."

    else: ###### Ellie middle

        R "Yeah, a cute couple oblivious to the horror around them..."

        E "Well... I've been like that before..."

        R "You've ignored a {i}creepy guy with a knife{/i} whilst cuddling?"

        C "Really sets the mood, doesn't it."

        if pizza:
        ##### Caz -> Ellie -> Rosie

            R "God, what carnage... what horror..."

            C "You're talking about the pizza, aren't you."

            E "So sad..."

            R "So sad!"

            C "So what was with the creepy knife guy outside?"

            P "Uhhh..."

            R "He murdered the pizza!"

            E "Oh no!"

            R "Oh no!"

            "Caz looks unimpressed."

        else:
        ###### Rosie -> Ellie -> Caz
            R "Yeah, well, your ignorance led to my {i}death{/i}."

            E "And ours!"

            R "Yeah! So much death outta nowhere! Talk about no foreshadowing!"

            C "Oh come on, the tone was setting it up."

            R "See a creepy skeleton, see your friends cuddling, {i}get killed by a knife guy??!{/i}"

            "You do have to admit, it kinda came out of nowhere."

            P "I was trying to get back on track..."

            "Everyone looks unimpressed."

elif ellie_score == 2: ####################### ellie majority

    E "I liked that it was mostly cute..."

    if not kitty:

        R "Yeah, you got a cute cuddly couple and a birthday."

        E "It was nice! I didn't want to hear a scary story before we go to sleep, it's so... spooky out here."

        "She gestures around to the mostly-empty campsite, the wind making only slightly less noise than in the story."

        if rosie_score == 1: ####### Rosie -> Ellie -> Ellie

            R "Just don't think about those spooooooky plastic skeletons."

            C "Who puts them up for {i}birthdays{/i}?"

            R "Spooky people! Spooky birthdays!"

            C "But it's August!"

            E "I'm not spooky, either..."

            P "Yeha, they were... a bit out of place, I guess."

        if caz_score == 1: ####### Caz -> Ellie -> Ellie

            R "Just don't think about the creepy knife guy outside."

            E "...well NOW I'm thinking about them!"

            P "I guess that was... uhhh..."

            C "It was simply the setup, of course."

            C "For a grisly birthday-party slasher murder!"

            E "Noooooo they were just... umm..."

            R "Bringing the knife to cut the cake?"

            "Nobody looks convinced by that."

            E "...yeah..."

    elif stoned: ##### Ellie -> Rosie -> Ellie 

        R "Yeah, you got a nice kitty and a party."

        E "It was nice! I didn't want to hear a scary story before we go to sleep, it's so... spooky out here."

        "She gestures around to the mostly-empty campsite, the wind making only slightly less noise than in the story."

        C "And you got two people stoned on your sofa."

        "You wince at the reminder."

        E "Yeah... I guess that's kinda realistic..."

        R "It's real life, innit."

        C "Depressingly so."

        E "...yeah..."

    elif pizza: ##### Ellie -> Ellie -> Rosie

        R "Yeah, you got a nice kitty and a cute couple."

        C "Then a burnt pizza and a room full of smoke."

        R "So sad..."

        E "So sad..."

        "You wince at the disappointing ending."

        E "I guess it was nice. I didn't want to hear a scary story before we go to sleep, it's so... spooky out here."

        R "But now you're going to be haunted at night.... by the ghost of the pizza!"

        E "..."

        C "..."

        P "..."

        R "Yeah okay that wasn't a great joke, was it."

    elif death: ##### Ellie -> Caz -> Ellie

        R "Yeah, you got a cute kitty and a birthday party."

        C "And a double-murder."

        E "But it wasn't a murder! It was fake blood, right?"

        C "That was totally a cop-out."

        E "Noooo it was a surprise so I didn't find out about the party..."

        R "..."

        R "It was definitely a cop-out, lol."

        "Yeah, it definitely was."

        C "Shame you couldn't commit to the party-slasher-horror setup."

        E "Noooo that's not what it was! Don't make me worry about a slasher."

        E "That wasn't the story, right?"

        P "..."

        P "...no, the murders were, uh. Pretend."

        "Nobody really looks impressed."

    else: ##### Ellie -> Ellie -> Caz

        R "Yeah, you got to see a cute kitty and a nice cuddle."

        R "Then I fucking DIED."

        C "Oh come on, the tone was setting it up."

        R "What part of that was setting up to {i}get killed by a knife guy??!{/i}"

        "You do have to admit, it kinda came out of nowhere."

        P "I was trying to get back on track..."

        E "I wish you hadn't..."

        R "Yeah, you kinda spoiled a cute story for baby Ellie."

        "Ellie pouts and you feel bad."

elif rosie_score == 2: ################ rosie majority

    R "I liked that it was mostly kinda funny."

    C "A regular stoner comedy."

    R "Yeah! Right!"

    R "Just..."

    if not stoned:

        R "Without anyone actually getting stoned."

        "Woops..."

        E "Yeah..."

        if ellie_score == 1: ####### R E R

            E "I mean, there was a cute couple!"

            C "If it was Jake and Amy, they probably {i}were{/i} stoned. They usually are."

            R "Yeah! guess it was just, like... implied..."

            P "Right. Yeah. Implied."

            R "..."

            C "Actually, it's kind of depressing, isn't it?"

            C "You run into some halloween decorations outside, in {i}August{/i}, then go in to find your friends made out too much and fell asleep and burned a pizza."

            E "..."

            R "..."

            P "...I guess that wasn't a great story, was it..."

        else: ###### R C R

            R "Yeah, they just fucking... died..."

            C "If it was Jake and Amy, they probably {i}were{/i} stoned. They usually are."

            R "Yeah! guess it was just, like... implied..."

            R "Impldied."

            "Ellie giggles at the mashed pronunciation."

            C "It's like an anti-drugs advert."

            "Woops..."

            C "Don't do drugs, kids! You'll get killed by a knife murderer!"

            R "And burn your pizza!"

            E "So sad!"

            R "So sad!"

            P "..."

    elif not pizza:

        R "With a kinda leftfield ending..."

        "Woops..."

        E "Yeah..."

        if ellie_score == 1: ###### R R E

            E "I mean... it was kinda cute to go from comedy to a fun party..."

            E "I didn't want to hear a scary story before we go to sleep, it's so... spooky out here."

            "She gestures around to the mostly-empty campsite, the wind making only slightly less noise than in the story."

            C "So you get a birthday party, that's happening whilst two people are stoned on your sofa."

            E "Yeah... I guess that's kinda realistic..."

            R "It's real life, innit."

            C "Depressingly so."

            P "..."

        else:  ######## R R C

            R "Yeah, I just fucking... died..."

            E "So did we! Or... whoever's meant to be the character..."

            "It was kinda muddled as to who the protagonist was..."

            C "I thought it was alright."

            R "It was so out of nowhere!"

            C "It was a classic one-two-three misdirection."

            C "Setup, repeat, twist."

            P "Uhhh yeah that's what - "

            R "Oh come on, it felt like an anti-drugs advert."

            "Caz laughs suddenly, and pats her thigh in amusement."

            C "Don't do drugs, kids! You'll get killed by a knife murderer!"

            E "But the protagonist didn't, did they? Whoever we were..."

            C "...I guess not."

            R "Don't be in proximity to drugs?"

            C "Doesn't really work, does it..."

            P "..."

    else:

        R "Kinda started slightly a bit clunkily..."

        C "What, you mean the ominous narration?"

        if ellie_score == 1: ##### E R R

            R "No, like, the cat..."

            E "The kitty was nice!"

            E "Don't you like saying hi to a cat?"

            R "I mean yeah totally. But it's a weird narrative, innit?"

            C "Pet a cat, see your stoned friends, take a burnt pizza out the oven?"

            P "..."

            E "It just sounds like a generic day..."

            R "Yeah, dang."

            "You admit to yourself that it wasn't the most gripping story..."

        else: #C R R

            R "No, like, the fucking... knife guy hanging around."

            R "What was with that??"

            E "It was scary..."

            "It was a bit out of place..."

            C "It's foreshadowing the death of the pizza."

            R "That wasn't {i}stabbed{/i} though."

            C "Foreshadowing the abstract concept of death."

            E "Pizza death..."

            P "..."

            E "So sad..."

            R "So sad..."

elif caz_score == 2: ################# caz majority

    C "I liked most of it."

    C "Nearly a solid slasher narrative."

    if ellie_score == 1:

        E "Yeah..."

        E "But at least it had a little cute moment!"

        if kitty: ##### E C C

            R "Oh, the cat?"

            E "Yeah!"

            E "We got to see a cat before everyone died..."

            R "The dreaded black cat... a bad omen..."

            "Huh, guess that scene kinda worked in context..."

            C "They're not bad omens. They're just cats."

            C "They get so much shunning for having black fur..."

            R "Oh, Caz, I was {i}joking{/i}."

            C "Hmmph."

            P "..."

            E "I hope the cat survived..."

            P "I wouldn't kill a cat in a story!"

        elif not death: ###### C E C

            C "You mean Jake and Amy passed out on the sofa."

            E "Yeah! Having a cuddle..."

            E "It sounds nice."

            R "And then a murderer breaks in!"

            C "Blood everywhere as they scream."

            "Ellie pouts and shakes her head at the two of them."

            E "It's so back and forth..."

            C "Everyone knows the couple who make out die in a horror film."

            R "Did they die, though? I thought we did? Or like... whoever the protagonist was."

            P "..."

            P "I didn't specify if they died."

            E "I hope they're not dead."

            R "I mean, they're not in real life."

            C "Could be a slasher at our house right now."

            E "Nooo..."

        else: ###### C C E

            E "I got a nice birthday party!"

            R "You mean the \"Happy birthday! My friends are dead and there's a knife guy outside laughing at us!\" bit?"

            E "But it wasn't a murder! It was fake blood, right?"

            C "Yeah. That was totally a cop-out."

            "She glances over at you, unimpressed."

            E "Noooo it was a surprise so I didn't find out about the party..."

            R "..."

            R "It was definitely a cop-out, lol."

            C "Shame you couldn't commit to the party-slasher-horror setup."

            C "Or maybe it's a double-bluff, and next the slasher comes in for real."

            C "That'd be fun."

            E "Noooo that's not what it was going to be! Don't make me worry about a slasher."

            E "That wasn't the story, right?"

            P "..."

            P "...no, the murders were, uh. Pretend."

            "Nobody really looks impressed at that compromise."

    else:

        if pizza:  ###### C C R

            R "Yeah, just derailed by the pizza-murder ending."

            E "The saddest part..."

            R "So sad..."

            C "Sadder than your two friends getting stabbed?"

            R "They'd be sad about the pizza too!"

            C "Hmmm."

            C "I guess it's a good black comedy twist."

            "Yeah, that's totally what it was."

            C "A bit anticlimatic though."

            P "Yeah, I guess."

        elif stoned: ##### C R C

            R "How was it? You see a creepy guy, see your stoned friends, then I'm dead?"

            C "Yeah. Setup, distraction, payoff."

            C "Shame we don't see what happens to Jake and Amy."

            E "Or... whoever's meant to be the character..."

            "It was kinda muddled as to who the protagonist was..."

            C "Yeha. I guess it's like an anti-drugs advert."

            P "Uhhh... yeah..."

            C "Don't do drugs, kids! You'll wake up to your recording engineer dead by knife!"

            R "However will they record their EP without me..."

            C "They'll be missing a certain spark, that's for sure."

            E "But it's not like {i}we{/i} took any - I mean, the protagonist... whoever they are."

            R "I mean, I probably did. It's implied."

            R "Heh. Impldied, you could say."

            "Ellie snorts at the bad pun."

            C "God, you probably got knife-murdered for that level of pun."

            R "Hey, you love my jokes!"

            "Caz looks unimpressed."

        else: ###### R C C

            R "What do you mean? It was rock solid, even if I {i}died{/i}."

            C "I mean, the sofa death comes out of nowhere."

            C "Just a few skeleton jumpscares beforehand."

            R "That's, like, setting up misdirection, innit."

            "You're glad that Rosie is covering for your inconsistent storytelling..."

            R "Funny, too..."

            E "If you put up jumpscare skeletons this halloween, I'll scream..."

            R "Heh heh heh..."

            C "Really, though, if [Emily] was going for a misdirection, there'd be {i}two{/i} of them to really sell it."

            C "A skeleton jumpscare, then - I don't know, something else, {i}then{/i} knife murder."

            P "..."

            P "Guess I'll remember that for next time..."

            R "Hey, next storytime, maybe me and the band can {i}survive{/i}? Just a thought."

            E "Once upon a time, Rosie and the band didn't die. The end, happy ever after."

            R "Thanks, El, that's perfect."

else: ############### i don't think this should come up?

    R "That was a fucking mess."

    C "Indeed. So much so you're seeing text the writer didn't forsee you seeing."

    E "Awh don't make fun of them..."

    R "Lol."

"Rosie blows out a breath and laughs briefly, stubbing her roach into the grass."

R "Anyway, storytime over. Where's the snacks..."

C "They're in the tent."

"Rosie crawls off to fetch them, leaving Ellie to curl up on the blanket."

"In her camp chair, Caz leans back and looks at the stars."

"Your story seems to have... well, at least entertained them a bit."

"Maybe you could've told it a bit more consistently..."

"But it seemed like a good idea to try and please everyone, " 

"Caz seems to notice you staring frustratedly at the fire, and whistles quietly to get your attention."

C "Hey, [Emily], it wasn't that bad. Trying to appeal to everyone is... admirable, at least."

P "Thanks..."

P "Thought that counts, right?"

"..."

"Mixed Ending"

return