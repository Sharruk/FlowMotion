import os
import re
import platform
from django.conf import settings
from django.urls import reverse


def slugify_name(name):
    """Simple slugify to make filenames human readable."""
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '-', name)
    return name.strip('-')


def create_habit_widget_shortcut(habit, request=None):
    """
    Creates a desktop shortcut for a specific habit.
    - Windows: Creates a .url shortcut file
    - Linux: Creates a .desktop shortcut file
    """
    system = platform.system()

    # Dynamic host and port derivation
    if request:
        host = request.get_host()
        scheme = 'http'
        base_url = f"{scheme}://{host}"
    else:
        base_url = "http://127.0.0.1:8000"

    relative_url = reverse('habit_detail', kwargs={'habit_id': habit.id})
    widget_url = f"{base_url}{relative_url}?widget=true"

    try:
        desktop_path = os.path.expanduser("~/Desktop")
        if not os.path.exists(desktop_path):
            os.makedirs(desktop_path)

        slug = slugify_name(habit.name)

        if system == 'Windows':
            return _create_windows_shortcut(desktop_path, slug, habit, widget_url)
        else:
            return _create_linux_shortcut(desktop_path, slug, habit, widget_url)

    except Exception as e:
        return False, str(e)


def _create_windows_shortcut(desktop_path, slug, obj, widget_url):
    """Create a Windows .url shortcut file."""
    file_name = f"FlowMotion-{slug}.url"
    file_path = os.path.join(desktop_path, file_name)

    content = f"""[InternetShortcut]
URL={widget_url}
IconIndex=0
HotKey=0
IDList=
[{{000214A0-0000-0000-C000-000000000046}}]
Prop3=19,11
"""
    with open(file_path, "w") as f:
        f.write(content)

    return True, file_path


def _create_linux_shortcut(desktop_path, slug, obj, widget_url):
    """Create a Linux .desktop shortcut file."""
    file_name = f"{slug}.desktop"
    file_path = os.path.join(desktop_path, file_name)
    
    # Handle both Habit (name) and CountdownWidget (title)
    display_name = getattr(obj, 'name', getattr(obj, 'title', 'Widget'))
    
    # Calculate days left for icon selection
    days_left = 0
    if hasattr(obj, 'created_at') and hasattr(obj, 'duration'):
        from django.utils import timezone
        from datetime import date
        today = date.today()
        start_date = obj.created_at.date()
        days_passed = (today - start_date).days
        days_left = max(0, obj.duration - days_passed)
    elif hasattr(obj, 'target_date'):
        from datetime import date
        today = date.today()
        days_left = (obj.target_date - today).days

    # Choose emoji icon based on days left
    icon_name = "happy.png"
    if days_left > 20:
        icon_name = "happy.png"
    elif days_left > 10:
        icon_name = "neutral.png"
    elif days_left > 5:
        icon_name = "warning.png"
    else:
        icon_name = "fire.png"
    
    # Get absolute path to the icon
    icon_path = os.path.join(settings.BASE_DIR, 'static', 'icons', icon_name)

    content = f"""[Desktop Entry]
Name={display_name}
Comment=Track: {display_name} ({days_left} days left)
Exec=xdg-open "{widget_url}"
Icon={icon_path}
Terminal=false
Type=Application
Categories=Utility;
X-KeepTerminal=false
"""
    with open(file_path, "w") as f:
        f.write(content)

    os.chmod(file_path, 0o755)
    return True, file_path


def check_widget_exists(habit):
    """Checks if a shortcut file for the habit exists on the desktop."""
    desktop_path = os.path.expanduser("~/Desktop")
    slug = slugify_name(habit.name)
    system = platform.system()

    if system == 'Windows':
        file_name = f"FlowMotion-{slug}.url"
    else:
        file_name = f"flowmotion-{slug}.desktop"

    return os.path.exists(os.path.join(desktop_path, file_name))
