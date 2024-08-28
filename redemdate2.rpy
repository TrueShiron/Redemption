label redemdate2: 

scene black with dissolvemed

$ renpy.pause (0.5)

scene cafe with dissolvemed

play music "mx/jazzy.ogg" fadein 2.0

m "When I arrived at the café, I noticed that Maverick was sitting at the same table Reza and I were sitting last time."

m "Remembering what he told me, I was sure that this wasn’t a coincidence."

c "Good evening, Maverick." 

show maverick normal flip at left with dissolve

Mv "Good evening, [player_name]. It’s good to see that you decided to work together with me."

m "I was surprised by his more or less friendly behavior." 

m "Maybe he was actually giving me a chance to prove that I wanted to help."

show adine normal b at right with easeinright

if adinestatus == "bad" or adine1unplayed == True:

    Ad "Welcome to our establishment. My name's Adine, and I'll be your waitress today."

else:

    Ad "Oh, hello [player_name]. Nice to see you again."

c "Hi, Adine."

Ad "Good evening to you too, Maverick."

Mv "Good evening, Adine."

#hide maverick normal flip at left with easeoutleft

if adinestatus == "bad" or adine1unplayed == True:

    Ad "What can I bring you two?"

else:

    show adine giggle b with dissolve

    Ad "I really enjoyed our last meeting, [player_name]."

    c "I did, too."

    show adine giggle b with dissolve

    Ad "Then you better not forget to call me."

    Ad normal b "What can I bring you two?"


#show maverick normal flip at left with easeinleft

Mv "I'll have a coffee."

#hide maverick normal flip at left with easeoutleft

show adine normal b with dissolve

Ad "Thank you. And what can I bring you, [player_name]?"

menu:
    "I'll also take a coffee, please.":

        $ maverick_redem_drink = "coffee"

    "Just a soda.":

        $ maverick_redem_drink = "soda"

    "Bring me a beer please.":

        $ maverick_redem_drink = "beer"


Ad "No problem, I'll be right back."

show adine normal b flip
$ renpy.pause(0.3)
hide adine with easeoutright

c "I didn’t know you two knew each other."

#show maverick normal flip at left with easeinleft

Mv "I often come here during my break. The coffee helps me to stay awake on long days especially when I’m the flyer on duty."

c "Do you think it’s a good idea to meet here? I thought you wanted our meetings to stay a secret for now?"

Mv "That won’t be a problem. Sebastian already knows about it and agreed to keep it a secret. Bryce is most likely at Zhong’s bar at this time."

if brycestatus == "bad" or bryce1unplayed == True:

    pass

else:

    c "Yeah, I remember it from the last time I met him. When I went to the police station to share some information about Reza, we ended up in the bar."

    Mv "I sure hope that he didn’t start a drinking contest again. The council has their eyes everywhere and they wouldn’t be too happy if anything happens to their important ambassador, no offense."

    c "Actually, we ended up in that contest."

    Mv laugh flip "Yeah, that's the Bryce I know…did you at least win?"

    c "I don’t know. It's a little hard to remember."

    Mv normal flip "You still deserve respect for challenging a dragon to a drinking contest."


c "It sounds as if Bryce visits the bar often."

Mv "Being in the force isn’t easy and we all have different ways of dealing with it."

m "Feeling that Maverick wasn’t comfortable with the topic I tried to change it." 

m "I nevertheless was surprised that he was actually doing small talk instead of going straight to business."

c "That sounds as if your team only has 3 members."

Mv "We are a small town so we don’t need that many members. Kalinth is our archivist and Naomi is our analyst."

Mv "She is a nice and hard-working girl but sometimes stays in the office long after her shift ends. Not that I’m any better."

show adine normal b at right with easeinright

$ renpy.pause(0.6)
play sound "fx/dishes.wav"

Ad "Here you go. Enjoy."

stop sound fadeout 1.0

show adine normal b flip
$ renpy.pause(0.6)
hide adine with easeoutright

m "Suddenly I noticed a change in Maverick’s behavior. It wasn’t a grumpy face like last time but more of an official business one."

Mv "Let’s go back to the reason we’re here. After our last meeting, I had time to think about everything you told me."

c "Since you called me for a second meeting it looks as if you’re starting to trust me."

Mv "Unlike the other dragons I believe that trust has to be earned. So far, you made good progress and I hope you won’t disappoint me."

m "It was not what I was expecting but I was able to work with that."

