# tests/test_game.py

import pytest
from unittest.mock import patch
from io import StringIO
from escape_school.__main__ import SchoolRoom, Courtyard, WallClimb


@pytest.fixture
def isolated_io():
    """隔离 I/O：屏蔽 print、模拟 input、阻止 exit"""
    with patch("builtins.input") as mock_input, \
         patch("sys.stdout", new_callable=StringIO), \
         patch("sys.exit") as mock_exit:
        yield mock_input, mock_exit


# 场景跳转测试数据：(场景类, 用户输入, 期望下一场景)
SCENE_TRANSITIONS = [
    (SchoolRoom, "假装肚子疼", "courtyard"),
    (SchoolRoom, "翻窗", "library_detention"),
    (SchoolRoom, "发呆", "detention"),
    (Courtyard, "挖花盆", "temple_fair"),
    (Courtyard, "翻墙", "wall_climb"),
    (Courtyard, "散步", "courtyard"),
    (WallClimb, "向左", "temple_fair"),
    (WallClimb, "向右", "gate"),
    (WallClimb, "上天", "wall_climb"),
]


@pytest.mark.parametrize("scene_class, user_input, expected", SCENE_TRANSITIONS)
def test_scene_navigation(isolated_io, scene_class, user_input, expected):
    mock_input, mock_exit = isolated_io
    mock_input.return_value = user_input

    # 执行场景逻辑
    scene = scene_class()
    result = scene.enter()

    # 验证：未触发 exit（即非失败路径）
    assert not mock_exit.called, f"{scene_class.__name__} 意外调用了 sys.exit()"

    # 验证：跳转结果正确
    assert result == expected