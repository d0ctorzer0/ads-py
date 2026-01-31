label END_heathtrue:
    window auto
    scene black
    with fade
    $ daynum = "52"
    $ dayday = "On the road..."

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)
    
    scene black with fade
    play music deathtoaperture
    rd "Temperatures are expected to be in the high 80s today, with little to no clouds..."
    rd "It's a perfect day to get out there and explore!"
    mc "Sounds like we picked the right time for our vacation."
    show h offrail with easeinbottom
    h "Did we ever! Oh, I'm so excited."
    show h sad offrail
    h "I wish you had told me where we're going..."
    mc "That would've ruined the surprise, Heath."
    mc "But I can probably tell you now..."
    hide h with easeoutbottom
    scene colon with dissolve 
    n "You slow down as you pass by the sign -"
    n "COLON - MAGIC CAPITAL OF THE WORLD"
    show h look offrail with easeinbottom
    h "Magic capital of the..."
    show h offrail
    h "HOLY HOWARD THURSTON YOU DIDN'T!"
    mc "I did."
    h "Oh my Copperfield!!"
    h "I'm so excited! I can't believe it!"
    show h sad offrail
    show heath blush with Dissolve(0.05)
    h "Oh wow. You're so sweet."
    mc "I'm just surprised it was close enough that we could drive to it."
    hide heath blush
    show h offrail
    h "How'd you even find this place?"
    mc "It wasn't easy. Took a lot of looking through papers, asking around, making a couple calls..."
    mc "But it's all worth it for you."
    h "You're more full of surprises than I am."
    mc "Don't flatter me too much, now."
    mc "Anyways. There's museums about the history of magic here, and popular magicians perform here all the time..."
    mc "I figured it'd be perfect for you."
    show h sad offrail
    h "It's almost as perfect for me as you are."

    scene black with fade
    scene colon with fade
    n "Eventually, you reach the house you're looking for - a quaint little bed and breakfast just outside the town."
    n "You park your car, take off your seatbelt, and pop the trunk."
    n "You slide your oven mitts on - something you've had to invest in to handle Heath recently - and pick her up gently."

    show h offrail with easeinbottom
    mc "Cooler time."
    h "My favorite."
    n "You place her down carefully in a very spacious cooler you keep in the trunk."
    n "It keeps her internal systems at a normal temperature - most of the time."

    mc "I've gotta hide you now. You'll be alright till we get up there, right?"
    show h look offrail
    h "Don't worry about me - I'm super stealthy when I want to be."
    mc "I don't believe you."
    show h offrail
    h "Haha, you got me."
    hide h with easeoutbottom
    n "You close the cooler lid and head up to the house entrance."

    scene colon bnb with fade
    mc "She was nice. What did she say her name was? Dolores or something?"
    n "A muffled voice comes from the cooler."
    h "Dolly."
    mc "Ah, yes. You're right."
    n "You place the cooler down on the bed and open the lid. Water vapor spills out."
    show h offrail with easeinbottom
    h "What can I say? I'm a smokeshow no matter where I go."
    mc "Oh, stop."
    h "This is a nice place. Very cozy. Nothing like where we came from, haha!"
    mc "Our apartment isn't cozy?"
    show h sad offrail
    h "Oh no! That's not what I meant at all. I - I was talking about Aperture."
    mc "Oh. Yeah. That place was kind of depressing, wasn't it?"
    h "Yeah..."
    h "But without it -"
    show h offrail
    show heath blush with Dissolve(0.05)
    h "I never would've met you. And that would've been a shame."
    show h look offrail
    h "S-Sorry."
    hide heath blush
    mc "What do you have to be sorry for?"
    h "I don't think I've thanked you enough. For saving me from that place."
    show h offrail
    h "You've got a different kind of magic in you. One I could never replicate, haha!"
    h "That's what I love about you."
    mc "You mean so much to me, Heath."
    mc "We should both get some rest, though. That was a pretty long drive."
    show h sad offrail
    h "Yeah, my systems are yelling at me again. I should shut down for the night."
    mc "Goodnight, Heath."
    show h offrail
    h "Goodnight."

    scene black
    with fade
    $ daynum = "53"
    $ dayday = "Colon, Michigan"

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)

    scene colon bnb with fade

    n "You wake up and hurriedly lean over the bed to check on Heath."
    n "Thankfully, you hear the gentle whirring of her internal mechanisms - although they're slower than they were yesterday."
    n "They've been getting slower, and quieter, since the two of you left Aperture."
    n "In addition, Heath herself has been slowing down as well..."
    n "She'd never admit it though."
    n "You let her rest for a little longer."

    scene black with fade
    scene colon bnb with fade

    mc "Heath - it's time to get up."
    show h offrail with easeinbottom
    h "Mmm. I'm up, I'm up. Sorry, did I sleep in?"
    mc "Not at all."
    h "Good. I'm so excited for today!"
    h "I'm sure you have lots in store for us."
    mc "You bet I do."
    mc "Give me just a second to change and we'll be on our way."
    h "Awesome!"
    
    scene colon museum with fade
    n "The museum is packed - not with people, but with magical history."
    n "For a core that's been underground - literally - her whole life, Heath seems to know a lot about this stuff."
    show h offrail with easeinright
    h "Percy Abbott! Not very well known, but I've heard about him."
    show h look offrail
    h "I may or may not have combed through every record Aperture had on magic..."
    show h offrail
    h "And a Doug Henning autograph! He's a legend of magic revival!"
    h "Wow..."
    h "Oh my god! Is that one of Houdini's props?!"
    show h look offrail
    h "Certainly you've heard of Houdini, right?"
    mc "Of course I have. Everyone's heard of Houdini."
    mc "I think he's the most popular magician ever."
    show h offrail
    h "I used to dream I'd get to be as popular as him one day."
    show h sad offrail
    h "A little ridiculous, I know, being stuck down in Aperture and everything..."
    mc "And even above the surface, we still have to hide you most of the time."
    h "Yeah... but it's alright."
    show h offrail
    h "I kind of always knew it was a far-away dream."
    show h sad offrail
    mc "Heath..."
    show h look offrail
    n "Heath coughs harshly."
    mc "You're burning up. We need to get you back to the cooler."
    h "Y-Yeah. Okay."
    n "You bundle Heath up and run her back out to your car."
    
    scene colon park with fade
    n "You decide to head to a nearby park, where you can hopefully get some water to fill Heath's cooler."
    mc "You've been overheating a lot lately..."
    show h look offrail with easeinbottom
    h "A little too much, huh? Haha..."
    mc "What do you mean?"
    h "Oh, nothing. Just... I've been getting weaker lately."
    h "I stay at my normal temperature less and less every day..."
    h "Hell, I have to stay in the cooler half the time..."
    show h sad offrail
    h "Plus, when was the last time you actually saw me perform a trick?"
    n "You think back to the past couple weeks."
    mc "You're right. You haven't performed for a while."
    show h look offrail
    h "I just don't have the energy anymore."
    show h offrail
    h "I have the mindset! I have the desire!"
    show h sad offrail
    h "But not the power."
    mc "Heath, be straight with me. What are you saying?"
    show h look offrail
    h "..."
    h "I don't know how much longer I'll last, darling."
    h "My systems are constantly giving me warnings... and no matter how much coolant you put in, it evaporates within the hour."
    show h sad offrail
    h "I can't be a burden like this forever."
    h "And my systems won't let me."
    mc "Heath, I..."
    mc "Are you saying you're... dying?"
    show h offrail
    h "Haha... sure. In human definitions."
    h "That probably would've been easier, huh?"
    mc "Heath..."
    show h sad offrail
    h "Can I... do one last trick for you?"
    mc "Of course. I love your tricks."
    show h offrail
    h "I know you do."
    $ cutscenetextbox = True
    show screen cuttextbox
    scene heath cutscene 6 with fade
    python:
        if persistent.hc6 == False:
            persistent.cutscenes_seen += 1
            persistent.hc6 = True
    if persistent.cutscenes_seen == cutscene_count and persistent.ach_picture == False:
        python:
            achievement.grant("ach_picture")
            achievement.sync()
            persistent.ach_picture = True
            ach_name = "picture"
        show screen ach_popup with easeinbottom
    n "{color=#fff}Heath closes her optic and slowly opens her shell -"
    n "{color=#fff}- Something you didn't know was possible, even with all your time in Manufacturing."
    n "{color=#fff}What follows is perhaps the most beautiful display of colors you've ever seen from an Aperture product."
    h "{color=#fff}I can't use this trick usually."
    h "{color=#fff}It kills me. Basically."
    h "{color=#fff}I learned how to do it after studying my own programming for hours and hours..."
    h "{color=#fff}...just in case the opportunity arose."
    h "{color=#fff}Anything for a good trick, right?"
    h "{color=#fff}I love making people smile."
    mc "{color=#fff}You've made me smile everyday since we left that place, Heath."
    mc "{color=#fff}I'm sorry I couldn't -"
    h "{color=#fff}There's nothing you could have done anyway."
    h "{color=#fff}You know better than anyone that robotics can't last forever -"
    h "{color=#fff}Especially when you overclock them."
    h "{color=#fff}I love you."
    h "{color=#fff}And the little time I had with you..."
    h "{color=#fff}It was the best time of my life."
    h "{color=#fff}When I felt the most seen."
    h "{color=#fff}The most loved."
    h "{color=#fff}I've been on stage for my entire existence..."
    h "{color=#fff}But you were the first to look up there and see... {i}me."
    h "{color=#fff}Thank you."
    mc "{color=#fff}Thank you, Heath."
    mc "{color=#fff}I... I love you too."
    h "{color=#fff}Y-You might want to let go of me now."
    h "{color=#fff}I'm fairly sure I explode at the end of this... trick."
    n "{color=#fff}You let go of Heath, lay her down in the grass looking at the sky, and back away."
    n "{color=#fff}And in one final, yet somehow quiet, burst -"
    stop music fadeout 2.0
    n "{color=#fff}- she's gone."
    n "{color=#fff}A single yellow ribbon piece left behind."
    window hide
    scene black with fade
    python:
        showpopup = False

        # These are arranged in order of priority. Lowest priority will be overwritten
        # by higher priority, so if multiple achievements are gained, only the highest
        # priority will show.

        if persistent.ach_heathtrue == False:
            persistent.endings_got["heathtrue"] = True
            ach_name = "heathtrue"
            showpopup = True
            achievement.grant("ach_heathtrue")
            persistent.ach_heathtrue = True

        if persistent.endings_got["kristrue"] and persistent.endings_got["heathtrue"] and persistent.endings_got["heathtrue"] and persistent.endings_got["cctrue"] and persistent.endings_got["robtrue"] and persistent.endings_got["gregtrue"] and persistent.endings_got["unknowntrue"]:
            if persistent.ach_ultrobo == False:
                ach_name = "ultrobo"
                showpopup = True
                achievement.grant("ach_ultrobo")
                persistent.ach_ultrobo = True
        
        if sum(persistent.endings_got.values()) == ending_count:
            if persistent.ach_seenitall == False:
                ach_name = "seenitall"
                showpopup = True
                achievement.grant("ach_seenitall")
                persistent.ach_seenitall = True
        
        if all_achievements_unlocked():
            if persistent.ach_lore == False:
                ach_name = "lore"
                showpopup = True
                achievement.grant("ach_lore")
                persistent.ach_lore = True

        achievement.sync()

    if showpopup:
        show screen ach_popup with easeinbottom
        $ renpy.pause(4.0, hard=True)
    $ renpy.movie_cutscene("ENDCREDIT_heath.webm")
    $ MainMenu(confirm=False)()