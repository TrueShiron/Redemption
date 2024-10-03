label redemchapter5:

show black with dissolvemed

$ renpy.pause (0.5)

scene o2 at Pan((0, 250), (0, 250), 0.0) with dissolveslow

play sound "fx/door/doorbell.wav"

$ renpy.pause(1.0)

c "(That must be him.)"

stop sound fadeout 0.5

$ renpy.pause(0.4)

play sound "fx/door/handle.wav"

$ renpy.pause(1.0)

show maverick rehappy flip at left with easeinleft

Mv rehappy flip "Good evening, [player_name]."

c "Good evening, Mav."

Mv "I hope you’re ready for the show."

c "I sure am. Let’s go and find a good spot."


scene black with dissolvemed

$ renpy.pause (0.5)

scene viewingspot with dissolvemed

play music "mx/amb/night.ogg" fadein 5.0

m "After a few minutes of walking we arrived at a rather empty looking area near the edge of town."

c "If this is everyone then I’m disappointed."

show maverick normal flip  at left with easeinleft

Mv "I decided that it might be better to watch the fireworks from a different place. You’re kind of a celebrity and I thought you’d prefer to watch the show in peace."

c "You’re right. It always better to watch events like this together with friends instead of a huge group of people."

m "We both sat down on a meadow and waited for the fireworks to start."

Mv "Waiting for the show to begin brings back memories."

c "Good or bad ones? "

Mv "A bit of both I guess."

Mv "When Anna and I still used to date we used to watch them together. Neither of us was ready for the commitment of a deeper relationship. That's why I didn't protest when she and Miles…"

Mv "We still did a few romantic things like watching the fireworks but after our relationship ended I stopped caring for them."

Mv "However, the time I spent with you made me reconsider. Maybe I should change some of my views and be more optimistic toward the future."

c "We both had been through a lot bad things. Being more optimistic might be a good thing for both of us. Life is short and we should enjoy it."

Mv "You’re right about that."


if maverick_redem_maverickromance == True:

    Mv "I still can’t believe how you came into my dull and depressing life and changed everything."

    Mv "For the first time since Miles' death, I’m looking forward to the future."

    m "Maverick moved his head closer and we shared a kiss."

    c "Before I met you all I had in life was the hope that life might get better someday. Then I met you and gave me more happiness I ever hoped for. Thanks to you, I’m able to be happy again." 

    c "I love you Maverick and no matter what the future holds for us, I’m looking forward to spend my life with you."

    Mv "I love you too [player_name]."


elif maverick_redem_annaromance == True:

    Mv "I've known Anna for long enough to see that she cares for you. Once all of this is over, you should talk to her."

    c "I thought about calling Anna, but I got the feeling that tonight wouldn't be best time. I don’t want to risk her life even if I can’t explain why I’m thinking like that."

    Mv "Yeah, I know that feeling. It's as if we're getting closer finding Reza."

    c "One way or the other, it’ll be over soon."


elif maverick_redem_bryceromance == True:

    Mv "I know that you’d most likely preferred to come here with Bryce, but I feel as if we’ll get better results when we are working outside the police line of action. Even if we might get in trouble for it."

    c "You’re right Maverick. I’m sure Bryce will understand my reasons once we explained everything."

    Mv "I can help you if you want."

    c "Thank you, Mav."

elif maverick_redem_adineromance == True:

    Mv "I've talked to Sebastian earlier today. He was watching over the stunt flying competition and it seems as if Adine, or should I say [adinestagename], didn’t fly in the end."

    m "I felt as if there was a load off my mind when Maverick told me about the competition. I had called Adine the day after we went hiking but didn’t hear anything from her since."

    Mv "I don’t know what you said to her but it worked."

    c "The day after we went hiking, I had called her. It didn’t go well."

    c "When I tried to reason with her she got mad and hung up on me. That was the last time I heard from her."

    c "I’m relieved that she’s fine."

    Mv "I guess the competition means a lot to her and missing it out isn't easy."

    Mv "I’m sure she knows that you only had her best interest in mind."

    c "I hope you’re right Maverick. However, as long as she’s safe I’m happy, even if she won’t talk to me anymore."

    Mv "Don’t worry; she seems like a smart girl. Give her some time and then call her again."

    c "Thank you, Mav."



elif maverick_redem_noromance == True:

    pass



else:

    Mv "I know that you’d most likely preferred to come here with [maverick_redem_romance_partner], but I think it’s better to keep [maverick_redem_romance_partner] out of this until we caught Reza."

    c "You’re right Maverick. I’m sure [maverick_redem_romance_partner] will understand my reasons once I explained everything."

    Mv "I can help you if you want."

    c "Thank you, Mav."


c "Oh, I think it's starting."

play soundloop "fx/fireworks3.ogg"

m "We waited quietly as the stillness of the night enveloped us. Soon, I heard the sound of the first rocket making its way into the night sky after which it exploded in a pattern of colors."

m "More rockets followed, their thunderous noise echoing throughout the land."

show fireworks at Pan((0, 545), (0, 0), 15.0) with dissolveslow

$ renpy.pause (6)



stop music fadeout 2.0

hide fireworks with dissolveslow



m "Suddenly, a terrible realization hit me."

play music "mx/judgement.ogg" fadein 0.5

m "Considering how public of an event this was and how everyone would be watching the fireworks, now would be the best time for Reza to make his move."

m "Not only was the village basically deserted, but the sounds of the fireworks would also overshadow any gunshots, giving him as much security as he would ever have."

m "As the portal had been repaired by the mysterious person I met, now was the perfect time for Reza to make his getaway, and I was the only one who knew."

c "Maverick, I think we need to go. Now."

Mv  "What are you talking about [player_name]? The fireworks just started."

c "I know where Reza is. We need to stop him."

Mv "How do you know that so suddenly?"

c "I just realized that the whole town is watching the fireworks. It’s the perfect timing for him to finish his mission."

Mv "And with the sounds of the fireworks, no one would take notice of the sound of his gun."

c "Exactly. If we act now we can finish this once and for all."

Mv "Tell me where he is and I can scout the place from above until you arrive."

c "He’ll be somewhere close to the portal."

Mv "I’m on my way."

hide maverick normal flip with easeoutright


scene black with dissolvemed
$ renpy.pause (0.5)
scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow

$ renpy.pause (3.5)

m "I arrived at the portal just a few minutes later. While I checked out the portal itself, Maverick landed next to me."

play sound "fx/flapx.ogg"        

$renpy.pause(1.0)

show maverick normal flip at left with easeinleft

m "I was glad to see it was still turned off. Had it been used recently, it would either still be running or in the process of recharging. Reza was still here, somewhere."

Mv "I searched for Sebastian but didn’t find him. I hope he’s safe…"


if persistent.sebastianfail == False:

    c "Don’t worry, I’m sure he’s safe."

    m "He still looked worried but both of us knew that we had to stop Reza first."

    m "I just hoped Sebastian followed my advice and was watching the fireworks from a safe place."

else:

    c "I called him earlier today and convinced him to watch the fireworks."

    c "It means a lot to him and I never thought that Reza would choose today for his plan."

    Mv "You might have saved his life. Sebastian is a good officer but I’m sure Reza would have surprised and killed him."

    $ sebastiansaved = True




Mv "While you were on your way I found this."

c "What is it?"

Mv angry flip "Eggs, a suitcase full of them. That bastard broke into the hatchery again."

c "Looks like it. Luckily he hasn't used the portal yet, though."

Mv normal flip "How could he after I disabled it?"

c " It seems as if someone had repaired it."

Mv "Then he must be close but where is he? What is so important that he won't leave without it?"

c "The underground building."

m "The Administrator had told me all about the prowess of the generators within. It probably hadn't been hard for Reza to guess the same and now that the facility was even more deserted than usual was the perfect time for him to steal it."

Mv  "That must be it."

c "So, what do we do now?"

Mv  "We could wait for him here, but I think I've got an even better plan… but it’s dangerous. Mostly for you."

c "What is it?"


if maverick_redem_mapgiven == "True":

    Mv "You go in first and I'll use the other entrance. Thanks to the map I already found one a few days ago and made sure it stays open. I’ll only need a few minutes to be in position."

    Mv "If you meet Reza, you can confront him and maybe talk him down. Try to buy me some time and if he won't surrender, I’ll try to catch him alive."

    m "I agreed to his plan and we both went our way. However before I entered the tunnel, I removed the PDA from my wrist and stored it on top of the suitcase with the eggs. It was as if it was the right thing to do. "

    m "Even in the darkness, it was easy for me to spot the site where they had unearthed the building's entry as it was in a roped off area that I had seen from afar before."

    show maverick normal at left

    $ renpy.pause (0.5)

    hide maverick normal with easeoutleft

    m "Even in the darkness, it was easy for me to spot the site where they had unearthed the building's entry as it was in a roped off area that I had seen from afar before."

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene hallway at Pan((0, 0), (0, 150), 3.75) with dissolvemed

    $ renpy.pause (2.0)

    m "When I entered the building, I was met by a long, illuminated hallway that was lined with doors on both sides."


