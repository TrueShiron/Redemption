
#Inside images

image redem_reza_apartment = "bg/in/redem_reza_apartment.png"
image redem_reza_kitchen = "bg/in/redem_reza_kitchen.jpg"
image redem_reza_bath = "bg/in/redem_reza_bath.jpg"
image redem_reza_bedroom = "bg/in/redem_reza_bedroom.png"
image redem_maverick_apartment_a = "bg/in/redem_maverick_apartment_a.jpg"
image redem_maverick_apartment_b = "bg/in/redem_maverick_apartment_b.jpg"
image redem_maverick_apartment_c = "bg/in/redem_maverick_apartment_c.jpg"
image redem_hike_hut_inside = "bg/in/redem_hike_hut_inside.jpg"
image redem_mc_bedroom_a = "bg/in/redem_mc_bedroom_a.png"
image redem_mc_bedroom_b = "bg/in/redem_mc_bedroom_b.png"
image redem_hospital_a = "bg/in/redem_hospital_a.jpg"

#Outside images
image redem_park2night = "bg/out/redem_park2night.png"
image redem_hike_hut_outside = "bg/out/redem_hike_hut_outside.png"
image redem_hike_top = "bg/out/redem_hike_top.jpg"
image redem_hike_forest_a = "bg/out/redem_hike_forest_a.png"
image redem_hike_forest_b = "bg/out/redem_hike_forest_b.jpg"
image redem_hike_forest_c = "bg/out/redem_hike_forest_c.jpg"
image redem_hike_forest_d = "bg/out/redem_hike_forest_d.jpg"
image redem_hospital_b = "bg/out/redem_hospital_b.jpg"
image redem_hike_end = "bg/out/redem_hike_end.jpg"
image redem_aw_glitch = "bg/out/redem_aw_glitch.png"

#Endings	
image redem_e_ending = "cg/redem_e_ending.png"
image redem_good_ending = "cg/redem_good_ending.png"

#Credits
image redem_credits = "cg/redem_credits.png"

#Sprites - not working with sideimages
image maverick reannoyed = "cr/maverick_reannoyed.png"
image maverick reirritated = "cr/maverick_reirritated.png"
image maverick relost = "cr/maverick_relost.png"
image maverick rerelief = "cr/maverick_rerelief.png"
image maverick rerelief c = "cr/maverick_rerelief_c.png"
image maverick resad = "cr/maverick_resad.png"
image maverick reshock = "cr/maverick_reshock.png"
image maverick resideeye = "cr/maverick_resideeye.png"
image maverick resideeye b = "cr/maverick_resideeye_b.png"
image maverick reblush = "cr/maverick_reblush.png"
image maverick reblush b = "cr/maverick_reblush_b.png"
image maverick recry = "cr/maverick_recry.png"
image maverick recry b = "cr/maverick_recry_b.png"
image maverick rehappy = "cr/maverick_rehappy.png"

image maverick reannoyed flip = im.Flip("cr/maverick_reannoyed.png", horizontal=True)
image maverick reirritated flip = im.Flip("cr/maverick_reirritated.png", horizontal=True)
image maverick relost flip = im.Flip("cr/maverick_relost.png", horizontal=True)
image maverick rerelief flip = im.Flip("cr/maverick_rerelief.png", horizontal=True)
image maverick rerelief c flip = "cr/maverick_rerelief_c.png, horizontal=True"
image maverick resad flip = im.Flip("cr/maverick_resad.png", horizontal=True)
image maverick reshock flip = im.Flip("cr/maverick_reshock.png", horizontal=True)
image maverick resideeye flip = im.Flip("cr/maverick_resideeye.png", horizontal=True)
image maverick resideeye b flip = im.Flip("cr/maverick_resideeye_b.png", horizontal=True)
image maverick reblush flip = im.Flip("cr/maverick_reblush.png", horizontal=True)
image maverick reblush b flip = im.Flip("cr/maverick_reblush_b.png", horizontal=True)
image maverick recry flip = im.Flip("cr/maverick_recry.png", horizontal=True)
image maverick recry b flip = im.Flip("cr/maverick_recry_b.png", horizontal=True)
image maverick rehappy flip = im.Flip("cr/maverick_rehappy.png", horizontal=True)

#New name for variables -> maverick__redem_variable
#Makes is almost impossible to conflict with other mod's variables

init python:


#For if/else

    #Starting the mod
    maverick_redem_sendmessage = False

    #Choosing between this mod and the base game or Savior in chapter 4
    maverick_redem_trust = False

    #Chosing the endings
    maverick_redem_mapgiven = False
    maverick_redem_dream = False

    #Reza investigation during date 2
    maverick_redem_bathroom_search = False
    maverick_redem_bedroom_search = False
    maverick_redem_kitchen_search = False
    maverick_redem_living_room_search = False
    maverick_redem_fridge_search = False

    #Romance partner
    maverick_redem_adineromance = False
    maverick_redem_annaromance = False
    maverick_redem_bryceromance = False
    maverick_redem_maverickromance = False
    maverick_redem_naomiromance = False
    maverick_redem_remyromance = False
    maverick_redem_noromance = False

    maverick_redem_maverick_accept = False

    #Other things
    maverick_redem_complications = False 

#For everything else

    maverick_redem_status = None
    maverick_redem_drink = None
    maverick_redem_rezasearch = 0
    maverick_redem_scenesfinished = 0
    maverickdead = False
    maverickstatus = None
    maverickscenesfinished = 0
    redemadine4unplayed = False


    #adding the name of the romance partner for [maverick_redem_romance_partner]
    maverick_redem_romance_partner = None
