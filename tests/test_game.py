from escape_school.parser import route_action

def test_school_room():
    assert route_action("school_room", "假装肚子疼") == "courtyard"
    assert route_action("school_room", "翻窗") == "library_detention"
    assert route_action("school_room", "发呆") == "detention"

def test_courtyard():
    assert route_action("courtyard", "挖花盆") == "temple_fair"
    assert route_action("courtyard", "翻墙") == "wall_climb"
    assert route_action("courtyard", "散步") == "courtyard"

def test_wall_climb():
    assert route_action("wall_climb", "向左") == "temple_fair"
    assert route_action("wall_climb", "向右") == "gate"
    assert route_action("wall_climb", "向上") == "wall_climb"

def test_school_room_keywords():
    assert route_action('school_room', '肚子疼') == 'courtyard'
    assert route_action('school_room', '我肚子不舒服') == 'courtyard'
    assert route_action('school_room', '想上厕所') == 'courtyard'

def test_detention_keywords():
    assert route_action('school_room', '偷偷溜走') == 'detention'
    assert route_action('school_room', '我想跑') == 'detention'