else:

    Mv "You go in first and I'll stay behind and out of sight. If you meet him, you can confront him and maybe talk him down. If he won't surrender, I’ll try to catch him alive."

    c "Alright. Let's go."

    m "Before we entered the tunnel I removed the PDA from my wrist and stored it on top of the suitcase with the eggs. It was as if it was the right thing to do. "

    m "Maverick led me to the dig site where they had unearthed the building's entry. Once we got nearer, he stayed behind and motioned for me to go forward."

    scene black with dissolvemed

    $ renpy.pause (0.5)

    scene hallway at Pan((0, 0), (0, 150), 3.75) with dissolvemed

    $ renpy.pause (2.0)

    m "He slowly followed me, trying to stay in cover as I entered the building."

    m "Inside, I was met with a long, illuminated hallway that was lined with doors on both sides."










label redem_reza_a:

m "Since the lights were already on, Reza had to be very close. I wasn't surprised at the building still having electricity, since its generators were also powering the portal."

play sound "fx/door/hallwaydoor.ogg"

m "Suddenly, one of the doors opened, and out came Reza, carrying a large cardboard box."

m "When he spotted me, he set it on the ground."

play sound "fx/box1.wav"

$ renpy.pause (1.0)

show reza normal at Position (xpos = 0.9) with dissolve

play music "mx/path.ogg" fadein 0.5

Rz "[player_name]! You're here? You don't know how glad I am to see you. I've wanted to talk with you for so long. I even tried to contact you, but I couldn't with someone tailing you the whole time."

Rz "But talking can wait. Now that you're here, we've got everything. Come on, help me with this and let's get out of here."

c "No."

Rz annoyed "No? What are you talking about?"

c "I'm not doing anything until you answer a few questions."

Rz amused "You want to talk now? Sure, why not? We've probably got a few hours if we wanted to. None of them will disturb us here. We could even get the backup generator as well after we send this one over."

c "When did you realize we were in the past? How did you know about the comet?"

Rz normal "I've known for a while. It's what I wanted to talk with you about when we met at the portal. How about you?"

c "I only recently found out."

Rz annoyed "Looking back, it just seems so obvious to me now. I'm not sure how exactly you figured it out, but there are so many damn clues when you think about it."

Rz normal "I mean, how could a supposedly completely different, independent civilization speak the same language as us? What was this supposed to be? An alternate reality? No, it was just a different time."

Rz annoyed "When was there ever anything resembling these ... creatures on Earth? It's not hard to make the jump from dragons to dinosaurs when some of them here look pretty damn near identical to dinosaurs we knew about."

Rz "And then, there are also the prehistoric fruits, the plants and the fact that their technological level is nearly exactly the same as our own past society."

Rz normal "But we don't even have to think that abstract. You just needed to look at the sky."

Rz annoyed "The sun, the moon, even the stars are the same. Constellations change over time, of course, but you know we could account for that stuff."

Rz "You could've just pointed your PDA at the sky and it would've told you the time period - including the imminent threat of being eradicated."

Rz "You could even see the meteorite in the sky, and how it would change its position day after day."

c "Are you done being condescending?"

Rz normal "I guess so."

c "You killed those dragons, Reza."

Rz amused "What a brilliant deduction, Sherlock."

c "Why did you do it?"

Rz annoyed "Do you really need me to spell it out? I thought better of you."

Rz "After I found out the truth about this place, I knew just waiting for the generators we were owed was not an option anymore."

Rz normal "It would have taken who knows how long, but I didn't intend to stay a day longer than necessary."

Rz annoyed "You wouldn't believe how hard it was for me to acquire some generators. Some of the dragons didn't go down easily."

Rz amused "But who cares that they got back the generators I stole? With just this one, we won't need any of the others."

c "How could you do this?"

Rz annoyed "{i}How could I do this?{/i}"

Rz amused "Let me ask you this: What harm is there really in taking their generators when their whole civilization will be gone in a few weeks, anyway? The ones I killed just died a little earlier than scheduled."

Rz annoyed "Even if that creep hadn't shown up and interrupted our meeting, we wouldn't have had the time for them to make the generators for us."

c "How about we don't let them all die?"

Rz amused "They aren't going to be extinct any time soon, if that's what you're concerned about. I paid the hatchery another visit before I came here."

Rz normal "With the right... persuasion, I think we'll have plenty of reasons to keep at least some of them around. Bodyguards, border patrols, weapons. Even as pets or companions, as long as we make the necessary changes."

Rz amused "See, it's not as bad as you might think."

c "I'm not going to just abandon them like that, only for their whole civilization to be wiped out."

Rz angry "Get your priorities straight, [player_name]."

Rz "Next you'd rather starve, because you suddenly empathize with a steak. And you're not satisfied just starving by yourself. No, you're going to let all of us starve, because you want to impose your morals on everyone."

Rz annoyed "Since when do you think that you get to have any say in this? You know why you're here. What you're proposing is treason, and you know the consequences."

Rz amused "Personally, I don't mind if you want to stay here. You know I don't care about corporal punishment."

Rz normal "Just let me through and you can do whatever you wish."

c "I can't do that, Reza."

Rz annoyed "I see how it is. They've told you they need this generator to stop the comet, huh? And now you've become their lackey."

Rz "Don't tell me you've been drinking up what they've been telling you. You know they have as much of a vested interest in this whole thing as humanity does - that I and you do, or at least used to."

Rz "Do you think they wouldn't do the same thing if it was their families on the line instead of ours?"

c "Their entire world is on the line here."

Rz "They live in perfect harmony, with their perfect green energy source and no reason for wars or conflicts, yadda yadda yadda. We had that too, and you know what happened then? Of course you do."

Rz "This is such an idiotic trope, you know. Random person meets weird natives, learns their ways and then ends up saving them."

Rz "What do they need you for, huh? Maybe they're going to be extinct for a reason if they can't even save themselves."

c "You know of our suffering, yet will let them have it?"

Rz angry "I don't care what happens to them, but unlike you, I was at least trying to save humanity."

c "At any cost."

Rz "We have the solution right here, and you want to get philosophical now? Don't you think we deserve it?"

Rz "They've had it for who knows how long. Now it's time for us."

c "Not like this."

Rz "Do you think I like it? If there was a different way, I wouldn't have spent the last few weeks doing what you didn't."

Rz "We don't live in this fairy tale world of yours where there is a perfect solution to everything. You should know that. Just being here for a few weeks must have messed you up."

Rz annoyed "I think I know why."

Rz "You got too used to all the comforts they have here. You actually don't care if they all die back home, do you?"

Rz "As long as you can stay here, in this perfect little world of yours. You have discarded everything and everyone back home, and replaced it with this."

Rz "Maybe it is because you just don't have a life back home."

Rz normal "I can even understand that a little. Of course it would be nice to just stay here where they have everything that we don't, but being here also reminded me of everything I hated about our world as it used to be."

Rz angry "The pettiness and the politics. Say about the solar flare what you want, but it leveled the playing field and gave people like us a chance to make a difference."

Rz "For all of our efforts, what did we get? A vote that was meaningless in a sea of stupidity and lies. Now everyone has to pull their own weight. We make the rules."

Rz "You, of all people, should understand."

Rz "Of course they wouldn't. They haven't experienced how it is, to live like we do now. To see the world burn and everyone you know die around you."

c "And because I have, I won't let the same thing happen to them."

Rz "How many do you think died back home just in the two weeks you've been here because we don't have power for the hospital, huh? Do you think those victims aren't worth mentioning, or do you just care about the few dragons I killed?"

Rz "Our city is the last bastion of a civilized society in a world where nothing else is left."

Rz annoyed "Maybe you have forgotten about them, but I haven't."

Rz "How many of us do you think will still be there in a month? A year? Or are they just a statistic to you?"

c "The same could be said for the dragons."

Rz "What do you want to do? Talk me down from doing this? And then what?"

Rz "It's too late, anyway. You think they're just going to let us go after what I've done? Fat chance."

Rz normal "Whatever you may think, you'll find that our leaders back home agree with my course of action."

c "Why are you telling me this?"

Rz "Because I expect you to join me."

c "That's not going to happen."

Rz angry "And you call yourself an ambassador? This generator is the only thing we need for our city to survive. How can you even argue about this?"

