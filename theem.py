#!/bin/bash

# Function to change the color scheme
change_colors() {
  echo "Select a color scheme:"
  echo "1) Dracula"
  echo "2) Solarized Dark"
  echo "3) Solarized Light"
  echo "4) Monokai"
  echo "5) Default"
  read -p "Enter your choice (1-5): " color_choice

  case $color_choice in
    1)
      echo "Applying Dracula theme..."
      termux-change-settings colorscheme="dracula"
      ;;
    2)
      echo "Applying Solarized Dark theme..."
      termux-change-settings colorscheme="solarized_dark"
      ;;
    3)
      echo "Applying Solarized Light theme..."
      termux-change-settings colorscheme="solarized_light"
      ;;
    4)
      echo "Applying Monokai theme..."
      termux-change-settings colorscheme="monokai"
      ;;
    5)
      echo "Applying Default theme..."
      termux-change-settings colorscheme="default"
      ;;
    *)
      echo "Invalid choice. Exiting."
      exit 1
      ;;
  esac
}

# Function to change the font
change_font() {
  echo "Select a font:"
  echo "1) Ubuntu Mono"
  echo "2) Fira Code"
  echo "3) DejaVu Sans Mono"
  echo "4) Default"
  read -p "Enter your choice (1-4): " font_choice

  case $font_choice in
    1)
      echo "Applying Ubuntu Mono font..."
      termux-change-settings font="UbuntuMono"
      ;;
    2)
      echo "Applying Fira Code font..."
      termux-change-settings font="FiraCode"
      ;;
    3)
      echo "Applying DejaVu Sans Mono font..."
      termux-change-settings font="DejaVuSansMono"
      ;;
    4)
      echo "Reverting to default font..."
      termux-change-settings font="default"
      ;;
    *)
      echo "Invalid choice. Exiting."
      exit 1
      ;;
  esac
}

# Main menu
echo "Termux Theme Change Script"
echo "1) Change Colors"
echo "2) Change Font"
echo "3) Change Both"
read -p "Enter your choice (1-3): " main_choice

case $main_choice in
  1)
    change_colors
    ;;
  2)
    change_font
    ;;
  3)
    change_colors
    change_font
    ;;
  *)
    echo "Invalid choice. Exiting."
    exit 1
    ;;
esac

echo "Theme changes applied successfully!"