c "So that’s why you chose this place for meeting me. This was the place we went to after we visited the production facility and got the generator."

c "We are even sitting at the same table."

Mv "If we want to catch Reza then I need to know more about him; his habits, his way of thinking and his past."

Mv "You said you were friends and you were the last one he talked to. So if you’re not his accomplice then you’re our best witness for this case."

c "I’ll try my best to remember everything that might help us to find him."

Mv "Good, and then we can arrest him."

c "Yes, but only if Reza is behind all of this."

m "Maverick gave me a skeptical look."

Mv "So you’re still thinking that he’s innocent?"

c "I know it sounds crazy that I still believe in him, especially after he shot you, but try to look at it from my point of view."

c "Just think about how Bryce is now, and then, for some reason, you two wouldn’t be able to see each other for years."

c "The next time you’d meet him would be in a different world after your whole civilization had collapsed and you’d only been able to talk to him for a few minutes."

c "He asks you for a private meeting, but then your conversation gets interrupted by an angry officer."

c "He might have gotten frightened and thought he had to defend himself, but the next day Bryce is suddenly accused of murder."

c "Would you be able to think rationally or would a part of you try to refuse seeing the truth?"

m "Maverick was silent for a moment and thought about the situation. Surprisingly, his response was different from what I had expected."

Mv "I see your point and if I’d be in your situation I might also have problems accepting it. Especially if the officer that tells me that would also suspect and attack me."

Mv "However, I wouldn’t blindly trust my feelings for an old friend either."

c "Neither do I, otherwise I wouldn’t be here. I still hope that all of this turns out to be a misunderstanding but I can’t ignore the truth either."

c "Reza shot you without hesitating nor showing any remorse. Then, out of nowhere, someone starts murdering dragons in an otherwise peaceful town?"

c "Like you said, there are no coincidences."

Mv "I was wrong about you, so maybe I’m wrong about him too. As unlikely as it seems for now."

c "Thank you… for both."

Mv "Well, let’s start with the basics. What did you talk about when you were here?"

c "After complaining about you following him, he asked me if I also noticed that this place is strange."

c "At first I didn’t know what he was talking about but now…"

Mv "What do you mean? Is it about us dragons or about our culture as a whole?"

c "It’s about everything to be honest; the furniture, the technology and even the food."

c "If I wouldn’t know that I was in a different world full of dragons, I would think that this was my home before the flare and our advanced technology."

Mv "Is our civilization that similar to yours?"

c "Yes, and it’s actually very interesting."

c "I read some of your literature and it seems that we humans played an important part in your history and myths."

c "Moreover, you are the second known sentient species, so that combined with your creation myth might explain why this place feels like home."

Mv "I never was one of the believers of the creation myth but it’s still interesting to learn that our civilizations are similar."

c "We're even speaking the same language. Mankind has many different languages but English became the global language."

Mv "I have to agree; that is more than just coincidence."

Mv "I don't remember reading anything about the origin of our language and we only have one, but the believers of the creation myth are calling it the language of humans. They believe that the humans not only helped us to gain sentience but also taught us to speak."

Mv "However that might be a topic for another day."

m "As fascinating as it was, Maverick was right. We had other matters to discuss."

Mv "What happened after that?"

c "He told me that he can’t talk openly, so he was planning to send me a coded message and that I'd know what to do."

Mv "So you didn’t plan the code or something similar?"

c "No, but I knew that it couldn’t be something complicated."

c "I spent half the day searching my apartment, thinking that he’d most likely had a similar one."

c "After checking some books I went to the pantry and noticed the lemons."

Mv "How did you know it had to do with lemons?"

c "I remembered a class I had with Reza years ago where we learned that, if you write something with lemon juice on a piece of paper, it would disappear."

c "However, if you’re carefully heating it up, oxidization occurs and reveals the message. It’s actually a trick that children learn at school."

Mv "So it’s an effective and easy to use trick to write coded messages?"

c "Yes, more or less. I’m still surprised that Reza never questioned my ability to read it."

c "It was as if he was sure I’d remember that one random chemistry class we went to."

Mv "Was he always like that?"

c "Well, I know he values the use of his own intellect and he expects others to be the same. That’s why he was sure I’d be able to decode his message."

Mv "What else can you tell me about him?"

c "He was an above-average student and always very outspoken. Reza never failed to speak up to make his opinions known."

c "He spoke a lot, but you could also expect him to act on his word."