c "The dragons also need that generator and I'll do what is necessary to stop you if I have to."

Rz annoyed "So, that makes you judge, jury and executioner. What a wonderful set of morals you have there, [player_name]."

c "We only need to wait until the comet has passed safely."

Rz "You think you can stop the comet? And you need this generator to do that?"

Rz "Sure, and if your plan fails, then not only is this world gone, but we also lose any and all hope to save our own."

Rz angry "We are so close now. We can't risk anything by waiting for your crazy plan when back home they are dying by the minute. I will not let you."

c "You only want to save your own two-faced hide, because you don't want to face the consequences of what you did."

Rz "..."

Rz normal "..."

Rz laugh "Hahahahahahahahahahaha!"

c "Why are you laughing about this?"

Rz "Because it's a joke. It must be. I'm the one with the gun, and you thought you could just waltz in here and lecture me."

Rz amused "Listening to you was fun and all, but the grownups must get back to work now."


if maverick_redem_mapgiven == "True":

    c "Are you sure that this is what Jenna would have wanted? "

    Rz "How do you know that name?"

    c "I found your diary when I searched your apartment. "

    Rz "Do you really think that you can use old stories to make me stop my plan?"

    c "Can’t you see the error of you ways? Do you really want to ignore the man you once were and the dreams you had? "

    Rz "If you read my diary you should know that my old self died back when she died. I was weak just like she was. That day, I was woken up from my dreams. I became strong and I learned to do what was needed to get what you want. "

    Rz "I was sent for this mission because our leaders knew that I would get rid of all possible problems, no matter what I had to do."

    c "You can’t be serious? You’re actually willing to commit genocide?"

    Rz "You never were able to see the bigger picture. That's why you were chosen as my partner… or victim if you'd become a problem. "

    c "So our leaders did actually choose me as a pawn for their games? "

    Rz "Of course they did. Your degrees are worthless at home, you aren’t important enough to survive and no one cares if you would die. No family, no friends… you were perfect for the job."

    m "I already figured all of that out myself but hearing it still was painful."

    Rz "However, we once were something like friends. So if you’d help me you could also benefit from all of this. "

    c "What do you mean benefit? Aren’t you doing this to help our people? "

    Rz "That’s why you’ll never be fit to become a leader. You still don’t understand anything." 

    Rz "Our people are nothing more than wild animals; mankind had everything it needed to rebuild our society after the flare but instead they chose violence and war. They only seek power and follow those with power."

    Rz "Whoever brings back the generator will earn the support of the people. You can pick any job you want and no one can stop you as long as the masses are on your side. That’s how you can manipulate and control them."

    Rz "As soon as I return I’ll choose my own destiny. I’ll join the ranks of our leaders and then I can start to getting rid of everyone standing in my way." 

    Rz "The dragons are as stupid as our people were before the flare; too lazy to act and too stupid to question the motives of their leaders. They just live their lives as long as they won't be bothered. That’s why they’re stuck at their current technological level."

    Rz amused "Deep down they want for someone to take control over their lives. To tell them what to do and what to think. The few freethinkers will always be ignored and sabotaged, just like that bitch Anna."

    m "Reza seemed to love the sound of his own voice but that only gave me more time to think of a way to stop him. I only hoped that Maverick would be there when I needed him. "

    Rz laugh "That idiot Damion only thought of himself. He thought he could use me to do his dirty work by leaving a note close to the portal, easy to find it if you want to use it. I’m surprised the cops didn’t find it first. "

    c "Wait, so he tried to work with you but instead you murdered him? Why?"

    Rz "Damion made a map of the town, marked Anna's apartment and the way to its generator. All he asked for was that I’d get rid of Anna for him so he would be celebrated as the genius he thought he was. He even offered me the PDAs. "

    Rz laugh "You should have seen the look on his face when I was about to cut his throat. Him begging for mercy was hilarious. That beast was so desperate that he even tried to fight back." 

    Rz "It seems he never realized that the PDAs were more important for my plan than a single generator."

    c "You are crazy Reza. You’ve completely lost your mind."

    Rz amused "How could I not after everything that happened since the flare? I'm surprised that you didn't go mad yet but I’ll promise you, it will happen sooner or later. Our sick world will break you just it has broken me. "

    Rz "You know, a few years ago I might have acted like you and would have tried to find a way to save both worlds but the past made me realize that, from the moment we're thrown into this world, we're fated to bring each other nothing but pain and misery."

    Rz "We had everything we needed to just rebuild out world even without our advanced technology but instead our people chose to fight against each other. " 

    Rz "This sick world we’re living in has taken everything from me but it made me stronger. That’s how I survived the madness of this post-apocalyptic hell. Caring for others only makes you weak. "

    Rz "The Raiders are able to survive even without the help of advanced technology because they have adapted to the new situation just like I did."

    m "Despite everything Reza had done a part of me felt bad for him. He had everything and was living a happy life but the flare and the following events had broken him. "

    m "I started to wonder if I would have also become like him if had our roles been reversed?"

    Rz "You know, before I moved to Bastion I had some problems with one of the raider clans, the Carrions. They attacked the people that saved me and killed a few of them. "

    Rz "I tracked them down and took care of their whole clan; not for the people of course but because the raiders became a problem for my safety."

    Rz "In the end, even those merciless raiders were no different than those dragons, begging for mercy when I slaughtered them like the animals they were."

else:

    pass

Rz "So [player_name] I'll give you one last chance; join me and I might even make you my right hand man when I'll take over Bastion, or refuse and die with those beasts. "

c "You don’t really expect me to join your side, do you? I know you’d kill me either way."

Rz "Oh, it seems there really is a brain inside your head. You’re right, it doesn’t matter what you choose and you’re more useful to me dead than alive. "

Rz gunself "The best part is that I don't even need to kill you. The comet will be doing the dirty work for me. "

Rz "Don’t worry, I’ll tell the people that you fought bravely before those bloodthirsty beasts tore you apart. All to make sure that I would be able to safely return to our people. "

Rz "However your little friends won’t go extinct. I’ll take a few of their eggs with me for my own personal guard… or shooting targets if I’ll get bored of them."

Rz "Alright. Game's over."

Mv " Not if I still have a word to say."

play music "mx/fervor.ogg" fadein 0.5

m "Suddenly, Maverick appeared, ready to fight Reza if needed."

show maverick angry flip at Position(xpos=0.2, xanchor='center') with easeinleft

Rz annoyed "Do you really think I’d be afraid of you? I was looking forward to kill you myself, you annoying beast."

play sound "fx/rev.ogg"

show reza gunself with dissolve

show reza gunpoint with dissolve

m "He pulled out his gun, not sure which one of us he should be aiming at."

Rz "The six bullets I have in here should be more than enough for you two."

Mv "I wouldn't be so sure of that."

c "Do you think you can really do that, Reza? Do you think this is worth risking your life for?"

Rz angry "I've been risking my life for this every day for the last two weeks. What did you do during that time, sip champagne in your nice apartment?"

Rz "Besides, this generator and the whole building came from our time."

Rz "They belong to humanity!" with Shake((0, 0, 0, 0), 2, dist=10)





if maverick_redem_dream == "False" and maverick_redem_mapgiven == "False":

    jump redem_ending_f

elif maverick_redem_dream == "True" and maverick_redem_mapgiven == "False":

    jump redem_ending_d

elif maverick_redem_dream == "False" and maverick_redem_mapgiven == "True":

    jump redem_ending_e

else:

   jump redem_good_ending






label redem_good_ending:


m "Deciding that Maverick was the bigger threat, Reza aimed at him. My first instinct was to run away, but as Maverick started charging, so did I."

m "Maverick was fast, pouncing on Reza before he had a chance to pull the trigger."

play sound "fx/snarl.ogg"
show maverick angry flip with dissolve

$ renpy.pause (1.0)

show maverick at Position(xpos=0.65, xanchor='center') with move6

play sound "fx/impact3.ogg"

show maverick at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top")
show reza gunpoint at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top")
with move9

m "He was knocked to the ground and Maverick embedded his teeth into the body before him."

queue sound "fx/bite.ogg"

m "Reza was screaming. He aimed at Maverick's head and frantically pulled the trigger twice."

play sound "fx/gunshots4.ogg"

m "Luckily Maverick was faster and instead of his head, Reza hit Maverick in the chest."

m "Despite being shot twice, Maverick managed to avoid any mortal wounds as if he had known that this would happen."

m "Reza aimed the gun at Maverick again but this time I was faster and grabbed his arm."

m "As we were fighting for his gun, I tried my best to aim its muzzle away from me."

m "However, Reza was faster and I suddenly heard a gunshot followed by a burning pain in my chest."

