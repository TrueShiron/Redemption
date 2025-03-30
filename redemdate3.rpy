label redemdate3: 

scene black with dissolvemed

$ renpy.pause (0.5)

scene redem_maverick_apartment_a with dissolvemed

play music "mx/fireplace.ogg" fadein 2.0

show maverick normal flip at left with easeinleft

Mv "Good evening [player_name]. I’m glad you made it."

c "Thank you for inviting me."

m "Maverick and I went inside his apartment and he offered me a beer. We both took a sip from our beer and sat down."

c "So, what’s our next step in finding Reza?"

Mv "For today it’s waiting for him to make his next move, as much as I hate to admit it."

c "Isn’t there anything we can do? I mean, he has murdered three dragons already and I can’t just wait until he finds his next victim."

Mv "You’re new to working with the police and still need to learn that sometimes, the best way to solve a case is by waiting. We did all we could and more but without new clues, we can’t do anything right now."

c "I can't just sit around and do nothing. It’s my responsibility to find him. Without the two of us, none of your people would have died."

Mv "You mean without Reza. As far as I know, you’ve done more than anyone else to find him and bring justice to his victims. So don’t tell yourself that it’s your fault ‘cause it isn’t."

m "Having Maverick of all dragons to care for me left me speechless. It was true that we met a few times but I didn't think that he would consider me a friend until we finally caught Reza. Without even realizing I said what was on my mind."
 
c "If I wouldn’t know better I’d say that you’re going soft."

Mv angry flip "I am NOT going soft."

Mv normal flip "You’re just being a better partner when you’re rested and don’t overwork yourself."

Mv resideeye flip "Especially after everything we learned so far. You need to learn that we can't change things that were beyond our control."

Mv normal flip "Now shut up and drink your beer."

m "With a silent smile I took a sip from the beer while Maverick tried his best to keep a neutral look."

m "Deciding to not tease Maverick any further even after he called me partner, I opted to change the topic."

if c3stay == True:

    c "By the way, that was a good idea with the portal and the letter."

    Mv "What letter?"

    c "When I got home today I found a letter warning me not to go to the portal. It was written on a computer so I thought it was from you."

    Mv "That wasn’t me."

    c "It couldn’t have been Reza either. "

    Mv "Why do you think that?"

    c "One way or the other, the gunshots would have caught my attention and I would have gone to the portal. So it was either Reza’s plan to get my attention to escape together or…"

    Mv "…or he was trying to lure you out to murder you."

    c "Yes. Either way the letter prevented me from investigating the gunshots by calling the police."

else:

    c "By the way, someone had slipped something under my door while I was gone last night."

    c "Whoever it tried to warn me about going to the portal, but I had a bad feeling… especially when I heard the gunshots."

    Mv "Yeah, I also heard that noise but I was too late to catch Reza."

    c "Despite the warning, I went to the portal but someone stopped me."

    Mv "Were you able to see the person?"

    c "No, it was too dark and I didn't see their face."

    m "I felt bad for hiding the full story from Maverick but until I learned more about the hooded figure it was better to keep it a secret."

    m "Although it was possible that another human came through the portal, it felt as if the whole story was bigger than I thought."

    c "However, whoever it was, it was not Reza."

    Mv "Why do you think that?"

    c "One way or the other, the gunshots would have caught my attention and I would have gone to the portal. So it was either Reza’s plan to get my attention to escape together or…"

    Mv "…or he was trying to lure you out to murder you. So it might be possible that the person saved your life."

    Mv "However, going all alone to the portal, especially with that warning, was a bad idea. Who knows what could have happened without that person stopping you."

    c "You're right, I'm sorry. It just felt like a chance to stop Reza from hurting more people."

    Mv "I know that you want this case to end as much as do I but we can't be reckless."

Mv "Do you still have the letter?"

c "Yes, I brought it with me. There is no way to analyze the handwriting though."

m "Maverick looked at the letter and then stored it in a pocket."

Mv "That might be true but maybe Naomi can find any other leads that could help us…"

Mv resideeye flip "However…"

m "It was difficult to read Maverick emotions as if he was hiding something. He tried to avoid looking at me and took a sip from his beer."

Mv "…there is something else I need to tell you. I also heard the gunshots and went to the portal as fast as possible."

Mv "Sadly Reza was already gone when I arrived and I wasn’t able to tell where he escaped to. However the whole incident made me realize something."

Mv "As long as the portal is working he can always escape and cut the connection on your side. So I did the only reasonable thing and took it offline."

c "I didn’t know you had an engineering education before you went to the police."

Mv "Actually, I don’t. I just {i}borrowed{/i} a part from the console."

show maverick normal with dissolve

$ renpy.pause(0.5)

hide maverick with easeoutleft

$ renpy.pause(2.5)

show maverick normal flip at left with easeinleft

m "Maverick stood up and when he returned he was holding something he had hidden in a different room. I was shocked when I saw what it was."

c "You just ripped out a part of the console?"

m "He had expected that reaction but tried to stay calm. It wasn’t easy but I knew that Maverick wouldn’t do something like that without a very good reason."

Mv scared flip "I’m sorry [player_name]. It wasn’t an easy decision especially since I knew that I’d betray your trust."

Mv "However, you know as well as I that I had to disable the portal for now. If Reza is able to escape we’ll never be able to catch him."

