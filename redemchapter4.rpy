label redemchapter4:

Sb "The chief will explain everything once we get there. Let's not keep him waiting, shall we?"

stop music fadeout 2.0

play sound "fx/steps/clean2.wav"

scene black with dissolvemed
$ renpy.pause (1.0)
scene hatchery at Pan ((0, 0), (0, 360), 5.0) with dissolveslow

$ renpy.pause (3.3)

play music "mx/threat.ogg"

m "We arrived at a place that would look like an ordinary house, had it not been for its extraordinary size. It reminded me more of a hostel than a family home."

show sebastian normal b flip at left with easeinleft

Sb "Chief!"

show bryce brow b at right with easeinright

jump redemchapter4_end 




label redemchapter4_A:

Mv "When he was at the portal a few days ago, I nearly got him and managed to follow him for a while before I lost him. Based on that, where he's been and where his victims have been found, I could triangulate his whereabouts."

Mv "[player_name] and I concluded that he had to live somewhere, right? He needs a base to hide the generators and everything he has stolen."

Mv "So our idea was that, before [player_name] arrived here, Reza must have scouted the town at night when no one was watching him."

play sound "fx/unwrap.ogg"

m "Bryce cleared the clutter on a table and smoothed out a map of the town on its surface. It already had a few locations related to the case marked on it."

Br "Show it to me."

Mv "Prior victims were found here, and here. Today's was here. She was following him, likely because she wanted to save the eggs he stole. This is the path he took from the portal when I followed him a few days ago."

Mv "So we have established this as his area of operation. Extrapolate it and we can narrow it down to this. Now, where could he be hiding in this area?"

Mv "He's certainly not within the village borders, so unless he's decided to live in the wilderness or in a hole in the ground, the only option is here."

Br brow b "The abandoned farm."

Br "When did you figure all of this out?"

Mv "Just a few minutes ago. When I did, I immediately came here."

Br stern b "Damnit, Maverick. This might be it."

Sb "Should we send an observation team?"

Br "As if we had one to spare. Heck, we're going there right now."

Br "What about you, Maverick?"

Mv "I'm still on sick leave, remember?"

Mv "Besides, if I saw Reza right now, I'd probably do something I shouldn't."

Br brow b "How about you, [player_name]?"

c "Isn't this going to be dangerous?"

Br stern b "Reza probably won't harm you, as you're the only one he could possibly consider an ally."

c "Good point."

m "I had the strange feeling as if this was a point to decide which way I would go now."

m "By trusting my feelings for Maverick, we might both get our redemption."

m "On the other hand, there could be a way for Bryce to become the savior for all of us. Either that or it would be one of the timelines I already went to."

menu:

    "[[Trust Maverick.]":

        m "I decided to trust Maverick. Together we would catch Reza and get our redemption." 

        $ maverick_redem_trust = True


    "[[Trust Bryce.]":

        m "I decided that I'd give Bryce his time to shine."

        m "He'd either become our savior, or I'd experience an old timeline again."

        scene redem_aw_glitch

        $ renpy.pause (0.5)

        show black

        scene office at Pan ((128, 250), (0, 250), 3.0) with dissolve

        show bryce stern b at right with dissolve

        $ renpy.pause (0.1)

        show sebastian normal b at Position(xpos = 0.85) with dissolve

        $ renpy.pause (0.1)

        show maverick normal flip at Position(xpos = 0.1) with dissolve

        m "It felt as if reality around me had changed. I couldn't explain what happened but it wouldn't stop me from my mission."

        $ maverick_redem_trust = False


Sb "If anything - with you there, we might be able to convince him to give up. Or we could act like we intend to trade you for the eggs if he tries to use them as a bargaining chip."

jump redemchapter4_A_end 


label redemchapter4_B:

Sb "We'll see about that."

c "I suppose if it's necessary, I'll have to play along."

Br "I've got your back. If there's one thing we could do to make this whole situation even worse, it would be messing up with you."

Sb "We have the element of surprise if we walk into his base right now, but we risk Reza lashing out with his weapon. If we want to resolve this peacefully, observation is probably the way to go."

Br brow b "I guess we won't need [player_name] there for that, though."

Sb "True enough."

