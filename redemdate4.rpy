label redemdate4: 

scene black with dissolvemed

$ renpy.pause (0.5)

scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

m "I didn’t need to wait long until I heard the doorbell. Once more I envied the winged dragons and how fast were."

play sound "fx/door/doorbell.wav"

m "When I opened the door I was surprised to see Maverick being so excited and happy. He was really looking forward to go hiking again."

m "Just like me, he had also prepared a backpack. It was very big and I wondered what he was carrying inside."

show maverick normal flip at left with easeinleft

c "Hey Maverick."

Mv rehappy flip "Hey, [player_name]. I hope you’re ready for our trip."

c "I was looking forward to it all day for this."

Mv "Great, then let’s go."



$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_hike_forest_a with dissolvemed

play music "mx/cruising.ogg" fadein 2.0


m "Together we made our way out of town and into the forest.  From what Maverick told me it wouldn’t take us long to reach the hut he had rented for today."

m "It seemed as if dragons and humans had more in common than I thought."

m "I looked at Maverick and he seemed like a completely new dragon. He was smiling and clearly enjoying his time."

show maverick rehappy flip at left with easeinleft

Mv rehappy flip "I never realized how much I missed being out here again. Our town is nice and usually peaceful but being here feels just right."

c "I know what you mean. Back in my world, I loved hiking through the forest. Even with all our technology and the possibilities they opened, there is nothing more relaxing than going outside without all of that. "

c "Well, except maybe something to help you to dispel predators."

Mv normal flip "Don’t worry; the area around our town is safe. There are a few small carnivores but they are harmless toward us."

c "That’s good to know. What kinds of animals live around your places? I barely saw any animals during my time here." 

Mv "We have mammals like Mouflons, Aurochs and some smaller ones like the Cimolodonta. There are also birds like the Vegavis."

m "While we made our way deeper into the forest, Maverick stopped talking to concentrate on the path ahead. It gave me some time to think about the Administrator."

m "Was it true that they didn’t bring any DNA samples to this place? I had learned that there had been mammals and birds on Earth 65 million years ago but Mouflons and Aurochs weren’t among them as far as I remember."

m "Did we never find any fossils of them or was the Administrator lying? All I knew was that I had the feeling that there was more to the story than what the Administrator was telling me."

m "After a short break to make sure we were still on the right path, Maverick continued. "

Mv "You’re lucky that the portal was found in one of our safety zones because the animals outside of them are way bigger and more dangerous. Even the strongest of us could end up as prey to them."

c "What do you mean with safety zones? "

Mv "Despite of what you’ve seen so far our world is quite dangerous. Each time when we build a new settlement we need to install sonic poles to increase our space. Otherwise our feral brethren would most likely attack us. "

c "I guess those feral brethren are similar to what apes are to humans; an ancestor that evolved over time into your species."

Mv "Yes, you can say it like that. They look similar to us, especially to runners and flyers, but they neither have sentience nor any of our natural weapons like fire breath. "

Mv "Some scientists are unsure about the theory that we’re related to them because our feral brethren are exothermic while we produce our own body heat. Not to mention the difference in our DNA. "

c "Maybe it changed when your ancestors slowly gained sentience."

Mv "That’s one of the theories our people have; a more developed brain and generations of changes to become what we are now. "

Mv "I’m not an expert but it seems that there are still many unanswered questions and a lack of fossils of links between us and our feral brethren. That’s why many of us still believe the myth that we were created by humans."  

m "If the Administrator story was true it could have a huge impact on the dragons and their society. So I decided to not mention any of this to Maverick for now. At least until I had more information."

c "What do you believe is true?"

Mv "I don’t really care about how we became the way we are but what we do with the gift of sentience. It’s important to appreciate the life we have been given and make the best of it. Not just for ourselves but also those who’ll follow us."

Mv "I guess that’s how I ended up in Bryce’s team. I wanted to make a difference."

c "Did you always want to become a police officer? "

Mv "No, I actually wanted to become a stunt flyer when I was younger."

Mv "I guess most of us with wings want to do that when they're younger."

Mv "However, when I got older and was understood that my kind wasn't fit for stunt flying, I started to search for my own calling."

Mv "I never was into politics, science or any other job like that. The thought of spending my whole life at a desk writing documents seemed like a nightmare. "

c "Doesn't your job also have a lot of paperwork?"

Mv "That's true but I can spend most of the time on the street and helping others. "

Mv "However… someone challenged me to look deeper into what I like or what I'm good at, and how I can use that in a job. "

Mv "My species is as strong as earth dragons but we can also fly."

Mv "During my time in school I also kind of became the one who looked after the younger students. I guess they looked up to me for some reason."

Mv "In my later years I met Bryce and we became friends. Unlike me, he already had plans for his future and wanted to join the police."

Mv "In the end, it was similar to what I did in school; helping and protecting others."

c "So Bryce was the one who helped you to find your calling?"

Mv "Yes, without him it might have taken me longer to find out what to do with my life."

m "He gave a small laugh and I wondered if Miles was the one Maverick mentioned. Even without knowing much about him he seemed like a nice person."

Mv "Thinking back, it was also Bryce who asked Naomi to join our BBQ and she ended up joining the team, too."

if naomiscenesfinished >= 2:

    c "She told me about that and how she wasn’t sure if he was just being nice or trying to hit on her."

    Mv laugh flip "Knowing Bryce it was probably a mix of both but at least he knew better and didn’t try anything."

    show maverick normal flip with dissolve

else:

    pass

c "Bryce seems like someone who sees something in others that they don’t see. "

c "I mean, after Reza shot you, Bryce had no reason to trust me. Given all the information he had at that time, he should have suspected me as well but instead he asked me to help with the case."

Mv "You’re right; Bryce has a special talent to see the potential of others. His instincts and hard work have helped him to become the chief of our town’s police department despite his young age."

Mv "In hindsight, I should have trusted his judgment."

c "Don’t worry about that. You had more than enough reasons to have your doubts. I could have turned out to be another Reza."

m "It seemed as if he wanted to say something but then changed the topic instead."

Mv "What about you? Was being an ambassador always something you wanted to do? "

c "In some way it might actually have been but for a different reason that the political aspect. "

Mv "How so? "

c "As a child, I always dreamed of becoming an astronaut or adventurer. I hoped that I’d discover something new or establish the first contact with an alien species. We had been close developing the technology to leave our solar system but political reasons put a halt on it. The flare did the rest."

Mv "So you guys were able to travel through space like in those sci-fi movies?"

c "Yes although the farthest we had been were our moon and a neighboring planet. We tried to colonize both places but in the end it didn’t work out with the technology we had at that time."

Mv "That’s amazing. We might have the technology to leave the planet but the council never really cared for our space program. The most we have are satellites for communication but everything else was defunded."

c "Maybe with the knowledge of the PDAs that will change."

Mv "Maybe but I guess we first have to learn more about our own planet before leaving it. Despite a few satellites for communication, we don’t really use them for anything else. Not even for making a map of our planet."

Mv "At least a few brave adventurers are trying to look if there are other continents out there."

c "So you also have ships?"

Mv "Yes but mostly for fishing or transporting resources. Only a small number of sailors actually care about looking for other places."

c "You know, being a pirate in the early days of our civilization also was something I dreamed about."

Mv laugh flip "So you wanted to become one of the bad guys, sailing the seas? "

c "Kind of but I saw it more as a romantic dream full of adventures and freedom. Being free to do what you want without any rules or consequences and living your life the way you want to."

Mv normal flip "I have to admit, that it does sound nice."

c "Yes, sadly it was far from the truth."

c "Once I was old enough I understood that there was nothing left to explore on our planet. With all our technology, we had traveled to every place on earth, even the depth of the ocean."

Mv "So it seems your technology was a blessing and a curse at the same time?"

c "Yes, more or less."

c "My degree in biology was mostly because it could help me to find a good job. I always was good in science so it was a good choice, even if it wasn’t what I really dreamed of when I was younger."