Mv "He might make sure that your people shut down their end of the portal or, what's more likely, they could send more people like him."

Mv "We don’t know who else he is working with or their resources. You saw what happened with just Reza and his gun. A whole group of armed humans would be too much for us to handle."

m "Maverick must have seen that I wasn’t happy about the decision and quickly tried to calm me down."

m "Maybe he felt bad that he went behind my back after all the hard work we needed to make peace with each other."

Mv normal flip "Don’t worry; I’m sure our engineers can fix it once the Reza case is over."

m "I knew Maverick was right but I still was mad at him. What if he damaged the portal beyond repair?"

m "I wanted to be angry and shout at him but for some reason I wasn’t afraid about the portal or my mission."

m "I couldn’t explain this feeling but for some reason I knew that he had to disable the portal and that someone would fix the damage before all of this was over."

m "Maverick was unusually quiet and avoided looking at me, as if he was waiting for my response. I let out a sigh and looked at him."

c "I know, Maverick. For now it’s the only way to keep Reza from leaving."

c "Although it would have been nice if you’d have warned me before you did that."

Mv "I’m sorry but it just felt like the right thing to do. As if … I don’t know, it doesn’t make any sense."

menu:

    "[[Say nothing.]":

        m "It was easy to notice that he felt uncomfortable about something but I didn’t want to make it worse by asking him about what he wanted to say." 

        m "So instead I let him he change the topic."

        $ maverick_redem_dream = "False"

        jump redemdate3B

    "[[Ask about the feeling he had.]":

        m "It was easy to notice that he felt uncomfortable about something but it was as if he felt the same as me."

        c "It felt as if some kind of force was telling you what to do?"

        m "Maverick looked at me with a surprised face."

        Mv scared flip "Yes, how did you know?"

        c "Since I got here I had strange feelings. Some events felt as if I had experienced them already." 

        c "It’s like a déjà vu but all the time." 

        c "I know that I should be mad at you for the portal and that I should be afraid of never being able to return but somehow…I know that it was the only possible way to save my people."

        c "It’s impossible but I’m sure that, by the time we’re ready to face Reza, the portal will be working again."

        Mv normal flip "It’s the same for me. From the moment I met Reza, I knew that he was bad news. It wasn’t because of his rude behavior or his gun but something else." 

        Mv "Almost as if I knew that one of us would end up killing the other."

        Mv "Those feelings only grew stronger when you appeared. My instinct guided me as if I knew that there was a disaster about to happen but it felt as if someone else was pulling the strings."

        c "You know, since I went to the portal and arrived in your world I also had those weird realistic dreams."

        c "Usually I wouldn’t pay them any attention but I saw people I never met and events that never happened… until they did." 

        Mv "What is the meaning of this?"

        c "I don’t know but my people had a theory that the portal might also connect different universes. Something about wormholes or alternative timelines."

        c "I don’t have any knowledge in quantum physics so I didn’t really understand it."

        Mv rerelief flip "This is making my head hurt. I can deal with thieves and murderers, but that stuff is more for scientists like Anna."

        Mv normal flip "Seriously, first we find a portal to a different world, then two humans from our myths appear and now we have this weird stuff."

        m "Maverick took another sip from his beer and looked at me."

        Mv "I mean what’s next; a comet killing all of us or a time traveler from the future? It feels like we’re in a sci-fi movie."

        c "Well, I’m drinking beer with a dragon from human myths while talking about prophetic dreams." 

        c "By now I’d say everything is possible, even sentient spaceships wiping out all advanced species in the galaxy."

        Mv laugh flip "Oh, I know those movies. They were some of the first interactive chose-your-own-path movies and were quite popular. However the ending sucked."

        Mv normal flip "I mean seriously, it was always the red, blue and green ending no matter what kind of path you followed."
  
        c "You have them too? I really should give your version a try."

        m "We both were thinking about the dreams and if they had any meaning. I wasn't sure what to think but since they helped so far, it might be bad to ignore them."

        c "You know, I’m not sure what those dreams or feelings are about but so far it seems as if they are helping."

        c "You were right about Reza and the portal last night and without even knowing, I was able to save Anna’s life by making her go home earlier."

        Mv "And I’ll forever be in your debt for saving her. Even after all that time since we’ve broken up, I still care for her. I don’t know what I’d have done if she would have died… "

        m "He didn’t finish his sentence and looked concerned for a moment. Maybe he still had feelings for Anna after all."

        Mv "However, those feelings weren’t right about you."

        c "You’re right, but it might still be a good idea to not ignore them. Who knows, maybe they can save one of us someday."

        $ maverick_redem_dream = "True"

        jump redemdate3B


label redemdate3B:

m "Maverick finished his second beer before he talked again. By now his voice sounded friendlier that usual. It seemed that he was one of those who hid behind a grumpy attitude but was friendly and caring behind all of that."

Mv resideeye flip "You know, I never asked you if you have anyone to return to on your side of the portal."

Mv normal flip "You told me about the flare and the situation of your people but nothing about your friends or family."

c "To be honest, there really isn’t anyone left at home. My parents passed away before the flare and all true friends I had died during the flare or the following years."

c "I have a few people I’d call friends but those are only shallow friendships. There’s no one left who’d mourn over my death if I didn't return."

