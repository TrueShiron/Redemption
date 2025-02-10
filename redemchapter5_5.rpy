label redem_chapter5_5:


if adinestatus == "abandoned":

    $ adinestatus = "good"

else:

    pass


if annastatus == "abandoned":

    $ annastatus = "good"

else:

    pass

if brycestatus == "abandoned":

    $ brycestatus = "good"

else:

    pass

if naomistatus == "abandoned":

    $ naomistatus = "good"

else:

    pass


if remystatus == "abandoned":

    $ remystatus = "good"

else:

    pass


scene black with dissolveslow

$ renpy.pause (0.5)

nvl clear
window show

play music "mx/flashback.ogg"

n "Despite not feeling any pain from my wound, there was a different feeling. It was as if someone or something was grabbing my shoulders. There also was a mix of mumbling as if two or more people were talking but I couldn’t understand a single word."

n "I never expected death to be like this but maybe I was in hell. Although I couldn’t remember any details, I knew that I failed to save the dragons several times. I saw my friends die and because of me trying to save everyone my actions only caused their death more than once."

n "As if the fog in my mind lifted a little I remembered other timelines and how Maverick and I opposed each other. I saw myself with Reza’s gun in my hands, killing Maverick after he murdered Izumi while it felt that, in a different and way older timeline, Maverick had killed me one time. I was almost able to feel his teeth on my neck." 


scene black with dissolve
window hide
nvl clear
window show

n "It was as if we were puppets in Izumi’s scheme to save the dragons; having the illusion of being free to make our own decisions but in truth we were on strings that forced us to go against each other until we saved both worlds. At least in this timeline I thought that we were able to cut the strings."

n "We made peace with each other and as partners we confronted Reza together. In the end however, we still didn’t get a happy end and I failed to save mankind."

n "I saw images of our time in this timeline again and again while short, annoying beeping sounds appeared. The more I tried to ignore them the louder and painful they got."


scene black with dissolve
window hide
nvl clear
window show

if maverick_redem_noromance == True:

    n "I tried ignore it, forcing myself back to the emptiness and my memories of my friends but it only caused the beeping sounds to become longer, like an endless sound. A painful shock went through my whole body and suddenly, the noise changed back to the short beeping sounds. When I tried to do it a second time the result was the same."

else:

    n "I tried ignore it, forcing myself back to the emptiness and my memories of [maverick_redem_romance_partner] and my other friends but it only caused the beeping sounds to become longer, like an endless sound. A painful shock went through my whole body and suddenly, the noise changed back to the short beeping sounds. When I tried to do it a second time the result was the same."

n "It seems there was no way to escape the noise so I started to accept it. Slowly the pain went away and after some time it felt as if I was lying on a cloud. Calming warmth came from my side and grabbed my hand. Suddenly, if felt as if the emptiness around me was taken over by light."

n "Powerful claws grabbed and lifted me out of the cold darkness back into the warmth of the world."


window hide
nvl clear

stop music fadeout 1.5

scene black with dissolvemed



$ renpy.pause (1.5)

scene redem_hospital_a with dissolvemed

play music "mx/eveningmelody.ogg" fadein 2.0

m "Slowly I opened my eyes and found myself in an unknown environment. It took me a few seconds to realize that I was lying on a bed."

show anna normal b at right with dissolve

$renpy.pause (1.0)

An smirk b "Well, look who is back. Good morning, squishy."

m "It took me a while to realize that I wasn’t dead but in a hospital."

c "Anna?"

An smirk b "Good, it seems your memory is still working."

c "How long was I out?"

An sad b "Three years."

c "What…?"

show anna sad b 

$ renpy.pause (2.0)

show anna smirk b with dissolve

m "Despite the situation I couldn’t help but laugh at her joke."

c "You’re such a jerk."

An smirk b "Thank you."

m "I tried to make a move but quickly regretted it when the pain hit me."

An normal b "Careful, your wound still hasn’t completely healed."

m "As gently as possible Anna helped me to sit up. I was surprised to see that I even had similar hospital clothes on as back home."

m "It seems as if someone had told them that humans were always wearing some sort of clothes."

if maverick_redem_maverickromance == True:

    c "Where is Maverick? "

    An smirk b "My, my, not even awake for a minute and already asking for Maverick? I should be jealous but I’m happy for you two."

    m "I felt my cheeks burning but luckily Anna didn’t made further comments."

    An normal b "It’s been a week since you two stopped that jerk Reza. Maverick’s wounds have mostly healed and he’s helping Bryce with the investigation of the portal." 

    An sad b "They want to make sure that Reza didn’t leave any more presents behind like the bomb he was carrying with him."

    An face b "Seriously, it’s a miracle that Maverick’s fire didn’t cause it to ignite."

    c "I’m glad that he’s able to work again. When I saw him last time… I didn’t know how bad his wounds were."

    An normal b "Oh, don’t get any wrong ideas. Usually he’d still be on sick leave but since your operation he was always by your side."

    An "We were worried about his recovery and Bryce almost had to drag him out of your room. He doesn’t often show his emotions, but he’s a real softie when he cares for someone."

    An "The work is more to distract Mav and force him to focus on his own recovery."

    An "Don’t worry; he’ll visit you as soon as his shift has ended."  

    c "Thank you. Being worried all the time can’t be good for your health."

    An face b "That’s what we tried to tell him but you know how grumpy he can get."

else:

    pass


c "What happened after we stopped Reza? "

An normal b "Oh that’s a good story. After Maverick called the medics they tried and failed to fix your wound. So they had to call the only dragon that had some knowledge on human biology…"

An smirk b "…yours truly."

An "However you didn’t make it easy and really wanted your beauty sleep."

An sad b "We almost lost you there."

m "It took Anna a few moments to continue and I had time to realize how close it must have been for me to die."

An normal b "Luckily you had me to fix you up and after you started to act like a good human, we were able to close your wound. Although we had to improvise to make it work. "

c "Improvise how? I hope I’m not growing a tail or something…"

An smirk b "Oh, you don’t like tails? They are pretty useful and you could use some extra help for your squishy human body."

c "Anna…"

An normal b "Okay, okay. Well, you had lost a lot of blood and obviously we didn’t have any banked human blood."


if blood == False:

    An sad b "Since you didn’t gave me any blood when we first met I wasn’t really sure if there was a way to save you."

    An "We were desperate so I used a method I developed years ago and used dragon blood, hoping that it would work."

    c "Well, I’m alive and well thanks to your quick thinking."

    m "Anna had an unreadable expression and tried to avoid my gaze. It gave me a bad feeling but I had faith in Anna’s abilities."

    An normal b "You know, blood transfusion between different species usually wouldn’t work, even with the method I used. So far, you body accepted the blood without any problematic complications but we need to keep an eye on you for any possible reactions from your body."

    m "While Anna didn’t understand how this was possible, I knew how Izumi created and modified the dragons. However, even with this knowledge it was surprising to realize how similar our two species were and that, with some modifications, even a blood transfusion seemed to be possible."

    c "What kind of {i}complications{/i} are we talking about? "

    An sad b "To be honest, I don’t know. It could just be you feeling dizzy or tired but it could also be worse. There shouldn’t be any lethal complications but, truth to be told, the chances aren’t zero." 

    An normal b "We’ll have to do several checkups for the next few weeks to see how your body reacts to the transfusion. This is a unique situation and we might have to adjust your medication to reduce the risks."

    An "However, just in case, I already started to create artificial human blood with a sample I took. Although I really hope we don’t need to do an exchange transfusion."

    c "Thank you, Anna. I’m sorry that I didn’t give you any blood when you asked me."

    c "For more reasons than just my current situation."

    An normal b "It would have made everything easier but I understand your reasons. We had just met and there was no way for you to make sure I wouldn’t use it for anything bad. "

    $ maverick_redem_complications = True