c "With most of our difficult tasks being done by machines anyways, I chose sociology as my second subject. I mean, we already reached the point where poverty was gone and everyone was able to live a good life."

c "…and to be completely honest, a part of me always hoped that we would sooner or later find a different civilization. We had many programs that searched for extraterrestrial signals and we were certain that it was only a matter of time until we’d find something out there in space."

c "However then the flare happened and both of my degrees became mostly useless."

Mv "I wouldn’t say that. Without those degrees, your people would have chosen someone else as your species’ ambassador. Maybe even someone who would have made things worse."

c "I guess you’re right. Even though I wasn’t the first to come here, I'm now more or less living my dream… well, except for the whole Reza case."

Mv "Don’t worry; once we caught him and your people got the generators, you have a whole world to discover…or at least the parts which we have colonized so far."

c "I like the sound of that. "

Mv laugh flip "Maybe we can even buy a ship and become pirates."

m "We both laughed and made our way to the next part of the hike. The path steepened and soon we were walking up the mountain. Somewhere up there was the hut."


$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_hike_forest_b with dissolvemed

show maverick normal flip at left with easeinleft

m "As we went deeper into the forest, the way got steeper and more difficult. After some minutes, we had to cross a small river. Luckily someone already had prepared a bridge."

m "Carefully not to fall into the water I crossed the river. All the time Maverick watched me and made sure I was safe although it seems my arm got his attention."

Mv "You know, I never asked but what kind of machine do you have on your wrist? "

c "This device is similar to a PDA but with a smaller storage and not as advanced as the PDAs I’ve delivered. "

c "When my people agreed to send someone through the portal, they decided that it was a good idea to give us these devices. " 

c "After I offered my own PDA for the trade, I got this one to take notes for everything I’d learn here. In theory, the two PDAs should also be able to communicate with each other. In hindsight, it might have been part of their plan to betray the trade."

Mv "Now that you mention it I’ve seen Reza with one of those on his first days here but once I was assigned as his escort he stopped wearing it."

c "I guess he was worried that your people would be able to track him when he’s wearing it. "

c "The night he escaped I tried to find him with my PDA but he is blocking all signals. Guess he knew that someone would try to find him."

Mv "With everything we learned, it only makes sense that he got rid of his PDA."

c "I just hope your people won’t step back from the trade if they hear about Reza’s mission."

Mv "There's no need to worry; with your help and the PDAs, we can say that it was his own doing and that there was no big plan behind his actions."

c "So you’d lie to the council to help me?"

Mv "I don’t see a reason to reveal all information as long as we can catch Reza. There is no reason to make your people suffer just because some politicians are acting like jerks."

c "That’s means a lot to me, thanks."

Mv "You’re welcome."

Mv "I’m curious on what we’ll learn from all the data you brought with you. We didn’t have that many technological advancements in the last few years but with the PDAs it will change."

c "I’m sure the data will be useful for your people. However, besides our technology, there is also information about our culture, history and medicine."

if persistent.heardaboutcancer == True:
 
    m "The thought about the PDAs and the medical data made me think of Anna and her condition. Sure, once the trade was finished we’d be able to cure her cancer but for some reason I added a note to my PDA."

    m "I quickly wrote \"The cure for cancer might be in the PDA’s medical data \". "

else:

    m "The thought about the PDAs and the medical data caused a strange feeling. I didn’t know why but it was as if a voice in my head urged me to add a note to my PDA. "

    m "I quickly wrote \"The cure for cancer might be in the PDA’s medical data\". "

m "Once I was finished I noticed that Maverick was looking at something in the distance."

Mv rehappy flip "We’re almost there. I can already see the hut from here."

m "Despite my best effort, I couldn’t see anything but trees. Once more I envy the dragons for their abilities."

c "You have good eyes. I can’t see anything but trees. "

Mv "I guess that one of those things my kind is better at. You have way better hands than any of us and your technology is better than anything we have. "

c "That’s true, from the beginning we lacked weapons or special abilities all the other animals had. However, that led us to develop tools and weapons to survive."

c "In the end, despite our differences, both of our species reached sentience and were able to create an advanced civilization."

Mv "I’m sure both of our species might be able to advance even further once we start to work together."

c "I hope so. Despite my leaders making the wrong decisions to save mankind, I’m sure we’re stronger together as friends as all alone. " 

Mv "We’ll prove to them that cooperation is better than what they’re doing."



$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_hike_top with dissolvemed

$ renpy.pause (0.3)


label redemdate4_b:


m "Less than a hour later we reached our goal. We had a clear few over the forest and in the distance I could even the farm and the town. "

m "The hut Maverick mentioned was a little further into the forest so that it looked as if it was night even if it was still afternoon. "

show maverick normal flip at left with easeinleft

Mv "Here we are; looks just like in the good old days." 

Mv "I know the hut doesn’t look like much but it has everything we need, even a working bathroom. That’s the benefit of a species with wings; you can quickly move everywhere, even on top of a mountain."

c "Back in my world we had machines that helped us to fly called planes and helicopters. However, even then only a few people were able to use them and only for certain things. Your wings are way better."

Mv "My kind might not be as good as other flyers like Adine’s kind but I can’t think about a life without them."

c "That makes me wonder; how many different kinds of dragons do you have?"

Mv "There are basically 4 main categories; earth dragons, flyers, runners and walkers. Despite looking different, both Damion and Zhong would be considered as walkers. I’d say their kind would be the closest to humans."

Mv "Next to the main categories are the sub-categories and depending on the location, some species prefer one location over another. However as of now, it’s not possible for one species to have children with a different one."

Mv "Usually interspecies couples would either adopt a child or only one of the parents would be biologically related."

Mv "How does it work for humans? Do you also have different species or did your whole kind developed the way you and Reza are?"

c "During our evolution there had been a few different species like the Neanderthal and Homo sapiens but in the end only the Homo sapiens survived and became the ancestor of mankind."

c "I’d say the only difference would be the tone of our skin but it’s only on the outside and depends on where the ancestors lived; like the more sun was present the more the people developed a darker skin to resist the sun. "

c "However, we all are one species. Before the flare we were close to unity despite all our different cultures, but in the end… well, you know what happened."

c "Maybe once all of this is over I could show you my world. We would have to rebuild everything, and solve the problem with the Raiders but then you could see what my world looks like."

Mv rehappy flip "I’d love to visit your world."

play sound "fx/rumble.ogg"

$ renpy.pause (1.0)

Mv laugh flip "…but I think I should catch us something to eat first."

c "Sounds like a plan."

m "While I collected wood and prepared the fireplace, Maverick was flying above me, searching for our dinner. "

$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_hike_hut_outside with dissolvemed

$ renpy.pause (0.3)


m "Luckily the fireplace was at a secure location without any trees close by. I wasn’t sure how strong Maverick’s fire breath was but at least it was far away from anything that could cause a forest fire."

m "I didn’t need to wait long until saw Maverick flying down. A few minutes later he returned, carrying his prey on his back."

show maverick normal c flip at left with easeinleft

Mv normal c flip "Oh, you already prepared the fireplace. Perfect timing; I found our dinner."

Mv "You might want go behind me; the others are always telling me that my fire is too big."

m "I quickly went behind Maverick before he ignited the campfire. To say that his fire was too big would have been an understatement. "

$ renpy.pause (1.5)

play sound "fx/firex.ogg"

$ renpy.pause (2.0)

play soundloop "fx/fire2.ogg"

if bryce3unplayed == False:

    m "What he unleashed was more or less an inferno. Now I understood why Bryce and the others didn’t want him to make the fire during the BBQ."

else:

    m "What he unleashed was more or less an inferno."

c "That was way bigger than I expected. I’m glad there aren’t any trees nearby."

Mv "Luckily the owner of the hut made sure that even dragons with my kind of fire breath can use the fireplace. We kind of had some problems because of that years ago."

Mv "If I’m not mistaken, you humans can only eat cooked meat, can’t you?"

c "Yes, raw meat can be dangerous to us."

Mv "We can’t let that happen. Let me prepare some meat for the both of us."

play sound "fx/gore.ogg"