Mv "I’m… sorry to hear that. Maybe it helps a little to know that you have true friends here."

c "Thank you Maverick, that means a lot to me." 

Mv "I never considered how hard your life must have been. Even after you told me the truth, I always only saw you as the mythical human everyone adores. At least until we spent more time together."

Mv laugh flip "However, I’m sure you’ll be celebrated as a hero once you get home."

$ renpy.pause(0.3)

show maverick normal flip with dissolve 

c "I don’t think so. The main focus of this mission has always been Reza, the smart and cunning hero as they called him."

c "My degrees in biology and sociology are more or less useless in our current society and having no living relatives might have been another reason why my people chose me to be Reza’s partner."

c "By now I’m certain that you were right about me being a pawn my leaders could use if Reza would fail or to leave behind if he’d succeed."

Mv normal flip "I never meant it like that."

m "I gave him a knowing look and he avoided my gaze while taking a sip from his beer."

Mv resideeye flip "Ok, I meant it when I still suspected you and I apologize for that." 

Mv normal flip "Now that I know you better I know that your people are stupid if they don’t see how important you are."

Mv "If they would have sent a second Reza we would have cancelled this trade as soon as possible."

c "That might have been the nicest thing you’ve ever said to me."

Mv reblush flip "Yeah, whatever."

m "It looked as if he wanted to say more but was struggling with himself."

Mv resideeye flip "So… if you’d have the chance…"

Mv "…would you stay here?"

m "That was a question I didn’t expect, especially not from Maverick."

m "I never really thought about my life once my mission was over and we’d get the generators from the dragons. Would I still be needed as an ambassador or would my leaders send someone else because I messed with Reza’s plan?"

m "I had the strange feeling that I had this conversation with a different dragon already but I couldn’t remember when and where but it felt as if water or a pool was involved…"

m "It was as if there was thick fog in my mind that prevented me from remembering any details."

c "I don’t think that I’ll actually have a choice. Too many people are depending on my help and even if my leaders are agreeing with Reza’s actions, I can’t abandon all the innocent people waiting for me."

Mv normal flip "So you are willing to go back even if your leaders might decide to kill you for standing in their way?"

c "I know that it sounds reckless or even suicidal but if the flare taught me one thing, than that, for the greater good, some must live and some must die."

c "As long as I can save my species from extinction, I’m willing to sacrifice my own happiness and, in the worst case, also my life."

if inv == "high":

    Mv "You know, you really would make a fine officer. " 

else:

    Mv "You might need some training but after that you might make a fine officer." 


m "For a few moments we both just sat there in silence before I decided to confess what I really wanted if I had the chance."

c "To be honest, if I’d actually be free from all responsibilities toward my people, free to make my own decisions and follow my own dreams… then yes, I’d love to say here."

c "It’s kind of strange that this place is making me feel more welcome than my actual home…"

m "We were looking at each other and for a short time, I could see a softness in his eyes I didn’t know he had."

c "…and the people here are also friendlier. "

Mv "Is there someone special you’re talking about?"

