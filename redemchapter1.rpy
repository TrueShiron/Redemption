label redem_meetmaverick :
$persistent.maverickmet = True
$maverickscenesfinished = 0
jump redem_meetmaverick_return


label redem_chapter1moodchange :
$ maverickstatus = "bad"
jump redem_chapter1moodchange_return

#Adding these two labels for status screen purposes, hoping this tracks with how you imagined the story Shiron. - Nyxondra


label redemchapter1: 

m "I saw Bryce escorting Maverick away from the crime scene and wondered if there was a way to prove to him that I wasn’t working with Reza. "

m "Sebastian was still close by, escorting Adine to the department while taking notes. If I wanted a way to solve the problem with Maverick, I had to make a decision. "


menu:

    "[[Call Sebastian.]":

        hide maverick with dissolve

        hide bryce with dissolve

        show sebastian normal b flip at left with easeinleft

        m "I gave Sebastian a sign that I wanted to talk to him in private without the others hearing us."

        Sb "Do you need something [player_name]?"

        c "Well, I just wondered if you’d know a way for me that would help me to gain Maverick’s trust… or at least to make him stop accusing me of being Reza’s accomplice."

        Sb "Maverick is a good and loyal friend but I’ve learned that it takes time for him to trust others. Sadly your situation is special so I doubt that there is a way to solve things anytime soon. Unless…"

        c "Unless?"

        Sb drop b flip "Actually, forget I said anything. It could only make things worse."

    "[[Say nothing.]":

        $ maverick_redem_sendmessage = False
        
        jump redemchapter1_end 

menu:

            "[[Tell Sebastian to go on.]":

                c "What do you have in mind?"

                Sb drop b flip "Well, you could try and talk to him. As long as you stay calm and don't act suspicious he won’t do anything stupid, I guess."

                c "You guess?"

                Sb normal b flip "Since Reza appeared here Mav is way more tense than usual. I doubt that he’d attack you for no reason but you should still be careful." 

                Sb "Do you want me to send him a message?"

            "[[Agree.]":

                c "Maybe you’re right. I hope time will prove to him that I’m not his enemy."

                Sb "That might be better. I really need to go now. Bye."

                hide sebastian with dissolve

                $ renpy.pause (0.5)

                show maverick normal flip at Position(xpos = 0.13) with dissolve

                show bryce stern b at right with dissolve

                m "Bryce looked at Sebastian and me when I returned to him but didn’t say anything. In the distance I could still hear Maverick’s angry voice."

                $ maverick_redem_sendmessage = False
                

                jump redemchapter1_end



menu:

                        "[[Send a message.]":

                            c "Yes, I think it might be better to give it a try."

                            Sb "Ok, I’ll tell him to give you a call. However, I’ll keep an eye on you both, just in case."

                            c "Thank you, Sebastian."

                            Sb "You’re welcome, [player_name]. I’m sure everything will work out."

                            Sb "I really need to go now. Bye."

                            hide sebastian with dissolve

                            $ renpy.pause (0.5)

                            show maverick normal flip at Position(xpos = 0.13) with dissolve

                            show bryce stern b at right with dissolve

                            m "Bryce looked at Sebastian and me with a concerned look when I returned to him but didn’t say anything. In the distance I could still hear Maverick’s angry voice and hoped that I didn’t make a grave mistake."

                            $ maverick_redem_maverickromance = False

                            $ maverick_redem_sendmessage = True
                            
                            $ maverickstatus = "bad"

                            jump redemchapter1_end 


                        "[[Don’t send a message.]":


                            c "No, I think it might be too risky for now and my mission is too important for mankind. I hope time will prove to him that I’m not his enemy."

                            Sb "That might for the best. I really need to go now. Bye."

                            hide sebastian with dissolve

                            $ renpy.pause (0.5)

                            show maverick normal flip at Position(xpos = 0.13) with dissolve

                            show bryce stern b at right with dissolve

                            m "Bryce looked at Sebastian and me when I returned to him but didn’t say anything. In the distance I could still hear Maverick’s angry voice."

                            $ maverick_redem_sendmessage = False
                            
                            jump redemchapter1_end 

label redem_call1:

    if maverick_redem_sendmessage == False:

        pass

    else:

        play sound "fx/answeringmachine.ogg"

        $ renpy.pause (0.5)

        Mv "Sebastian gave me your message."
        Mv "I don’t know what game you’re playing but you better not try to trick me."

        play sound "fx/answeringmachine.ogg"

        $ renpy.pause (0.5)

        m "I guess there was no backing out now."

        m "If I wouldn't meet him today then all the work was for nothing."

        jump ml_answeringmachine_end

    jump ml_answeringmachine_end