m "Maverick quickly prepared several pieces of meat for the two of us and placed it near the fire."

c "What kind of animal is that? "

Mv "It’s called barasingha and lives here in the mountains. Although Anna once told me that she found one while she was making a trip to the woods for a week."

Mv "Could you watch over our food for a few minutes? Need to get all that blood off of me."

c "Sure, no problem."

show maverick normal c with dissolve

$ renpy.pause (0.5)

hide maverick normal c at left with easeoutleft

m "While I watched over the meat, Maverick went to a nearby river and cleaned himself. I haven’t even noticed the river before."

m "Using a stick, I was flipping over the meat to make sure it was cooked from both sides. By now it was getting darker and colder but luckily the fire was keeping me warm. "

m "When Maverick returned he sat down next to me."

show maverick normal flip at left with easeinleft

Mv "That’s much better. Looks like the meat is finished already."

Mv rehappy flip "Enjoy your meal."

c "Thanks, you too."

scene stars dk at Pan((0, 200), (0, 0), 6.0) with dissolve

m "While we were eating in silence, I looked up to the stars. Since I talked to the Administrator, I had been trying to look for star formations familiar to me. "

m "Of course it wasn’t possible with my eyes since the stars haven't moved to become the night sky I remembered yet but using my PDA, I actually confirmed the Administrator’s story. I tried my best to remember all the ways we had to save the planet from comets but most of them would have been impossible for the dragons."

m "So it came down to what the Administrator suggested; getting as many generators as possible to use the energy to divert the comet. Blueprints for the machines had been on the PDAs, so all they had to do was to build the machine while we made sure that Reza was captured."

$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_hike_hut_outside with dissolvemed

$ renpy.pause (0.3)


label redemdate4_c:

m "Lost in my thoughts I hadn’t noticed that Maverick had finished his meat by now. He was also looking at the sky as if he was wrestling with his feelings."

m "Once I was finished with my meat, Maverick’s look had changed and I could see that he had made a decision."

stop music fadeout 2.0

stop soundloop fadeout 2.0

play music "mx/prophecy.ogg" fadein 2.0

show maverick normal flip at left with dissolve

Mv "[player_name] there is something I should tell you." 

Mv "It’s something I’m not very comfortable talking about it but it’s something that at least my close friends should know."

Mv "It kind of explains why I am the way I am and why I focus so much on the details during my work."

m "I could see that it wasn’t easy for Maverick to tell his story and I wondered if I should tell him that he doesn’t need to go on. However, there was something in his eyes, a look that showed how important it was to him to tell me the truth. "

Mv "I'm sure you heard the story or parts of it already but I had an older brother, Miles. He was my only sibling and we grew up together."

Mv "I always looked up to him and he was the kind of dragon everyone liked, including Bryce and Anna. He and Anna had even been a thing although it wasn’t about love but just… well, you know."

Mv "Miles worked for a big company that did charity projects for children or other dragons in need and even if he could be a little special sometimes, he had a good heart."

Mv "You probably already guessed it, but he was the one I used to go hiking with, and we also did other things together. We always had been a team, even after he got sick."

Mv "It was a degenerative disease we weren’t able to cure at that time. We had medicine to help him and stop it from getting worse but it had taken several more years until they were able to cure it… way too late for Miles."

m "He stopped for some time, looking sadly at the sky. I knew that it wasn’t easy for him to talk about Miles so I put my hand on his shoulder, trying to comfort him."

m "He seemed to appreciate my gesture and gave me a sad smile before he continued."

Mv "A few years ago we had a murder case where the victims were not only killed but also… eaten."

Mv "No member of the whole police department had ever had a case like that before and they made the most promising officer the case leader, Bryce."

Mv "At first we thought that the barrier around our town was damaged and the sonic poles were malfunctioning, so that one of our feral brethren had been able to sneak in but we weren’t prepared for the horrible truth."

Mv "When we finally found the killer it turned out that it was Miles who was feeding on another victim. We tried to talk to him but he was acting like a wild animal and didn’t even recognize me."

Mv "Suddenly he attacked Bryce, burying his teeth into his chest, causing the scars you probably noticed."

Mv "I tried to talk to Miles but when I realized that Bryce would die without my help, I had to kill him."

Mv "Bryce survived and luckily wasn’t mortally wounded but it didn't change the fact that I had just murdered my own brother."

Mv "An autopsy later revealed that his brain had degenerated beyond repair and that his sickness was the cause for his behavior. Anna did some digging and found out that the medication was wrong, but it didn’t change anything for me."

Mv "After Miles’ funeral, I tried to hunt down a drug dealer named Raph. Although it was never confirmed, I had always believed that it was his drugs that caused Miles' condition. "

c "So you think those drugs actually caused Miles' sickness? "

Mv "I don’t know. Possibly not but it felt better to give someone the fault for it than accepting that it was just a natural reason. "

c "Did ever you find Raph? "

Mv "Bryce did a few weeks later. Same story as always; he was selling drugs at the bar but this time the client was actually an undercover cop. He was punished but he didn’t have any of those pills with him he had sold to Miles."

Mv "Despite all the pain he caused, Raph got released a few years ago. They said his \"rehabilitation was successful\" but I have tried to keep an eye on him until he disappeared from one day to the other. "

Mv "If Bryce hadn't stopped me after Miles’ death, I would have searched for Raph on my own. To be honest, I don’t know what I would have done to him…"

Mv "Guess Bryce saved me from doing something stupid that would have ruined my life."

Mv "Bryce is a good friend and he helped me through it but I guess a part of me died with Miles…"

m "He released a sigh and looked at the stars. I knew that he needed some time to finish his story and I didn’t want to interrupt him. "

m "It was, as if he had waited years to finally find the courage to tell someone about his feelings. "

Mv "You’ve seen how I can be. Even under normal circumstances I’m… what’s the fitting word? "

c "Grumpy? Angry? Always playing the bad cop? "

Mv laugh flip "Yeah, more or less all of that." 

Mv normal flip "I was different before all of that crap happened. I mean, I wasn't as outgoing and flirty as Bryce but I’d say more like Sebastian, I guess. I was pretty naive and tried to see the good in everyone but Miles’ death changed me." 

Mv "I always had some problems telling those close to me how I felt, which might be a reason why it didn’t work out with Anna and me but losing Miles, knowing that I murdered him…"

c "Maverick, from everything you told me I’d say that Miles was already gone and beyond saving. If you would have reacted in a different way, then he would have first killed Bryce and then you."

c "Weren’t you the one who told me that we can’t change things that are beyond our control? "

Mv "I did but still… I just think that, if I would have tried harder or would’ve just talked to him the day after Anna got sick because of the pills… maybe I could have saved him. "

Mv "However I was mad at him because of those stupid drugs and canceled our hiking trip. I couldn’t have known that it would have been our last one."

m "I knew how hard the truth was and how much a tragedy like this hurt but I wanted to help Maverick to move on. Even if a part of me wasn’t sure about his reaction."

c "Miles is dead and feeling guilty over something that never was your fault will only hurt you more. "

Mv "I know but I… it’s…"

c "Do you think Miles would have wanted that?"

Mv "No, I guess you’re right, he wouldn’t want that."

Mv "We had our differences because of his stupid antics, but other than that we always had fun and supported each other." 

Mv "For years I asked myself if I could have prevented it if I wouldn’t have been mad about him… but I guess it’s one of those questions without an answer."

c "If the cause was the medication then there was no way for you to prevent it."

m "Maverick still looked unsure but then gave a weak smile."

Mv "Miles would probably be mad at me for acting like the way I do. Maybe it’s time to move on even if it means to accept that there was no other way for me to react."

Mv "Miles will forever be a part of me but you’re right, it’s time for me to let go of the past, no matter how hard it will be."

c "I’ll be there for you if you need me, just like Bryce and your other friends."

Mv "Thank you [player_name], for everything."

c "That’s what friends are for, Mav."

Mv "You know, I never talked to someone about all of this."

Mv "Bryce and Naomi tried to talk to me despite having their own problems in life, but I just blocked everything out. I kept pushing them away until they stopped trying." 

