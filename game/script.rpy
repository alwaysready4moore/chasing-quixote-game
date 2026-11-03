# Chasing Quixote — non-canonical mechanical test scene.
# Open this file in a Ren'Py SDK-created project, alongside cq_notebook.rpy.
# All dialogue and event details below are placeholders, not story canon.

define fox = Character("Fox", color="#bbd5cd")
define sunny = Character("Sunny", color="#ebc9a2")

default cq_evidence = []
default cq_seen_topics = []
default cq_reconstruction_complete = False

init python:
    def cq_record_observation(identifier):
        if identifier not in store.cq_evidence:
            store.cq_evidence.append(identifier)

label start:
    scene black
    "CHASING QUIXOTE — Mechanical Prototype"
    "Temporary dialogue and objects. This is a spoiler-free test, not an adaptation of a manuscript scene."
    fox "I've been aboard for fifteen minutes. I'm already looking for somewhere quiet."
    sunny "There's a schedule in your cabin."
    fox "One of us sounds optimistic."
    jump cq_demo_hub

label cq_demo_hub:
    menu:
        "Inspect the event schedule":
            if "schedule" not in cq_evidence:
                $ cq_record_observation("schedule")
                "The event schedule has been revised. Two activities share a time slot."
                fox "This is a remarkably expensive way to teach people about calendars."
            else:
                "Fox has already copied the schedule into his notebook."
            jump cq_demo_hub

        "Check the noticeboard":
            if "noticeboard" not in cq_evidence:
                $ cq_record_observation("noticeboard")
                "A printed notice says the event room changed this morning."
                fox "Fine. At least somebody wrote it down."
            else:
                "The notice has not changed."
            jump cq_demo_hub

        "Ask Sunny about the changes":
            if "sunny" not in cq_seen_topics:
                $ cq_seen_topics.append("sunny")
            sunny "We moved the afternoon session. The signs are being updated."
            fox "Should I follow the signs or the schedule?"
            sunny "Whichever looks newer."
            "Sunny returns to her work."
            jump cq_demo_hub

        "Open Fox's notebook":
            call screen cq_notebook
            jump cq_demo_hub

        "Compare the records":
            if "schedule" in cq_evidence and "noticeboard" in cq_evidence:
                jump cq_demo_reconstruct
            else:
                "Fox needs two independent observations before comparing them."
                jump cq_demo_hub

        "End prototype":
            return

label cq_demo_reconstruct:
    "Fox reviews the schedule and the noticeboard side by side."
    menu:
        "What would he check?"
        "Ask whether the room change explains the schedule conflict":
            $ cq_reconstruction_complete = True
            fox "I'm not investigating the schedule. I just want to know which room to walk into."
            "Reconstruction complete. A new conversation could now become available in the full game."
        "Assume the printed schedule must be correct":
            fox "That's a tempting theory for a man who has never encountered a printer."
            "The observations remain available. Nothing has been lost."
    jump cq_demo_hub
