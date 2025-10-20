#!/usr/bin/env python3
from Quartz import CGEventCreateKeyboardEvent, CGEventPostToPid, CGEventCreateScrollWheelEvent
import subprocess
import time
import random

def get_firefox_pid():
    result = subprocess.run(['pgrep', '-x', 'firefox'], capture_output=True, text=True)
    pids = result.stdout.strip().split('\n')
    return int(pids[0]) if pids[0] else None

def send_key(pid, keycode, delay=0.1):
    # Key down
    event_down = CGEventCreateKeyboardEvent(None, keycode, True)
    CGEventPostToPid(pid, event_down)
    time.sleep(0.05)

    # Key up
    event_up = CGEventCreateKeyboardEvent(None, keycode, False)
    CGEventPostToPid(pid, event_up)
    time.sleep(delay)

def send_scroll(pid, amount, delay=0.15):
    # Crée un événement de scroll (amount négatif = scroll vers le bas)
    # kCGScrollEventUnitLine = 0, wheelCount = 1
    scroll_event = CGEventCreateScrollWheelEvent(None, 0, 1, amount)
    CGEventPostToPid(pid, scroll_event)
    time.sleep(delay)

# Keycodes
RIGHT = 124
DOWN = 125
LEFT = 123
UP = 126
ENTER = 36
SPACE = 49
PAGE_DOWN = 121

# Exécution
pid = get_firefox_pid()
if not pid:
    print("Firefox non trouvé")
    exit(1)

print(f"Firefox trouvé (PID: {pid})")
print("Séquence démarrée. Appuyez sur Ctrl+C pour arrêter.")

try:
    while True:
        # Attendre random 1-5 secondes
        delay1 = random.uniform(1, 5)
        print(f"Attente {delay1:.1f}s...")
        time.sleep(delay1)

        # Page Down
        send_key(pid, PAGE_DOWN)
        print("📄 PAGE_DOWN")

        # Attendre random 1-3 secondes
        delay2 = random.uniform(1, 3)
        print(f"  Attente {delay2:.1f}s...")
        time.sleep(delay2)

        # Page Down 2 fois
        for i in range(2):
            send_key(pid, PAGE_DOWN)
            print("  📄 PAGE_DOWN")

        # Attendre random 1-5 secondes
        delay3 = random.uniform(1, 5)
        print(f"  Attente {delay3:.1f}s...")
        time.sleep(delay3)

        # Page Down 2 fois
        for i in range(2):
            send_key(pid, PAGE_DOWN)
            print("  📄 PAGE_DOWN")

        # Attendre random 1-5 secondes
        delay4 = random.uniform(1, 5)
        print(f"  Attente {delay4:.1f}s...")
        time.sleep(delay4)

        # Flèche droite
        send_key(pid, RIGHT)
        print("→ RIGHT")
        print("---")

except KeyboardInterrupt:
    print("\nSéquence arrêtée.")
