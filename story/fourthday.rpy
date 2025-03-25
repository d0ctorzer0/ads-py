label day4:
    scene mctemproom
    with fade

    n "You put in the code to your room and enter it, dropping your paperwork on the floor."

    if wkd3:
        n "You never expected Kris to act so... sensitively. It seemed almost out-of-character."
    if whd3:
        n "You're glad you spent the day with Heath. She kept you entertained."
    if wad3:
        n "You figure you learned more about botany today than you ever did in your schooling years."
    if wcd3:
        n "CC's conversations can get very deep. It gave you a lot to think about."
    if wrd3:
        n "You're exhausted from your shift today, much more than usual. But it feels good."
    else:
        n "You wonder if maybe you should've done something different today, or asked Miss Esther to come with you despite management's wishes."
    # ^ this line plays regardless of previous variable values. fix later
    n "Regardless, you need your rest for tomorrow's shift. You change out of your work attire and lay down for stasis."

    scene black
    with fade
    $ daynum = "4"
    $ dayday = "Thursday"

    show screen daytransition
    $ renpy.pause(2.0, hard=True)

    scene mctemproom with fade

    n "You wake up at 08:00 as usual, get dressed, and head out the door."

    scene office with pixellate

    n "Miss Esther greets you at the door."

    show e with easeinright
    e "Hello, Doctor!"

    mc "Hello, Miss Esther."

    e "Are you ready for another day? We're back to our regular routine!"

    mc "You're awfully cheery today."

    show e laugh
    e "Oh yes, I suppose I am. It's Thursday, which means we're more than halfway through the week!"
    show e
    e "I'm simply excited for the weekend."

    mc "What do you even do over the weekend, anyway?"

    show e annoy
    e "I have hobbies! I do... things!"
    
    show e
    e "Anyways, we'd better be on our way to Kris. Saturday will come quicker than you expect! Let's go!"
    hide e with easeoutright

    if cc1 == True and picture == True:
        n "You glance at the picture of Multnomah Falls on your desk and remember what CC said yesterday."
        menu:
            extend " You decide to..."

            "Bring it with you.":
                n "You pick up the picture and tuck it in with your paperwork."
            "Leave it behind.":
                n "You leave the picture on the desk. Maybe another day."
    
    n "You follow Miss Esther out of the office and towards the conference room."

    jump krisday4

label krisday4:

    scene kristemproom with pixellate

    n "You enter the conference room to see Kris whizzing across his management rail, back and forth, rapidly."
    n "The screen behind him has a lot more red on it than usual."

    show e with easeinright
    e "Kris, we're here for your..."
    hide e with easeoutright
    
    show k angry with easeinright
    k "No time to talk. I'm trying to find the source."

    mc "The source of what?"

    k "Can't you read? Our stock plummeted overnight. We've had no large experiments lately, no important investments to make..."
    k "It just doesn't make sense!"

    menu:
        extend ""
        "(Reassure him.)":
            $ romance_points["Kris"] += 3
            jump impresskris4
        "(Let him think.)":
            $ romance_points["Kris"] += 1
            k "I've reported it to finanical already, left a note that I believe it may have been a mistake, or something in Testing..."
            k "I've... done everything I have to. I've done my job."
            k "I'm not sure why I'm still panicking."

            show k flirt
            k "Sorry, Doctor. I am... calmer now."
            jump krisday4pt2
        "(Criticize him.)":
            $ romance_points["Kris"] -= 3
            jump offendkris4

label impresskris4:
    if wkd3 or romance_points["Kris"] >= 7:
        mc "Woah, Kris. Take a breath. You're the senior officer in charge of watching the stock, right?"

        show k flirt
        k "Yes. That's why -"

        show k angry
        mc "That's why you'll be fine. This is your whole job. You've got this."
        mc "But first you need to slow down."

        show k
        k "Yes. Yes... you're right, Doctor. I apologize."
        jump krisday4pt2
    
    else:
        mc "That's interesting. Can you solve it?"

        k "It's not my JOB to solve it. My job is to WATCH the stock, nothing more, and report to Finanical when it drops below a certain threshold."
        k "I've already reported it."

        mc "Then you've done all you can, yes?"

        show k flirt
        k "I... suppose I have."

        mc "Then there's no reason to panic."

        show k
        k "Yes. Yes... you're right, Doctor. I apologize."
        jump krisday4pt2

label offendkris4:
    mc "Get a hold of yourself, Kris. This is highly unprofessional."

    show k
    k "Excuse me?"

    mc "You're running all over the place in a panic. This job is not a high-stress one. There is no reason to panic."

    k "Yes, but I've just never seen such -"

    mc "No excuses. Pull yourself together."

    k "Uh... yes, ma'am."

    if wkd3:
        show k angry
        k "Whatever happened to the Doctor I had yesterday?"
    
    jump krisday4pt2

label krisday4pt2:
    mc "I don't think I need to ask if you're doing your job."

    hide k with easeoutright
    show e annoy with easeinright
    e "Yes, he made it clear right away that he was."
    e "And his rambling put us behind schedule, Doctor."

    mc "Oh. Yes. Sorry."

    hide e with easeoutright
    show k with easeinright

    k "I'll... handle this. You should be on your way."

    mc "Thank you, Kris."

    n "You head out the door and towards the break room."