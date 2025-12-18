#!/usr/bin/env python3
"""
ASCII UI Designer Helper Script
Generates common ASCII UI patterns and templates for web development mockups.
"""

import argparse
from typing import Optional

def create_navigation_bar(logo: str = "Logo", items: list[str] = None, width: int = 80) -> str:
    """Generate a navigation bar ASCII template."""
    if items is None:
        items = ["Home", "About", "Services", "Contact"]
    
    items_str = "  ".join(items)
    total_width = width
    logo_width = len(logo) + 4
    search_width = 8
    content_width = total_width - logo_width - search_width - 4
    
    nav_content = f" {logo}    {items_str[:content_width-5]} 🔍 Search "
    
    return f"""
┌{'─' * (total_width - 2)}┐
│{nav_content.ljust(total_width - 2)}│
└{'─' * (total_width - 2)}┘
""".strip()

def create_card_grid(title: str = "Card Title", num_cards: int = 3, card_width: int = 20) -> str:
    """Generate a card grid ASCII template."""
    border = f"┌{'─' * (card_width - 2)}┐"
    empty_line = f"│{' ' * (card_width - 2)}│"
    bottom = f"└{'─' * (card_width - 2)}┘"
    
    title_line = f"│ {title.ljust(card_width - 4)} │"
    divider_line = f"│{' '.join(['─' * (card_width - 4)])}│"
    content = f"│ Content{' ' * (card_width - 10)}│"
    action = f"│ [Action]{' ' * (card_width - 10)}│"
    
    card = f"{border}\n{title_line}\n{divider_line}\n{content}\n{action}\n{bottom}"
    
    cards = "  ".join([card for _ in range(num_cards)])
    
    return cards

def create_form(fields: list[str] = None, width: int = 40) -> str:
    """Generate a form ASCII template."""
    if fields is None:
        fields = ["Name", "Email", "Message"]
    
    lines = [f"┌{'─' * (width - 2)}┐"]
    lines.append(f"│ Form{' ' * (width - 7)}│")
    lines.append(f"├{'─' * (width - 2)}┤")
    
    for field in fields:
        lines.append(f"│ {field.ljust(width - 4)} │")
        lines.append(f"│ {'[' + '_' * (width - 6) + ']'}{' ' * (width - len(field) - 4)}│")
        lines.append(f"│{' ' * (width - 2)}│")
    
    lines.append(f"│ [Submit] [Cancel]{' ' * (width - 22)}│")
    lines.append(f"└{'─' * (width - 2)}┘")
    
    return "\n".join(lines)

def create_sidebar_layout(logo: str = "Logo", nav_items: list[str] = None, width: int = 80) -> str:
    """Generate a sidebar layout ASCII template."""
    if nav_items is None:
        nav_items = ["Dashboard", "Users", "Settings", "Logout"]
    
    sidebar_width = 20
    content_width = width - sidebar_width - 2
    
    lines = [f"┌{'─' * (sidebar_width - 1)}┬{'─' * (content_width - 1)}┐"]
    
    # Header row
    logo_str = f"│ {logo.ljust(sidebar_width - 3)} │ Main Content"[:width]
    lines.append(f"{logo_str}{' ' * (width - len(logo_str))}│")
    
    # Divider
    lines.append(f"├{'─' * (sidebar_width - 1)}┼{'─' * (content_width - 1)}┤")
    
    # Nav items and content rows
    for i in range(6):
        if i < len(nav_items):
            nav_item = f"│ ► {nav_items[i].ljust(sidebar_width - 6)}"
        else:
            nav_item = f"│{' ' * (sidebar_width - 1)}"
        
        content_line = f" │{' ' * (content_width - 1)}│"
        lines.append(f"{nav_item}{content_line}")
    
    lines.append(f"└{'─' * (sidebar_width - 1)}┴{'─' * (content_width - 1)}┘")
    
    return "\n".join(lines)

def create_modal(title: str = "Modal Title", content: str = "Are you sure?", width: int = 50) -> str:
    """Generate a modal dialog ASCII template."""
    lines = [f"┌{'─' * (width - 2)}┐"]
    lines.append(f"│ {title.ljust(width - 5)} [×] │")
    lines.append(f"├{'─' * (width - 2)}┤")
    
    # Split content into lines if it's long
    content_lines = content.split('\n')
    for line in content_lines:
        formatted_line = line.ljust(width - 4)
        lines.append(f"│ {formatted_line} │")
    
    lines.append(f"├{'─' * (width - 2)}┤")
    lines.append(f"│ [Cancel]{' ' * (width - 22)} [OK] │")
    lines.append(f"└{'─' * (width - 2)}┘")
    
    return "\n".join(lines)

def create_table(headers: list[str], rows: list[list[str]], widths: Optional[list[int]] = None) -> str:
    """Generate a data table ASCII template."""
    if widths is None:
        widths = [len(h) + 2 for h in headers]
    
    lines = []
    
    # Top border
    border_parts = [f"┌{'─' * (w - 1)}" for w in widths]
    lines.append("".join(border_parts) + "┐")
    
    # Header row
    header_parts = [f"│ {h.ljust(w - 3)} " for h, w in zip(headers, widths)]
    lines.append("".join(header_parts) + "│")
    
    # Header divider
    divider_parts = [f"├{'─' * (w - 1)}" for w in widths]
    lines.append("".join(divider_parts) + "┤")
    
    # Data rows
    for row in rows:
        row_parts = [f"│ {str(cell).ljust(w - 3)} " for cell, w in zip(row, widths)]
        lines.append("".join(row_parts) + "│")
    
    # Bottom border
    border_parts = [f"└{'─' * (w - 1)}" for w in widths]
    lines.append("".join(border_parts) + "┘")
    
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(
        description="ASCII UI Designer - Generate ASCII art UI templates for web development"
    )
    parser.add_argument(
        "template",
        choices=["navbar", "cards", "form", "sidebar", "modal", "table"],
        help="Template type to generate"
    )
    parser.add_argument("--title", default="", help="Title or heading text")
    parser.add_argument("--width", type=int, default=80, help="Width of the ASCII art")
    parser.add_argument("--items", nargs="+", help="Items for navigation or form fields")
    parser.add_argument("--count", type=int, default=3, help="Number of items (e.g., cards)")
    
    args = parser.parse_args()
    
    if args.template == "navbar":
        print(create_navigation_bar(
            logo=args.title or "Logo",
            items=args.items or ["Home", "About", "Services"],
            width=args.width
        ))
    elif args.template == "cards":
        print(create_card_grid(
            title=args.title or "Card Title",
            num_cards=args.count,
            card_width=args.width // args.count
        ))
    elif args.template == "form":
        print(create_form(
            fields=args.items or ["Name", "Email", "Message"],
            width=args.width
        ))
    elif args.template == "sidebar":
        print(create_sidebar_layout(
            logo=args.title or "Logo",
            nav_items=args.items or ["Dashboard", "Users", "Settings"],
            width=args.width
        ))
    elif args.template == "modal":
        print(create_modal(
            title=args.title or "Confirm Action",
            content="Are you sure you want to continue?",
            width=args.width
        ))
    elif args.template == "table":
        headers = args.items or ["Name", "Email", "Status"]
        rows = [
            ["John Doe", "john@example.com", "Active"],
            ["Jane Smith", "jane@example.com", "Inactive"],
        ]
        widths = [len(h) + 4 for h in headers]
        print(create_table(headers, rows, widths))

if __name__ == "__main__":
    main()