Mv laugh flip "Guess I have to make it up to them for being such a grumpy friend."

c "How about another BBQ?"

m "I looked at the burned ground next to the meat."

c "…but please let someone else make the fire." 

Mv "The fire wasn’t that bad, was it?"

m "I didn’t say anything and instead looked at the fireplace. He followed my look and saw the damage his fire caused."

Mv "Ok, maybe I need to train the size of my breath a little."

Mv laugh flip "Would be a shame to lose the forest."

c "I really hope you’ll never catch a cold. Your sneezing would cause way too much damage."

Mv laugh flip "That’s an old joke. Bryce did that one last year when Zhong got his cold."

Mv rehappy flip "I think we should get inside. I don’t want you to catch a cold; the nights up here can be very chilly."

c "Sounds like a good idea even if I love watching the sky from here."

stop music fadeout 2.0

$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_hike_hut_inside with dissolvemed

play music "mx/anna4.ogg" fadein 2.0

m "Before Maverick and I went back inside the hut, I took a still burning branch from the slowly dying campfire. As soon as we both went it I ignited the cooking pot to heat up the room."

m "We both sat down next to the fire and enjoyed the warmth. Even after almost two weeks of being here, it still felt like a dream to be in a world full of sentient and friendly dragons."

m "If only Reza would have been able to see this world as I did then he might have given the trade a chance instead of becoming a serial killer."

m "Even if we could get all the generators, we still needed more than just energy. The dragons could provide us with resources like food or medicine, maybe even producing things for us or sending people to help us rebuild, while we on the other hand could teach them about our technology and everything else we had."

m "This short time here has made me realize something."

show maverick normal flip at left with easeinleft

if blood == True:

    c "We're not that different, you know."

    Mv "What do you mean?"

    m "I reached into my pocket."

    c "(I still have that? I don't know how long it's been...)"

    play sound "fx/paper2.ogg"

    m "I pulled out the wrinkled piece of paper and showed it to him."

    c "According to these test results, humans and dragons show remarkable similarities for different species from different evolutionary lines and completely different worlds."

    Mv normal flip "That’s interesting especially since our species seem to be way too different. "

    Mv "I know that we’re friends but I just want to make sure that you understand that it wouldn't have made a difference to me if other dragons came through the portal instead of humans."

    Mv "I was the only one who followed Reza and knew something was off, but all of my concerns were swept away in the wind."

    Mv "It was never about you being humans. It's about my people not hearing my pleas, and the leniency they were willing to show you, all in the name of fostering this diplomatic relationship."

    Mv "But then two mythical humans came in here and one of them strutted around like he owned the place as he tore my home apart. The blood of those who died is on the hands of everyone who allowed this to happen."

    Mv "If they had listened to me in the first place, maybe I'd have caught Reza that day I was wounded, and things would look very different right now."

    c "I agree. Even back then I never hated you for your behavior because I knew that, in your way, you only wanted to protect your people."

    Mv "I’m glad you decided to talk to me despite my behavior. You had more than enough reasons to distrust me but you still tried to solve the conflict by talking to me."

    c "I just thought that it would be better to work together instead of opposing each other. It was easy to see that, despite your behavior toward me and Reza on my first day here, you were always doing what you felt was the best for your people."

    Mv "I’m very glad that I was wrong about you. I guess after all those years as a cop I still have to learn a lot."

    Mv nice flip "Wait a minute, you had Anna perform these tests for you?"

    c "It was more the other way around. She was the one who wanted to study my blood. "

    Mv normal flip "Suddenly, I'm not surprised that you had these tests done. She can be ruthless when she wants something."

    Mv "What did she do to get your blood?"

    c "She asked nicely for it."

    Mv "..."

    show maverick laugh flip with dissolve

    Mv "HAHAHAHAHAHAHAHA!" with Shake((0, 0, 0, 0), 3, dist=30)

    Mv "She asked nicely?"

    Mv "Nothing else in this world right now could be worth more than samples of your blood. And you just gave them to her."

    c "I mean, it was a little reckless, not knowing what she would do with it but truth to be told, I was curious, too."

    Mv normal flip "I agree that it was a little reckless but at least Anna won’t do anything bad with it. She’s not that kind of person. "

else:

    c "I’ve been here for almost two weeks now and it seems we're not that different."

    Mv "What do you mean?"

    c "When we met at the café I’ve told you how your world was similar to how our world looked like before the flare. Spending some time here showed me that it’s not just the way your world looks like but also how your society works."

    c "During the whole case and also my free time here, it felt just like home. Sure, there are many differences but every time I talked to someone it felt as if I could close my eyes, not knowing that I was talking to a dragon, I’d think that another human would be in front of me."

    Mv normal flip "That’s interesting especially since our species seem to be way too different. "

    Mv "I know that we’re friends but I just want to make sure that you understand that it wouldn't have made a difference to me if other dragons came through the portal instead of humans."

    Mv "I was the only one who followed Reza and knew something was off, but all of my concerns were swept away in the wind."

    Mv "It was never about you being humans. It's about my people not hearing my pleas, and the leniency they were willing to show you, all in the name of fostering this diplomatic relationship."

    Mv "But then two mythical humans came in here and one of them strutted around like he owned the place as he tore my home apart. The blood of those who died is on the hands of everyone who allowed this to happen."

    Mv "If they had listened to me in the first place, maybe I'd have caught Reza that day I was wounded, and things would look very different right now."

    c "I agree. Even back then I never hated you for your behavior because I knew that, in your way, you only wanted to protect your people."

    Mv "I’m glad you decided to talk to me despite my behavior. You had more than enough reasons to mistrust me but you still tried to solve the conflict by talking to me."

    c "I just thought that it would be better to work together instead of opposing each other. It was easy to see that, despite your behavior toward me and Reza on my first day here, you were always doing what you felt was the best for your people."

    Mv "I’m very glad that I was wrong about you. I guess after all those years as a cop I still have to learn a lot."

    c "I feel the same way. I’m kind of regretting that I didn’t give Anna any blood when she asked on my first day here. Maybe the results would have shown more similarities."

    Mv "Maybe but I can understand your decision. Nothing else in this world right now could be worth more than samples of your blood and you didn’t know what she would do with it."


if maverick_redem_annaromance == True:

    c "I’m glad she nevertheless agreed to spend time with me."

    m "Thinking about Anna brought back the guilt I felt when I heard about the death of her assistant, Damion. "

    c "You know, I think that I’m not so different than Reza in the end."

    Mv "What do you mean?"

    c "When the third victim was found, Bryce wanted to talk to me about the changes of the case and that I’d be in even more problems now because of it changing to a serial killer case. "

    c "At first Bryce asked me for Anna and I felt my heart drop. I couldn’t see the body but in my mind I saw Anna lying there… but then Bryce asked me for her assistant, Damion… and I was relieved. "

    c "For a brief moment I didn’t care that someone had died and was just happy that Anna was safe. However, then I realized that Damion was dead and I felt like a monster."

    c "How could I be happy that someone I love is safe when someone else was murdered in her place?"

    Mv "Your feelings are only dragon… or human in your case. It’s true that the death of someone always is a tragedy but if it’s someone close to us, then it’s even worse."

    Mv "We aren’t machines that only work on logic but sentient beings with feelings." 

    Mv "Being relieved that someone you love escaped death is natural and the fact that you feel guilty because you were relieved despite someone else being dead only proves that you have a good heart."

    Mv "So don’t think of yourself as being like Reza. He chose to murder innocent people despite never being in danger. Even if I would have arrested you both that night, neither of you would have been in danger. "

    Mv "Bryce would have been mad at me and he would have apologized to both of you for my actions. Other than that, nothing would have happened and you would have gotten the generators." 

    Mv "Reza never believed in the trade and that’s why he chose this path while you’re doing anything in you power to make sure that we bring justice to his victims."    

    c "Thank you Mav, your words mean a lot to me. "

    Mv rehappy flip "You’re welcome."

else:

    pass






c "You know, it’s scary to think how lucky we were today." 

