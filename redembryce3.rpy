label redem_bryce3:

Br "Yes, and he assured me that he will keep the peace. Can you do the same?"

c "Sure."

$ renpy.pause (0.5)

Br normal "Thanks, I appreciate it."

Br brow "Let's just hope there won't be any incidents."

$ bryce3mood += 1

show bryce normal with dissolve

jump redem_bryce3_end



label redem_bryce3_B:

c "Hey, Maverick."

Mv "..."

m "It wasn't difficult for me to see how Maverick tried to keep his hostile behavior to fool everyone else, but I hoped it would be enough to fool Bryce and Zhong."

hide maverick with easeoutleft

Br "Alright, let's get this BBQ started."

show bryce at Position(xpos = 1.175) with ease

show sebastian smile flip at left with easeinleft

show maverick normal behind bryce at Position(xpos=0.825) with easeinright

show zhong normal flip at Position(xpos = 0.05) with easeinleft

jump redem_bryce3_B_end


label redem_bryce3_C:

Br "If you ask me, you can do whatever you like as long as you're here. Knock yourself out."

Br flirty "Maybe you already found interest in a certain dragon on sick leave."

m "Maverick and I both hesitated for a moment before I saw an annoyed look on his face."

c "I don’t know what you’re talking about, Bryce. You know that we’re not really the best of terms right now."

Br laugh "Oh, are you sure about that?"

Br flirty "A little Mouflon told me that you two were spending time with each other without any bad blood between you."

m "It seems as if Maverick and I had been busted."

Mv angry "Sebastian…"

Sb shy flip "I haven’t told Bryce anything, I swear."

Br "I heard your little conversation the other day about sending Maverick a letter."

Br flirty "We dragons have good ears."

Br flirty "Is there anything you two want to tell us. Maybe about human-dragon relationships?"

Mv angry "Get off my case, Bryce."

Mv normal "[player_name] and I are just working on the Reza case and following some promising leads."

Br stern "You know you aren’t allowed to do that, even if you weren’t on sick leave. I’m not sure if I can protect you if you get caught, Maverick. [player_name] is protected by his ambassador status but you aren’t."

c "Don’t worry, Bryce, we are careful."

Br "I hope you two know what you’re doing."

Sb normal flip "Maybe we should not talk about work tonight."

Br laugh "You are right, Seb. We’re here to have fun and not to talk about work."

jump redem_bryce3_C_end


label redem_call3:

play sound "fx/answeringmachine.ogg"

$ renpy.pause (0.5)

Mv "Hey, [player_name]."
Mv "I asked Seb to leave you a note with my address at your apartment."
Mv "You know, just in case you want to come visit if you're free today."

play sound "fx/answeringmachine.ogg"

$ renpy.pause (0.5)

jump ml_answeringmachine_end