play sound "fx/gunshot2.wav"

m "All of my strength disappeared and I fell on the ground, unable to move."

m "I heard Reza’s footstep walking away from me and toward Maverick, who was still lying on the ground."

m "I tried my best to move my head only to see Reza with a victorious smile on his face, aiming at Maverick’s head again."

Rz gunpoint b "This is the last time you stand in my way you annoying beast."

Mv angry flip "You should have gone for the head."

m "Before Reza was able to fire his gun, Maverick had already opened his mouth and was letting out an inferno that burned Reza's upper body."

play sound "fx/fire.ogg"

$ renpy.pause (1.5)

m "He didn't even have a chance to scream before the flames killed him. "

show redem_good_ending at Pan ((0, 326), (580,0), 10.0) with fade

$ renpy.pause (8.5)

hide redem_good_ending
with fade

stop music fadeout 2.0

play music "mx/fragments.ogg" fadein 2.0

m "Wounded, Maverick stood up and ran toward me. Carefully, he rolled me on my back."

show maverick reshock flip at left with dissolve

Mv reshock flip "No, this can’t be happening. [player_name], can you hear me? "

m "Maverick looked back at my bleeding wound and tried his best to stop it. "

m "I felt tired and just wanted to sleep but I knew that this might be my last chance." 

m "I had to make sure that the dragons would survive this timeline. I forced myself to open my eyes to look at Maverick."

Mv recry flip "Don’t you dare die on me now, [player_name]." 

c "Mav, there is something I have to tell you. "

Mv resad flip "That can wait until later. I’m going to get help. "

m "Maverick tried to run away to get help but I weakly grabbed his hand."

c "No, we might not … have much time left. It’s … it’s too important for your people."

m "Reluctantly Maverick stopped and kneeled down next to me."

c "The upcoming danger…the one Reza mentioned. It’s the comet that your scientists had discovered."

Mv "I heard about it in the news but they said it would pass by."

c "No, they made a mistake. The gravitation… of the moon… the comet’s route will be changed. It will cause a global extinction event."

m "It was getting harder and harder for me to talk but I forced myself to continue, fighting the drowsiness."

c "Reza, that bastard…he knew what was about to happen but he only cared …for his own goals." 

Mv reshock flip "Does that mean everything we did was for nothing?" 

c "No, you can still … divert the comet. The underground generator we just saved …you might have enough energy … to save your civilization. You need…"

m "I knew that I’d lose consciousness soon. I didn’t have much time left."

c "Take my PDA to your scientists… it has all the data they need to prove everything… They still have a few weeks left until the comet arrives."

Mv resad flip "You can count on me. I promise you that we’ll save our world."


if maverick_redem_maverickromance == True:

    m "He grabbed my hand with one of his claws and gave it a soft squeeze"

    Mv recry flip "But right now you need my help. I don’t want to lose you."

    m "I knew that it could cause more harm than good, but for once I decided to be selfish. In this timeline the most unpredictable outcome had actually happened."

    m "With my remaining strength I lifted my face toward Maverick’s face and kissed him one last time."

    c "I love you Maverick."

    m "Then the world around me turned black."



elif maverick_redem_noromance == True:

    Mv recry flip "But right now you need my help, so don’t die on me. "

    m "I tried to respond to him but my strength finally left me and the world around me turned black." 


else:

    Mv recry flip "But right now you need my help, so don’t die on me."

    Mv "Just think about [maverick_redem_romance_partner] and how happy [maverick_redem_romance_partner] will be to be with you again. You can’t give up."

    c "I wish …I could have spent more time…with [maverick_redem_romance_partner]…"

    m "I wasn’t able to finish my thought when my strength finally left me and the world around me turned black." 
 

m "I could hear Maverick’s voice in the distance but was unable to make out what he was saying." 

stop soundloop

scene black with dissolveslow

$ renpy.pause (0.5)

nvl clear
window show

n "I once again failed my mission but at least I was able to save Maverick and the dragons in this timeline."

n "I knew that, as long as Izumi was able to travel back in time, there was still a chance for a better outcome. Izumi never cared for mankind and we already had disagreements in a previous timelines."

n "However just like there were subtle differences in each version of me, I also noticed subtle differences about her other than the color of her hair."

n "I could only hope that this version of Izumi was willing to give mankind another chance."

stop music fadeout 2.0

jump redem_chapter5_5






label redem_ending_d:

m "Reza aimed his gun at us. My first instinct was to run away, but as Maverick started charging, so did I."

m "Maverick was fast, pouncing on Reza before he had a chance to pull the trigger."

play sound "fx/snarl.ogg"
show maverick angry flip with dissolve

$ renpy.pause (1.0)

show maverick at Position(xpos=0.65, xanchor='center') with move6

play sound "fx/impact3.ogg"

show maverick at Position(xpos=0.8, xanchor='center', ypos=1.0, yanchor="top")
show reza gunpoint at Position(xpos=1.0, xanchor='center', ypos=1.0, yanchor="top")
with move9

m "He was knocked to the ground and Maverick embedded his teeth into the body before him."

queue sound "fx/bite.ogg"

m "Reza was screaming. He aimed at Maverick's head and frantically pulled the trigger twice."

play sound "fx/gunshots4.ogg"

m "Luckily Maverick was faster and instead of his head, Reza hit Maverick in the chest."

m "Reza aimed the gun at Maverick again but this time I was faster and grabbed his arm."

m "As we were fighting for his gun, I tried my best to aim its muzzle away from me."

m "When I finally got a good hold on it, Reza screamed in pain as I took the gun, breaking one or two of his fingers in the process. However his shock only lasted a few seconds and soon he grabbed the knife he used to kill the dragons."

play sound "fx/gunshot2.wav"

m "I was prepared and shot at Reza’s leg making him fall. He was still holding his knife but there was no way Reza could win anymore. Despite that, neither Maverick nor I dared to lower our guard."

c "It’s over Reza. I have your gun and you’re wounded. Just give up and we can save both worlds."

show reza angry b at right with dissolve

Rz "You ruined everything I've worked so hard for. Do you really think I’d let you have your little happy ending?"

c "Reza, there is nothing you can do anymore."

m "Suddenly I felt a shiver through my body. I knew something wasn’t right but I didn’t know what it was. Then Reza slowly took something out of his trousers' pocket. It looked like a cylindrical object but I didn’t know its purpose."

m "Then I saw the grin on his face and realized what he planned."

c "Maverick, take the generator and get to safety. Now!"

m "The gray dragon looked confused but did I as said while I took a step back from Reza"

Rz "You won't save anyone, traitor. If I can’t have my victory, then I’ll make sure you and those beasts won’t get it either."

m "He lifted the object and pressed on its button. Then it was as if time slowed down."

hide reza angry b with dissolve

queue sound "fx/explosion.ogg" 

stop music fadeout 2.0

m "Realizing the danger Maverick and I tried to escape the explosion of the bomb Reza just activated." with Shake((0, 0, 0, 0), 2, dist=10)

m "Luckily it seemed that the explosion didn’t reach the backup generator which would have caused a second, much stronger explosion."

$ renpy.pause (1.0)

play music "mx/path.ogg" fadein 0.5

m "It seemed the generator room was built with reinforced materials, so no matter what happens now, the backup generator is safe and the portal should still work."

m "Sadly, the same wasn’t true for the rest of the facility."

m "I saw a part of the ceiling coming down, separating me from Maverick. I had been too close to the now broken ceiling."

m "My leg was stuck under the debris but otherwise I was unharmed." 

m "Reza on the other hand was dead, blown apart in his last attempt to kill me and Maverick."

m "Despite trying, I wasn’t able to free myself on my own, so I needed to wait until Maverick would find me."

Mv normal "[player_name], can you hear me?"

c "I’m here Maverick. I was able to avoid the explosion but my foot is stuck. What about the generator?"

Mv rerelief flip "Thank goodness! I feared that I’d lost you there. The generator is next to me and undamaged."

c "Good job on saving it. Without that we wouldn’t have been able to save your people."

Mv normal "Are you talking about that comet Reza was talking about? You mean it is real threat?"

c "Yes, I’ll…"

m "I was interrupted by a sound I couldn’t define. Whatever it was, it was slowly getting louder and somehow it reminded me of a waterfall. Then I remembered the water pockets surrounding the underground facility."

m "In all previous timelines I slowly started to remember, I never re-entered the facility after the generator was destroyed."

m "In one timeline Maverick and I freed Bryce from it but he was close to the exit and on a higher level than I was right now."

m "I looked in the corridors next to me and saw fissures on the walls and water dropping of the leaks. Soon this place would be gone and there was no way to escape."

