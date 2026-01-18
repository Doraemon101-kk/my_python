school_room_words = ('肚子', '疼', '不舒服', '生病', '拉肚子', '痛')
library_detention_words = ('窗', '翻', '爬')

def route_action(current_scene: str, user_input: str) -> str | None:
    user_input = user_input.strip()

    if current_scene == "school_room":
        if any(word in user_input for word in library_detention_words):
            return "library_detention"
        elif any(word in user_input for word in school_room_words):
            return "courtyard"
        
        else:
            return None

    elif current_scene == "courtyard":
        if "挖" in user_input or "花盆" in user_input:
            return "temple_fair"
        elif "翻" in user_input or "墙" in user_input:
            return "wall_climb"
        else:
            return None

    elif current_scene == "wall_climb":
        if "右" in user_input or "东" in user_input:
            return "gate"
        elif "左" in user_input or "西" in user_input:
            return "temple_fair"
        else:
            return None
        
    return None