c "If Bryce would have went to the door instead of me…"

Mv normal flip "I hate the thought that I’d almost lost a friend. Knowing Bryce, he would have opened the door without paying attention. Thanks to you two of my friends have escaped death this past two weeks."

Mv "I’m also glad that you’re safe. I talked to Seb and Bryce and it seems as if the trap was put up in a hurry. Otherwise the bomb would have exploded as soon as you opened the door even just a little."

c "It's all thanks to your hard work that we were able to find his hideout so quickly. A day later and he might have finished the bomb and I wouldn’t be here now."

c "Although I’m surprised that it was possible to use the generator to build a bomb. Is it really that easy? "

Mv "You only need a little knowledge to build a bomb out of a generator. It’s still surprising that Reza was going as far as risking all the stolen generators and the PDAs just for a trap."

c "I fear that he has bigger plans for us. All of this feels like some sort of military operation out of an action movie. Do you think he tried to kill everyone working on the case to make sure he was free to do whatever he wants to?"

Mv "It’s possible. We only have a small team in this town. Murdering one of our team could have been enough for him to take bigger risks without us being able to do something especially if he would have gotten Bryce or you."

Mv "However, I just can’t understand why he would steal eggs from the hatchery. Was he trying to use them for blackmailing us in case of us finding him? "

c "I fear that this might be the most optimistic view of his intention."

Mv "I’ve been in the force for years and have seen many things but if that is the most optimistic possibility, then I’m almost afraid to ask what the worst possibility could have been."

c "Well, mankind’s history is written with blood. During the thousands of years of our civilization, my species had done horrible things to each other and animals."

c "Before we reached a society that valued life and the rights of others, those with power didn’t care about anyone else. More than once they forced others to work for them against their will."

c "Moreover, some of our medical data was achieved by experiments on animals or even other humans. That mostly happened during the darker times or in countries without ethical standards."
 
c "Most of my people condemned those things after we reached a higher level of understanding the meaning of life but with millions and later billions of humans those things sadly happened."

Mv "So you think he was trying to take to eggs to your world and do unspeakable things to our children?"

c "Two weeks ago I would have denied that accusation but after everything we learned… I fear Reza would actually do those kinds of things."

Mv "I’m glad we were able to save the eggs."

Mv angry flip "Taking innocent children hostage for whatever reason. He’s lucky that we didn’t find him yet."

c "I agree with you. We need to make sure that he won’t be able to harm any more dragons. Is there a way to protect the hatchery? Maybe with some guards?"

Mv normal flip "We sadly don’t have enough dragons to guard the place. Let’s just hope that he won’t try to sneak in a second time."


if maverick_redem_bryceromance == True:

    Mv "Did Bryce already try to make a move on you or are you two still trying to hide your feelings?"

    c "I don’t think he did. After the BBQ we cleaned up and he told me how he got the scar on his face and that that incident had influenced him to join the police. "

    if brycestatus == "good":

        c "I mean, we did share his couch that night but, other than that, nothing happened."

    else:

        c "I was sleeping at his place that night, but other than that, nothing happened. "

    Mv laugh flip "So no fun basket yet."

    c "Fun basket? Do I want to know what that is? "

    Mv rehappy flip "It’s something he gets when he’s in a relationship but none of us knows what’s inside."

    Mv "Well, except something alcoholic I guess."

    c "Yes, he loves drinking a little too much. I know it’s because of the job but still."

    Mv normal flip "It got even worse since the whole Reza incident began. He’s blaming himself for not seeing that Reza was planning something and for the people that died."

    Mv "He also apologized to me for not taking my concerns seriously and for me getting hurt but, to be honest, I went too far. It was only natural for him to ignore what I said."

    c "I guess most people would have been too naive if they meet someone from their myths." 

    c "Some of you are even seeing humans as godlike beings that created you, so I can understand how most of you didn’t want to believe that some humans were bad."

    c "Something similar might have happened if your people would have visited us. Most of our myths don’t show dragons as gods who’ve created us, but the thought of meeting a different sentient species would have blinded us, too."

    Mv "Maybe you’re right. If Miles never had died, I might have reacted the same way as they did."

    c "So about Bryce; do you think it could work out between him and me?"

    Mv "To be honest, I don’t know. Bryce doesn’t really have a certain type he likes and just enjoys the relationship while it lasts."

    Mv "However, he is always loyal and honest and that’s what he’s asking from others, no matter if it's in a friendship or relationship."

    Mv "He might act like he’s just looking for some fun but I’m sure that he’s searching for a lasting relationship."

    Mv "Before Reza, he even managed to reduce his drinking. It was still a lot but it shows that he knows that he has problems. With the right partner, and of course without Reza, he would be able to get it under control."

    c "I hope so. Of course there’s nothing wrong with drinking from time to time but I saw how it turned good people into a shadow of themselves back home and I don’t want to see something similar happening to Bryce."

    Mv "Don’t worry, it won’t. If things will get worse, Naomi, Seb and I will take care of it. After all, our little squad is more than just a group of friends; we are a family."

    Mv "If you two finally decide to become a thing we’d support you. I mean, by now you’re more or less part of the family even without actually being a cop."

    c "Thanks, Mav. Who knows, maybe I’ll join your team once my ambassador mission is over."

    Mv laugh flip "Just make sure to tell us what’s inside the fun basket. Naomi, Seb and I made a bet on what’s inside. "

    $ renpy.pause (1.0)

    show maverick normal flip with dissolve


else:

    pass



c "Since the whole case with Reza I’ve been thinking over a lot of things. It feels that, one way or the other, the case will be over soon."

c "However, if things turn for the worst and I’d have to make a decision on which world to save I’d choose your people. My mission is to get the generators for my people, but I’d never act like someone like Reza, and wouldn't sacrifice others for that goal."

Mv "Just because Reza decided to become a serial killer doesn't mean that you should give up on your world. We will save your people too."

c "Thank you Maverick but I think you misunderstood me. I’m not saying that I’m giving up on my people. Heck, if needed I would even make sure to take Reza down with me if it would make sure both of our worlds would be saved."

c "However I think you don’t know enough about mankind. We had everything we ever wanted and more but our politicians still supported war and violence to make a profit. " 

c "Even the risk of an electromagnetic pulse destroying our technology was known for decades but our leaders didn’t want to waste money for a {i}hypothetical scenario{/i} even if we literally had weapons that could easily cause those effects. "

c "Then, when the solar flare hit us my people chose violence over rebuilding and only made the situation we were in worse. I understand that they had been scared, I was also scared, but together we could have made things better instead of worse. "

c "Your people on the other hand value the life of every person and even accepted a trade with a unknown species."

c "There are situations when some must live and some must die."

c "We had our chance and we wasted it. Your people shouldn't have to face any consequences just for a chance to revive my species."

Mv "I think I understand what you mean but as long as we have a chance, I’ll make sure to save both worlds. Even if we still don’t know what kind of danger Reza was talking about."

Mv "We are partners and together we will make sure that both worlds will be saved. You don’t have to worry, [player_name]."

c "Don’t worry Mav, I won’t do anything reckless or similar. I just wanted you to know that, no matter what happens when we find Reza, I’ll have your back."

Mv "Likewise."

Mv "It’s getting late. I guess it would be better to go to bed now."

c "You’re right. We still have the best part ahead of us tomorrow." 

Mv "Yes and I’m looking forward to it. It has been way too long."

m "I quickly extinguish the fire and we both went to the bed. Luckily the light of the moon was bright enough for me to see in the dark."

