#!/usr/bin/env python3
from Quartz import CGEventCreateKeyboardEvent, CGEventPostToPid, CGEventCreateScrollWheelEvent
from AppKit import NSWorkspace
import subprocess
import time
import random
import argparse

def get_browser_pid(browser_name):
    # Map browser names to their process names
    browser_processes = {
        'firefox': 'firefox',
        'safari': 'Safari',
        'chrome': 'Google Chrome'
    }
    process_name = browser_processes.get(browser_name.lower(), browser_name)
    result = subprocess.run(['pgrep', '-xi', process_name], capture_output=True, text=True)
    pids = result.stdout.strip().split('\n')
    return int(pids[0]) if pids[0] else None

def is_browser_focused(browser_name):
    """Vérifie si le navigateur spécifié est l'application au premier plan"""
    try:
        workspace = NSWorkspace.sharedWorkspace()
        active_app = workspace.frontmostApplication()
        app_name = active_app.localizedName()
        # Debug: décommentez la ligne suivante pour voir quelle app est détectée
        # print(f"[DEBUG] App active: {app_name}")
        # Map browser names to their app names
        browser_app_names = {
            'firefox': 'firefox',
            'safari': 'safari',
            'chrome': 'chrome'
        }
        target_browser = browser_app_names.get(browser_name.lower(), browser_name.lower())
        return app_name and target_browser in app_name.lower()
    except:
        return False

def wait_if_browser_focused(browser_name, pause_delay):
    """Attend tant que le navigateur a le focus, puis attend encore pause_delay secondes"""
    if not is_browser_focused(browser_name):
        return False

    print(f"⏸️  PAUSE - {browser_name.capitalize()} a le focus (interaction utilisateur détectée)")

    # Attendre que le navigateur perde le focus
    while is_browser_focused(browser_name):
        time.sleep(CHECK_FOCUS_INTERVAL)

    print(f"⏳ Attente de {pause_delay}s après perte de focus...")
    time.sleep(pause_delay)
    print("▶️  REPRISE de la séquence")
    return True

def smart_sleep(browser_name, duration):
    """Sleep intelligent qui vérifie le focus du navigateur et met en pause si nécessaire"""
    start_time = time.time()
    while time.time() - start_time < duration:
        # Vérifier si le navigateur a le focus
        if is_browser_focused(browser_name):
            wait_if_browser_focused(browser_name, PAUSE_DELAY_AFTER_FOCUS_LOST)
            # Réinitialiser le timer après la pause
            start_time = time.time()

        remaining = duration - (time.time() - start_time)
        if remaining > 0:
            time.sleep(min(CHECK_FOCUS_INTERVAL, remaining))

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

# Configuration pause automatique
PAUSE_DELAY_AFTER_FOCUS_LOST = 10  # Secondes à attendre après perte de focus avant de reprendre
CHECK_FOCUS_INTERVAL = 0.5  # Fréquence de vérification du focus (secondes)

# Arguments
parser = argparse.ArgumentParser(description='Contrôle automatique de navigateur avec séquences de navigation')
parser.add_argument('-b', '--browser', type=str, default='firefox',
                    choices=['firefox', 'safari', 'chrome'],
                    help='Navigateur à contrôler (défaut: firefox)')
parser.add_argument('-n', '--sequences', type=int, default=None,
                    help='Nombre de séquences à exécuter (défaut: infini)')
args = parser.parse_args()

# Exécution
pid = get_browser_pid(args.browser)
if not pid:
    print(f"{args.browser.capitalize()} non trouvé")
    exit(1)

print(f"{args.browser.capitalize()} trouvé (PID: {pid})")
if args.sequences:
    print(f"Démarrage de {args.sequences} séquence(s). Appuyez sur Ctrl+C pour arrêter.")
else:
    print("Séquence démarrée en mode infini. Appuyez sur Ctrl+C pour arrêter.")
print(f"La séquence se mettra en pause automatiquement si vous interagissez avec {args.browser.capitalize()}")
print(f"et reprendra {PAUSE_DELAY_AFTER_FOCUS_LOST}s après la fin de l'interaction.\n")

try:
    sequence_count = 0
    while args.sequences is None or sequence_count < args.sequences:
        # Vérifier avant de commencer
        wait_if_browser_focused(args.browser, PAUSE_DELAY_AFTER_FOCUS_LOST)

        # Attendre random 1-5 secondes
        delay1 = random.uniform(1, 5)
        print(f"Attente {delay1:.1f}s...")
        smart_sleep(args.browser, delay1)

        # Page Down
        wait_if_browser_focused(args.browser, PAUSE_DELAY_AFTER_FOCUS_LOST)
        send_key(pid, PAGE_DOWN)
        print("📄 PAGE_DOWN")

        # Attendre random 1-3 secondes
        delay2 = random.uniform(1, 3)
        print(f"  Attente {delay2:.1f}s...")
        smart_sleep(args.browser, delay2)

        # Page Down 2 fois
        for i in range(2):
            wait_if_browser_focused(args.browser, PAUSE_DELAY_AFTER_FOCUS_LOST)
            send_key(pid, PAGE_DOWN)
            print("  📄 PAGE_DOWN")

        # Attendre random 1-5 secondes
        delay3 = random.uniform(1, 5)
        print(f"  Attente {delay3:.1f}s...")
        smart_sleep(args.browser, delay3)

        # Page Down 2 fois
        for i in range(2):
            wait_if_browser_focused(args.browser, PAUSE_DELAY_AFTER_FOCUS_LOST)
            send_key(pid, PAGE_DOWN)
            print("  📄 PAGE_DOWN")

        # Attendre random 1-5 secondes
        delay4 = random.uniform(1, 5)
        print(f"  Attente {delay4:.1f}s...")
        smart_sleep(args.browser, delay4)

        # Flèche droite
        wait_if_browser_focused(args.browser, PAUSE_DELAY_AFTER_FOCUS_LOST)
        send_key(pid, RIGHT)
        print("→ RIGHT")

        sequence_count += 1
        if args.sequences:
            print(f"--- Séquence {sequence_count}/{args.sequences} terminée ---\n")
        else:
            print(f"--- Séquence {sequence_count} terminée ---\n")

    if args.sequences:
        print(f"\n✅ Toutes les séquences terminées ! ({sequence_count} séquence(s) exécutée(s))")

except KeyboardInterrupt:
    print("\nSéquence arrêtée.")
    if sequence_count > 0:
        print(f"{sequence_count} séquence(s) exécutée(s).")