c "Maverick, my PDA has all the information about the comet I was able to gather. It will be enough to make sure your people will believe you about the threat. I left it with the suitcase containing the eggs."

Mv "I remember but why are you telling me that? Did something happen?"

c "The explosion caused damage facility and its connections to the water pockets. I’m not sure if I can make it out on my own."

Mv reshock flip "Damn it, don’t give up. I’ll free you. "

m "I heard the sound of stones being moved but I knew Maverick wouldn't have enough time left. The sound of breaking walls and water was getting louder and I knew what I had to do."

c "Maverick, please listen to me. Do you remember what I told you last time? That some must live and some must die?"

Mv normal flip "Don’t talk like that. I’m coming for you."

c "I told you that I’d do anything to save your people. If you don’t get the generator out of the facility, it might get damaged and that would be your people's doom."

Mv "I refuse to leave you behind to die!"

c "Mav, you know that I’m right. Take the generator outside."

m "I knew that he wouldn’t just leave me behind so I relied on giving him false hope."

c "You can come back after that and free me. If you’re quick we can make it but you have to stop risking the generator."

Mv normal flip "…ok, I’ll be right back so don’t you dare to give up."

c "Thank you Mav."

if maverick_redem_maverickromance == True: 

    m "I knew it was my last chance and that it might harm Maverick but I couldn't leave my feelings unspoken. Not if I was going to die soon."

    c "I love you."

    Mv "…I … I love you too [player_name]. I’ll be back as fast as possible."

else:

    pass

m "Then I heard him leave. It didn’t take long for the walls to break, releasing a torrent of water. It quickly arrived and hit me with strong force, slamming my head against the debris. Then I could only feel cold and darkness." 

m "I once again failed my mission but at least I was able to save Maverick and the dragons in this timeline."

m "I knew that, as long as Izumi was able to travel back in time, there was still a chance for a better outcome. Izumi never cared for mankind and we already had disagreements in a previous timelines."

m "However just like there were subtle differences in each version of me, I also noticed subtle differences about her other than the color of her hair. I could only hope that this version of Izumi was willing to give mankind another chance."


scene black with dissolveslow

$ renpy.pause (2.0)

scene hallway at Pan((0, 0), (0, 150), 3.75) with dissolvemed

$ renpy.pause (2.0)

c "You can come back after that and free me. If you’re quick we can make it but you have to stop risking the generator."

m "As much as I hated to admit it, [player_name] was right. If our roles were switched, I’d act just like him. Reluctantly, I gave up."

Mv "…ok, I’ll be right back so don’t you dare to give up."

c "Thank you Mav."

if maverick_redem_maverickromance == True: 

    Mv "I love you."

    m "Tears started to fill my eyes. \"Why does the world hates me so much? Why can’t I find happiness without losing it again?\"."

    m "I’d return and free [player name] but if I was too late…I had to tell him how I felt."

    Mv "…I … I love you too [player_name]. I’ll be back as fast as possible."

else:

    pass

m "I grabbed the damn generator and left the facility as fast as possible. Quickly and gently I put the generator down next to the suitcase and made my way back to the underground facility."

scene black with dissolveslow

$ renpy.pause (2.0)

scene np1r at Pan((100, 0), (500, 150), 6.0) with dissolveslow

$ renpy.pause (3.5)

m "(Sebastian, where the hell are you?)" 

play sound "fx/dragonscream.wav"

m "I let out a loud roar, hoping that someone would hear it, and then made my way back down to the entrance. Shocked I saw that there was already water flowing down the holes of the debris."

Mv " [player_name] can you hear me?"

m "Quickly I grabbed the stones and made the hole bigger. I ignored the water that came out of it but soon it was too much and I had to dive to continue my work."

m "(Please let [player_name] be there.)"

m "Then I finally saw him. He had his eyes closed and didn’t move. I desperately needed air but I refused to leave him behind again."

m "With all my might, I removed the stone that trapped [player_name] and freed him."

m "Wasting no time, I grabbed him by an arm and dragged him with me, back to the entrance. It was getting harder and harder to hold my breath but I was able to see the surface."

m "My lungs greeted the fresh air when I finally escaped the water."

m "I laid [player_name]’s body down on the grass and noticed that he wasn't breathing. Carefully I tried cardiopulmonary resuscitation despite our different bodies." 

m "As gentle as possible I pressed his chest and blew air into his mouth but it had no effect."

stop soundloop fadeout 2.0

m "When Bryce, Sebastian and the medical team finally arrived I already knew that it was too late. [player_name] was dead."

m "Once again I was responsible for killing someone I cared for."

m "Bryce and Sebastian, devastated by [player_name]'s death, tried to comfort me but I wasn't in the mood for their caring words. I left as soon as the medics allowed me to go."

m "I took the eggs and carried them back to the hatchery."

m "I also took the PDA with me. [player_name] mentioned that it'd be important if something happens… as if he knew that he'd die."

m "In the end, knowing about the dreams didn't save anyone."

m "If only there would have been a second entry to that damn facility. Then I could have surprised Reza before he used his bomb."

m "Maybe the map he had searched for was for the underground facility. Not that it mattered anymore."

m "After delivering the eggs I went home. I needed rest and a strong drink." 

m "Never did I expect that this day would change everything for me a second time."

stop music fadeout 2.0

scene black with dissolveslow

$ renpy.pause (2.0)

scene redem_maverick_apartment_c with dissolvemed

play music "mx/fragments.ogg" fadein 2.0

m "When I closed the door to my apartment I went straight to the kitchen to get some whiskey. Having just survived one of the worst days of my life and losing a friend were only fitting for my shitty life."

m "Ever since the day Miles decided to take those drugs, my life only got worse. I ended up losing my Miles, my relationship with Anna and now also [player_name]. I just couldn’t protect those I care about."

m "I was about to open the bottle when I heard a sound behind me."

show izumi normal ar right with dissolve

play music "mx/clocks.ogg" fadein 2.0 

As "Good evening Maverick."

Mv angry "I don’t care who the hell you are but I chose the wrong day to piss me off."

m "Angrily I faced the intruder surprised to notice that it was a human. However, I couldn’t care less. Ready to attack I got into position."

if maverick_redem_maverickromance == True:

    As "You wouldn’t hurt the one you love, would you?"

else:

    As "You wouldn’t hurt your friend, would you?"

m "For some reason, I stopped right before attacking. That voice…I’d recognize it anywhere. Then the masked human showed me its face and what I saw was impossible."

hide izumi with dissolve

play sound "fx/undress.ogg"

$ renpy.pause (0.3)

Mv shocked "You're alive?! But how is that possible?"

m "[player_name] put the mask back on and sat down on the couch. Too shocked to know what to do I sat down next to him."

play sound "fx/undress.ogg"

$ renpy.pause (0.5)

show izumi normal with dissolve

Mv "I saw your… body. How can you be alive?"

As "I’m sorry Maverick, but I’m not the [player_name] you know."

Mv reannoyed flip "I’m not in the mood for jokes, not after I just thought that I lost you."

As "Maverick, did you ever figure out why we had those weird dreams or the feeling as if we have to do something without knowing why?"

Mv "No, why do you ask about that now?"

As "The answer is, we already did all of this. What you and the other me experienced were memories of other versions of us, other timelines."

Mv angry "Other timelines? What the hell are you talking about?"

As "In my timeline, we two didn’t talk about the dreams we had but I gave you the map. We went to confront Reza and he killed you."

As "After I saved your species and your… burial, I used the emergency coordinates of the portal to travel back in time."

m "He then took off a necklace he was wearing and showed it to me."

As "Bryce gave it to me after… you know."

m "I tried my best to come up with any idea that might prove this as a sick joke but there wasn’t. What [player_name] showed me were my dragon tags including the damage on one side."

m "It was impossible for him to have them since I never showed him where they were nor what they looked like. Just to make sure I checked my cabinet and there they were."

m "How could there be two sets of my dragon tags? Then I realized that [player_name] would never lie to me about especially not about something like this."

Mv "So you… really are a different [player_name]."

As "Yes, I’m sorry Maverick."

Mv angry "If you had been here along then than why didn’t you help us? Why appear now after all the time? My [player_name] could still be alive!"

As "Taking care of Reza was too important. I had to make sure that you’d get to this day and confront him."

As "In each timeline the current version of me always tries to talk him down because it’s the only way to save your world and mine."

As "I’ve died many times already. I remember each death and each mistake I made."

m "I wanted to be angry at this [player_name] but hearing that he died many times, all to save us and his own people…"

Mv resideeye "How long have you been trying?"

As "We’ve lost count. However, no matter the outcome, it was important that someone stayed alive to use the portal if this world or the human world couldn’t be saved."