menu:

    "You.":

        c "I’d say that we two were a good team so far."

        Mv "You might lack the training of a officer but you have good intuition." 

        Mv "With the right training and knowledge you’d be the perfect partner. Well, except in combat against criminal dragons."

        c "It’s a tempting offer. I mean, once I'd finish my mission and my people don't need an ambassador anymore it could be possible. Not that I’d be able to take down a dragon."

        Mv "You could always go for the forensics team and work with Naomi. However, with the right partner to protect you, you could also do the same work as Bryce, Seb or I." 

        Mv "Not that there are many dangerous cases in our town." 

        Mv "The most dangerous one we had before Reza was a shoplifter; a mother of two who had no other choice and didn’t resist when we arrived." 

        c "What happened to her?"

        Mv "She quickly confessed and told us her story. In the end, the shop owner offered to cover the fines and other legal expenses. There will still be a trial for breaking the law, but everyone understands her situation so there will be lenient sentence like community service." 

        c "So even in your peaceful society there are things like poverty."

        Mv "Yes, despite some members of the council trying to fix the problems, others are causing new ones. This single mother will get help to change her life and that of her children for the better but others aren’t that lucky."

        Mv "I remember a case I worked on some years ago with a teacher, I think her name was Linnea, and her family. They moved from the city to our town because of their daughter and at first everything seemed to be fine. Then one of the mothers caused problems which ended in them losing their house and the teacher her job." 

        c "Do you know what happened to them?"

        Mv "The last report we got was that the problem causing mother was arrested and sentenced to community service, after she threw a brick through the teacher's window."

        if persistent.varasaved == True:

            m "I remembered Vara and her dead mother and wondered if that was the same dragon Maverick was talking about." 

        else:

            pass

        c "Does something like that happen often?"

        Mv "In bigger cities it does but luckily not here. Since I've been working for the police we only had three other cases involving murder. Most over the other ones are harmless and without any violence."

        Mv "So even a human would be able to work for the police."

        c "Do you really think I’d fit into the team?"

        Mv "We were a good team so far. Seb and Bryce also seem to like, so I’d say your chances are good. Who knows, maybe you can stay here once the trade is over."

        c "I’d like that."

        Mv "With you we’d be four people for the investigation team and you’d work with each of us in a team depending on the case… or duty."

        m "Maverick went silent as if he wasn’t sure about what he was going to say. When he continued, his voice was unusually sheepish, something I never expected him to be."

        Mv resideeye flip "You’re smaller than a dragon, so I could… you know, even carry you on my back for flying duty. It can be pretty boring being all alone in the sky."

        c "Then I’d actually be a dragon rider."

        Mv laugh flip "I didn’t know you where that open minded."

        c "What do you m-… oh my, I didn’t mean it like that."

        show maverick normal flip with dissolve

        m "I felt my face burning with embarrassment."

        c "I meant that, in some myths, dragons were more like companions; fighting alongside humans and letting them ride on their back during battle." 

        Mv laugh flip "I guess that would work, too."

        m "Was Maverick actually flirting with me? I trusted Maverick by now and even saw him as a friend but until now, I never considered to be more with him than just friends."

        m "However, the more I thought about it the more I felt that I actually cared for him more than just a friend. I had no idea how or when that happened but I knew that it felt right."

        c "Not that I’d be against the idea."

        Mv reblush flip "Wait, are you actually talking about… I mean… That’s… "

        m "I couldn’t help but laugh. Never in my life would I have expected Maverick, of all people, acting all shy. Had he actually been the soft and romantic one during his relationship with Anna?"

        m "It didn’t take Maverick long to turn back to his usual self."

        Mv normal flip "So you would actually consider a relationship with a dragon?"

        c "It’s true that we’re the only sentient species on our side of the portal, and it might be frowned upon to consider a different species for dating. However to me, I don’t really see a difference between the two of us except of our species."

        c "We’re both intelligent, sentient creatures, we can communicate with each other and we’re both adults. So I wouldn’t care if the one I love is a human or a dragon."

        Mv "Do you think your people will see it the same way?"

        c "As soon as we catch Reza and finish the trade, our two societies might start working even closer together. Someday, dragons could move to our town and humans could move here, so it would only be a matter of time until human-dragon relationships would happen."

        Mv "I’m not sure about more humans coming here but I’ll give them the same chance I gave you. Not everyone has to be like Reza or the people behind him."

        c "Thank you for giving my people a second chance."

        Mv "You’ve earned it."

        $ maverick_redem_maverickromance = True

        $ maverickstatus = "good"

        $ maverick_redem_romance_partner = "Maverick"

        jump redemdate3C

    "Adine." if persistent.adinegoodending == True and adine3unplayed == False and adinestatus != "bad":

        c "I’ve been spending quite some time with Adine, the waitress from the café we’ve visited last time."

        Mv "I remember her. She seems like a nice girl."

        c "She’s one of the sweetest persons I’ve ever met and always has a positive view on the world."

        Mv "Does she like you, too?"

        c "I'm not sure."

        c "We’ve met a few times and it was always fun. I think at first she was interested in me because I’m a human. She really likes all the myths and anything about my species but now I think that she actually likes me for being me and not just because I’m a human."

        Mv "Being a celebrity isn’t easy."

        c "That’s true but luckily most dragons I met so far don’t seem to care that much. Sure, Adine loves humans, especially that sitcom, but she doesn’t go all crazy about it." 

        Mv "Yeah, crazy fans are always a problem. Not in our town luckily but I heard about some cases in the cities."

        Mv "That’s another reason why I prefer this town over bigger places. I like a calm life with less trouble."

        c "I can drink to that."

        m "We both took a sip from our beer and I thought about the last time I met Adine. Being a flyer himself, maybe Maverick could help me."

        c "I’m actually a little worried about Adine."

        Mv "Why's that?"

        c "We went to the beach last time and she showed me a few of her flying tricks. During her last trick she crashed and ended up hurting herself."

        c "She said that her wing would be completely healed before the festival and the flying competition but I fear that she will fly even if her wing isn’t completely healed."

        Mv "Did you talk to her about your worries?"

        c "No, I didn’t have the chance yet and I don’t really know how to bring up the topic."

        Mv "Being a stunt flyer is her dream, I guess?"

        c "Yes. I know that I’m not a dragon and don’t know how fast your injuries heal but if she crashes again… I doubt that there will be a beach to soften her fall this time."

        Mv "I’ve met a few stunt flyers before and know how much they care about flying. If you really care about her then you have to talk to her."

        c "What if she ends up hating me for it?"

        Mv "Sometimes we have to accept that those we care about hate us for caring about them."

        Mv "However, Adine seems like a smart girl and I’m sure she’ll realize that you only did it because you care about her safety."

        c "I hope you’re right."

        c "In her free time she spends time with the children at the orphanage, so maybe I can convince her to think about them and how they’d feel if something happens to her."

        c "She cares a lot about them so maybe it'll change her mind. I mean, there is always another year." 

        c "…Or maybe I’m worried for no reason and her wing is actually better than it looked like."

        Mv "I know who she is so I could try to look at her flying when I see her. Just to make sure she stays safe."

        c "That would be a great help. Thank you, Maverick."

        Mv "That’s what friends are for."

        $ maverick_redem_adineromance = True

        $ maverick_redem_romance_partner = "Adine"

        jump redemdate3C


    "Anna." if persistent.annagoodending == True and anna3unplayed == False and annastatus != "bad":

        c "Well, I’ve been visiting the production facility quite a few times."

        Mv "So you’ve been meeting Anna?"

        c "Yes. I hope you don’t mind because of what was between the two of you."

        Mv "Don’t worry; I don’t have any romantic feelings for her anymore. After we broke up, we both changed and became different dragons."

        Mv "I don't know if we'd even have a chance if we'd try again. Sometimes it's better to enjoy the memories and move on."

        c "Can I ask you something? I mean, if you don’t mind. "

        Mv "You want to know why we have broken up?"

        c "If that’s okay with you."

        m "Maverick closed his eyes as if it was difficult for him to talk about it. However, before I was able to tell him that he didn’t need to tell me, he opened his eyes again and looked at me."

        Mv "What Anna and I had going was good while it lasted but neither of us was ready for the commitment of a deeper relationship; I had my work at the police and Anna was working at her lab while also helping the department."

        Mv "I wanted to prove my worth and for Anna, her studies always came first. We still made it work out somehow but we never went the next step in our relationship."

        Mv "Then a certain… incident happened, keeping me busy, while Anna suddenly quit her job at the police. I called her the same day but she suddendly wanted to end our relationship." 

        Mv "She told me the reason and in her eyes, it made sense but she wanted to call me for another try if she would find the cure she was searching for."

        Mv "However, when that special case was solved, Anna helped me through the worst part. It was just as friends and after a year or two of waiting for her call, we both realized that there might be no second chance for us."

        Mv "We both are different dragons now than we were years ago."

        m "Of course I knew that Miles’ death was the incident Maverick was talking about but I never realized how much pain it was causing him even years after it happened. He wasn’t even able to say his name, as if he was blaming himself for Miles’ death."

        Mv "We still consider each other friends and she helps the department but still…"

        m "Out of reflex I grabbed his hand and gave him a little squeeze. To my surprise, he didn’t get mad but seemed to appreciate the little gesture. Then we both took our hands back."

        Mv "Listen [player_name], as long as you don’t want to play any games with her and actually care about Anna, I’ll support you."

        c "I promise you, I don’t intend to hurt Anna. I don’t know if she cares for me even if just a little or if she’s just trying to use me for her research, but I enjoy spending time with her."

        c "Despite her being a little difficult from time to time."

        Mv laugh flip "Yeah, that sounds like Anna. If she is actually spending time with you outside of her lab, then you must have impressed her."

        Mv normal flip "I won’t give you any private information but a general advice. Show her that you care, no matter how… moody she gets and trust me, she will be. She’s the only dragon even I would never piss off."

        c "That sounds as if you’re afraid of her."

        Mv laugh flip "I’d rather deal with 10 armed Rezas than one angry Anna."

        c "Yeah, I can totally imagine Anna throwing a fridge at someone she’s mad at."

        show maverick scared flip with dissolve 

        m "Suddenly Maverick was unusually silent."

        c "Wait, she didn’t actually…?"

        Mv "It was only once and, in her defense, she didn’t aim directly at me."

        c "Okay, I’ll remember to never piss Anna off."

        Mv laugh flip "That might be the best for all of us. I'm running out of places to hide the bodies."

        Mv normal flip "By now you should know her good enough to realize how difficult she can be. She hates commitments, acts as if she hates everyone and everything and doesn’t believe that others are caring for her without any ulterior motives."

        Mv "However, if you’re be lucky enough to gain her trust, then you’ll see that she’s actually a nice and caring woman. Just don’t make the same mistake as me and let work get in your way."

        c "If there a chance to be with her, then I’ll try my best to not mess it up."

        Mv "That’s the spirit. She really needs some happiness in her life."

        $ maverick_redem_annaromance = True

        $ maverick_redem_romance_partner = "Anna"

        jump redemdate3C


    "Bryce." if persistent.brycegoodending == True and bryce3unplayed == False and brycestatus != "bad" and nodrinks == False:

        c "It’s always fun to hang out with Bryce."

        Mv laugh flip "I remember you mentioning that he asked you for a drinking contest."

        c "That’s true and it seems he really likes to drink… although I think that it might be for more than just the fun of it."

        Mv normal flip "Working for the police isn’t easy. You’ll see and learn things you don’t want to know."

        c "I’ve only been helping your team for a short time but I think I understand what you mean."

        Mv "Protecting others means that you have to see the worst things people can do to each other."

        Mv "I’m sure you’ve also seen more than enough of those things in your world."

        m "I wanted to respond to him but I guess the look on my face was answer enough."

        Mv "Sorry, I didn’t want to bring back bad memories."

        c "It’s ok, I’ve learned to live with that but… well, some days are harder than others."

        Mv "That’s true. Every one of us has a different way to deal with that kind of stuff."

        Mv "For me it’s focusing almost all my time on work. After Anna, work has become my life and without our annual BBQ or our weekly {i}team building activity{/i}, as Bryce calls it, I’d most likely be like Anna; working nonstop."

        Mv "Most of us only see a few cases and victims but as the chief, Bryce has to see it all."

        Mv "I won’t tell you how the others are dealing with the stress but dating a cop won’t be easy. Sooner or later it will affect your relationship and, if you aren’t prepared for it, your relationship won’t survive."

        if zhongunplayed == False:

            c "Zhong mentioned something like this; that Bryce seems to have someone new every couple of months."

            c "I guess many of those relationships are because people only seeing him as the strong, handsome chief with an interesting life, but as soon as they realize how his work affects their lives, they leave."

        else:

            c "Back in my world some people were attracted to police officers for their dangerous and interesting job but never really understood the truth about the dark side of it."

            c "Only those who really care will stay while the fun seeking people will leave, searching for the next adventure."

        Mv "It seems I’ve misjudged you. You actually know the effects the job in the force can have on not only the cop but also the partner."

        c "I do, although it is mostly because of stories and statistics. My world never was free of crime, not even during our most peaceful times, and there were statistics about the effect the job had on the officers, or similar jobs like firefighters."

        Mv "It’s the same here but mostly in bigger places. Our town is peaceful and rarely has any crimes involving violence. Since I've been serving on the force we only had three murder cases, four including Reza."

        Mv "Even then we sometimes get more… disturbing cases, or need to help other teams. Since Bryce is the chief, he has to help them from time to time or has to go to continuous police education."

        Mv "However, with the right partner by your side even those things can be fixed and I really wish Bryce a happy and lasting relationship."

        $ maverick_redem_bryceromance = True

        $ maverick_redem_romance_partner = "Bryce"

        jump redemdate3C

    "Naomi." if persistent.naomigoodending == True and naomi3unplayed == False and naomistatus != "bad":

        c "On my first day here I've met Naomi after we got the generator from Anna. It was a unique way meet someone, and we ended up going for lunch."

        Mv laugh flip "So our analyst caught your eye?"

        Mv normal flip "A few days ago I might have suspected you for trying to sabotage our case by getting friendly with Naomi, but now I know that you wouldn't do something like that."

        c "Thank you for your trust Maverick."

        Mv "You've earned it. Though I'm curious; how did you two started to talk?"

        Mv "Usually, Naomi is very shy around people she doesn't know. {w} Not to mention that you’re an ambassador from a different world."

        c "After I spoke with Anna I got distracted and wasn't looking were I was going, while Naomi was in a hurry and didn't expect anyone in the hallway. "

        c "So she ended up running into me."

        Mv laugh flip "That really is a unique way of meeting someone. I'm sure she freaked out when she realized what just happened."

        $ renpy.pause (0.3)

        show maverick normal flip with dissolve

        $ renpy.pause (0.3)

        c "She thought that she was in trouble but it was just a mistake from both sides and no reason to make a big deal out of it."

        c "Naomi was in a hurry but gave me her number. After the investigation, we've met at the cafe and had a good time."

        Mv "It's rare that she's comfortable around new people, so I guess you must have made a lasting impression."

        c "So did she. She invited me over some other day and we watched a movie. Naomi told me that she was unhappy with Bryce forcing her to take a day off but in the end she didn't mind."

        Mv "Did she ask you to go diving with her?"

        c "How did you know that?"

        Mv "Naomi has problems with her shyness but there are a few occasions where it's different."

        Mv "One is when we're having our BBQ since we're only a small group of friends. Of course it took some time until she warmed up to talking to us."

        Mv "The other one is talking about her favorite topics, like diving."

        Mv "More than once she talked about the adventures she had."

        c "We actually went diving. I was surprised to learn that you even have equipment for that."

        Mv "It's more popular than you might think. I hope you had a safe adventure."

        m "I winced at the term \"safe\" but tried my best to hide my emotions. Sadly Maverick was too good at his job."

        c "Yes, it was a nice and relaxing day."

        Mv laugh flip "Do you want to try again? Maybe then I'm convinced."

        c "No, that was the best I got. You're too good at your job."

        Mv normal flip "Just between the two of us; what happened? I won't tell Bryce."

        c "When we were diving, we discovered an ancient human ruin with a damaged generator. Long story short, we almost caused an explosion with no way to escape."

        c "Luckily we were a good team and secured the generator without any of us dying."

        Mv "Ok, that’s definitely story you shouldn't tell Bryce."

        Mv "By now you should know me good enough to know that I really care for my friends."

        Mv "You should be careful around Naomi because she still has some problems with her confidence. A little mistake could lead to bad consequences. Not that I’d believe that you’d do anything like that on purpose. "

        c "I’d never do anything to hurt Naomi."

        Mv "You know, her lack of confidence also has something to do with someone she once dated."

        Mv "He started to act all nice and friendly but in the end he just wanted her money."

        c "Sounds like an jerk. What happened to him?"

        Mv "Let’s just say that I had a little conversation with him and he agreed that it might be better to leave her alone."

        m "Maverick took a sip from his drink and I decided that it was better to not ask further questions. We just became friends and I didn’t want to jeopardize anything."

        c "It’s good to teach people like those a lesson. {w} Naomi is lucky to have a friend like you."

        Mv "That’s a reason why Naomi is careful when she meets someone she likes. "

        Mv "I’m just asking you to be a good friend to her."

        c "Don’t worry, I really care for her and only want to make her happy."

        $ maverick_redem_naomiromance = True

        $ maverick_redem_romance_partner = "Naomi"

        jump redemdate3C


    "Remy." if persistent.remygoodending == True and remy3unplayed == False and remystatus != "bad":

        c "I’ve been spending quite some time with Remy, the dragon I first met when I came to your world."

        Mv "Is he the one working for Emera?"

        c "Yes, that’s him. I met him again when I visited the library and since then we try to meet when both of us are free."

        m "Maverick looked as if he was trying to remember something."

        Mv "I think I remember him from one of our cases."

        c "Was he a witness or something similar?"

        Mv "No, but he was at the funeral of a dragoness who died during one winter. That was after Anna did some experiments on the body."

        c "You let her experiment on dead bodies?"

        Mv "Anna is working on many important tasks and there are still diseases we don’t understand."

        Mv "As far as we had known during at the time, the dragoness had neither family nor friends we could have asked for permission."

        Mv "After some time, the body was released and buried. Remy was one of the dragons who came to the funeral but he didn’t respond when I asked him if he had known her."

        c "I’m sure the dragon was Amelia, Remy’s fiancée. They had to keep their relationship a secret because of their work."

        c "They planned to move in together after the problems with their work were solved, but then she died."

        Mv "That explains a lot. I tried to keep an eye on him and noticed that his behavior had changed after the funeral."

        c "Did you suspect him for having a role in Amelia’s death?"

        Mv resideeye flip "No, but because of my job I’ve talked to people who lost their loved ones and after what we did with Amelia’s body…"

        Mv normal flip "…Maybe we didn’t search long enough for her dependents. Knowing how it feels like, I tried to offer him help but he refused."

        c "Yeah, Remy has some difficulties talking about his personal problems but I hope I was able to help him a little." 

        c "He always wanted to have children so I told him about the orphanage. Adine, also one of Amelia’s friends, is helping them and I hope that Remy will reconcile with her."

        Mv "You have a good heart."

        Mv "You know, the more I learn about you the more I can’t believe how wrong I was. In hindsight, I can’t understand why I misjudged you that much."

        $ maverick_redem_remyromance = True

        $ maverick_redem_romance_partner = "Remy"

        jump redemdate3C


    "There is no one special.":

        c "I’ve met a few nice dragons and found friends but so far there is no one I’d go beyond friendship."

        Mv "I see. Is it because you’re a human and not a dragon?"

        c "It’s true that we’re the only sentient species on our side of the portal, and it might be frowned upon to consider a different species for dating. However to me, I don’t really see a difference between, for example, the two of us except of our species."

        c "We’re both intelligent, sentient creatures, we can communicate with each other and we’re both adults. So if I’d meet someone special and fall in love, I wouldn’t care if it’s a human or a dragon."

        Mv "Do you think your people will see it the same way?"

        c "As soon as we catch Reza and finish the trade, our two societies might start working even closer together. Someday, dragons could move to our town and humans could move here, so it would only be a matter of time until human-dragon relationships would happen."

        Mv "I’m not sure about more humans coming here but I’ll give them the same chance I gave you. Not everyone has to be like Reza or the people behind him."

        c "Thank you for giving my people a second chance."

        Mv "You’ve earned it."

        $ maverick_redem_noromance = True

        jump redemdate3C


