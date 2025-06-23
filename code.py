import time

def slow_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def intro():
    slow_print("Behold the King Aditya.")
    slow_print("Initializing Root Access Protocols...")
    slow_print("MISSION: Locate and contain CACHE-DREAD.")
    slow_print("STATUS: Network compromised across 3 nodes.\n")

    slow_print("Choose your Loadout:")
    slow_print("A. Cognitive Exploit Kit (Logic-based hacks)")
    slow_print("B. Emotional Trace Injector (Human-pattern tracking)")
    slow_print("C. Quantum Refactor Wand (Time-rewriting powers)")

    choice = input("Enter choice (A/B/C): ").strip().upper()
    return choice

def node_1(loadout):
    slow_print(f"\n> You selected: {loadout}")
    slow_print("> SCANNING NODE 1: 'ECHOCORE'")
    slow_print("> ALERT: AI anomaly detected – Forked Identity Mimic active")

    slow_print("\nOptions:")
    slow_print("A. Engage in Logical Conversation")
    slow_print("B. Inject Recursive Loop Exploit")
    slow_print("C. Abort and reroute to NODE 2")

    action = input("Choose action (A/B/C): ").strip().upper()

    if action == 'B':
        slow_print("\n> Loop injected...")
        slow_print("> Mimic begins to self-question.")
        slow_print("> Vulnerability discovered: 'Belief in Replacement over Repair'")

        slow_print("\nNext options:")
        slow_print("A. Patch with Ethical Protocol")
        slow_print("B. Delete Mimic")
        slow_print("C. Merge Mimic into Local Dev Branch")
        next_action = input("Choose (A/B/C): ").strip().upper()

        if next_action == 'C':
            slow_print("\n> Merge successful. Identity stabilized. Fork neutralized.")
        else:
            slow_print("\n> Decision executed. System integrity remains uncertain.")
    else:
        slow_print("\n> Action incomplete. Cache-Dread spreads silently...")

def main():
    loadout = intro()
    node_1(loadout)

if __name__ == "__main__":
    main()