if maverick_redem_maverickromance == True:

    Mv "You know, the bed is big enough for both of us."

    c "You’re right. I don’t want anyone to sleep on the floor."

    m "Even if the bed was big enough for the two of us, we were both very close. Not that I minded. "

    m "It seemed as if Maverick was thinking the same. Even if he tried to avoid my gaze, I could still see his big, brown eyes looking at me. "

    Mv reblush flip "I wonder if you’d like to… you know, go further…"

    menu:

        "[[Accept.]":

            m "It was adorable to see the usual tough dragon acting shy but it was only one more reason for me to love him."

            c "I never knew you where this bold, Mav. "

            Mv "Is that a yes?"

            c "It is."

            m "I surprised Maverick by kissing him on the lips but he quickly returned the kiss while putting his arms around me. He wasn’t the only bold one here after all."

            m "We both enjoyed this moment of affection between us, and I didn’t even notice my clothes coming off. "

            m "Despite being bigger and stronger than me, Maverick was a gentle lover and I knew that, no matter what would happen in the future, this night belonged to the two of us."

            scene black with dissolveslow

            $ renpy.pause (0.5)

            $ maverick_redem_maverick_accept = True
            
            jump redemdate4_flying


        "[[Reject.]":

            c "I’d love to Maverick but maybe we should wait until the Reza case is over."

            Mv normal flip "I guess you’re right."

            $ renpy.pause (0.5)

            show maverick reblush flip with dissolve

            m "I surprised Maverick by kissing him on the lips but he quickly returned the kiss while putting his arms around me."

            m "Even if it was just a short moment of affection, we both enjoyed it."

            c "Goodnight, Maverick."

            Mv "Goodnight [player_name]."

            scene black with dissolveslow

            $ renpy.pause (0.5)

            $ maverick_redem_maverick_accept = False

            jump redemdate4_flying



else: 

    Mv "The bed is a bit small for both of us, so I’ll just be sleeping on the floor."

    c "Are you sure? "

    Mv "Yes, don’t worry about it."

    if maverick_redem_noromance == False:

        Mv laugh flip "… and I don’t want [maverick_redem_romance_partner] getting the wrong idea."

        c "I really need to get used to you making jokes, Mav."

        Mv rehappy flip "You haven’t seen anything yet. Goodnight [player_name]."

    else:

        pass

    c "Goodnight, Maverick."

    stop music fadeout 2.0

    scene black with dissolveslow

    $ renpy.pause (0.5)

    jump redemdate4_flying


label redemdate4_flying:

$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_hike_hut_inside with dissolvemed

play music "mx/cruising.ogg" fadein 2.0

m "It was still early in the morning when the sunlight woke me up."

if maverick_redem_maverickromance == True:

    m "Maverick was still asleep, lying on his chest with his wings above us like a blanket. I tried my best to not to move too much but his instincts as a cop were too good and he slowly opened his eyes. "

    c "Good morning sunshine. How did you sleep?"

    show maverick normal flip at left with dissolve

    Mv "That might have been the best sleep I had in a long time; being here with you and able to move on from the past."

    Mv "How about you?"

    if maverick_redem_maverick_accept == True:

        m "I moved closer to Mav and pulled him into a kiss which he gladly returned."

        c "I’d say it was the best night of my life."

        Mv reblush flip "So you liked it?"

        c "It was different than I expected given our differences but I really enjoyed it. How about you?"

        Mv "I did, too. "

        Mv normal flip "I was just wondering what your people would think if they hear about us?"

        Mv "Would they accept you dating a different species?"

        c "Dragons are people, so I don’t see a problem. Screw those people who might disagree of us being together."

        Mv laugh flip "I didn’t expect a comment like that from you."

        c "You haven’t seen anything yet, Mav."

        m "Maverick stretched not unlike a big cat and got out of the bed. "

    else:

        m "I moved closer to Mav and pulled him into a kiss which he gladly returned."

        c "I’d say it was the best sleep since I got here."

        Mv rehappy flip "I’m glad to hear that."

        m "By now it was easier for me to see when Maverick was bothering something. "

        c "Are you alright? "

        Mv normal flip "Yes, I just wonder what your people would think if they hear about us?"

        Mv "Would they accept you dating a different species?"

        c "Dragons are people, so I don’t see a problem. Screw those people who might disagree of us being together."

        Mv laugh flip "I didn’t expect a comment like that from you."

        c "You haven’t seen anything yet, Mav."

        m "Maverick stretched not unlike a big cat and got out of the bed. "

else:

    m "Maverick was still asleep on the floor next to the bed. I tried my best to not to move too much but his instincts as a cop were too good and he slowly opened his eyes. "

    c "Good morning Maverick. How have you slept?"

    show maverick normal flip at left with dissolve

    Mv "That might have been the best sleep I had in a long time; no dreams about the night Miles died anymore."

    Mv "How about you?"

    c "I’d say it was the best sleep since I got here. I’m still worried about Reza but talking with you made be feel better."

    Mv "I’m glad I was able to help."
 
    m "Maverick stretched not unlike a big cat while I got out of the bed. "

m "We both got ready for the day; luckily I packed a pair of fresh clothes for today. He gave me some bread and water from his backpack and as soon as we finished our breakfast we cleaned up and left the hut."


$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_hike_top with dissolvemed



m "Together we went outside and I remembered that we’d soon fly down and back to the town. Despite trusting Maverick I nevertheless started to get nervous."

m "I went a little closer to the edge of the cliff but looking down was a mistake. Luckily Maverick noticed my tension and tried to calm me down."

show maverick normal flip at left with easeinleft

Mv "I know what you’re thinking but don’t worry, I’ll promise you nothing will happen."

c "Did you already carry someone on your back?"

Mv reblush flip "Well, promise me that you won’t laugh, but I actually did."

Mv normal flip "It was a few months ago when I was helping with a problem at the orphanage. Nothing big, just a broken window after a storm but that’s also part of the job."

Mv "I always had a soft spot for hatchlings and when this little girl, I think her name was Amely, asked me about flying and letting her ride on my back I wasn’t able to say no. "

c "I never knew you were such a softie Mav. I’m sure you’ll make a great father one day."

Mv "Maybe but I’m still too young to think about children."

Mv "However, when I was preparing for the hike I rented this backpack. It comes with some extras like being able to be used as a saddle."

Mv laugh flip "You’d be surprised how often younger or smaller dragons are carried by flyers like me. Especially for families where one parent is a flyer and the other isn’t."

c "I think that’s a good system for your people. Flying was always one of mankind’s dreams."

Mv rehappy flip "You might not have the technology anymore but today you can fly again. Just let me prepare the backpack first."

m "I was surprised that, despite the size of the backpack, it was mostly empty. It seems the few things we had for breakfast were the only items Maverick brought with him."

m "Quickly and carefully Maverick changed the backpack into some sort of saddle. It has a hole on each side for the legs and even something similar to a safety harness. He really thought of everything to make sure I was safe. "

Mv normal flip "I once offered Anna to accompany Miles and me to our trip. She’s of course way too big for this, and it would have needed both Miles and me to carry her, but sadly Anna refused."

c "Was there a reason why she refused?"

Mv "Well, she said she didn’t like high places. I guess that’s true for many dragons without wings."

m "Once he was satisfied, Maverick put on the now transformed backpack. I helped him with the final preparations until we were finished. "

m "Even if I still wasn’t sure if it would work, there was no going back now. Luckily I had a light breakfast."

Mv "Everything is ready. Just climb on my back and we can see if everything fits."

m "After taking a deep breath, I climbed onto Maverick’s back and slid my legs into the holes of the saddle-backpack. Once I made sure the safety harness was where it should be, Maverick stood up again."

Mv "Let’s give this thing a little test, shall we? Tell me if something feels wrong."

m "Maverick started to walk; slowly at first but then faster. To make sure everything was safe; he ran for a short time, jumped and even took off without flying too high. Then he stopped."

Mv "How do you feel? Did everything work out or was something wrong?" 

c "To be honest, I’m actually surprised how well this saddle works. I’m bigger than a hatchling but despite that, everything is tight enough to hold me in position without being too tight or too lose."
 
Mv "Sounds perfect. It’s one of the best versions and I made sure that, if we’re doing this, then there should be as few risks as possible."

Mv "Are you ready for the main event?"

c "I never was more ready."


stop music fadeout 2.0

$ renpy.pause (0.5)

play music "mx/zhongrock.ogg" fadein 2.0

m "Maverick was getting in position while I prepared myself for what was coming next." 