else:


    An "Luckily, thanks to analyzing the blood you donated, I was able to use a method I developed years ago to use dragon blood. Surprisingly you humans have similar blood groups as us so it was easy. "

    An "Well, at least for someone who knows what she was doing."

    An "Usually blood transfusion between different species wouldn’t work, even with the method I used, and it was more or less a desperate attempt. However, for some reason you body accepted the blood without any dangerous complications."

    m "While Anna didn’t understand how this was possible, I knew how Izumi created and modified the dragons. However, even with this knowledge it was surprising to realize how similar our two species were and that, with some modifications, even a blood transfusion seemed to be possible."

    c "Wait, you said {i}any dangerous complications{/i}? So there are some? "

    An "Yes, but we were able to reduce the effects. You might still feel a little tired or dizzy for some time but I already planned and prepared the right medication for you so you won’t suddenly collapse or something like that." 

    An "However, I’d still feel better if we’d do some checkups for at least the next few weeks, just to be safe. There might be other side effects that might occur and I want to be prepared."

    c "Thank you, Anna. I prefer feeling dizzy or tired over… well, you know. "

    An "You know, just in case, I already started to create artificial human blood. If you want to stay here for longer it’s better to be prepared for all situations."

    c "Better safe than sorry."

    An smirk b "You’re reading my mind."

    $ maverick_redem_complications = False


c "…but I interrupted you. What happened with Maverick and the comet? "

An normal b "While we were saving your life, Maverick was waiting outside the whole time. He then gave his report to Bryce and the council but they had problems understanding the information they needed." 

An "Luckily they used their brains for once and our scientists quickly confirmed your warning."

An "They’re already working on the plan to divert the comet as soon as it is within reach."

An "The bad news is that you won’t be able to return home until the comet is diverted because they need all the energy they can get. Not that you’re in any condition to leave the hospital for now."

c "I’m glad your council was listening to Mav." 

An "Yeah, not even they are stupid enough to ignore a possible mass extinction event." 

m "Anna avoided her gaze as if she wasn’t sure how to continue. When she looked at me again she seemed unsure."

An smirk b "There also was another interesting bit of information on your PDA."

c "What do you mean?"

An sad b "It seems as if Maverick told you about my… condition. Before he handed your PDA to the council he found some notes you made."

m "Anna turned away and looked out of the window. By the look of the sky I guessed that it was noon or early afternoon but right now I only cared for Anna."

m "Then Anna spoke again and for the first time since I knew her, Anna’s voice became almost a whisper but also hopeful."

An sad b "Do you guys really have a cure for cancer?"

c "Yes, we have one. It took us a long time to develop it but as soon as we have the generators we should have enough energy to produce it again. "

m "Although it was true that we could cure Anna on the other side of the portal I didn’t know the condition of the coordinates in this timeline."

m "I had the feeling that this wasn’t the first or even second attempt to save the dragons and mankind. If Izumi deleted the coordinates then there was only one other option left. "

c "However, with the threat of the comet we should first try to check the PDAs I brought with me." 

c "Part of the trade was to give your people all the knowledge we had to offer and despite the difference of our anatomy, the medical data was also included."

An normal b "Do you really think our council would let me use the PDAs when they’re trying to get me into prison?"

c "Anna, you saved my life. I’m sure that saving an ambassador from a different world is a good reason for dropping any cases against you. I won’t let you die because of some stupid political games."  



if maverick_redem_annaromance == True:

    An smirk b "If you don’t stop, I might get attached to you."

    c "I wouldn’t mind that."

    if anna3unheard == False:

        An sad b "You know, that day when the cops raided my place I was calling you but you never called back."


    else:

        An sad b "You know, that day when the cops raided my place I was thinking about calling you but I wasn’t sure how you’d react."

    c "I’m sorry, Anna. I wanted to call you but …"

    An normal b "You don’t have to apologize. Maverick already explained everything to me."

    c "I know but I still feel bad about it. " 

    An "You should know me a little by now; people hate me and I hate people. There were only a few exceptions in my life like Maverick. When they told me that I got the same sickness I tried to cure, my life turned into a living nightmare."

    An sad b "I broke up with him because I knew the chances of me finding a cure weren’t as good as I hoped. He would have stayed by my side, I would have gone through the treatments but in the end, he would have seen me die a painful death."

    An "It wasn’t the best way but I broke up with him over the phone, hoping it would hurt him less than seeing me suffer and die… little did I know that only a short time later he’d be forced to kill his own brother."

    c "I remember what you told me and Maverick added a few parts to the story. Was there a way for Maverick to save Miles? "

    An normal b "For Maverick there wasn’t. Not at that point of Miles’ sickness. If the doctors wouldn’t have messed up, then Miles could still be alive but the medication was wrong."

    An "Miles was already lost when they found him. Killing him was an act of mercy, as cruel as it sounds. With all our technology, there was no way for us to bring him back after his brain had degenerated that far."

    c "Maverick told me that they had developed a cure for the sickness by now."

    An "That’s true but what he possibly didn’t tell you was that he allowed the doctors to do tests on Miles’ body. He wasn’t the only one with this sickness but his condition had been the worst known case."

    An "The data the doctors gathered from Miles’ body ultimately helped them to fully understand how the sickness was working and how to cure it. Even if there are only a few cases, Miles’ death helped to save other families from the same fate."

    m "Anna smiled sadly, looking out of the window."

    An sad b "That’s typical for Miles; even after his death he was helping those around him, even while Maverick and I were mourning over his death."

    An "I tried to comfort Maverick after it happened but I knew that I had to continue with my work if I wanted to survive. You can guess what happened after that."

    An "The media, the council and everyone else began to stand in my way and tried to ruin everything I was working for. They almost got me and I had to get rid of anything they could use against me."

    An "I escaped prison the first time but the punishment still held me back and I had to make a deal with Damion."

    An disgust b "I gave that piece of shit what he wanted as long as I was able to work on that cure but in the end I failed. Even after his death Damion was able to ruin everything and the council tried to lock me up."

    An smirk b "That was before I saved your butt."

    if anna3unheard == False:

        An sad b "However, that night I realized that I started to care for you and when you didn’t call back…"

        An face b "I know that I was a pain to deal with and I used you for my own goals but for some weird reason, you always came back to me."

    else:

        An sad b "However, that night I realized that I started to care for you but I wasn’t sure how you felt about me… "

        An face b "I know that I was a pain to deal with and I used you for my own goals but for some weird reason, you always came back to me."


    c "Well, I love spending time with you."

    An sad b "Said no one ever."

    An "I knew that, one way or the other, it wouldn’t last. You’d go back to your world and I’d die in prison."

    An "I guess I was afraid that you’d also reject me like everyone else or worse, that you actually cared about me but gave up because of me pushing you away."

    c "I’d never hurt you on purpose Anna. I’m far from perfect and there are things I need to tell you when I’m out of here but I care for you."

    c "Everything has changed now. You won’t die and the council will have to drop all cases on you."

    An sad b "But as soon as your mission is over, you’ll leave."

    c "I doubt that it’s a good idea for me to return home after everything that happened. My people most likely won’t be happy about Reza’s fate so returning home might be bad for my health."

    An disgust b "Wait, you really think your own people would kill you for saving us?"

    c "When Maverick and I were working on the Reza case we found some information and then, during our final confrontation, Reza mentioned a few things."

    c "By now I’m sure that I’d have some sort of unfortunate accident some time after my return. Reza most likely wasn’t working alone and even if my people didn’t agree to the murders, they still agreed with working behind the scenes like stealing generators."

    c "So I think that I’ll still try to do my job as an ambassador and make the trade happen, but after that I’d stay here." 

    An normal b "Seems as if politicians are assholes in every world."

    m "With a smile on her lips she moved her head closer to me."

    An smirk b "Then I can have you all for myself, [player_name]."

    c "I wouldn’t want it any other way, Anna."

    $ renpy.pause (1.0)

    play sound "fx/knocking1.ogg"
    
    show anna disgust b with dissolve
    
    m "Suddenly someone knocked on the door and Anna moved her head back, giving the door a deadly glare. So close and yet so far away from her…"

    $ renpy.pause (1.0)

    play sound "fx/door/door_open.wav"
    
    $renpy.pause(2.0)
    
    show maverick rehappy flip at Position (xpos = 0.1) with easeinleft
    
    $ renpy.pause (1.0)

    m "Maverick opened the door and entered the room. As happy as I was to see him, I was still a little mad at his timing. I just hoped he didn’t see anything but my hopes where crushed when he looked at Anna and me."

    Mv laugh flip "I hope I’m not interrupting something."

    An smirk b "Actually, you are but I’ll let it pass this time since you helped to save [player_name]."

    m "I felt my face turning red again and Maverick started to laugh when Anna was giving me a kiss on the check didn’t help either."

    play sound "fx/kiss.wav"

    $ renpy.pause (1.0)

    m "Luckily the whole situation quickly changed back to normal although I’d prefer to spend more time alone with Anna, now that I knew how she felt about me."

