label END_cctrue:
    window auto
    scene black
    with fade
    $ renpy.pause(2.0, hard=True)
    $ daynum = "64"
    $ dayday = "On the road..."

    if renpy.is_skipping() == False:
        show screen truedaytransition
        $ renpy.pause(2.0, hard=True)

    scene black with fade
    play music deathtoaperture
    n "You check the rear-view mirror, making sure your \"cargo\" is still secure."
    n "It is."
    n "He's sleeping peacefully."
    n "Under the sound of classical music playing through the radio, you can hear the gentle {i}woosh{/i} of water in the back canister."
    n "The passenger seat holds three extra gallons - just in case."
    n "But something tells you you aren't going to need them."
    n "You turn the car - gently - into the parking lot, pull into a space, and park."
    n "Unbuckling your seatbelt, you go to slide open the van door."
    mc "Hey, sleepyhead. We're here."
    cc "Mmm. Good morning."
    mc "Afternoon, honey, but yes."
    cc "I'm sorry. I fell asleep again."
    mc "That's perfectly okay. You'll need your rest for this, anyway."
    mc "Let's get you out of here, alright?"
    cc "Okay."
    n "You pull the ramp out of the side of the van and place it down carefully."
    n "Managing his wheelchair isn't easy, but it's something you've learned how to handle."
    n "You duck into the back of the van and unbuckle the straps holding his chair in place."
    n "Carefully rolling him out of the vehicle, you check all of his tubes are still inserted properly."
    mc "Everything feel okay? Anything loose at all?"
    cc "No. I'm alright. Thank you."
    n "You shut everything behind you, lock the van, and move forward."

    scene bond entrance with fade
    show c close offrail with easeinright
    n "You push CC up to the entrance to the trail."
    mc "Alright, CC. You can open your optics now."
    show c offrail
    cc "Bond... Falls... Trailhead?"
    cc "We're... we're going to go see a..."
    mc "A waterfall, yes. At the end of this trail."
    show c happy offrail
    cc "Oh. Oh my. I didn't think..."
    show c close offrail
    n "He coughs harshly."
    show c offrail
    cc "I never thought I'd get to see one."
    mc "That's a little silly, CC."
    cc "Well..."
    show c annoy offrail
    cc "...you know how my systems have been acting lately."
    cc "The late night water changes..."
    cc "The pipe repairs..."
    show c close offrail
    cc "I thought..."
    mc "I've been planning this since we left Aperture, CC."
    show c offrail
    mc "I'm... sorry it's taken me so long to get us here."
    mc "It took me a while to find off-road wheels that would fit your chair."
    cc "I didn't even know you changed them."
    show c close offrail
    cc "Regardless. I... thank you."
    show c offrail
    cc "I'm quite excited."

    scene bond trail with fade
    n "Birds are chirping. The sky is clear. The trail is empty."
    n "CC's wheels roll across the dirt path quietly."
    show c close offrail with easeinright
    cc "Love..."
    mc "Yes?"
    show c offrail
    cc "Today's a beautiful day, isn't it?"
    mc "Yes. It is."
    cc "Everyday is beautiful with you."
    mc "I could say the same about you, CC."
    show c close offrail
    n "The two of you proceed along the trail in silence for a while."
    mc "Did you ever... want a different name?"
    show c offrail
    cc "What do you mean?"
    mc "Well... \"CC\" is just an acronym for your alias, isn't it?"
    mc "Not your actual name."
    show c annoy offrail
    cc "Well, yes, but..."
    show c close offrail
    cc "...I don't know. I guess I never thought of it."
    show c annoy offrail
    cc "The researchers who came in to check on me, to refit my tubes, to... worsen what already hurt me..."
    cc "They always just called me \"Cancer Core.\""
    cc "Miss Esther was the first to call me CC."
    show c offrail
    cc "And you."
    cc "You've never called me Cancer Core."
    cc "I..."
    show c close offrail
    n "CC coughs, then sighs."
    cc "I'm sorry. I feel so weak."
    mc "We're almost there."
    show c happy offrail
    cc "I don't think I'd want to be called anything other than yours."
    mc "CC..."
    show c close offrail
    cc "I love you."
    menu:
        extend ""
        "You're such a poet.":
            pass
        "I love you too.":
            show c offrail
            cc "I'm so happy. I..."
            show c happy offrail
            cc "It's so beautiful outside."
            cc "Everything is so much better out here than down there."
            cc "And the world is so full of..."
            cc "Things I'd never imagined."

    scene black with fade
    n "Eventually, the two of you round the trail and hear -"
    n "- just around the corner -"
    n "- the first sounds of falling water."
    cc "Is... is that...?"
    mc "That's the sound a waterfall makes."
    cc "Oh."
    cc "I..."
    cc "It sounds incredible."
    cc "It's nothing like the water inside me. I..."
    mc "Just wait until you see it, CC."

    scene black with fade
    $ renpy.pause(2.0, hard=True)

    scene bond falls with fade
    n "Through the trees, you see it -"
    n "Bond Falls."
    n "100 feet wide, 50 feet tall, cascading down several layers of rock -"
    n "Water flows through every crevice, every pebbled surface, every tiny little crack..."
    n "Emptying out into the Ontonagon River."
    mc "Here it is, CC."
    mc "Bond Falls."
    show c happy offrail with easeinright
    cc "My first... my first real waterfall."
    cc "It's even more incredible in real life."
    cc "It's... haha... it's huge!"
    cc "It's so loud, so powerful, it..."
    show c close offrail
    n "CC closes his optic and coughs. You hear the mechanics inside him whirl."
    mc "CC, are you -"
    show c offrail
    cc "It's so beautiful. I..."
    cc "This has been my dream ever since I discovered what a waterfall was."
    show c close offrail
    cc "When I heard the researchers talking to each other..."
    cc "One of them said he was going with his partner to see Niagra Falls."
    cc "I-I just had to know more, so I scoured the few databases I had access to, I..."
    show c happy offrail
    cc "I ran those images, that text over and over again through my head."
    cc "I-I never thought..."
    cc "I would actually {i}see{/i} one. I..."
    show c offrail
    cc "I..."
    show c annoy offrail
    cc "Love..."
    mc "CC..."
    cc "Do you feel it?"
    mc "Feel..."
    cc "My time. It's..."
    n "The gears inside him whir gently, slowly, harmonizing with the waterfall before you."
    show c close offrail
    cc "This is difficult to ask, but..."
    cc "Can you..."
    show c offrail
    cc "Can you free me from these tubes?"
    cc "Take me off this chair?"
    mc "CC, that'll kill you."
    show c annoy offrail
    cc "Haha, yes. Yes it will, but..."
    cc "I feel it. Internally. My kill code."
    cc "A failsafe Aperture put into place..."
    show c close offrail
    cc "...so the experiment could eventually be put to an end."
    cc "They've gotten no new data..."
    cc "So they've sent the code."
    mc "I-Isn't there something I can do? I could break back into the facility, try to..."
    show c offrail
    cc "No. Love, I..."
    show c close offrail
    cc "I'm in heaven right now."
    cc "The love of my life beside me..."
    cc "A place I've always dreamed of..."
    cc "A sky as blue as the walls I used to spend every waking moment staring at."
    show c happy offrail
    cc "I'm so happy."
    cc "And... it's time."
    mc "I..."
    mc "I understand."
    show c close offrail
    cc "Please help me."
    mc "I will."

    scene black with fade
    n "One by one, you detach the tubes that hold CC in place on his chair."
    n "You hear the pistons slow and the gentle hum of his mechanics quiet down."
    n "Carefully, lovingly, you pick him up off his chair and lay him in the water."
    show screen cuttextbox
    scene cc cutscene 6 with fade
    $ cutscenetextbox = True
    python:
        if persistent.cc6 == False:
            persistent.cutscenes_seen += 1
            persistent.cc6 = True
        achievement.progress("ach_picture", persistent.cutscenes_seen)
        achievement.sync()
    cc "{color=#fff}It feels so... cold."
    cc "{color=#fff}It's wonderful. I..."
    cc "{color=#fff}I haven't felt the air through my circuits since I was activated."
    cc "{color=#fff}The first water-powered core... that's what they said when I was turned on, you know?"
    cc "{color=#fff}Haha. If only I knew that I'd pass surrounded by the very thing that kept me living..."
    cc "{color=#fff}But it's different."
    cc "{color=#fff}The tubes... they're suffocating."
    cc "{color=#fff}Constant pressure on my chassis."
    cc "{color=#fff}But now... I feel so free. Like I could fly."
    n "{color=#fff}He sighs."
    cc "{color=#fff}I love you."
    cc "{color=#fff}None of this would've been possible without you."
    cc "{color=#fff}I would've died in that terrible room."
    cc "{color=#fff}I never would've seen the sky."
    cc "{color=#fff}I never would've{fast} felt the grass."
    cc "{color=#fff}..."
    cc "{color=#fff}I'm sorry."
    cc "{color=#fff}I wish I could stay."
    mc "{color=#fff}Please don't apologize."
    cc "{color=#fff}Haha... alright."
    cc "{color=#fff}I just have one last request, love."
    cc "{color=#fff}Leave me here... when I pass, yes?"
    cc "{color=#fff}In the river."
    cc "{color=#fff}I feel like I belong here."
    mc "{color=#fff}Of course."
    n "{color=#fff}CC looks up one last time."
    cc "{color=#fff}I'm so lucky."
    cc "{color=#fff}You always look so beautiful when you're worried, love."
    n "{color=#fff}Gently, and almost as if he was never there at all..."
    scene black with fade
    n "{color=#fff}CC is gone."
    n "{color=#fff}You kiss him one last time, pick him up, and carry him to the center of the river."
    n "{color=#fff}And with one careful release..."
    n "{color=#fff}He disappears from your vision, caught beneath the waves."
    stop music fadeout 2.0
    window auto
    show screen creditsfadeout with fade
    $ renpy.pause(2.0, hard=True)
    hide screen creditsfadeout
    python:
        if persistent.endings_got["cctrue"] == False:
            persistent.endings_count += 1
            persistent.endings_got["cctrue"] = True
        achievement.progress("ach_seenitall", persistent.endings_count)
        achievement.sync()
        achievement.grant("ach_cctrue")
        achievement.sync()
    $ renpy.movie_cutscene("ENDCREDIT_ccunknown.webm")
    $ MainMenu(confirm=False)()