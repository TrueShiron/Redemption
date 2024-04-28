label redemchapter2A: 

show maverick normal flip with dissolve
$ renpy.pause (0.5)
show maverick normal at Position(xpos = 0.29)
$ renpy.pause (0.3)
hide maverick normal with easeoutleft
$ renpy.pause (0.5)

hide sebastian with easeoutright

show sebastian normal b flip at left with easeinleft

m "Before he was leaving, Maverick looked me in the eyes. Even if it was for just a second, I noticed that there wasn’t any anger in his look anymore."

m "Luckily neither Bryce nor Sebastian noticed anything when Maverick finally left."

jump redemchapter2A_end



label redemchapter2B: 

stop music fadeout 1.0

m "I had a feeling as if I was supposed to meet someone here." 

m "However since I saw no one, I went on with my work."

nvl clear

$ renpy.pause (1.0)

window show

n "On the way to the police station, Maverick's look kept finding their way back into my mind. I couldn't decide how to feel about it."

n "I wasn't even sure if he was starting to trust me or not but at least he couldn’t accuse me of hiding anything from him anymore."

n "However, his actions were growing more calculated, and he seemed very sure of himself. I wondered if he’d accept my help in the future."

n "But that wasn't the problem at hand."

window hide

scene black with dissolveslow

$ renpy.pause (1.0)

scene office at Pan ((128, 250), (0, 250), 3.0) with dissolveslow

$ renpy.pause (1.0)

nvl clear

show sebastian normal b with dissolve

play music "mx/barren.ogg" fadein 1.0

Sb "Hey, [player_name]!"

jump redemchapter2B_end



label redemchapter2C: 

c "Sebastian, would it be ok if I could get a copy of everything we found out today?"

m "Sebastian was looking unsure at first, but then smiled at me."

Sb smile b "Let me guess, it’s because of the little {i}walk{/i} you had last time? Well, as long as you don’t tell anyone else about it, it should be ok."

m "A few minutes later he gave me an envelope."

Sb normal b "Maybe you’ll notice something we’ve missed."

c "Thank you, Sebastian."

Sb "You’re welcome. Can you find your way back to your apartment?"

c "Of course."

jump redemchapter2C_end


label redem_call2:

play sound "fx/answeringmachine.ogg"

$ renpy.pause (0.5)

Mv "I’ve got a plan on what to do next."
Mv "If you still want to help, give me a call."

play sound "fx/answeringmachine.ogg"

$ renpy.pause (0.5)

jump ml_answeringmachine_end