As "The me from this timeline must have felt that something bad was about to happen. That’s why he had hid his PDA next to the case with the eggs."

Mv "Yes you… he said that, if something happens, I’d need it."

As "The PDA holds data you need to save your world from the comet. It has a possible plan and calculations your people might find helpful."

As "That’s why you needed to save the generator Reza was trying to steal. Without it, your world is doomed."

As "That’s what happened the first few times… I even experienced it a few times in timelines where one version me used the emergency coordinates while the other stayed behind."

Mv "[player_name] really thought of everything to make sure we’re safe."

As "Unlike Reza or Izumi, the human that taught us about the portal, I’m not satisfied with just saving one world. I always try to save you and mankind."

As "However, with both Reza and the other me gone, there will be no chance left to save mankind. To make sure that Reza won’t escape, I had to delete the coordinates to the human portal."

m "It seems as if I wasn’t the only one who had to make sure that Reza won’t escape. So even after repairing the console [player_name] had found a way to keep Reza here."

m "However, was the portal still working despite the damage of the explosion?"

Mv "The underground facility was heavily damaged. So even if the coordinates were there, can you still use the portal?"

As "The underground facility was built with military standards. That means even if the building is damaged or flooded, the generators are safe and won't take damage as long as they are inside their holding chambers."

As "Izumi had to make sure that the portal would still work even if the facility itself was badly damaged."

As "Even in timelines where the main generator was destroyed and the facility blew up, the portal was still working."

Mv "What about this Izumi? Can’t she help us?"

As "Sadly not. She died a few timelines ago and for some reason I didn’t meet her yet. So until I’ll find a timeline where she’s still alive, I have to keep going back in time."

Mv "So… I guess you’ll leave now?"

As "Yes, but maybe next time we get the outcome that makes all of us happy."

As "However, before I go there is one last thing I need to tell you."

As "The dreams I had a few days before the confrontation with Reza made me think that I might die during the confrontation."

As "It happened before, so at some point, I decided to add information to the PDA I thought helpful… in one way or the other."

As "You’ll find a note about the cancer cure and that it is on the PDAs I’ve bought with me from the human world. That way, Anna can create a dragon version and can heal herself and many others."

As "You just need to make sure that the case against her will be dropped."

Mv "It won’t be easy since some ministers hate her, especially the minister of science, but I’ll try my best."

if maverick_redem_noromance == True:

    pass

elif maverick_redem_maverickromance == True:

    As "There is also a more personal message I’ve left for you. You and I, we shared the same bond in my timeline as you did in yours."

    m "We both looked at each other and we both knew that we felt the same pain because of our loss."


else:

    As "There is also a more… personal message I’ve left for [maverick_redem_romance_partner] in case of my death."


As "Maverick, I know that you’re feeling guilty about the other me’s death but he and I are the same. I knew the risk but I did it anyway. So don’t start becoming all grumpy again like you did after Miles’ death."

As "It never was your fault."

Mv "I can’t promise anything but for you… I’ll try. That’s doesn’t mean that I and the others won’t mourn over your death."

Mv "No matter which timeline you’re in, you’ll always have friends in our world."

As "Thank you Maverick. I promise you that I’ll never give up on getting all of us a happy ending, no matter how long it takes."

Mv "Goodbye [player_name], I’ll never forget either of you."

As "Goodbye Maverick and I hope you’ll finally get the good life you deserve."

hide izumi with dissolve

m "Then he left and I was sure that I’d never meet someone like him again."

m "It was surreal; at first I didn’t believe in humans and then I hated them when they appeared."



if maverick_redem_maverickromance == True:

    m "[player_name] showed me the errors of my thinking but instead of having a future together, fate has taken him away from me."

    m "Instead of drowning my sorrow in alcohol, I took the PDA and read his last message for me. As much as it pains me to read his last words for me, it still comforts me."

    m "When I went to bed I knew that a part of [player_name] would forever be with me and I’d not fall back into my old habits."
 
else:

    m "[player_name] showed me the errors of my thinking but instead of us having a future together as friends, fate has taken him away from us."

    m "Instead of drowning my sorrow in alcohol, I took the PDA and read his notes about the comet. I still had a mission to finish tomorrow."


scene black with dissolveslow

$ renpy.pause (0.5)

nvl clear
window show


if maverick_redem_maverickromance == True:

    n "And thus I had to finish my last mission for [player_name], an unlikely partner who I wished I could have spent more time with."

    n "As soon woke up, I visited the council to tell them about the comet. At first they tried to ignore the threat but the notes [player_name] added quickly convinced them otherwise."

    n "Soon they started their plan to divert the comet and I left again."

    n "I went to Tatsu Park and thought about [player_name]'s last message and our time together. Just like me, he had dreams and hopes for the future but didn't have the time to fulfill them."

    n "Our relationship was short but I’d always keep it in my heart."

    n "\"Some must live and some must die\" … I'd remember his words, knowing that he gave his life for our civilization."

    n "I’d make sure that we'd not waste the chance he gave us and maybe somewhere, sometime all of us would get the happy ending we hoped for."



elif maverick_redem_bryceromance == True:

    n "And thus I had to finish my last mission for [player_name], an unlikely partner who I wished I could have spent more time with."

    n "As soon woke up, I visited the council to tell them about the comet. At first they tried to ignore the threat but the notes [player_name] added quickly convinced them otherwise."

    n "Soon they started their plan to divert the comet and I left with the last message [player_name] left for Bryce."

    n "I made my way to Bryce’s office to deliver [player_name]'s last message. Just like me he had dreams and hopes for the future but didn't have the time to fulfill them."

    n "\"Some must live and some must die\" … I'd remember his words, knowing that he gave his life for our civilization."

    n "I’d make sure that we'd not waste the chance he gave us and maybe somewhere, sometime we all would get the happy ending we hoped for."




elif maverick_redem_noromance == True:

    n "And thus I had to finish my last mission for [player_name], an unlikely partner who I wished I could have spent more time with."

    n "As soon woke up, I visited the council to tell them about the comet. At first they tried to ignore the threat but the notes [player_name] added quickly convinced them otherwise." 

    n "Soon they started their plan to divert the comet and I left again."

    n "I went to Tatsu Park and thought about [player_name]. Just like me he had dreams and hopes for the future but didn't have the time to fulfill them."

    n "\"Some must live and some must die\" … I'd remember his words, knowing that he gave his life for our civilization."

    n "I’d make sure that we'd not waste the chance he gave us and maybe somewhere, sometime different versions of the both of us would get the happy ending we hoped for."


else:

    n "And thus I had to finish my last mission for [player_name], an unlikely partner who I wished I could have spent more time with."

    n "As soon woke up, I visited the council to tell them about the comet. At first they tried to ignore the threat but the notes [player_name] added quickly convinced them otherwise."

    n "Soon they started their plan to divert the comet and I left with the last message [player_name] left for [maverick_redem_romance_partner]."

    n "I made my way to [maverick_redem_romance_partner] to deliver [player_name]'s last message. Just like me he had dreams and hopes for the future but didn't have the time to fulfill them."

    n "\"Some must live and some must die\" … I'd remember his words, knowing that he gave his life for our civilization."

    n "I’d make sure that we'd not waste the chance he gave us and maybe somewhere, sometime we all would get the happy ending we hoped for."






scene black with dissolve
window hide
nvl clear
window show

n "During the following weeks we managed to find a way to divert the comet and, just as [player_name] told me, the underground generator proved to be vital for our plan."

n "On the down side, the inspection of the portal showed what I already knew; the coordinates to mankind were gone."

n "There was no way to fulfill our part of the trade and so the council decided to give access to the PDAs to scientists and scholars. A new age was about to begin for our civilization."

scene black with dissolve
window hide
nvl clear
window show

n "The council also struck true to their word and dropped all cases against Anna. Furthermore they allowed her to study the human's cancer cure and only a few wakes later she developed the experimental version for dragons."

n "Given her condition getting worse by the day, she was the first to test the new cure. She laughed at the irony that she, who did experiments on others, now ended up being the test subject for once." 

n "Surprisingly it worked better than anyone expected despite the difference between humans and dragons and soon cancer was beaten all over our land."

n "It was strange; despite losing [player_name] I didn't fall into depression like after Miles. I mourned his death but it was as if [player_name] had taken all my guilt with him. I was free."


scene black with dissolve
window hide
nvl clear
window show

if maverick_redem_maverickromance == True:

    n "This time, I actually accepted help from my friends. [player_name] and I shared a short but deep love and losing him hurt but I knew he would have wanted me to move on, no matter how hard it was for me."

    n "Anna and I got closer during her cancer treatment and decided to give our relationship a second chance. With her being cured and me focusing on a better life, we might have a chance this time."