Br stern b "Alright, [player_name], you stay here and wait for further instructions. We may need you at a moment's notice. Don't do anything without us telling you to, understand?"

c "Okay."

Br "Alright, then. Let's go, Sebastian."

Sb "After you, Chief."

Br "And Maverick: Good job."

Mv "Thanks, Chief."

show bryce stern b flip

$ renpy.pause (0.3)

hide bryce with easeoutright

show sebastian normal b flip

$ renpy.pause (0.3)

hide sebastian with easeoutright

$ renpy.pause (0.5)

m "Shortly after they vanished, Maverick also turned to leave."

$ renpy.pause (0.3)

show maverick normal

stop music fadeout 2.0

$ renpy.pause (0.3)

menu:
    "Tell Maverick to wait. {image=image/ui/status/havemap.png}":

        c "Wait."

        play music "mx/mysteryambience.ogg"

        m "He stopped and waited for a few seconds."

        Mv normal flip "Do you need something, [player_name]?"

        c "I’ve been thinking about one detail about Reza’s behavior before I arrived we never were able to solve."

        Mv "I guess you’re talking about the map? "

        c "Yes. When I was helping Sebastian last time, he asked me to visit the police archive. Kalinth had already prepared what you had collected and I was able to check everything you had about the underground facility."

        c "As it turned out, it was created by humanity. I don’t know how it’s possible but it was built by a company from my world."

        Mv "As interesting as it sounds, how can this information help us?"

        c "Together with the information I found this map."

        play sound "fx/unwrap.ogg"

        m "I put the map on the table and Maverick looked at it."

        c "The facility has two entrances, one close to the portal and a second one in Tatsu Park. As you can see, Bryce already marked a spot."

        c "The second entry can be used through your town's sewer system. "

        Mv "So you think this was the map Reza was searching for? "

        c "I’m not sure but you said it yourself; if he’s not able to stay within the town, he has to stay live in the wilderness or in a hole in the ground. "

        m "I pointed at the second entrance."

        c "This is a hole in the ground and it not only leads to the portal but also a well guarded human facility. So as long as your council won’t start exploring the facility, no one would bother Reza."

        Mv "Yes it would be a good hideout. He can rest during the day and then sneak out of the hatch in Tatsu Park at night."

        c "It still doesn’t mean that my theory is true but if it is…"

        Mv "It is good that you didn’t tell Bryce about it. We don’t have enough people to search the facility and Bryce would most likely storm it which would alarm Reza. People could get hurt and we dragons aren’t good fighters in closed rooms."

        c "Especially against Reza with his gun. He already proved that he’s skilled with his gun and with six bullets he could kill many dragons without reloading. You on the other hand can check the facility without alarming Reza and then could call for backup."

        Mv "I like the way you’re thinking. If Reza is not in the farmhouse then I’ll give it a try. I know the town better than you and know how to move without anyone noticing."

        play sound "fx/paper.wav"

        Mv "Good job, [player_name]. I'm glad you're on our side and not on his."

        c "I would've never joined him, no matter how desperate we are for the generators."

        Mv "That's why I like to spend time with you."

        Mv "Well, I need to go now. See you later, [player_name]."

        c "See you later, Maverick."

        $ persistent.havemap = False

        $ maverick_redem_mapgiven = "True"

        stop music fadeout 2.0

        $ renpy.pause (0.5)

        show maverick normal

    "Don't say anything.":

        $ maverick_redem_mapgiven = "False"

        $ renpy.pause (0.5)

$ renpy.pause (0.3)

hide maverick with easeoutleft

$ renpy.pause (0.3)

play sound "fx/door/doorclose.ogg"

$ renpy.pause (0.5)

m "Then I had to wait. Bryce and Sebastian were observing the farm now, and if anything new happened, I would be the first to know."

jump redemchapter4_B_end




label redem_call4:

play sound "fx/answeringmachine.ogg"

$ renpy.pause (0.5)

Mv "Hey, [player_name]."
Mv "I prepared everything for the hiking trip."
Mv "If you still want to join me give me a call."
Mv "I'm looking forward to hearing from you."

play sound "fx/answeringmachine.ogg"

$ renpy.pause (0.5)

jump ml_answeringmachine_end
