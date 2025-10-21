#!/usr/bin/env python3
"""Script de test pour vérifier la détection du focus Firefox"""
from AppKit import NSWorkspace
import time

print("Test de détection du focus Firefox")
print("Cliquez sur différentes applications pour voir ce qui est détecté")
print("Appuyez sur Ctrl+C pour arrêter\n")

last_app = None
try:
    while True:
        workspace = NSWorkspace.sharedWorkspace()
        active_app = workspace.frontmostApplication()
        app_name = active_app.localizedName()

        if app_name != last_app:
            is_firefox = 'firefox' in app_name.lower()
            status = "✅ FIREFOX DÉTECTÉ" if is_firefox else "❌ Autre app"
            print(f"{status}: {app_name}")
            last_app = app_name

        time.sleep(0.3)

except KeyboardInterrupt:
    print("\nTest arrêté")