c "Even when he clashed with others, including school staff, his genuine enthusiasm also garnered praise from them."

Mv "I know those kinds of people. They can achieve great things, no matter if those things are good or bad. Most of them decide to become politicians."

c "That’s what I expected him to become, too. Either that or an activist."

c "We lost contact after we graduated. When we found the portal I was surprised to learn that he had volunteered to visit your world."

c "In the end, we never were that close but we still called each other friends."

c "With everything that happened the last few years, it feels as if he’s one of the last people left from the pre-flare world."

Mv "Sometimes it’s hard to let go of the past even if causes more pain."

c "That’s true."

Mv "Tell me about your meeting at the portal."

c "To be honest, there wasn’t much time to talk before you appeared."

c "We planned to send the generator Anna gave us back home. Then he told me that something was about to happen."

Mv "Can you remember his exact words?"

c "He asked me if I would know what this place was and that he was afraid that this whole place will be gone soon. He was about to tell me more but then you appeared."

Mv "So whatever this danger is he was talking about, he didn't have a chance to tell you more."

Mv "Maybe he’ll tell us once we found him."

c "I hope so. By the way, I have something for you."

m "I grabbed the envelope Sebastian gave me and opened it."

c "I asked Sebastian for a copy of all the evidence we collected today. Most of it seems trivial for now like some sort of map Reza was searching for."

c "However, this one makes me feel nervous."

m "I showed him Reza’s shopping list and by the look on Maverick’s face, he had the same thought as I."

Mv "He bought a lot of lemons and all of those purchases are close to the dates of him sending letters to your people."

m "He gave me a scrutinizing look as if he was waiting for a certain reaction."

c "I know what you’re thinking but no, I didn’t know about any hidden messages between Reza and my people."

Mv "Did they ever show you the letters?"

c "I never saw the original letters, only copies or summaries of longer ones."

m "I could see that he wanted to ask another question but for some reason, he didn’t."

Mv "I’m not sure if Bryce will agree with my theory but there might be someone behind Reza, someone who’s giving him orders only he’s allowed to know."

Mv "It’s a shame we never found any of his other letters."

c "Did you already search his entire apartment? "

Mv "Yes but we didn’t find anything useful."

show maverick rehappy flip with dissolve

m "At first Maverick didn’t show any reaction but then he roguishly smiled."

Mv "Except you want to search it a second time. Maybe you humans know of hiding places we wouldn’t think of."

c "That was my intention."

Mv "I like the way you’re thinking. Who knows, maybe you’re actually fit to be a police officer one day."

m "With that we paid for our drinks and gave Adine a generous tip before we left for Reza’s apartment."

hide maverick with dissolve




label redem_Reza_apartment:

$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_reza_apartment at Pan((0, 250), (0, 250), 0.1) with dissolvemed

play music "mx/path.ogg" fadein 2.0

m "It didn’t take us long to arrive at the location of Reza’s old apartment." 

m "Just like mine, it was isolated from the other apartments to keep us safe and undisturbed by other residents."

m "We tried to maintain a low profile when we finally arrived at the door, sneaking behind the cordon. "

m "Luckily the door didn’t have a police seal, so we were able to open the door without leaving any traces behind."

m "We entered the apartment and Maverick made sure that the curtains were closed before he turned on the light. I once more envied the dragons and their abilities like having a better night vision than us humans."

m "The interior decoration of the apartment was almost identical to mine including the same books and furniture. It seemed as if the dragons prepared the apartments the same way before Reza and I even had arrived."

m "I wondered if Remy was in charge for preparing the apartments or if he was only responsible for the food and books."

m "At least I now was sure that Reza also must have guessed that we both had the same things in our apartments when he prepared his message."

label maverick_redem_reza_search:

$ renpy.pause (0.3)

scene redem_reza_apartment at Pan((0, 250), (0, 250), 0.1) with dissolvemed

if maverick_redem_rezasearch == 3:

   m "When we were returning to the living room I heard a creaking sound. After paying closer attention I noticed that one of the floorboards was loose." 

else:

    pass