else: 

    play sound "fx/knocking1.ogg"

    $ renpy.pause (1.0)

    show anna disgust b with dissolve

    m "Suddenly someone knocked on the door and Anna and I looked at the door."

    m "Maverick opened the door and entered the room. It was good to see that he was doing well despite his second injury since Reza had appeared here."

    show maverick rehappy flip at Position (xpos = 0.1) with dissolve



Mv rehappy flip "[player_name], I’m glad you’re finally awake. "

$ renpy.pause(0.4)

play sound "fx/door/door_close.ogg"

$ renpy.pause(1.0)

m "Maverick closed the door and sat down next to Anna and my bed. It didn’t take a genius to notice that he felt bad for what happened at the facility."

Mv normal flip "I was worried sick the whole time. I saw how you…"

Mv reshock flip "Damn it, I saw you die when they brought you here! "

Mv "If I’d been more careful you might have never got hurt but instead I messed everything up!"

m "I’ve never seen Maverick like that and took his hand to calm him down. Even Anna was there to comfort him. Despite everything that happened between them, they still cared for and helped each other."

show maverick normal flip with dissolve

c "I know that you’ve been scared and I felt the same when I was down there. I thought that I’d die but the thought that you and this world were safe made it easier for me even if I was afraid. "

c "In the end, we were able to take down Reza and save your species. I guess, the way it happened might have been the best possible way to solve the case. "

m "I could see that Maverick wanted to say something but we both knew that things could have gotten way worse if he wouldn’t have trusted his feelings or if I never gave him the map."

m "It was as if we both knew that we could have died down there if our decisions had been different. Not that it made any of us feel better."

m "Each decision I made had brought us here and I really hoped that I’d never again had to decide the fate of my friend’s lives once all of this was over."

m "It also made me realize how important it was to trust my feelings even if I kind of betrayed Bryce’s and Maverick’s trust when I made a copy of the map without asking them."

c "(The next time we’re out drinking I’ll have to buy the drinks for us as an apology.)"

c "You know, I guess you were right about Reza; everything that happened since the solar flare had broken him. He was nothing more than a shadow of who he once was. "

An disgust b "Even then he had the choice to move forward like you did but instead he chose to murder innocent people." 

Mv laugh flip "I never thought you of all people would count Damion as innocent. "

An smirk b "You’re right, my bad; he killed innocent people and Damion."

c "I guess I now can understand why you hated him so much. Being an asshole is one thing but trying to hire a murderer…"

show maverick normal flip with dissolve

An rage b "Yeah, Mav told me about his plan. Heck, after everything he did I should have known that Damion would find a way to stoop even lower. That piece of shit got what he deserved. "

Mv normal flip "It would have been better if no one had died but who knows what else Damion would have tried."

m "I noticed that Anna avoided eye contact with Maverick and me and wondered how bad Damion really had been. Luckily, it didn’t take long until Maverick broke the silence. "

show anna sad b with dissolve

Mv "I… heard what Reza said, how your life was on your side of the portal."

Mv "I guess you had more than one reason to break down like he did but you chose to move forward without losing yourself." 

c "You’re right; my life wasn’t easy since the flare. I lost almost everything and everyone I loved and more than once I asked myself why I didn’t end up like so many of the lost souls. " 

c "Maybe, deep down, I thought that things would work out in the end. "

show anna normal b with dissolve

Mv "It takes a strong will to stay positive but you managed to not only stay true to your morals but also were able to save two worlds. " 

Mv "Despite Reza’s actions, the council decided to keep their word and deliver the generators as soon as the comet is diverted. "

m "I had the feeling that this would never happen and that the connection to mankind was already gone but decided to keep it a secret for now. We all needed some time to recover from what happened."

c "Despite everything he’s done I hope that Reza will find his peace. "

Mv "I agree although I’m glad it was him and not us. "

An "As much as I hate to break this moment, it’s better to let [player_name] rest now. He still needs to recover from everything that happened. "



if maverick_redem_annaromance == True:

    Mv laugh flip "You just want to spend some more time alone with [player_name]. "

    An smirk b "As much as I want to, I’m responsible for taking care of him and he needs to rest. " 

elif maverick_redem_maverickromance == True:

    Mv laugh flip "I know you too well to argue with you, Anna."

    An smirk b "That’s good to hear. After all, as the only expert on humans I’m responsible for taking care of him and he needs to rest. " 

    show maverick rehappy flip with dissolve

    m "Maverick came closer and we shared a kiss. I didn’t want him to leave me alone again but I knew Anna only wanted what was best for my recovery. "

else:

    Mv laugh flip "I know you too well to argue with you, Anna."

    An smirk b "That’s good to hear. After all, as the only expert on humans I’m responsible for taking care of him and he needs to rest. " 

Mv rehappy flip "I’ll come back tomorrow, [player_name] and don’t worry; I’ll let the others know that you’re better."

c "Thanks Mav, see you tomorrow."

An normal b "Goodnight Maverick."

Mv "Goodnight [player_name] and Anna."

show maverick normal with dissolve

play sound "fx/door/handle.wav"

$ renpy.pause(1.)

hide maverick normal at left with easeoutleft

$ renpy.pause(1.0)

play sound "fx/door/doorclose3.wav"

$ renpy.pause(1.0)

m "While I saw Maverick leaving the room, Anna was preparing a syringe. "

c "What is in that syringe?"

An "It’s something that helps you sleep. You still need to rest and I don’t want you to overwork yourself."


if anna3unplayed == False and mp.needles != "yes":

    An smirk b "I hope you didn’t develop a fear for needles since last time."

    c "It’s less about the needle it's just…"

elif anna3unplayed == True:

    An normal b "Don’t worry, I’ll be careful."

    c "Thanks but it’s less about the needle it's just…"

else:

    An normal b "I know you don’t like needles but I promise I’ll be careful."

    c "Thanks but it’s less about the needle it's just…"

m "I wasn’t able to finish that sentence. There wasn’t any danger and I knew Anna was right but I still couldn’t get rid of my fear."

An normal b "You can tell me everything. I won’t make fun of you, I promise."

c "I’m afraid to fall asleep again, knowing that I actually died. I… I can’t stop asking myself what’ll happen if I won’t wake up anymore."

An sad b"I know how you feel. To tell you the truth; I’ve been afraid since the day I got my diagnosis."

An "I wasn’t in your position but the fear of going to sleep and never waking up again is still there. My doctor, Dr. Valedo, always assures me that it’s normal and that I still have time but… it doesn’t really help."