m "Then he started to run and as soon as he reached the edge of the cliff, he jumped and spread his wings."

m "Quickly Maverick started to ascend and gained high. Wind was blowing in my face but the saddle and safety harness was keeping me in a safe position."



$ renpy.pause (0.2)

scene black with dissolvemed

$ renpy.pause (0.2)

scene redem_hike_forest_c with dissolvemed



m "Maverick gained more speed while I was able to see the forest from above. He was flying closer to the mountain and I could see a waterfall created by the river he had crossed yesterday. "

m "Even if it was difficult to talk while flying this fast, I was still able to hear Maverick’s voice. "

Mv "You know, I might never become a professional stunt flyer but I know a few tricks."

Mv "What do you say? Do you want to make things more interesting? "

c "Sure, show me what you’ve got."


m "As soon as I said that, Maverick started to nosedive to gain more speed before he pulled up again while making a roll. "

m "Since he wasn’t nearly as fast as the jets back at home, the g-forces were closer to a rollercoaster than an actual jet. Nevertheless, I was still feeling the effect of his speed."

m "He did another spin and even a looping and I grabbed the saddle by instinct. Not that there was any actual danger for me."

if adine3unplayed== False:

    m "It was true that Maverick wasn’t nearly as agile or skilled as Adine given the differences of their bodies but he nevertheless knew what he was doing."

else:

    pass

m "Once more we were closer to the mountain but this time Maverick flew right under the waterfall and through a giant gap between the two sides of the mountain."

m "I didn’t know how long we were flying but I noticed that we were slowly but steadily flying away from the mountain."

m "We were very fast and Maverick started to ascend higher and higher. Despite slowing down we were soon flying through the clouds and the sky was ours."

stop music fadeout 2.0

$ renpy.pause (0.5)

$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_hike_end with dissolvemed

play music "mx/basicguitar2.ogg" fadein 2.0

m "It was surreal how quiet it was up here and the view was breathtaking. By now the sun was slowly going down and we were able to see a beautiful sunset."

Mv rehappy flip "That… was way more exhausting that I thought… but it was worth it, don’t you agree?"

c "It totally was. I never expected to experience something like this and back in my world, even with all our technology, this would have been a dream that would have never come true."

c "Thank you for this, Maverick."

Mv "It was the least I could do for everything you did for me."

if maverick_redem_maverickromance == True:

    Mv "What do you say, was this close to those dragon riders you once mentioned?"

    c "I’d say it was even better. "

else: 

    Mv "I did some research and it seems one of your myths about dragons had something called dragon riders; some sort of partnership between a human and dragon fighting side by side."

    Mv "What do you say, was this close to those dragon riders?"

    c "I’d say it was even better. "

Mv "I’m glad to hear that."

Mv "We of course had some information about humans and despite his attitude Reza, also mentioned a few bits before he went rogue."

c "So Reza actually did his job for some time?"

Mv normal flip "I’m certain it was all an act and I didn’t really care at first but after we talked that night at the park you got me thinking."

Mv "I asked Sebastian to show me everything we had learned about you from Reza, and the few bits of information your people gave us before they sent you."

Mv "You gave me a chance when you called me despite my behavior, so I wanted to believe that there might be a chance that you were actually on our side."

if maverick_redem_maverickromance == True:

    Mv laugh flip "However, I’d never expected that we’d become this close or that I’d let you fly on my back."

else:

    Mv laugh flip "However, I’d never expected that we’d become close friends or that I’d let you fly on my back."

c "It’s funny how things can change if you start to trust each other. I wonder how things would have been if my people would have never sent Reza."

Mv rehappy flip "Well, we’d have 4 dead dragons less but who knows what the future holds for us."

c "Only time will tell."

Mv "Speaking of time, I think it’s time to get you home. Let’s go."



label redemdate4_d:

if maverick_redem_adineromance == True:

    m "While Maverick and I were flying closer to the town, I saw a familiar dragon flying in the distance."

    m "As soon as she noticed us, Adine flew in our direction. "

    play sound "fx/flapx.ogg"        

    $renpy.pause(1.0)

    show adine giggle c at right with easeinright

    Ad "Good afternoon [player_name] and Maverick."

    c "Good to see you Adine. "

    Mv "Good afternoon, Adine."

    Ad "Wow, never expected to meet you two up here, especially you [player_name]."

    c "Maverick and I went hiking and now we’re on our way back to town. What about you, Adine? "

    Ad "Oh, I’m just on my way to deliver some food. It’s the last one for today before I can help at the orphanage. "

    c "Are you sure it’s a good idea to fly with your injured wing?"

    Ad normal c "Don’t worry, as long as I wear the bandage I can fly without any problems."

    Ad giggle c "Anyway, I didn’t know you were interested in flying [player_name], or did my flying session inspire you to give it a try?"

    m "I noticed that she quickly changed the topic to avoid further comments, so I played along for now. However, it only reinforced my fear that she was in no condition for the competition." 

    c "Seeing you fly reminded me of home when we still had planes. I always loved watching the world from above when I was younger. "

    Ad giggle c "If I’d know that I could have offered you a ride."

    c "Are you sure I’m not too heavy for you? "

    Ad think c "I’m not sure but we can try after the competition. It might be good training."

    Ad giggle c "Only one way to know for sure. " 

    c "Sounds like a plan to me. "

    Ad "My offer for the festival still stands. Just give me a call if you’re free."

    Ad normal c "I’m sorry to leave already but I need to finish my deliveries now. It was nice meeting you two. Bye!"

    c "See you, Adine."

    show adine normal c flip with dissolve

    $renpy.pause(0.1)

    hide adine at right with easeoutright

    m "I watched as Adine flew away but even without being an expert in dragons or their flying style, it felt as if something was off."

    m "Maybe I was overreacting, I couldn’t help but to think that she refused to admit that she wasn’t in the right condition for the competition. "

    Mv laugh flip "You really should ask her for a date."

    c "What are you talking about? I’m not even sure if she likes me the same way."

    Mv normal flip "Oh [player_name], you really need to learn to understand body language. She clearly likes you. Not because you’re a human but for who you are as a person. "

    m "Mavericks words made me happy and I was glad he wasn’t able to see me blush."

    Mv "However, it might be better to talk to her about the competition first."

    c "Are you talking about her wing?"

    Mv "Yes, it was subtle but she still has problems even with the bandage. She’s in no condition for a flying competition."

    c "I’ll talk to her when I get the chance. I just hope she won’t be mad at me."

    Mv "Sometimes we have to risk such things to protect the people we love. I know how that feels but I’m sure she will understand your intentions."


elif maverick_redem_naomiromance == True:

    m "While Maverick and I were flying closer to the town, I saw a familiar dragon flying in the distance."

    m "As soon as she noticed us, Naomi flew in our direction. "

    play sound "fx/flapx.ogg"        

    $renpy.pause(1.0)

    show naomi normal b at right with easeinright

    Nm normal b "Hey Mav and hey [player_name]."

    c "Hey, Naomi."

    Mv "Good afternoon, Naomi. Are you on lunch break?"

    Nm "Yes, I had some free time while the guys in the lab are examining the diary and letter you gave us."

    Nm "There wasn't any evidence on the letter that told us who wrote it. The diary on the other hand was a very valuable addition to Reza’s profile, even without any hidden messages."

    Nm "Despite the missing pages, it showed us that he is suffering from the past trauma of losing his world and his partner."

    Nm "It won’t help us to find him. but if he shows up… you have to be on your guard."

    c "He still has his gun so it’s likely that he plans to resist."

    Nm "That might be true but what I meant is, that he’ll most likely try to go down fighting. His profile indicates that he could even try to take you down with him if he feels like he's failing his mission."

    Mv "We’ll be careful. Thank you for the warning."

    Nm smile b "You know, I’d have never expected meeting you up here, [player_name]."

    c "Maverick and I are returning from a hiking trip. I know you're worried but he made sure I was safe all the time."

    Nm "You better hope so, Mav. You better not drop [player_name] or else I’ll get very mad at you."

    Mv laugh "We can’t let that happen, can we? Not to mention all the paperwork I’d had to do."

    c "You know that I can hear you both?"

    Nm "We know but the look on your face was worth it."

    Mv rehappy "That’s true, even if I can’t see your face right now."

    Nm "I’ve been thinking about making up for our last meeting with you. It wasn’t as relaxing as I hoped it would be."

    c "I still enjoyed it. It was the first time for me to go diving and despite the little distraction, I wouldn’t mind doing it again someday."

    Nm "I’ll keep that in mind. However, the next time we should stay in the town. "

    c "Sounds like you already have a plan."

    Nm shy b "I might have some ideas already. {w} It will be a surprise but I’m sure you’ll like it."

    Nm "And don’t worry, there won’t be any distractions this time."

    c "As long as I can spend some time with you it’s already worth it."

    $ renpy.pause (0.5)

    show naomi smile b with dissolve

    c "I’ll give you a call when  I have time."

    Nm "I’m looking forward to it."

    Nm normal b "I sadly need to get back to the department. See you guys later."

    Mv "Goodbye Naomi."

    c "Bye Naomi."

    show naomi normal b

    $ renpy.pause (0.5)

    hide naomi normal b flip at right with easeoutright

    play sound "fx/flapx.ogg" 

    $ renpy.pause (0.5)