label redemdate3C:

$ renpy.pause (0.3)

scene black with dissolvemed

$ renpy.pause (0.5) 

scene redem_maverick_apartment_b with dissolvemed

show maverick normal flip at left with dissolve

m "I wasn’t sure how different a relationship with a dragon would be but I knew that I wouldn’t care about the species as long as both of us were happy."

m "Suddenly, I remembered about the relationship Reza once had and decided to tell Maverick about the information the diary had offered."

c "Do you remember the diary we’ve found? I was able to read it."

Mv "Did you find anything interesting or was it just stuff we already knew?"

c "The beginning of it was what we expected, daily life and topics about school. However close to graduation he found a girlfriend. They started to work at a company and had been happy."

c "However, despite surviving the flare, she was later murdered because of their supplies."

Mv "Damn, that kind of stuff can break someone especially after what happened to your world."

c "Yes, she was the last ray of hope in his life it seems. This was his last entry after she died."

m "I showed Maverick the last entry and he quickly understood what I meant."

Mv "So her death caused him to go crazy."

c "It seems so. He also murdered the ones who killed her. So if we go with everything we know, then it's likely to say that my people chose Reza because they knew he would do anything to get the generators."

Mv "Including murder. I’m still surprised that he was able to overpower two dragons. He surprised his second victim, but Damion and his first victim died on their back. That implies that he attacked them from the front."

