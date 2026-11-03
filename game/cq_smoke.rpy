# Smoke tests for the non-canonical mechanical prototype.
# These drive the existing script. They do not add story.
#
# From the Ren'Py SDK directory:
#   ./renpy.sh <project> test cq_prototype

testsuite cq_prototype:
    before testcase:
        $ _test.transition_timeout = 0.05
        $ renpy.unlink_save("1-1")
        $ renpy.unlink_save("quick-1")
        if not screen "main_menu":
            keysym "game_menu"
            click "Main Menu"
            click "Yes"
        assert screen "main_menu" timeout 5.0

    teardown:
        exit

    testcase clues_blocked_until_both_exist:
        click "Start"
        advance until screen "choice"
        click "Compare the records"
        advance until "two independent observations"
        advance until screen "choice"
        assert eval ("schedule" not in cq_evidence and "noticeboard" not in cq_evidence)
        click "Open Fox's notebook"
        assert screen "cq_notebook" timeout 2.0
        assert id "notebook_empty" timeout 2.0
        assert id "notebook_theory_empty" timeout 2.0
        click "Close notebook"
        assert not screen "cq_notebook"
        click "Ask Sunny about the changes"
        advance until screen "choice"
        assert eval ("sunny" in cq_seen_topics and not cq_evidence)
        click "End prototype"
        assert screen "main_menu" timeout 5.0

    testcase schedule_then_notice_save_rollback:
        click "Start"
        advance until screen "choice"
        click "Inspect the event schedule"
        advance until screen "choice"
        $ assert list(cq_evidence) == ["schedule"], list(cq_evidence)
        click "Back" until eval (not cq_evidence)
        $ assert list(cq_evidence) == [], list(cq_evidence)
        advance until screen "choice"
        click "Inspect the event schedule"
        advance until screen "choice"
        $ assert list(cq_evidence) == ["schedule"], list(cq_evidence)
        click "Check the noticeboard"
        advance until screen "choice"
        $ assert list(cq_evidence) == ["schedule", "noticeboard"], list(cq_evidence)
        click "Back" until eval ("noticeboard" not in cq_evidence)
        $ assert list(cq_evidence) == ["schedule"], list(cq_evidence)
        advance until screen "choice"
        click "Check the noticeboard"
        advance until screen "choice"
        $ assert list(cq_evidence) == ["schedule", "noticeboard"], list(cq_evidence)
        click "Open Fox's notebook"
        assert screen "cq_notebook" timeout 2.0
        assert id "notebook_schedule" timeout 2.0
        assert id "notebook_noticeboard" timeout 2.0
        assert id "notebook_theory_empty" timeout 2.0
        keysym "K_ESCAPE"
        assert not screen "cq_notebook"
        click "Save"
        click "Save slot 1"
        click "Return"
        click "Compare the records"
        advance until screen "choice"
        click "Ask whether the room change"
        advance until screen "choice"
        assert eval (cq_reconstruction_complete)
        run QuickSave()
        click "Back" until eval (not cq_reconstruction_complete)
        $ assert (not cq_reconstruction_complete) and list(cq_evidence) == ["schedule", "noticeboard"], (cq_reconstruction_complete, list(cq_evidence))
        run QuickLoad()
        click "Yes"
        $ assert cq_reconstruction_complete and list(cq_evidence) == ["schedule", "noticeboard"], (cq_reconstruction_complete, list(cq_evidence))
        keysym "game_menu"
        click "Load"
        click "Load slot 1"
        click "Yes"
        $ assert (not cq_reconstruction_complete) and list(cq_evidence) == ["schedule", "noticeboard"], (cq_reconstruction_complete, list(cq_evidence))
        click "End prototype"
        assert screen "main_menu" timeout 5.0

    testcase notice_then_schedule_alternate:
        click "Start"
        advance until screen "choice"
        click "Check the noticeboard"
        advance until screen "choice"
        click "Inspect the event schedule"
        advance until screen "choice"
        $ assert list(cq_evidence) == ["noticeboard", "schedule"], list(cq_evidence)
        click "Compare the records"
        advance until screen "choice"
        click "Assume the printed schedule"
        advance until screen "choice"
        assert eval (not cq_reconstruction_complete)
        click "Open Fox's notebook"
        assert screen "cq_notebook" timeout 2.0
        assert id "notebook_schedule" timeout 2.0
        assert id "notebook_noticeboard" timeout 2.0
        assert id "notebook_theory_empty" timeout 2.0
        click "Close notebook"
        click "End prototype"
        assert screen "main_menu" timeout 5.0