menu:

    "Search the living room." if maverick_redem_living_room_search == False:

        m "I made my way to the bookshelf and looked inside the books and the shelf itself, but I neither found hidden letters inside the books nor any kind of manipulation on the shelf itself."

        $ maverick_redem_living_room_search = True

        jump maverick_redem_reza_search


    "Search the kitchen." if maverick_redem_kitchen_search == False:

            $ renpy.pause (0.3)

            scene black with dissolvemed

            $ renpy.pause (0.5)

            scene redem_reza_kitchen with dissolvemed

            m "We entered the kitchen and the first thing I noticed was the knife stand or better the absence of it. Did the police take it when they were here or did Reza hide it somewhere?" 

            m "I tried to think about the knife stand in my apartment but I never really used it. Did Reza get his second weapon from here?"


            label maverick_redem_kitchen_search:

                menu:

                    "Search the fridge."  if maverick_redem_fridge_search == False:

                        m "I opened the fridge and noticed that there was a lot of meat and veggies."
                        m "Reza seemed to have deposed everything that was foreign to us and only bought food that was known to humans."

                        $ maverick_redem_fridge_search = True

                        jump maverick_redem_kitchen_search

                    "Search the pantry.":

                        m "The first thing I noticed when I inspected the pantry was the number of lemons."

                        m "By now I already realized that Reza had bought way too many lemons for just consuming them."

                        m "Hidden at the back of the pantry was the empty knife stand. It was a small one but still able to hold up to three knives."

                        c "I guess we have found the {i}sharp implement{/i} we were searching for."

                        show maverick normal flip at left with easeinleft

                        Mv "So he has at least three knives."

                        c "Did you follow Reza all the time, or were there moments where he was alone?"

                        Mv "After I convinced Bryce to let me follow Reza, we tried to keep an eye on him all day long."

                        c "What about the nights? Excluding Naomi, you only had three dragons for 24 hours ...or better 23 in the case of your world?"

                        Mv "Damn it, I didn't consider that he might sneak out at night."

                        c "So he had enough time to scout the town, maybe even setting up a hideout or two to store weapons and supplies."

                        Mv "That would explain why we can’t find him." 

                        Mv "I’ll inform Sebastian about those details tomorrow."

                        Mv "So, your days are 24 hours long?"

                        c "Yes, and our years have 365 days. Well, actually it’s 365 and a quarter so every 4 years we add that extra day to what we call a leap year, making it 366 days."

                        Mv "We always have 372 days a year and it never changes. You humans seem to like overcomplicating everything."

                        c "I guess you’re right and I didn’t even talk about summer and winter time or the different time zones we need for the places all around the globe."

                        m "We both laughed and then went back to work."

                        hide maverick normal flip with dissolve

                        $ maverick_redem_rezasearch += 1

                        $ maverick_redem_kitchen_search = True

                        jump maverick_redem_reza_search

                    "Return":

                        jump maverick_redem_reza_search


    "Search the bathroom." if maverick_redem_bathroom_search == False:

        $ renpy.pause (0.3)

        scene black with dissolvemed

        $ renpy.pause (0.5)

        scene redem_reza_bath with dissolvemed

        m "Reza’s bath wasn’t that different from mine and there weren’t any good hiding places except of the cabinet."

        m "I looked inside the cabinet and found a few razors. There was also an empty bottle of pain meds." 

        m "The police had watched Reza's apartment after he ran away so Reza must have taken them earlier…"

        m "A closer inspection revealed that Reza’s cabinet was also missing things like scissors and disinfectant. Stuff he could need in case of an injury."

        c "Did you also provide a first aid kit for the apartment? Maybe also a fire extinguisher?"

        show maverick normal flip at left with easeinleft

        Mv "The council decided to add a first aid kit for both of your apartments but they didn’t think of fire extinguishers." 

        Mv "Our team didn’t find the first aid kit when they were searching the place though."

        c "I guess he might have stored it somewhere else, just in case."

        Mv "That would explain how he was able to treat his wounds."

        hide maverick normal flip with dissolve

        $ maverick_redem_bathroom_search = True

        $ maverick_redem_rezasearch += 1

        jump maverick_redem_reza_search


    "Search the bedroom." if maverick_redem_bedroom_search == False:

        $ renpy.pause (0.3)

        scene black with dissolvemed

        $ renpy.pause (0.5)

        scene redem_reza_bedroom with dissolvemed

        m "We entered the bedroom and searched the places the police might have missed." 

        m "Thanks to the information Maverick got from Sebastian, we skipped the places they have searched already."

        m "I opened the cabinet and saw many unused papers and a pen. When I wanted to take a closer look, I smelled the flavor of lemons coming from the pen."

        m "It was modified and was most likely brought from the human world."

        c "I don’t like to admit it but it seems you were right. Look at this."

        show maverick normal flip at left with easeinleft

        Mv "It’s just a pen."

        m "He took it and clumsily tried to write something on a paper."

        m "Even if it was difficult to see, I noticed a few wet lines where the pen had touched the paper but no ink."

        Mv "And it’s broken."

        c "No, if you look closely you can still see the lines of what you wrote."

        Mv "Damn it, you’re right."

        c "It looks as if it was modified to write with lemon juice. I’m certain that he brought it with him from our side of the portal."

        Mv angry flip "So I was right about your people trying to trick us."

        $ renpy.pause (0.5)

        show maverick normal flip with dissolve

        m "As much as I wanted to, I couldn’t ignore the truth any longer. Reza had sent coded messages to my people back home. When I took a closer look at the unused paper, I noticed that one of them was different." 

        m "While the others were looking like new this one had been folded and was mixed with the others."

        m "I lit the candle on top of the cabinet while Maverick was observing me. Carefully not to burn the letter, I moved it closer to the fire. My hope that I was wrong was shattered when words appeared on the paper."

        m "\"{b}Mission in danger. Starting emergency protocol{/b}\" was written on it. Silently I handed over the paper and sat down on the bed." 

        m "I expected Maverick to say that he was right or worse, started suspecting me again, but I was instead surprised by him."

        Mv normal flip "Are you alright, [player_name]?"

        c "To be honest, I don’t know."

        m "Maverick gave me a worried look but I needed time to process what I just discovered and didn’t want to talk about it."

        c "Let’s check the other rooms."

        m "Before he was able to respond I stood up again and continued my inspection. I noticed that he wanted to say something but instead he just gave me a nod."

        hide maverick normal flip with dissolve

        $ maverick_redem_bedroom_search = True

        $ maverick_redem_rezasearch += 1

        jump maverick_redem_reza_search


    "Inspect the creaking sound." if maverick_redem_rezasearch == 3:

        if maverick_redem_rezasearch == 3:

            m "As I kneeled down to work on the floorboard, Maverick was watching me closely as I removed it."

            $ renpy.pause (0.5)

            show maverick normal flip at left with dissolve

            Mv "Using a floor as a hiding spot is a clever idea. Since we have buildings for different species, no one would pay attention if the floor creaks when a bigger dragon walks on it."

            Mv "Not to mention that most species lack hands to properly grab things, making this kind of hideout almost useless to most of us."

            c "Back in my world this was actually a common hiding spot. It even became kind of a cliché in crime series."

            m "Inside the hole was a little bag with spare ammo and a small book."

            Mv "So Reza hid more ammo in case he’d lose the ones he always carries with him."

            c "...or in case of you confiscating it."

            Mv "It seems had planned his escape for some time now."

            c "Let’s not forget that he ran away after you appeared at the portal."

            Mv angry  flip "Are you saying that it’s my fault that he escaped?"

            c "No, what I meant his that he wasn’t planning to hide that night. It’s very likely that he had no time to return to his apartment."

            c "Otherwise he would have taken the ammo and his book with him."

            Mv resideeye flip "You… might be right about that… sorry."

            $ renpy.pause (0.5)

            show maverick normal flip at left with dissolve

            c "Like you said, he most likely had plans for escaping and hiding in case of an emergency."

            c "The missing knives could be evidence that he already set up a hideout somewhere."

            c "You messed up his plans and he wasn’t able to destroy all the evidence like the letter we found…"

            m "I took the book and opened it. I smiled and looked back at Maverick."

            c "…or his diary. I’m sure there is something that can help us even if it’s just about his way of thinking."

            Mv laugh flip  "Are you sure you’re not secretly a police officer?"

            Mv normal flip "However, you're right. Maybe Naomi and the forensics team can find more information."

            m "He gave me a sign that he wanted me to give him the diary but I hesitated."

            c "If you don’t mind, I’d like to take the diary and read it first."

            c "Reza and I were once friends, so maybe I’ll notice something your people might miss."

            m "Maverick looked at me for a moment but then lowered his hand."

            Mv "That might be a good idea. You've been of great help so far and earned my trust …for now."

            m "Hearing that from Maverick seemed like a big compliment. I never expected him to blindly trust me after just two meetings so hearing those words felt good."

            c "You won’t regret it, Maverick."

            Mv "I think with all the new evidence we found we should leave now."

            Mv "Even if this apartment is isolated from the others, there is always a chance that someone might notice us."

            c "You're right. Let's leave for now."

            show maverick normal with dissolve

            $ renpy.pause (0.5)

            hide maverick normal at left with easeoutleft

            m "With that we left the apartment and Maverick made sure to open the curtains again to make sure no one would notice any difference."

            jump leave_apartment

        else:

            jump maverick_redem_reza_search






