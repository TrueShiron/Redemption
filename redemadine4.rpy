label redemadine4:

scene black with dissolvemed

$ renpy.pause (0.5)

scene o at Pan((0, 250), (0, 250), 0.1) with dissolvemed

m "The morning sun declared the arrival of a new day and woke me from my vivid dreams. Memories of my last meeting with Maverick and him carrying me on his back while we were flying raced through my head."

m "Then I had to think about Adine and I knew that I had to make a decision; calling and telling her that she should not fly at the competition or not calling and risking her safety, maybe even her life."

m "I knew that it might cause her to hate me, but I'd rather want her to be safe and hate me, than live with the consequences of her flying and having another accident."

play sound "fx/phonepickup.ogg"

$ renpy.pause(1.0)

m "I entered the number and waited for Adine to pick up the phone."

$ renpy.pause(2.0)

Ad normal b "Hello, this is Adine. Who am I speaking to?"

c "Good morning, Adine. This is [player_name]."

Ad giggle b "Oh, hi [player_name]. Are you calling because of the competition today?"

m "(No turning back now.)"

c "Yes I am but for a different reason as you might think."

Ad think b "I’m not sure I’m following."

c "The thing is; I saw you flying last time and you were still wearing the bandage."

c "I know that you want to take part in the competition today and how much it means to you, but I don’t want you to get hurt again because of you flying with an injured wing."

Ad normal b "I'm fine, really. Don't worry about it."

c "If you're fine without the bandage, how come you were wearing it up to just now? Did you need it for practice, too? If you couldn't practice without it, maybe you aren't ready to compete without it yet."

Ad annoyed b "Since when are you suddenly an expert on flying? I'm the one who has been doing this for years, not you. This is my dream we're talking about."

c "Do you want them to see you in this condition and judge you based on that rather than when you're at your best?"

Ad disappoint b "I.. just have to try, you know?"

c "What if something goes wrong, though? You don't want to be in that position."

Ad "If I start making excuses now, maybe I'll never stop. I'll always be too nervous, or too injured, or didn't eat right the day before. I feel bad enough as it is."

Ad "Right now, I have the chance to do this. And if I don't take it, maybe I never will."

Ad "I'll always just be a server and delivery girl making minimum wage."

Ad "Is this one chance really too much to ask for?"

c "No, but it doesn't have to be right now. There will always be another year."

c "They've never seen you compete before. If you fly this year, they'll judge you based on this performance. You only have one chance at making a first impression, and you know it won't be your best if you fly with an injured wing."

c "If it's not good enough, maybe they won't invite you again next year. If you fly this year, they won't accept any excuses. But if you tell them you're injured, they might let you fly another time."

Ad "But I don't want to wait another year. I want to do it this year. I trained so much, even with this injury, and you tell me I should just let it go?"

c "I just can't help thinking about last time. If you crash like that again, there's no sand there to cushion your fall. It would be much worse."

Ad annoyed b b "You think I don't know that? That I'm not already worrying about this more than I ever have for anything else? I just don't want to make excuses anymore."

Ad disappoint b "I don't want to wonder if I'll ever amount to anything more than a waitress. I want to be able to follow my dream, and I don't want to wait another year to find out."

c "What about Amely? If something happened to you, how do you think they would explain to her that you just suddenly stopped showing up, huh?"

Ad frustrated b "Don't you dare bring her into this! She has nothing to do with it."

c "Like it or not, what you are doing could have consequences, and there are others besides you who will be affected if something goes wrong."

Ad "You know what? I will fly and do the best damn job I've ever done, and there's nothing you can do to stop me."

m "Before I could reply, she angrily hung up on me."

m "While I had failed to convince her, at least I could say that I had tried my hardest to stop her."

m "All I could do now was hoping that she wouldn't have another accident."

$ adinestatus = "abandoned"

jump ml_date_end