c "How do you deal with those thoughts?"

An "I don’t stop working until I’m more or less too tired to think anymore. I know that it’s bad for my health but I guess I’m too afraid to get lost in my thoughts."

An "The cancer treatment and the medications aren’t helping to soothe my fears either."

An normal b "However, I’m still sick while you’re recovering. Once you've slept for a while you’ll wake up and feel better, I’ll make sure of that. "


if maverick_redem_annaromance == True:

    c "Will you be here when I’ll wake up? "

    m "Anna gently took my hand and kissed me on the lips while I felt the effects of the sedative. "

    play sound "fx/kiss.wav"

    $ renpy.pause (1.0)


else:

    c "Will you be here when I’ll wake up? "

    m "Anna gently took my hand while I felt the effect of the sedative. "



An "I’ll be here when you wake up, [player_name]."

m "I was still holding Anna’s hand like a scared child when I slowly started to fall asleep. Despite everything that happened, her presence made me feel safe."

An "Goodnight and sweet dreams."

stop music fadeout 2.0

$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)




scene redem_hospital_b with dissolvemed

play music "mx/creamclouds.ogg" fadein 1.0

m "It took a few more days until Anna agreed to release me. Even though I was able to go home, I still had to visit her every few days for a checkup." 


if maverick_redem_annaromance == True:

    m "Not that I minded having a reason to spend more time with her. "

else:

    pass

m "Maverick was helping me walk since I still had to take it easy. Together we left the hospital and made our way to my apartment. "




if maverick_redem_adineromance == True:

    jump redem_adine_5_5

elif maverick_redem_bryceromance == True:

    jump redem_bryce_5_5

elif maverick_redem_naomiromance == True:

    jump redem_naomi_5_5

elif maverick_redem_remyromance == True:

    jump redem_remy_5_5

else:

    jump redem_portal_5_5


label redem_adine_5_5:

m "While Maverick and I were on our way home, I saw Adine flying in the sky. I haven’t talked to her since I called her to talk about the flying contest."

m "Adine must have noticed us, and while I was still unsure about how to react, she landed next to Maverick and I."

play sound "fx/flapx.ogg"        

$renpy.pause(1.0)

show adine sad c at right with easeinright

c "…Hey Adine. "

Ad sad b "Hey, [player_name]."

m "There was an awkward silence between us and, for better or worse, Maverick had decided to stay out of our way."

m "While I was still struggling with what I wanted to say, Adine took the initiative."

Ad "[player_name] I’m sorry I got so mad at you when you called me about the contest. I know you only wanted to protect me from flying with an injured wing but I just didn’t want to wait any longer."

Ad "I had to think about everything you had said, how Remy and the children at the orphanage needed me and that there was always next year. "

Ad disappoint b " The truth is that you were right. I could never do anything that could harm the children in the orphanage. They need me, just like Remy."

m "Adine looked unsure, maybe a little scared and I had a feeling as if she was also affected by the portal just like Maverick and I."

Ad think b "I also had those weird dreams of me dying at the competition. You might have actually saved my life. "

Ad sad b "What I’m trying to say is that I’m sorry about the way I reacted and I really hope you can forgive me."

c "I was never mad at you, I was just scared that you might have gotten hurt if you had participated with an injured wing."

Ad normal b "I’m so relieved to hear that. I really missed spending time with you, [player_name]."

m "Adine pulled me into a hug, not knowing that my wound still hurt. Luckily Anna had given me enough pain killers earlier today that I barely felt any pain."

c "Please be careful Adine, I still haven’t fully recovered."

Ad sad b "Oh, I’m sorry. I hope it didn’t hurt you too much. "

m "It was then when Adine finally took notice of Maverick standing behind me. Adine must have been too focused on me that she completely overlooked the way bigger dragon. "

Ad giggle b "Oh, hello Maverick, I didn’t see you. Sorry."

show maverick rehappy flip at Position (xpos = 0.1) with dissolve

Mv rehappy flip "Don’t worry; I just didn’t want to interrupt you two."

Ad disappoint b "I’ve heard that you got hurt during the festival but I wasn’t able to get any information and to be honest, I wasn’t even sure if you still wanted to see me."

Ad sad b "I really hope your injury wasn’t too bad."

m "I knew that I’d had to tell her the truth sooner or later but I didn’t want to worry her too much after we just reconciled."

c "It still hurts and I need to recover but it’s all better now. I’ll tell you what happened some other time."

Ad giggle b "I can’t wait to hang out some more. "

Mv "I really hate to break the moment but we should get you home now. Anna said that you still need your rest and I don’t want her to be mad at me."

Ad "That’s ok, I still need to finish my delivery. I hope we can meet again soon, [player_name]."

c "Sure, I’ll give you a call, goodbye Adine."

Ad "Goodbye you two."

show adine normal c at right with dissolve

$renpy.pause(1.0)

hide adine normal c with dissolve

play sound "fx/flapx.ogg"

Mv "You two are really cute together. Awkward, but cute."

c "Since when are you able to tell jokes Mav?"

Mv rehappy flip "Oh, you’d be surprised."

jump redem_portal_5_5



label redem_bryce_5_5:

m "While Maverick and I were on our way home we suddenly ran into Bryce. He was wearing his badge, so he was still on duty. "

show bryce laugh b at right with easeinright

Br "Hey you two. Didn’t expect to run into you today."

c "Hey Bryce. "

show maverick rehappy flip at Position (xpos = 0.1) with dissolve

Mv "Hey Chief."

Br "I’m glad they finally released you, [player_name]. "

Br sad b "When we arrived at the crime scene… I’m glad you’re alive. "

c "I’m sorry for worrying you. We would have called for backup but when the fireworks started, we realized that that was the perfect time for Reza to make his move, and we didn't want to waste any time."

Br normal b "If you were working for me, I would have to give you a stern official warning for confronting Reza without backup, but given everything we’ve learned, you two have saved the world."

Br "You even managed to get Sebastian out of harm's way. "

c "I can’t really explain it but it felt as if I needed to make him watch the fireworks. "

Mv "During those two weeks [player_name] and I had those strange feelings as if we had seen certain events already. It might have been because of the portal but in the end that’s what saved both of us."

Br brow b "You know, you’re not the first ones to tell me that. Sebastian and I had similar experiences, even dreams of us dying. For me it was the bomb at the farmhouse and for Seb, the night at the portal."

Br laugh b "Those feelings have mostly stopped after you took down Reza, so whatever it was, it helped you two to save us all."

c "Yes and I really hope we won’t get them again. "

m "Despite having said that, a part of me highly doubted that this was the last time we had those feelings. It felt as if one storm had calmed down only for another to be brewing."

Br laugh b "You know, we should celebrate your release and the end of the case at the bar. Drinks are on me."


if brycebar == "False" or nodrinks == True:

    Br normal b "I hope you’ll join me this time."

    c "Now that all the stress from the Reza case is over, I’ll gladly join you."

    Br laugh b "That’s the spirit."

    c "However, no alcohol for me; doctor’s orders. I’ll have to take something non-alcoholic until I get the OK from Anna. "

    Br laugh b "Aww, that’s no fun but you’re right. Your health is more important and we can also celebrate without you drinking alcohol. "

else:

    c "Sorry Bryce, but no drinking contests for me anytime soon; doctor’s orders. I’ll have to take something non-alcoholic until I get the OK from Anna. "

    Br laugh b "Aww, that’s no fun but you’re right. Your health is more important and we can also celebrate without you drinking alcohol. "

    c "As long as someone else is dragging you home this time."

    Mv laugh flip "Don’t look at me, I had to drag your drunken ass home last time."

    Br "Oh come on, I wasn’t that drunk. "

    Mv rehappy flip "You were wearing your bowl as a hat."

    Br "You were laughing, too."

    c "Sounds as if you had a good time."

    Br "We had and once you’re recovered we need to see which species will win a drinking contest, no draws allowed."