label leave_apartment:

$ renpy.pause (0.5)

scene black with dissolvemed

stop music fadeout 2.0

$ renpy.pause (0.5)

scene np5e with dissolvemed

m "Maverick and I silently walked back to my apartment. He tried his best to keep a neutral face but I was able to notice that he was worried about me and what I learned today."

m "However, I needed time to come to terms everything and he seemed to respect it."

m "We were careful to avoid unwanted attention and soon we arrived at my apartment."

c "Thanks for escorting me home."

show maverick normal flip at left with easeinleft

Mv "Well, you helped me with the case so it was the least I could do." 

Mv "If you need anything or just want to talk…well, you can call if you want."

m "I appreciated Maverick’s attempt to offer his help. It was weird to think that, only a few days ago, he saw me as his enemy but now tried to comfort me."

c "Thank you Maverick. Good night."

Mv "Good night, [player_name]."

show maverick normal at left with easeinleft

$ renpy.pause (0.3)

hide maverick normal at left with easeoutleft


$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

play music "mx/rezatheme.ogg" fadein 2.0

m "After Maverick took off, I entered my apartment and had dinner. Not feeling tired yet I grabbed the diary we found at Reza’s apartment and started to read."

m "The first few pages were what I expected. Reza was writing about his time in our school and his plans."