c "I guess he survived a few years outside of Bastion, so he must have learned to adapt. Sure, he has lost his right arm and got a prosthesis but even then he needed skill to survive."

c "At least the first victim was able to wound him."

Mv "Do you think his prosthesis gives him advantage over dragons?"

c "No, his right arm might be stronger but you get the same result by training with dumbbells long enough. At most it could allow him to use his arm even when it’s badly wounded."

Mv "I see. Did you find any hidden messages?"

c "Actually, I didn’t think of that."

Mv "It might be better to give the diary to the analytical team just like the letter. I’ll let Bryce know everything we found out."

m "Maverick took the diary and put it in the same pocket as the warning I had given him earlier."

Mv laugh flip "But let’s stop talking about work. Today we’re having a free day to relax."

c "You’re right."

Mv "I’m glad you finally agree."

c "What do you usually do when you’re not working? I know you mentioned that your life is mostly focused on work but there needs to be some way for you to relax."

Mv normal flip "Well, there aren’t many things except flying or watching some shows on the TV."

c "Oh, is there some kind of genre you prefer?"

Mv resideeye flip "Well, comedy shows. With all the stuff happening in my life I try to not forget how to laugh from time to time. There are also some cop shows but most of them only remind me of work and the bad stuff."

Mv normal flip "How about you?"