Mv "I really hate to break the moment but we should get you home now. Anna said that you still need your rest and I don’t want her to be mad at me."

Br smirk b "Aww, just when it was getting fun but I guess you’re right. I still have some work to do and my break is almost over."

c "Goodbye Bryce."

Br "Goodbye you two."

hide bryce normal b with dissolve

Mv "You shouldn’t underestimate Bryce, no one has ever beaten him in a drinking contest yet."

c "Guess there is a first for everything. "

Mv rehappy flip "You really would be perfect for the team and for Bryce."

jump redem_portal_5_5


label redem_naomi_5_5:

if naomiscenesfinished != 4:

    m "While Maverick and I were on our way home, I saw Naomi flying in the sky. I haven’t talked to her since our diving trip."

    m "Naomi must have noticed us after a while and soon she landed next to Maverick and I."

    play sound "fx/flapx.ogg"        

    $renpy.pause(1.0)

    show naomi normal b at right with dissolve

    $renpy.pause(1.0)

    show maverick normal flip at Position (xpos = 0.1) with dissolve

    Nm "Hello [player_name], I’m happy to see that they released you from the hospital."

    m "Naomi wasted no time and pulled me in a hug. Despite my wound being healed she still tried to be as careful as possible for someone with her strength. "

    Nm sad b "I really thought that I’d never see you again when Maverick called for help that night."

    Nm "Bryce didn’t tell me what happened when he and medical team left but I was there when the investigation team took photos of the facility. "

    c "I’m sorry for worrying and for not calling you."

    Nm normal b "It’s alright; Maverick told me everything that happened. I’m just glad that you’re still alive."

    Nm "Both of you actually. "

    Nm "I read the reports and Reza had another bomb. Things could have gone way worse."

    Mv angry flip "Yeah, that bastard was prepared to kill himself rather than get arrested, just like you predicted." 

    c "Luckily your fire breath didn’t hit his bomb, Mav. "

    show maverick rehappy flip with dissolve

    m "Mav looked at me with a devious expression and I knew what he was about to say. "

    Mv "I know that you have more than enough experience with explosive situations. Like that trap Reza had planned for us or your little adventure with a certain dragoness."

    m "Maverick’s look switched between me and Naomi and it didn’t take the dragoness long to connect the dots."

    c  "(I think I preferred Maverick when he was grumpy instead of mischievous.)"

    Nm stern b " [player_name], did you tell Maverick about our diving trip? "

    m "She said that to me with the expression of a disappointed yet amused mother, who caught her child taking a cookie from the cookie jar."

    c "I’m sorry, but it’s impossible to hide something from him. Not to mention that he can be intimidating at times. "

    Mv rehappy flip "Me, intimidating? I’m the friendliest dragon around. "

    Nm confused b "Wait, did Maverick just make a joke without drinking? I think the world is actually ending. "

    Mv "Oh come on Naomi, I’m not that bad, am I? "

    show naomi shy b with dissolve

    m "Neither I nor Naomi said anything but the look on our faces might have been enough of an answer. "

    Mv "Ok, I get it, I was kind of grumpy. Even if I won’t change my personality, [player_name] helped me to move on from my past so I guess it won’t hurt to be a little less of a {i}sourpuss{/i} as some called me. "

    show naomi smile b with dissolve

    c "No one expects you to change your personality Maverick but I’m glad you’re able to be happy again. I’m sure Miles would’ve agreed with me. "

    show naomi concern b with dissolve

    m "I could see that Naomi winced when I said Miles' name, but to her surprise Maverick reacted differently than what she was used to. "

    Mv "You’re right, he would have wanted me to be able to live a happy and fulfilling life. "

    Nm normal b "You really did change over the last few weeks Maverick."

    Mv "I guess I really did. Who knows, maybe humans really are magical creatures."

    c "I sadly don’t have any special abilities but I’m always trying to help my friends."

    c "You know Naomi, once I’ve recovered we can go on date you had in mind."

    show naomi shy b with dissolve

    m "I was confused when Naomi suddenly blushed and looked away. Despite remembering tiny parts of my time with her in different timelines, I had no idea what our 4th meeting would have been like. "

    Nm "I’d like that."

    Mv "I really hate to break the moment but we should get you home now. Anna said that you still need your rest and I don’t want her to be mad at me."

    Nm "I guess I’ll return to the department. "

    c "Goodbye Naomi."

    Nm  "Goodbye you two."

    play sound "fx/flapx.ogg"

    hide naomi with dissolve

    $renpy.pause(1.0)

    Mv "You two are really cute together."

    c "You think so? "

    Mv rehappy flip "Yes, it’s rare to see Naomi that happy."

    jump redem_portal_5_5

else:

    m "While Maverick and I were on our way home, I saw Naomi flying in the sky. I haven’t talked to her since our night together and I was happy to see her again."

    m "Naomi must have noticed us after a while and soon she landed next to Maverick and I."

    play sound "fx/flapx.ogg"        

    $renpy.pause(1.0)

    show naomi normal b at right with dissolve

    $renpy.pause(1.0)

    show maverick normal flip at Position (xpos = 0.1) with dissolve

    Nm "Hello [player_name], good to see that they released you from the hospital. "

    m "Naomi wasted no time and pulled me in a gentle, painless hug and, to Maverick’s surprise, kissed me on the lips."

    play sound "fx/kiss.wav"

    show maverick reblush flip with dissolve

    $renpy.pause(1.0)

    m "Of course he knew that we were together but seeing someone as shy as Naomi showing affection in public surprised him. "

    Nm sad b "I really thought that I’d never see you again when Maverick called for help that night."

    Nm "Bryce didn’t tell me what happened when he and the medical team left but I was there when the investigation team took photos of the facility. "

    c "I’m sorry for worrying and not calling you. "

    Nm normal b "It’s alright; Maverick told me everything that happened.  I’m just glad that you’re still alive."

    Nm "Both of you actually. "

    Nm "I read the reports and Reza had another bomb. Things could have gone way worse. "

    Mv angry flip "Yeah, that bastard was prepared to kill himself rather than get arrested, just like you predicted. "

    c "Luckily your fire breath didn’t hit his bomb, Mav. "

    show maverick rehappy flip with dissolve

    m "Mav looked at me with a mischievous expression and I knew what he was about to say. "

    Mv rehappy flip "I know that you have more than enough experience with explosive situations. Like that trap Reza had planned for us or your little adventure with a certain dragoness."

    m "Maverick’s look switched between me and Naomi and it didn’t take the dragoness long to connect the dots."

    c  "(I think I preferred Maverick when he was grumpy instead of mischievous.)"

    Nm stern b " [player_name], did you tell Maverick about our diving trip? "

    m "She said that to me with the expression of a disappointed yet amused mother, who caught her child taking a cookie from the cookie jar."

    c "I’m sorry, but it’s impossible to hide something from him. Not to mention that he can be intimidating at times. "

    Mv rehappy flip "Me, intimidating? I’m the friendliest dragon around. "

    Nm confused b "Wait, did Maverick just make a joke without drinking? I think the world is actually ending. "

    Mv "Oh come on Naomi, I’m not that bad, am I? "

    show naomi shy b with dissolve

    m "Neither I nor Naomi said anything but the look on our faces might have been enough of an answer. "

    Mv "Ok, I get it, I was kind of grumpy. Even if I won’t change my whole personality, [player_name] helped me to move on from my past so I guess it won’t hurt to be a little less of a {i}sourpuss{/i} as some called me. "

    show naomi smile b with dissolve

    c "No one expects you to change your personality Maverick but I’m glad you’re able to be happy again. I’m sure Miles would’ve agreed with me. "

    show naomi concern b with dissolve

    m "I could see that Naomi winced when I said Miles' name, but to her surprise Maverick reacted differently than what she was used to. "

    Mv "You’re right, he would have wanted me to be able to live a happy and fulfilling life."

    Nm normal b "You really did change over the last few weeks Maverick."

    Mv "I guess I did. Who knows, maybe humans really are magical creatures."

    c "I sadly don’t have any special abilities but I’m always trying to help my friends."

    if naomiromance >= 100:

        Nm shy b "I wouldn’t say that. You do have some special abilities from what I recall from the last time we’ve met."

        Mv laugh flip "Ok, that’s too much information for me."

        show naomi smile b with dissolve

        $renpy.pause(0.5)

        m "I blushed while Naomi giggled at his comment. It seems even she can escape her usual shy behavior from time to time."

        Mv rehappy flip "I really hate to break the moment but we should get you home now. Anna said that you still need your rest and I don’t want her to be mad at me."

        Nm smile b "I guess I’ll return to the department. "

        c " Goodbye Naomi."

        Nm  "Goodbye you two."

        play sound "fx/flapx.ogg"

        hide naomi with dissolve

        $renpy.pause(1.0)

        Mv "You two are really cute together."

        c "You think so? "

        Mv rehappy flip "Yes, it’s rare to see Naomi that happy."

        jump redem_portal_5_5

    else:

        c "You know Naomi, once I’ve recovered we can go on another date. You know how much I enjoy the time we spend together."

        show naomi shy b with dissolve

        m "I smiled when Naomi suddenly blushed and looked away."

        m "I was too afraid of the outcome of the Reza case and I didn’t want to rush things with Naomi but I love her and now we had all the time in the world to be together."

        Nm "I’d like that."

        Mv "I really hate to break the moment but we should get you home now. Anna said that you still need your rest and I don’t want her to be mad at me."

        Nm smile b "I guess I’ll return to the department. "

        c " Goodbye Naomi."

        Nm "Goodbye you two."

        play sound "fx/flapx.ogg"

        hide naomi with dissolve

        $renpy.pause(1.0)

        Mv "You two are really cute together."

        c "You think so? "

        Mv rehappy "Yes, it’s rare to see Naomi that happy."

        jump redem_portal_5_5