m "In other circumstances I would have felt bad about invading his privacy but we needed every possible detail to understand him and his motivation."

m "Sure, he wanted to save mankind but the Reza I knew would have never murdered others. Not that I had any doubt left that he was behind the dead dragons."

m "The things in his apartment’s hiding spot had more than enough evidence that he was on a secret mission and that I was just a pawn."

m "Then something caught my attention. Close to our graduation a name appeared in almost every entry, Jenna. It seems she and Reza had a few classes together like politics or chemistry."

m "I also went to chemistry but I couldn’t remember a girl with that name."

m "I found my name a few times but there wasn’t anything left I didn’t already know. Jenna however appeared in every entry by now."

m "She graduated the same year as us but she and Reza didn’t go to prom night. Instead they went to some sort of job meeting. After that they celebrated and got drunk."

m "The entries after our graduation didn’t have any information about Reza’s job but mostly about his time with Jenna. They both had started a relationship and were happy together."

m "The way Reza had written during that time was like I never thought he could be; the words of someone deeply in love."

m "By now I couldn’t stop reading the diary. Reza and Jenna were still dating but there was some sort of accident."

m "The next few entries had been skipped and the writing of the new ones where slightly different."

m "I learned that Reza had lost an arm in the accident but his company implanted him a highly advanced prosthesis including artificial skin."

m "I’ve of course seen the advertisements for those prosthetics and that they were as close to a real limb as possible. The skin was the patient’s own, cloned and attached over the machine."

m "The new arm Reza had would have been able to feel everything his real arm could; warmth, cold, a soft touch and pain."

m "With the cloned skin no one would know the difference while Reza would have a slight advantage with his new arm."

m "He wasn’t super strong nor had he any other advantage like in sci-fi movies but his new arm was still as strong as if had trained for years."

m "It had taken Reza almost no time to get used to his new arm but then the scenery in the diary changed…the flare was about to happen."

m "He and Jenna had been hiding in a bunker under their company while it happened and the isolation had been enough for Reza to keep his arm working."

m "The following pages were as chaotic as the post-flare time. Chaos broke out, people died but Reza and Jenna were able to survive…until a few months after the flare."

m "The last entry was short but it told me everything I needed to know to how dangerous Reza might actually be."

m "\"Jenna is dead. They found and murdered her for our supplies. I was weak but now I’m strong.\""

m "\"I made them pay; all of them. No one will get in the way of my dreams ever again. No more weakness and no more mercy.\""

m "That was the last entry and I had the weird feeling that, by the end of this case, one of us would be dead while the other would deciding the fate of two worlds."


stop music fadeout 2.0

$ maverick_redem_scenesfinished += 1

jump ml_date_end






