c "Before the flare I also liked to watch TV or reading books. I often met with friends and we were walking through the forest or visiting lost places."

Mv "Lost places? What are those?"

c "From time to time, my people abandoned buildings and despite having different plans, they never actually did anything with them but let them rot."

Mv "So they are like modern ruins."

c "Yes, more or less. It was interesting to visit those places and see how nature took back the buildings."

c "Sadly a fun activity later turned into a way to survive after the flare."

Mv "In some way I understand how something you once loved turned into a reminder of something you lost."

m "I kind of knew what he meant so I tried to change the topic so something better."

c "Well, I have to confess that I was into romance crime series back before the flare. There were a few of them with the tough, smart and beautiful detective and the comedic sidekick."

Mv laugh flip "If you'd join the team, you…"

if maverick_redem_maverickromance == True:

    Mv "… could be my sidekick. I mean, I’d count as the tough and handsome detective, wouldn’t I?"


    c "Of course you would, Mav. Very tough and very handsome."

    show maverick reblush flip with dissolve


elif maverick_redem_bryceromance == True:

    Mv "… could be Bryce's sidekick. He’s not my type, but I guess he would count as a tough and handsome detective, wouldn’t he?"

    c "Yes, he would totally fit the job description." 


else:

    Mv "… you would be the sidekick of our department." 