elif maverick_redem_remyromance == True:

    m "While Maverick and I were flying closer to the town, I saw a familiar dragon flying in the distance."

    m "As soon as he noticed us, Remy flew in our direction. "

    play sound "fx/flapx.ogg"        

    $renpy.pause(1.0)

    show remy smile at right with easeinright

    Ry smile "Good afternoon [player_name] and Officer Maverick."

    Mv "Good afternoon and please, just call me Maverick."

    c "Good afternoon Remy. How are you today? "

    Ry "I’m actually a lot better. Our last meeting helped me come to terms with many things."

    Ry shy "I even went and talked to Adine. You were right; she tried to reconnect when she was visiting me at work the other day."

    Ry "It seems I was so focused on my own problems that I never realized that she was suffering as much as I."

    Ry "Together we can keep Amelia’s memory alive."

    c "I’m glad that you two are friends again."

    Ry smile "Me too. I even followed your advice and offered her to help at the orphanage. She gladly accepted."

    Ry "One of the hatchlings, a girl named Vara, seems to like me a lot. The poor girl had just lost her family and is all alone now."

    c "I know it’s sudden, but you mentioned that you always wanted children and maybe you could adopt her. "

    Ry look "I… maybe, I’m not sure. She needs a family but I’m not sure if I’d be a good father."

    Ry "If someone would help me… maybe it could be possible."

    Ry "I’m sure Adine would help me but she also needs to take care the other hatchlings."

    c "You can also count on my help, Remy."

    Ry normal "Thank you, but wouldn’t your ambassador mission make you leave?"

    c "That's tue but with everything going on, I’d try to stay here most of the time. Even with the generators we need help to recover."

    c "Maybe your people could help us with food, medicine or other resources in exchange for our people showing you how to build and use our technology."

    c "It would take a lot of negotiation with the council and my leaders, but together our species would be stronger."

    Ry smile "I like your way of thinking. Hopefully we can make it come true."

    Mv "If someone can do it, then it’s [player_name]."

    Ry "That’s true."

    c "I’m glad at least you two are believing in me. I hope the same is true for my people."

    Mv "I'm sure they will once they hear what Reza did."

    c "I hope so. By the way, I think this is the first time I’m seeing you fly, Remy."

    Ry normal "I’m not really skilled enough to carry many things while flying, so I usually walk. It’s still a nice way to distract myself from thinking too much about… you know."

    c "So I take it that you’re on a break right now?"

    Ry "Yes and I needed some time away from Emera."

    c "Was she giving you a hard time again?"

    Ry  "No more than usual but since our last meeting, I’m not letting her ruin my mood anymore."

    c "I’m glad to hear that. You deserve better than that, Remy."

    Ry "Thank you, [player_name]."

    Ry  "I sadly need to get back to work now. Goodbye you two."

    Mv "Goodbye Remy."

    c "Bye Remy."

    show remy smile flip

    $ renpy.pause (0.5)

    hide remy smile flip at right with easeoutright


    play sound "fx/flapx.ogg" 

    $ renpy.pause (0.5)



else:

    m "While Maverick and I were flying closer to the town I saw a few familiar dragons flying in the distance. However they were all too busy with their own situations so that Maverick and I were on our own."


$ renpy.pause (0.5)

scene black with dissolvemed

stop music fadeout 2.0

$ renpy.pause (0.5)

scene np5e with dissolvemed

m "A few minutes later, Maverick had landed close to my apartment and one of the best days of my life was coming to an end. I quickly helped Maverick remove the saddle-backpack, and a few minutes later it was once again usable as a backpack."

c "Thank you for this amazing experience, Maverick."

show maverick normal flip at left with easeinleft

Mv "Actually, it should be me thanking you. Before all of this my life has only been about work and Miles’ death. "

Mv "I never was able to let go and changed for the worse, but thanks to you I might finally be able to look forward again. No more \"What ifs\". " 

if maverick_redem_maverickromance == True:

    Mv "As you might have heard, the festival has fireworks every night. The biggest one will be on the last night. So I guess, as an ambassador, isn't it a part of your job to take part in our social events? "

    Mv "It will be at night and with Reza still on the loose."

    c "Are you asking me to go to the fireworks with you? "

    Mv "I guess I am. I know that we didn’t start on the best terms but I really care for you. Reza is still out there and probably pissed that you’re helping us instead of him. "  

    Mv sideeye flip "I’d feel better if I can keep an eye on you to make sure that this jerk doesn’t try to hurt my favorite human."

    Mv "It’s also kind of romantic and I’d love to spend more time with you. " 



elif maverick_redem_noromance == False:

    Mv "As you might have heard, the festival has fireworks every night. The biggest one will be on the last night. So I guess, as an ambassador, isn't it a part of your job to take part in our social events? "

    Mv "It will be at night and with Reza still on the loose."

    c "Are you asking me to go to the fireworks with you? "

    Mv "I know that you’d rather go to the fireworks with [maverick_redem_romance_partner] but Reza is probably pissed off that you’re helping us instead of him."  

    Mv normal flip "I’d feel better if I can keep an eye on you to make sure that this jerk doesn’t try to attack you both. So one way or the other I’d like to make sure that you’re safe."



else:

    Mv "As you might have heard, the festival has fireworks every night. The biggest one will be on the last night. So I guess, as an ambassador, isn't it a part of your job to take part in our social events? "

    Mv "It will be at night and with Reza still on the loose."

    c "Are you asking me to go to the fireworks with you? "

    Mv "I guess I am. I know that we didn’t start on the best terms but we’re friends. Reza is still out there and probably pissed that you’re helping us instead of him. "  

    Mv sideeye flip "I’d feel better if I can keep an eye on you to make sure that this jerk doesn’t try to hurt my favorite human."


c "I can’t promise that I’ll have time but I’d love to go to the fireworks with you. "

Mv rehappy flip "Great, just give me a call when you made a decision."

c "I will, goodnight Maverick. "

Mv "Goodnight [player_name]. "

show maverick rehappy at left

$ renpy.pause (0.5)

hide maverick rehappy at left with easeoutleft

stop music fadeout 2.0

$ maverickscenesfinished += 1


if adine3unplayed == False and adine4unplayed == True:

    jump redemadine4

else:

    pass

if anna3unplayed == False and anna4unplayed == True:

    $ annastatus = "abandoned"

else:

    pass

if bryce3unplayed == False and bryce4unplayed == True:

    $ brycestatus = "abandoned"

else:

    pass


if remy3unplayed == False and remy4unplayed == True:

    $ remystatus = "abandoned"

else:

    pass


if maverick_redem_maverickromance == True :
    $ maverickstatus = "good"
else :
    $maverickstatus = "normal"

# Repeat of the "if romance then impressed, if not then good" if branch from date 3 - Nyxondra

jump ml_date_end
