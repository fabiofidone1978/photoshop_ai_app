#!/usr/bin/env bash

# Rileva il separatore corretto per l'opzione --add-data
sep=";"
case "$(uname)" in
    *Linux*|*Darwin*) sep=":" ;;
esac

pyinstaller --noconfirm --onefile --windowed \
    --name PhotoshopAI \
    --add-data "editor.kv${sep}." \
    --add-data "gui.kv${sep}." \
    --add-data "assets${sep}assets" \
    --add-data "akivymd${sep}akivymd" \
    main.py
