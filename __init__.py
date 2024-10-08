from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml
import renpy.parser as parser
import renpy.ast as ast
@loadable_mod
class AWSWMod(Mod):
    name = "Redemption"
    version = "1.5"
    author = "Shiron"
    dependencies = ["MagmaLink", "A Solitary Mind", "!The Reckless Criminal"]

    def mod_load(self):
        ml.find_label("seccont") \
            .search_scene("fac1") \
            .search_say("Yeah, whatever. Just don't expect me to give you any special treatment like everyone else is and we'll be good.") \
            .hook_to("redem_meetmaverick") \
            .link_from("redem_meetmaverick_end")
            
        ml.find_label("continuation") \
            .search_say("Come on, I think you're overreacting, but we'll come with you if it'll help in any-{w=1.0}{nw}") \
            .hook_to("redem_chapter1moodchange") \
            .link_from("redem_chapter1moodchange_end")
            
        ml.find_label("quest6") \
            .search_say("Enough. You shouldn't even be here, so you better go now and get some rest before I have to take disciplinary action.") \
            .hook_to("redemchapter1") \
            .search_say("Fine, but when we find him, you'll see I was right. If I have to prove it myself, so be it.") \
            .link_from("redemchapter1_end")

        ml.find_label("chapter2") \
            .search_say("Tchk. Have your fun without me, then.", depth=600) \
            .hook_to("redemchapter2A", condition="maverickscenesfinished == 1") \
            .search_say("What do you think he wanted here, Chief?") \
            .link_from("redemchapter2A_end")

        ml.find_label("chap2cont2") \
            .search_say("(I'm not sure how my findings will help, but at least I have something.)") \
            .hook_to("redemchapter2B", condition="maverickscenesfinished == 1") \
            .search_say("Hey, Sebastian! I thought I'd meet you at the front desk. What are we doing in Bryce's office?") \
            .link_from("redemchapter2B_end")

        ml.find_label("chap2skip3") \
            .search_say("That should be all, then. Since Bryce still hasn't come back, I assume the search is still going on, and I better get out there and help him. Guess it's going to be a long day.") \
            .hook_to("redemchapter2C", condition="maverickscenesfinished == 1") \
            .search_say("Alright. I'll see you later.") \
            .link_from("redemchapter2C_end")

        ml.find_label("bryce3") \
            .search_say("Does he know that I'm here?") \
            .hook_to("redem_bryce3", condition="maverickscenesfinished >= 2") \
            .search_say("As we walked a few paces, I saw some familiar faces.") \
            .link_from("redem_bryce3_end")

        ml.find_label("bryce3") \
            .search_say("Hey, [player_name].", depth=600) \
            .hook_to("redem_bryce3_B", condition="maverickscenesfinished == 3") \
            .search_say("I don't see a grill or anything here. And where's the firewood?") \
            .link_from("redem_bryce3_B_end")

        ml.find_label("bryce3") \
            .search_say("Hey, I'm not getting between the beautiful thing Emera and Bryce have going on.", depth=900) \
            .hook_to("redem_bryce3_C", condition="maverickscenesfinished == 3") \
            .search_say("By the way, I think the food should be ready now.") \
            .link_from("redem_bryce3_C_end")

        ml.find_label("c4resultscontinue") \
            .search_say("The chief will explain everything once we get there. Let's not keep him waiting, shall we?") \
            .hook_to("redemchapter4", condition="maverickscenesfinished == 3") \
            .search_say("There you are.") \
            .link_from("redemchapter4_end")

        ml.find_label("c4resultscontinue") \
            .search_say("I've been tracking him for a while now.", depth=900) \
            .hook_to("redemchapter4_A", condition="maverickscenesfinished == 3") \
            .search_say("You're not really going to use me as ransom, right?") \
            .link_from("redemchapter4_A_end")
        
        ml.find_label("c4skip1") \
            .search_say("You're not really going to use me as ransom, right?") \
            .hook_to("redemchapter4_B", condition="maverick_redem_trust == True") \
            .search_say("I spent some time looking around Bryce's office, studying all the material he had gathered about the case, though there wasn't any information that I didn't already know.") \
            .link_from("redemchapter4_B_end")   

        ml.add_answ_machine_message("redem_call1", condition="maverick_redem_sendmessage == True", chapters=[1])
        ml.add_answ_machine_message("redem_call2", condition="maverickscenesfinished == 1", chapters=[2])
        ml.add_answ_machine_message("redem_call3", condition="maverickscenesfinished == 2 and annadead == False", chapters=[3])
        ml.add_answ_machine_message("redem_call4", condition="maverickscenesfinished == 3 and brycedead == False and remydead == False and loremdead == False", chapters=[4])

        ml.CharacterRoute("redemchapter1", "Maverick") \
            .add_date(text="Meet with Maverick.", condition="maverick_redem_sendmessage == True", jump="redemdate1", chapters=[1]) \
            .add_date(text="Meet with Maverick.", condition="maverickscenesfinished == 1", jump="redemdate2", chapters=[2]) \
            .add_date(text="Meet with Maverick.", condition="maverickscenesfinished == 2 and annadead == False", jump="redemdate3", chapters=[3]) \
            .add_date(text="Meet with Maverick.", condition="maverickscenesfinished == 3 and brycedead == False and remydead == False and loremdead == False and c4csplayed == 0", jump="redemdate4", chapters=[4]) \
            .set_ending(jump="redemchapter5", condition="adinedead == False and adinestatus != \"bad\" and annastatus != \"bad\" and brycestatus != \"bad\" and loremstatus != \"bad\" and naomistatus != \"bad\" and remystatus != \"bad\" and persistent.endingsseen != 0") \
            .build()
        
        #ml.StatusBox("maverick_redem_scenesfinished", condition="maverick_redem_sendmessage == True") \
        #    .add_status("image/ui/status/maverick_bad.png", "Bad", condition="maverick_redem_scenesfinished == 0") \
        #    .add_status("image/ui/status/maverick_neutral.png", "Neutral", condition="maverick_redem_scenesfinished == 1") \
        #    .add_status("image/ui/status/maverick_good.png", "Good", condition="maverick_redem_scenesfinished >= 2 and maverick_redem_maverickromance == False") \
        #    .add_status("image/ui/status/maverick_impressed.png", "Impressed", condition="maverick_redem_scenesfinished >= 2 and maverick_redem_maverickromance == True") \
        #    .build()

        #ml.StatusBox("naomiscenesfinished", condition="naomidead") \
        #    .add_status("image/ui/status/naomidead.png", "--", " ") \

        #ml.StatusBox("naomiscenesfinished", condition="persistent.naomimet") \
        #    .add_status("image/ui/status/naomi_neutral.png", "Neutral", "naomistatus == \"none\"") \
        #    .add_status("image/ui/status/naomi_good.png", "Good", "naomistatus == \"neutral\"") \
        #    .add_status("image/ui/status/naomi_neutral.png", "Good", "naomistatus == \"normal\"") \
        #    .add_status("image/ui/status/naomi_impressed.png", "Impressed", "naomistatus == \"good\"") \
        #    .add_status("image/ui/status/naomi_stern.png", "Bad", "naomistatus == \"bad\"") \
        #    .add_status("image/ui/status/naomi_abandoned.png", "Abandoned", "naomistatus == \"abandoned\"") \
        #    .build()

        #Old status box for MagmaLink

        tocompile = """
            screen dummy:
                vbox: 
           
                    xalign 0.791 yalign 0.655
                    if persistent.maverickmet:
                        if maverickdead:
                            add "image/ui/status/maverick_dead.png" xalign 0.5  at popup_offcenter
                            text _("Status: {b}--{/b}\\nScenes played: {b}[maverickscenesfinished]{/b}") style "status_text" 
            
                        elif maverickstatus == "none":
                            add "image/ui/status/maverick_neutral.png" xalign 0.5  at popup_offcenter
                            text _("Status: {b}Neutral{/b}\\nScenes played: {b}[maverickscenesfinished]{/b}") style "status_text" 
            
                        elif maverickstatus == "neutral":
                            add "image/ui/status/maverick_good.png" xalign 0.5 at popup_offcenter
                            text _("Status: {b}Okay{/b}\\nScenes played: {b}[maverickscenesfinished]{/b}") style "status_text"  
            
                        elif maverickstatus == "normal":
                            add "image/ui/status/maverick_neutral.png" xalign 0.5  at popup_offcenter
                            text _("Status: {b}Good{/b}\\nScenes played: {b}[maverickscenesfinished]{/b}") style "status_text"  
            
                        elif maverickstatus == "good":
                            add "image/ui/status/maverick_impressed.png" xalign 0.5 at popup_offcenter
                            text _("Status: {b}Impressed{/b}\\nScenes played: {b}[maverickscenesfinished]{/b}") style "status_text" 
                    
                        elif maverickstatus == "best":
                            add "image/ui/status/maverick_besties.png" xalign 0.5 at popup_offcenter
                            text _("Status: {b}Besties{/b}\\nScenes played: {b}[maverickscenesfinished]{/b}") style "status_text" 
            
                        elif maverickstatus == "bad":
                            add "image/ui/status/maverick_stern.png" xalign 0.5 at popup_offcenter
                            text _("Status: {b}Bad{/b}\\nScenes played: {b}[maverickscenesfinished]{/b}") style "status_text"  
            
                        elif maverickstatus == "abandoned":
                            add "image/ui/status/maverick_abandoned.png" xalign 0.5  at popup_offcenter
                            text _("Status: {b}Abandoned{/b}\\nScenes played: {b}[maverickscenesfinished]{/b}") style "status_text" 
        """        
        compiled = parser.parse("FNDummy", tocompile)
        for node in compiled:
            if isinstance(node, ast.Init):
                for child in node.block[0].screen.children:
                    modast.get_slscreen('status').children.append(child)

        tocompile = """
        screen dummy:       
            if persistent.redem_mavbadending:
                add "image/title/mavbad.png"    
    
            if persistent.redem_mavgoodending:
                add "image/title/mavgood.png"
             
        """
        compiled = parser.parse("FNDummy", tocompile)
        for node in compiled:
            if isinstance(node, ast.Init):
                for child in node.block[0].screen.children:
                    modast.get_slscreen('main_menu').children.append(child)


    def mod_complete(self):
        pass

# This file is free software under the GPLv3 license
# Thanks you Nyxondra for adding the new status, Maverick appearing on the main screen and helping me with fix all the errors and bugs of the mod