label redem_remy_5_5:

m "While Maverick and I were on our way home we suddenly ran into Remy. The look on his face when he saw us told me that he knew what had happened. "

show remy normal at right with easeinright

show maverick normal flip at Position (xpos = 0.1) with dissolve

Ry normal "Good afternoon [player_name] and Maverick."

Mv "Good afternoon, Remy."

c "Good afternoon, Remy. How are you?"

Ry "I’m better, now that I know that you’re better."

Ry sad "The day after you took down Reza, the whole council went in panic mode about the comet. That’s when I learned that you got shot."

Ry "I wanted to visit you but no one outside of the police was allowed to enter your room."

if remy3unheard == False:  

    Ry "After everything that happened in my life the thought of losing you scared me to death but I wasn’t allowed to know about your condition." 

else: 

    pass

Ry look "However, for some reason Anna was nice to me and told me that you’d make a full recovery. She broke the rules for me despite everything that happened between us."

m "Given their history, I wondered why Anna was suddenly nice to Remy. Did she learn that he was the reason I learned about her cancer which lead me to adding the note to my PDA?"

c "Anna is not as bad as people say. Sure, she has made some mistakes and might have to work on her way of treating others but she’s still a good person."

show maverick rehappy flip with dissolve

m "Even without looking at Maverick, I knew that he appreciated my words. I wondered if Anna would actually start to open up again once she was cured."

Ry normal "Oh, I never hated her or anything. I was just doing my job and I kind of felt bad because I once caused her research application to get rejected some years ago. "

Ry "I told you about my work back then and how it influenced the decisions of which ones were funded, and which ones were rejected."

Ry "You could call it a journalist for actual scientific journals and not the type of magazines Adine likes to read. "

Ry "Well, I was always proud of my work because I was independent and unbiased when I wrote an article… until I met Amelia."

c "You told me that she also had a project and that you had to hide your relationship because it could've made people think your relationship was influencing your work."

Ry sad "The worst mistake of my life. The more I thought about it the more I started to think \"Was I really unbiased or did my feelings for Amelia cloud my judgment?\" "

Ry "When I learned about Anna’s condition, it only made me feel worse since one of my articles caused her application to be rejected."

Ry "She always hated me because of my work for the council, while I started to admire her for going that far despite her condition."

Ry "You know how much I started to hate my work once I started working for Emera, so I kind of wanted to try and help Anna without breaking any rules."

c "So that one time when you talked to her about her work during the Reza case…"

Ry normal "I tried to warn her about the council. Someone was leaking data to them about Anna but none of that was enough to actually go against her."

Mv "I guess you thought that a member from the facility, more specifically her assistant Damion, was behind those documents?"

m "Maverick’s voice seemed to have startled Remy since he was more or less admitting doing something wrong without breaking any rules."

Ry "Y… yes. I mean, who else would have profited from a case against her? Sadly she always misinterpreted what I tried to tell her, thinking I was trying to sabotage her."

c "I think she realized the truth when she read the note on my PDA. There were only two ways for me to learn about her condition; betraying her trust and reading her documents or someone else telling me about it."

c "It wasn’t a secret that we two spent time together and she knew that, if someone had the power to snoop through her personal data, it could have only been you. "

c "Maybe it was her way to show gratitude because now she has a chance to be cured with the data on the PDAs."


if remy3unheard == False:

    Ry "I hope she’ll be cured. "

    Ry smile "She made sure that I won’t lose you. After everything that happened after Amelia’s death, I can finally find happiness again… with you."

    Ry "You appeared at the darkest time of my life and changed it for the better."

    Ry "For the first time since Amelia’s death I can look forward to the future and I also reconciled with Adine."

    c "Once I recovered, we really should spend more time together. Without the Reza case, I actually have more time to explore your world and I can’t think of anyone better by my side than you."

    Ry shy "I’d love that."


else:

    Ry smile "I hope she’ll be cured. After all, she made sure that I won’t lose you."

    Ry "You’re a great friend; one that appeared in my life when I needed him the most."

    Ry "For the first time since Amelia’s death I can look forward to the future and I also reconciled with Adine."

    c "Once I recovered, we can spend some more time together. There’s something I wanted to tell you, now that Reza won’t be able to harm anyone anymore."

    Ry "I’d like to spend more time with you, too."



c "Then it’s a date."

Ry shy "Yes, it is."

Mv normal flip "I really hate to break the moment but we should get you home now. Anna said that you still need your rest and I don’t want her to be mad at me."

Ry smile "Just give me a call when you have time again or want to talk."

c "I will, goodbye Remy."

Ry "Goodbye you two."

hide remy with dissolve

Mv "You two are really cute together."

c "You think so? "

Mv rehappy flip "Yes, I’ve tried to keep an eye on him since his fiancée’s funeral but I’ve never seen him this happy."

jump redem_portal_5_5





label redem_portal_5_5:

c "Mav, do you mind if we visit a different place before we go to my apartment?"

show maverick rehappy flip at Position (xpos = 0.1) with dissolve

Mv normal flip "I’m not sure. Do you think you’re fit enough for that?"

c "Yes and there is something I wanted to talk about with you when we’re there."

stop music fadeout 2.0

scene black with dissolvemed

$ renpy.pause (0.5)

scene np1x with dissolvemed

play music "mx/nostalgia.ogg" fadein 2.0

m "Despite taking it slow it only took us a few minutes to reach the portal. We made our way toward it until I finally reached the right place."

c "This is where it all began. Here's where Reza and I met that night when you appeared." 