elif maverick_redem_bryceromance == True:

    n "This time, I actually accepted help from my friends. Together, [maverick_redem_romance_partner] and I were keeping [player_name]’s memory alive."

    n "Anna and I got closer during her cancer treatment and after month of fighting my guilt over [player_name]'s death, Anna and I decided to give our relationship a second chance. With her being cured and me focusing on a better life, we might have a chance this time."

    n "I’m sure [player_name] would have been happy for us."

elif maverick_redem_annaromance == True:

    n "This time, I actually accepted help from my friends and [maverick_redem_romance_partner] and I were keeping [player_name]’s memory alive."

    n "The time we’ve spent together reignited the flame of our love and we decided to give our relationship a second chance. With her being cured and me focusing on a better life, we might have a chance this time." 

    n "I’m sure [player_name] would have been happy for us."


elif maverick_redem_noromance == True:

    n "This time, I actually accepted help from my friends and together we were keeping [player_name]’s memory alive."

    n "During her cancer treatment, Anna and I got closer and decided to give our relationship a second chance. With her being cured and me focusing on a better life, we might have a chance this time."

else:
    n "This time, I actually accepted help from my friends and [maverick_redem_romance_partner] and I became friends, trying to keep [player_name]’s memory alive. It helped both of us to come to terms with his death."

    n "During her cancer treatment, Anna and I got closer and we decided to give our relationship a second chance. With her being cured and me focusing on a better life, we might have a chance this time."

$ renpy.pause (0.3)

window hide
nvl clear
scene black with dissolvemed

$ renpy.pause (0.5)


window hide
nvl clear
scene black with dissolvemed

$ renpy.pause (1.0)

play sound "fx/system.wav"

s "Good work, you've seen the D ending. Mankind was saved in a different timeline but your sacrifice saved the dragons in this one."

s "I'm sure you can do better."

$ renpy.pause (1.0)

$ persistent.redem_mavbadending = True

jump ml_main_menu








label redem_ending_e:

m "Reza aimed his gun at us. My first instinct was to run away, but as Maverick started charging, so did I."

play sound "fx/snarl.ogg"

show maverick angry flip with dissolve

show reza gunpoint

$ renpy.pause (1.0)

m "Maverick was fast but sadly Reza was faster and pulled the trigger twice."

play sound "fx/gunshots4.ogg"

m "Reza hit Maverick in the chest and the gray dragon fell to the ground, mortally wounded."

hide maverick with easeoutbottom

play sound "fx/impact3.ogg"

m "Reza aimed the gun at Maverick again but I was faster and grabbed his arm."

show reza angry

m "As we were fighting for his gun, I tried my best to aim its muzzle away from me."

m "When I finally got a good hold on it, Reza screamed in pain as I took the gun, breaking one or two of his fingers in the process."

m "However his shock only lasted a few seconds and soon he grabbed the knife he used to kill the dragons. With his knife in his good hand he made his way toward me and I aimed the gun toward him."

m "I pulled the trigger, firing the remaining bullets while aiming at him until no more were left. When I didn’t hear any more gunshots I realized that I had emptied the whole chamber without even noticing."

play sound "fx/gunshots5.ogg"

$ renpy.pause (2.0)

hide reza with easeoutbottom

play sound "fx/impact3.ogg"

m "My hands were shaking when I realized that I just killed someone. Reza’s dead body rested against a wall, his bloody knife lying next to him."

show redem_e_ending at Pan ((0, 326), (580,0), 10.0) with fade

stop music fadeout 6.0

$ renpy.pause (8.5)

hide redem_e_ending
with fade


play music "mx/prayer.ogg" fadein 2.0 

Mv "I didn't know you had that in you."

c "Neither did I."

c "Hold on, I'll get a first aid kit to help you."

m "I hurried to the other room, quickly grabbed the first aid kit and ran back to Maverick. I tried my best to help him but the wounds were too deep and there was too much blood."

m "We both knew that there was nothing I or anyone else could do to save him. Nevertheless, I didn’t want to give up and pressed the panic button on my phone."

Mv "Maverick had shown me how it works, so I was sure that Bryce would soon appear with a medical team here. We just needed some more time…"

Mv "I don’t think that there is anything you can do anymore. I have been in the force long enough to know that my wounds are too bad."

Mv "I kind of had the feeling that I’d die here…"

c "Don't talk like that, Mav."


if maverick_redem_romance_partner == "Maverick":

    Mv "In hindsight, it's kind of funny. When I first met you I was sure that you’d be the same as Reza." 

    Mv "Never would I have thought that we'd become friends or that I'd fall in love with you."

    c "Please Mav, don’t leave me. Bryce and the medical team will be here soon and then we can fix you."

    c "You can’t just leave me alone, Mav."

    Mv "I’m sorry, [player_name]. I wish we had more …time together."

    Mv "I love you, [player_name]."

    m "I gently kissed Maverick on his lips, unable to hold back my tears."

    c "I love you too, Maverick"



else:

    Mv "In hindsight, it's kind of funny. When I first met you I was sure that you’d be the same as Reza. "

    Mv "Never would I have thought that we'd become friends or that I'd protect you from that freak."

    c "Mav, you have to stay strong. Bryce and the medical team will be here soon and then we can fix you."

    c "You can’t just leave you partner alone, can you?"

    Mv "I’m sorry, [player_name]. I really enjoyed …our time together. "

    m "I touched Maverick’s hand, unable to hold back my tears"

    c "I also enjoyed our time together. You were the best partner I could’ve ever asked for."


hide maverick normal flip at left with easeoutleft

scene black with dissolveslow

$ renpy.pause (0.5)

nvl clear
window show

n "A few minutes later Bryce, Sebastian and the medics finally arrived but it was already too late. Maverick had lost too much blood and there was nothing the medics could have done to save him."

n "All we were able to do was to be by his side when he closed his eyes for the last time."

n "I knew that, despite saving the dragons, this timeline was also a failed attempt to save everyone. Maverick was dead and the coordinates to my people were deleted."


scene black with dissolve
window hide
nvl clear
window show


n "During the following weeks I managed to convince the council about the threat of the comet. With the help of the underground generator they were able to divert it, saving their civilization."

n "With some help from Bryce and leaked information about Anna’s condition, I was also able to make sure that the case against her was dropped. As much as some of them hated Anna, they realized that she was worth more alive than dead."

n "Despite some light punishment, Anna was allowed to work on the human cancer cure and soon she was able to develop a new version for the dragons. "

n "As for me, I made my way to the portal, knowing that I had a mission to finish. This time I had to make sure that we all would get out happy ending."

window hide
nvl clear
scene black with dissolvemed

stop music fadeout 1.0

$ renpy.pause (1.0)

play sound "fx/system.wav"

s "Something went wrong; you've seen the E ending. Mankind was saved in a different timeline but your sacrifice saved the dragons in this one."

s "Try again and maybe you can get a better ending."

s "I'm sure you can do it."

$ renpy.pause (1.0)

$ persistent.redem_mavbadending = True

jump ml_main_menu








label redem_ending_f:

m "Reza aimed his gun at us. My first instinct was to run away, but as Maverick started charging, so did I."

play sound "fx/snarl.ogg"

show maverick angry flip with dissolve

show reza gunpoint

$ renpy.pause (1.0)

m "Maverick was fast but sadly Reza was faster and pulled the trigger twice."

play sound "fx/gunshots4.ogg"

$ renpy.pause (1.0)

m "Reza hit Maverick in the chest and the gray dragon fell to the ground, mortally wounded."

hide maverick with easeoutbottom

play sound "fx/impact3.ogg"

m "Then he aimed the gun at Maverick again but I was able to grab his arm before he could pull the trigger again."

show reza angry

m "As we were fighting for his gun, I tried my best to aim its muzzle away from me."

m "However, Reza was stronger and I suddenly heard a gunshot followed by a burning pain in my chest."

play sound "fx/gunshot2.wav"

$ renpy.pause (1.0)

m "All of my strength disappeared and I fell on the ground, unable to move."

m "I heard Reza’s footsteps walking away from me and toward Maverick who was still lying on the ground."

m "I tried my best to move my head only to see Reza with a victorious smile on his face aiming at Maverick’s head again."

Rz gunpoint b "This is the last time you stand in my way you annoying beast."

Mv angry "You should have gone for the head."

m "Before Reza was able to fire his gun, Maverick had already opened his mouth and was letting out an inferno that burned Reza's upper body."

play sound "fx/fire.ogg"

$ renpy.pause (1.5)

m "He didn't even have a chance to scream before the flames killed him."

hide reza with dissolve

