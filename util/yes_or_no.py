def yes_or_no(msg: str) -> bool:
    is_yes = input(f"\n{msg} y/n\n입력 :").strip().lower() == "y"
    return is_yes