c "For days I was wondering what Reza was going to tell me if you hadn’t show up."

show maverick rehappy flip at Position (xpos = 0.1) with dissolve

Mv "Do you think that we could have prevented the murders if I wouldn't have interrupted you two?"

c "No, I think I would have become his first victim. He was most likely trying to tell me about his plan and the comet. "

c "However, as soon as he'd have been done here, he'd have killed me even if I would have helped him and we both know that I’d have never sided with him."

m "I looked at Maverick. I still could see the spots were Maverick was hit by the bullets, a small one and two bigger ones. Soon they’d all be completely healed and disappear."

c "I’m sure you saved my life by interrupting us."

Mv "Even then I shouldn't have attacked you."

c "You just got shot by Reza and it's only natural to think that there was a chance that I was the same as him."

Mv rehappy flip "Luckily you decided to talk to me despite my behavior."

Mv "What do you think will happen now? Will your people understand why I had to kill Reza? "

m "By now I was sure that the coordinates to my world were gone even without me checking the console. Izumi had to make sure that Reza won't be able to escape and most likely deleted them."

m "It was time to tell Maverick about everything. I was sure he'd understand."

c "They'll never learn about anything that happened here. Izumi most likely deleted the coordinates to my world to prevent Reza from escaping."

Mv normal flip "Izumi? Who is that?"

c "She's a human and the one who built the portal and facility here. It's a long story but in short; the portal allows you to travel through time."

m "I didn't expect Maverick to believe me but he was silent and listened to my story."

m "I told him about the first time I arrived and failed, how I had to travel back to make sure we all get our happy ending… and that I'd have to use the portal again as soon as this timeline was saved."

c "I know that it's a lot to take in and you probably don't believe me."

Mv "Usually you'd be right but I trust you and as weird as it sounds, it answers some questions." 

Mv "I guess those feelings and dreams were caused by time travel?"

c "They're most likely memories from what previous versions of us experienced."

c "I only saw a few things and it wasn't easy to process."

Mv "Do you remember all of it? All that pain and all the deaths."

c "No, it seems the portal erases most of my memories."

c "I know that I saw my friends die a few times or that I died but right now, I can't remember any details. {w} Hopefully I never will."

Mv "I hope so. Memories like that aren’t easy to process and could easily break someone."

Mv "For years I thought about Miles and asked myself if I could have saved him."

Mv "Reliving that moment several times, making different decisions only to see him or others die over and over… "

Mv "You helped me let go of those thoughts, and concentrate on the future instead of the past."

Mv "You traveled back in time many times and I’m sure that, if it would have been in your power, you would have tried to prevent Reza from murdering those dragons."

c "I would have done that but it seems as if the only way to stop Reza and save your species is to follow the investigation toward the confrontation we had."

if remy3unplayed == False:

    c "I wish I could have saved everyone, even Miles and Amelia, but just changing the outcome of those two weeks had taken countless attempts and even getting here is still not the best possible ending."

    c "If the coordinates have really been deleted in this timeline, then mankind is doomed once more."

    c "Trying to change years…"

    Mv "Don’t worry about that [player_name]. I know that it’s impossible; that’s why I didn’t ask you."

else:

    c "I wish I could have saved everyone, even Miles, but just changing the outcome of those two weeks had taken countless attempts and even getting here is still not the best possible ending."

    c "If the coordinates have really been deleted in this timeline, then mankind is doomed once more."

    c "Trying to change years…"

    Mv "Don’t worry about that [player_name]. I know that it’s impossible; that’s why I didn’t ask you."


m "We both went silent leaving the question he had hanging in the air. Soon however, he had to ask it."

Mv "So I guess you'll leave this timeline, too?"

c "I sadly have to. As much as I want to leave this whole time traveling business behind me, I can't stop until I've saved mankind, too."

Mv "Do you have to leave now?"

c "No, I'll stay until I made sure that your world is safe."

As "You might not have to leave at all."


$ renpy.pause(1.0)

show izumi normal at right with dissolve

m "Maverick and I turned around and I saw the Administrator standing behind us."

play sound "fx/snarl.ogg"
show maverick angry flip with dissolve

$ renpy.pause (1.0)

m "Maverick positioned himself between me and Izumi, growling, but I put my hand on his side to calm him down."

c "Izumi, you're kinda late this time, too."

As "How ironic that you would remember her name now."

As "Besides, it didn't seem like you really needed me. Good job."

c "Her name? What are you talking about?"

As "I'm not Izumi."

hide izumi with dissolve

play sound "fx/undress.ogg"

$ renpy.pause (0.3)

m "The person I thought was the Administrator took off the mask, only to reveal a strangely familiar face underneath."

show maverick relost flip with dissolve

m "The person before me had a face that looked exactly like mine, down to the tiniest detail. It was like looking into a mirror or at a twin. It was me."

play sound "fx/undress.ogg"

$ renpy.pause (0.5)

show izumi normal at right with dissolve

As "You understand why I'm wearing the mask now?"

Mv relost flip "How is this possible? I thought you traveled back from the future but now there is another you."

c "I’m as confused as you are. How is this possible?" 

As "Did you never ask yourself why you didn't remember anything when you first got here?"

c "I thought it was because of the portal and the amnesiac effect of the time travel." 

As "You never went back in time but I did a few times."

show maverick normal flip with dissolve

As "Time travel adds memories from one timeline to the following ones. That’s why you remember other timelines."

As "You most likely had strange dreams or déjà vu like feelings during those two weeks."

c "Yes, Maverick and I both had them."

As "It is possible that you two aren’t the only ones. I have a theory that everyone close to us will be affected by the effects of repeated time travel."

c "Will that effect stop, now that we saved the dragons or will I remember all of the failed attempts?"

As "To be honest, I don’t know. It seems as if some versions of us traveled back in time long after the comet was diverted."

As "I guess one way or the other, there was another threat for this world or our own safety. "

As "There is also the possibility that you’ll remember other timelines the longer you stay here or the more time you spend with someone." 

As "Some versions of us seemed to remember everything while others only remembered the first confrontation."

As "It had taken me some time but I now remember all timelines. The experience… wasn’t pleasant. Some timelines had been worse than others."

As "However no matter what will happen, I know that our friends will be there to help you. You won’t be alone if it should happen."

m "Even if that wasn’t the answer I hoped for, I was confident that I’d be able to endure everything as long as I had my friends."

m "However, there was another question that was on my mind."

c "What happened to Izumi?"

As "She died during one of our confrontations with Reza. It happened before but sooner or later there will always be a timeline with another Izumi."

As "Until that time comes I'll have to gather information and save the dragons in the following timelines I’ll visit."

Mv "What about mankind?"

As "As long as the coordinates to mankind are there, Reza can escape and the dragons will die."

As "Repairing the portal after the confrontation won't work either."

As "According to what she told me, Izumi did that a few times but Reza was able to fix the portal on his own. Guess he has some knowledge of fixing things but you should already know that because of his bombs."

Mv "If you were here all the time then why didn't you appear earlier? You could have saved Reza's victims."

As "That's what Izumi tried a few times but the only way to save your kind is to follow the current path just like my other me told you."

As "As much as I hate to say it, 4 dragons have to die to save all of you."

c "At least I was able to save Anna in this timeline."

As "Yes, for some reason she is the only one of the victims that can be saved even if it means that her assistant Damion will take her place instead."

Mv reannoyed flip "Yeah, we're not crying for him after what he did. {w} He tried to team up with Reza to get Anna murdered."

As "He did? He never was a nice person in the timelines I saw but it seems that the Damion of this timeline was even worse."

show maverick normal flip with dissolve

c "Wait, so personalities can change, too?"

As "From all the timelines I experienced, it seems as if there are changes beyond those two weeks and they also effect both worlds."