c "I might not be a famous book author but a human would be a fitting sidekick for a dragon cop."

Mv normal flip "Maybe they should make a romantic crime series about our department."

c "I’d watch it. It has romance, action and dragons. How could anyone refuse to give it a try?"

Mv "Too bad that we’d all be celebrities then. I don’t really need all that attention."

c "Neither do I."

m "Maverick was silently looking at his drink, deep in thought. I wondered what he was thinking about but luckily I didn’t need to wait too long."

Mv "I was thinking about something the last few days."

c "Something special?"

Mv "Well, years ago I went hiking with…someone else. We did that every month but one day we had an argument and then some stuff happened…"

Mv "After that, I never did it again but now…"

c "So you're considering going hiking again?"

Mv "I… yes, think I am. It has been a long time and I kind of want to do it again before all of this is over."

c "You mean when we finally catch Reza."

Mv resideeye flip "Yes, that too."

Mv normal flip "I always enjoyed those trips. It was just the two of us in the woods while we climbed the mountain. At the top was a little cottage where we rested until the next day. Then at sunrise, we jumped from the cliff and flew down, admiring the view."

c "I really like the sound of it. The view must have been amazing."

Mv "It was and I kind of want to do it again. The last few days made me realize that it might be time to revive some old habits. Life is too short and you never know what might happen."

m "I wasn’t sure what he was talking about but he was right. The flare had taught me the same lesson."

Mv "You know, my kind isn’t really the best at taking off and I've spent months of hard training until I was good enough to become the flyer on duty. However back then, this was as close as I was to get the view that flyers always have. It was, as if the world was ours."

c "I hope that you’ll enjoy your trip."

Mv "Thanks. You know, if you’re free you could join me. I mean, if you want to. Those two weeks weren’t easy for you so it might help you to clear your mind and I can show you a little more of our world."

c "I like the idea but I sadly can’t fly."

Mv "Don’t worry; you’re smaller than a dragon so I’m sure I’d be able to carry you."

Mv "I know that it takes a lot of trust but I promise that I won’t be reckless and make sure you’ll be safe."

c "Thank you for the offer, Maverick. I’ll think about it."

Mv rehappy flip "That’s what I hoped to hear."

Mv "By the way, since we're all working on the case and Bryce figured out that we're working together, he wanted me to give you this."

m "Maverick handed me something that reminded me of the old mobile phones we had long before our PDAs."

Mv "It's an older version but the best he was able to get that fast."

Mv "In an emergency we dragons can call for back-up by just roaring but I don't think it'd work for you. So instead we thought this phone would help if you're ever in danger and none of us is around."

Mv laugh flip "It even has a panic button that would alarm the department."

c "Thanks, that's a good idea. Although I hope I'll never need it."

Mv rehappy flip "That's true but better safe than sorry."

m "When I looked out of the window I noticed that it was starting to get darker. Knowing that it’ll take some time to get to my apartment I had to leave soon."

c "I’m sorry Maverick but it’s getting late. Maybe I should go soon before it’s too dark."

Mv normal flip "Time sure moves fast when you’re in good company."

Mv "However, I think it might be better to not go outside alone while Reza is still on the loose. It might be safer if you stay overnight."

c "Are you sure it’s ok?"

Mv "Don’t worry; my place is big enough and I can escort you home tomorrow after breakfast."

c "Thanks Maverick."

Mv rehappy flip "Don’t worry, that’s what friends do."

stop music fadeout 2.0

$ maverickscenesfinished += 1
    
if maverick_redem_maverickromance == True :
    $ maverickstatus = "good"
else :
    $ maverickstatus = "normal"

# This if statement above is to decide whether he's impressed (romancing Mav) or just good with you (no romance/romancing someone else), this basically replaces the whole status screen gimmick of magmalink with something really simple. - Nyxondra

jump ml_date_end