stop music fadeout 6.0

show redem_good_ending at Pan ((0, 326), (580,0), 10.0) with fade

$ renpy.pause (8.5)

hide redem_good_ending
with fade

play music "mx/sad.ogg" fadein 2.0 


m "I used all my strength to stand up and go to Maverick. Both of us had been mortally wounded and I knew that we'd die here."

m "When I finally reached Maverick I collapsed next to him and we looked at each other."

Mv "Damn, that bastard got me good. Don’t think I’ll make it. How are you, [player_name]?"

c "Same as you I fear."

Mv "I’m sorry I wasn’t able to protect you."

c "It’s not your fault, Mav."

m "I looked at the body of Reza, his upper half burned. We had saved the dragons but Reza made sure we’d follow him."

c "At least we got the generator and dealt with Reza. "

Mv laugh flip "Always the optimistic one, aren’t you?"

m "He tried to laugh but I could see the pain he left on his face."

Mv normal flip "…but, you’re right."

c "If only there would have been a way to be more prepared… we could have made it out alive."

Mv "A different access to surprise him would have been nice…"

c "I had a strange dream that …one of us could die here but I ignored it, thinking it were just nightmares… caused by the case."

c "It seems… those dreams were more than just… imagination in the end."

Mv "We both were wrong about those dreams…"

Mv "…damn it; I never expected to die like this… killed on the job and taking my partner with me."

Mv "I might be the worst officer out there."

c "No, you are the best one… you saved your whole species."

c "Not sure if your kind believes in… heaven and hell but saving a whole species… has to be a free ticket to heaven."

Mv laugh flip "We actually do."

Mv normal flip "It is part of… the creation myth… maybe the only part I kind of believe in. It gave me hope that… I’d be able to see my friends and family again after death…"

Mv "I don't know if dragons… and humans share the same heaven… but if we do… meet me at the bar. Drinks are on me."

c "Maybe we can go… hiking there, too. It was one of the best days… of my life."

m "We both laughed, knowing that no matter where we'd end up, we would have each other’s back."


if maverick_redem_romance_partner == "Remy":

    m "Realizing that I’d die here made me think of Remy."

    m "I had enjoyed the time we spent together and I knew that I was in love with him."

    m "Yet, he was doomed to lose the second person he fell in love with and I feared that he would not be able to handle the situation."

    m "I was just glad that he and Adine were friends again. She would be there for him when he'd get the news of my death."

    m "Remy needed someone in his life who cares for and loves him and even if I had hoped that I would be this person, I hoped that he’d find someone he loves."

    m "Maverick tried to get my attention and I realized that I was lost in my thoughts for a moment."


elif maverick_redem_romance_partner == "Anna":

    m "Realizing that I’d die here made me think of Anna."

    m "I had enjoyed the time we spent together and I felt bad for not calling her last time. Luckily I added the note about the cure to my PDA."

    m "I knew the council would try it’s hardest to punish her but with the data of the comet and the cure, I hoped that Emera would use her power to fulfill my last wish and convince the other council members to drop the case against Anna."

    m "Even if I would be gone, Anna would survive. I wished for her to find true happiness and maybe she’d even remember me as someone who cared deeply for her."

    m "Maverick tried to get my attention and I realized that I was lost in my thoughts for a moment."


elif maverick_redem_romance_partner == "Adine" :

    m "Realizing that I’d die here made me think of Adine."

    m "I had enjoyed the time we spent together and felt bad that I didn’t go to the festival with her to see the stunt show. "

    m "Sebastian never called me about Adine in this timeline, so I was sure that she realized that she was in no condition to fly."

    m "I wanted to be by her side, comforting her but fate sadly had other plans for us."

    m "If felt bad for not being able to tell Adine my true feelings but I hoped that she'd get my last message."

    m "She would feel bad to lose a friend… or maybe even the person she loved but I was sure that she’d be able to find happiness."

    m "She was the sweetest, most caring person I’ve ever met and I knew that she’d find true love someday."

    m "Maverick tried to get my attention and I realized that I was lost in my thoughts for a moment."

else:

    pass


Mv "We have to call Bryce… before it’s too late."

m "I gave him a weak nod and took the phone he gave me to call Bryce. There wasn't much time left for the two of us."

Br laugh "Hi [player_name], how are you?"

Br flirty "I hope you and Maverick aren’t having too much fun all alone."

c "..."

Br normal "Hello, can you hear me? Is everything alright?"

m "I took a deep breath and tried my best to stay awake."

c "Bryce… we finally got Reza… he's dead."

Br stern "What happened? Where are you?"

c "The underground facility. Maverick and I… Reza got us good… we… won't make it."

Br normal "Don't talk like that, I'll contact the medical team and we'll get to you as fast as possible."

Mv "Just listen… Bryce. It's… important."

Br sad "Damn it Mav, if you talk like that… go on then."

c "I left my PDA at the portal next to a… suitcase full of stolen eggs… give it to the council."

c "There's information about the disaster Reza mentioned… a comet."

Mv "… it will kill all of us… but we got the generator. Our people… can be saved."

m "I could hear other voices in the background; it seems as if Bryce still hoped that he'd be able to save us."

c "We saved the generator… Reza tried to take."

Mv "This one is more advanced… it's the only way to divert the comet."

Mv "We're sorry Bryce… Reza was more dangerous than we thought… "

c "At least I was able to get Sebastian… out of harm’s way… Reza had the advantage and… Seb could've gotten hurt, too."

Br sad "The team is on the way. They'll save you and then we all go drinking again."

c "You're drinking too much… you should take better care of yourself."

Br sad "I will but then we need to do something else. Just keep talking to me you two… "

if maverick_redem_bryceromance == True:

    c "I always loved… to spent time with you, Bryce… I wish we had… more time together."

    Br sad "I was also having fun… I… I love you [player_name]."

    m "Tears filled my eyes when I heard those words. If only there would have been a way for Mav and I to survive this."

    c "I love you too, Bryce."

else: 

    pass


m "Suddenly the phone felt like it would weight a ton and I couldn't hold it anymore." 

m "I knew that it was all over but I couldn't stop being afraid. I could feel Maverick's hand and he looked at me. My voice was barely a whisper by now but Mav was still able to hear me."

c "I'm afraid… "

Mv "Me too [player_name] but whatever happens, I'll be by your side. We'll be together."

m "Even if I didn't know what awaited us I felt safe with Maverick by my side."

if maverick_redem_maverickromance == True:

    c "I love you, Mav. "

    Mv "I love you too, [player_name]."

    m "Ignoring the pain we gave each other one last kiss."

    m "He was holding my hand and we looked at each other, wishing to have more time together. I gave his hand a soft squeeze and he gave me a sad smile. We didn't need any words anymore."

    m "I smiled at him one last time before we both faded away, ready for whatever waited for us."

    c "Partners forever."

else:

    c "Partners forever."

    m "Maverick was holding my hand and we silently looked at each other. I gave his hand a soft squeeze and he gave me a sad smile. We didn't need any words anymore."

    m "I smiled at him one last time before we both faded away, ready for whatever waited for us."


Br "Are you still there [player_name]? Maverick, please answer… "

m "Emptiness filled my mind and I hoped that Izumi would give mankind a second chance. Hopefully she would travel back in time to give us a better ending."

Br sad "… please, don't leave me alone you two… "


stop soundloop

scene black with dissolveslow

$ renpy.pause (0.5)

nvl clear
window show

n "When Bryce and his team finally arrived they only found the dead bodies of Maverick, Reza… and my other self."

n "Just like in the other timelines, I wasn't able to help them. Without Izumi, I was the last person left to save both worlds and I couldn’t risk ending the cycle by dying."

n "Seeing the reaction of my friends when they found the bodies of their deceased friends wasn't easy but I had to stay behind and make sure that at least this world was saved."

n "It wouldn't be easy for my friends and they had hard times ahead of them but I was sure they'd be able to move on someday."

scene black with dissolve
window hide
nvl clear
window show

n "The council believed the data of my other self's PDA and together with the generator they were able to divert the comet. The data also helped to make a cure for cancer, saving Anna and many other lives."

n "I on the other hand was doomed to travel through the portal once more."

n "Maybe next time we'd get a better ending."

$ renpy.pause (0.3)

window hide
nvl clear
scene black with dissolvemed

stop music fadeout 1.0

play sound "fx/system.wav"

s "You've seen the F ending. Mankind was saved in a different timeline but your and Maverick's sacrifice saved the dragons in this one."

s "Did you try to fail on purpose? Maybe you should try again."

s "I'm sure you can do better."

$ renpy.pause (1.0)

$ persistent.redem_mavbadending = True

jump ml_main_menu