As "I saw a timeline where Naomi was the big, winged water-dragon you know from this timeline, while in others she was a pink runner. Funnily enough, both times she worked for the police, just with different tasks."

As "I’ve also met different versions of us; some fell in love with one of our friends while others only formed friendships."

if persistent.evilending == True:

    As "I’ve also seen a timeline where I was the same as Reza. Many of our friends died because of this and, in the end, he also killed Reza, took the generator and returned home."

    Mv "I have a hard time believing that you would ever do something like this."

    c "As am I. I would never act like that."

    As "Like I told you, the people can change with each timeline. I guess it was only a matter of time until I’d encounter an evil version of us."

    c "I’m not sure how to react to that. If a different version of me would act like that…"

    Mv "Don’t even think about that. During the last two weeks I’ve seen who you are and I know that you would never betray any of us. We are friends and I trust you."

    c "Thank you, Mav. At least this might explain why you had a feeling that I could be the same as Reza. A part of you remembered that asshole version of me."

    As "You shouldn’t worry about that. In all the timelines I’ve seen, we never acted like that except for that one timeline."

    As "We might never know why that one version of us went that way or what happened in his past but so far it was only one for many timelines I visited."

else:

    pass

As "With the way the portal changes the timelines and people, I was even able to see a timeline where Izumi was murdering the 4 dragons not Reza."

Mv "Why would she do that? Didn’t you tell me she was the good one?"

As "She is but her way of thinking is… let’s say special."

As "She's done way more time traveling than us, and it had taken her many tries to find a way to make sure that at least one version of us survives until the confrontation with Reza."

As "To Izumi, sacrificing 4 lives is a small price to pay to save all dragons."

As "I’d never go as far as she did but I tried to prevent the murders once… I'll spare you the details but the result wasn’t good and many more dragons lost their lives."

Mv "I see, so there really is no way to save them."

As "I fear so. At least not without risking both worlds by ignoring possible consequences."

As "However it would take a big trauma like saving both civilizations only to lose the person I love to make me even consider that."

As "Speaking of Izumi; I think you should have noticed that some parts of her story aren’t adding up."

c "What do you mean? Did you find out more about her mission before she got here?"

As "No, I never found her real hideout but during my mission I had time to look around."

As "I’ve seen birds as well as some mammals like Aurochs. Despite telling us that she didn’t have any DNA samples when she got here, we nevertheless have a few species that shouldn’t exist here."

m "I of course also noticed that some parts of Izumi’s story didn’t add up but I never really had the time to think about the implications. If she was actually lying about that part then what else was she lying about?"

Mv "I don’t really understand what our animals have to do with this Izumi."

As "It’s a long story for another time. However you should keep an eye open for anything strange."

As "Maybe you’ll find her hideout someday and learn more about her and the whole story."

As "I don’t think that Izumi had any ill intent, but at the same time, I’m sure that she only told us what she thought we needed to know. "

As "So even if you’ll never find out the whole truth, you should remember her for everything she did to make sure that the dragons survive."

m "Despite never meeting her I still remembered her. It was true that Izumi always kept her secrets and only revealed what was needed."

m "I doubted that she left anything that would be a danger for the dragons and, to be honest, I just wanted to enjoy a normal life without worrying about the future."

m "However, if there was anything left that would be a threat for the dragons then I had to find and destroy it."

c "What will happen now?"

As "Usually I’d give you the choice to stay here or travel through the portal. However, since I have more experience than you, I’ll be the one to go."

As "It’s only fair that you’re allowed to have a happy life after I failed my mission in my timeline."

As "Usually Maverick would suspect us until we caught or killed Reza but this timeline was different. Just like you I talked to my Mav and we became friends."

Mv "I guess your timeline didn’t have a happy ending?"

As "My Maverick and I were able to save the dragons but… let’s say that talking about the dreams and giving you the map was the right decision."

As "I saw all possible outcomes, some where either the map, or the talk about the dreams was missing, or even both. This is the best possible outcome for both of you."

m "Maverick and I both went silent at the implication the other me did but neither of us wanted to learn more about the fate of our other selves."

Mv "Will your mission ever be over?"

As "I don’t know. There has to be a way to save both worlds and with the portal I’ll someday encounter another Izumi to find a solution."

As "I think I should go now. You were able to create better world than I, and I hope you’ll be happy here."

m "After giving us a nod, Maverick and I watched as the other me went through the portal until he vanished."

hide izumi with dissolve

m "For the first time since I got here I didn't know what the future would look like for me and even though I knew that mankind as doomed in this timeline, I had hope that the other me would save mankind in a different one."

m "Even if the implication of me remembering the other timelines wasn’t something I was looking forward to."

Mv "I guess it's better to not tell the council about this."

c "Agreed. They'll find out about the portal soon enough so it's better to keep a low profile for now."

Mv rehappy flip "Let's get you back to your apartment, [player_name]."




$ renpy.pause (0.5)

scene black with dissolveslow

$ renpy.pause (0.5)

nvl clear
window show

n "During the following weeks we were able to prepare for the arrival of the comet and, with the help of the underground generator, the dragons were able to divert it, saving their civilization."

n "For our help in stopping Reza, Maverick and I were awarded the highest honor the council could bestow on us, citing our bravery and exceptional service to the community."

n "Staying true to their word, the council prepared to send the generators to mankind only for them to realize that the coordinates were missing. With no way to reestablish contact to my people, I lost my ambassador status but was offered a full citizenship."

n "An offer I gladly accepted. "


$ renpy.pause (0.3)

window hide
nvl clear
scene black with dissolvemed


n "For her saving my life, the case against Anna was dropped and she was cleared of all charges. Anna was also allowed to work on the cure for cancer to make a new version for the dragons."

n "Moreover, the council made sure to give the data on the PDAs to their scientists and scholars. It was the beginning of a new age for dragonkind and led to a chain of events none of us could have expected…"

n "However, that’s a story for another time. For the time being, I was just happy to have a happy life ahead of me, a life I was looking forward to."

$ renpy.pause (0.3)

window hide
nvl clear
scene black with dissolvemed

stop music fadeout 1.0

$ renpy.pause (1.0)




if maverick_redem_maverickromance == True:


    scene redem_credits with dissolve

    $ renpy.pause (4.0)

    scene black with dissolvemed

    play sound "fx/system.wav"

    s "Good work, you've seen best possible ending. Mankind was saved in a different timeline while you and Maverick saved the dragons in this one."

    s "I'm sure you and him will have a happy future ahead of you."

    s "Thank you for playing my mod."

    $ renpy.pause (1.0)

    window hide
    nvl clear

    $ renpy.pause (0.5)

    $ persistent.redem_mavgoodending = True

    jump ml_main_menu



elif maverick_redem_noromance == True:



    scene redem_credits with dissolve

    $ renpy.pause (4.0)

    scene black with dissolvemed

    play sound "fx/system.wav"

    s "Good work, you've seen C ending. Mankind was saved in a different timeline while you and Maverick saved the dragons in this one."

    s "I'm sure you will have a happy future ahead of you."

    s "Thank you for playing my mod."

    $ renpy.pause (1.0)

    window hide
    nvl clear

    $ renpy.pause (0.5)

    $ persistent.redem_mavgoodending = True

    jump ml_main_menu



else:


    scene redem_credits with dissolve

    $ renpy.pause (4.0)

    scene black with dissolvemed

    play sound "fx/system.wav"

    s "Good work, you've seen B ending. Mankind was saved in a different timeline while you and Maverick saved the dragons in this one."

    s "I'm sure you and [maverick_redem_romance_partner] will have a happy future ahead of you."

    s "Thank you for playing my mod."

    $ renpy.pause (1.0)

    window hide
    nvl clear

    $ renpy.pause (0.5)

    $ persistent.redem_mavgoodending = True

    jump ml_main_menu
