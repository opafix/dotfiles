# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) {upstream_browser_key}/{upstream_browser_version} Safari/{webkit_version}', 'https://web.whatsapp.com/')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://accounts.google.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99 Safari/537.36', 'https://*.slack.com/*')

# User agent to send.  The following placeholders are defined:  *
# `{os_info}`: Something like "X11; Linux x86_64". * `{webkit_version}`:
# The underlying WebKit version (set to a fixed value   with
# QtWebEngine). * `{qt_key}`: "Qt" for QtWebKit, "QtWebEngine" for
# QtWebEngine. * `{qt_version}`: The underlying Qt version. *
# `{upstream_browser_key}`: "Version" for QtWebKit, "Chrome" for
# QtWebEngine. * `{upstream_browser_version}`: The corresponding
# Safari/Chrome version. * `{qutebrowser_version}`: The currently
# running qutebrowser version.  The default value is equal to the
# unchanged user agent of QtWebKit/QtWebEngine.  Note that the value
# read from JavaScript is always the global value.
# Type: FormatString
config.set('content.headers.user_agent', 'Mozilla/5.0 ({os_info}; rv:71.0) Gecko/20100101 Firefox/71.0', 'https://docs.google.com/*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'chrome-devtools://*')

# Load images automatically in web pages.
# Type: Bool
config.set('content.images', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome-devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'devtools://*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'chrome://*/*')

# Enable JavaScript.
# Type: Bool
config.set('content.javascript.enabled', True, 'qute://*/*')

"""
BEGIN CUSTOM CONFIGS
"""

import subprocess

def read_xresources(prefix):
    props = {}
    x = subprocess.run(['xrdb', '-query'], stdout=subprocess.PIPE)
    lines = x.stdout.decode().split('\n')
    for line in filter(lambda l : l.startswith(prefix), lines):
        prop, _, value = line.partition(':\t')
        props[prop] = value
    return props

xresources = read_xresources('*')
d_black = xresources['*color0']
l_black = xresources['*color8']
d_red = xresources['*color1']
l_red = xresources['*color9']
d_green = xresources['*color2']
l_green = xresources['*color10']
d_yellow = xresources['*color3']
l_yellow = xresources['*color11']
d_blue = xresources['*color4']
l_blue = xresources['*color12']
d_magenta = xresources['*color5']
l_magenta = xresources['*color13']
d_cyan = xresources['*color6']
l_cyan = xresources['*color14']
d_white = xresources['*color7']
l_white = xresources['*color15']

c.colors.completion.category.bg = d_black
c.colors.completion.category.border.bottom = d_black
c.colors.completion.category.border.top = d_black
c.colors.completion.category.fg = l_white
c.colors.completion.even.bg = d_black
c.colors.completion.fg = l_white
c.colors.completion.item.selected.bg = d_blue
c.colors.completion.item.selected.border.bottom = d_black
c.colors.completion.item.selected.border.top = d_black
c.colors.completion.item.selected.fg = l_white
c.colors.completion.item.selected.match.fg = d_green
c.colors.completion.match.fg = l_green
c.colors.completion.odd.bg = l_black
c.colors.completion.scrollbar.bg = d_black
c.colors.completion.scrollbar.fg = l_black

c.colors.contextmenu.menu.bg = d_black
c.colors.contextmenu.menu.fg = l_black
c.colors.contextmenu.selected.bg = d_blue
c.colors.contextmenu.selected.fg = l_white

c.colors.downloads.bar.bg = d_black
c.colors.downloads.error.bg = d_black
c.colors.downloads.error.fg = d_red
c.colors.downloads.start.bg = d_black
c.colors.downloads.start.fg = l_green
c.colors.downloads.stop.bg = d_black
c.colors.downloads.stop.fg = d_yellow

c.colors.hints.bg = d_black
c.colors.hints.fg = l_white

c.colors.keyhint.bg = d_black
c.colors.keyhint.fg = l_green
c.colors.keyhint.suffix.fg = l_white

c.colors.messages.error.bg = d_black
c.colors.messages.error.border = d_red
c.colors.messages.error.fg = d_red
c.colors.messages.info.bg = d_black
c.colors.messages.info.border = l_green
c.colors.messages.info.fg = l_green
c.colors.messages.warning.bg = d_black
c.colors.messages.warning.border = l_yellow
c.colors.messages.warning.fg = l_yellow

c.colors.prompts.bg = d_black
c.colors.prompts.border = l_black
c.colors.prompts.fg = l_white
c.colors.prompts.selected.bg = d_blue

c.colors.statusbar.caret.bg = d_black
c.colors.statusbar.caret.fg = l_white
c.colors.statusbar.caret.selection.bg = l_white
c.colors.statusbar.caret.selection.fg = d_black
c.colors.statusbar.command.bg = d_black
c.colors.statusbar.command.fg = l_white
c.colors.statusbar.command.private.bg = d_black
c.colors.statusbar.command.private.fg = l_white
c.colors.statusbar.insert.bg = d_black
c.colors.statusbar.insert.fg = l_white
c.colors.statusbar.normal.bg = d_black
c.colors.statusbar.normal.fg = l_white
c.colors.statusbar.passthrough.bg = d_black
c.colors.statusbar.passthrough.fg = l_white
c.colors.statusbar.private.bg = d_black
c.colors.statusbar.private.fg = l_white
c.colors.statusbar.progress.bg = d_black
c.colors.statusbar.url.fg = l_white
c.colors.statusbar.url.hover.fg = l_cyan
c.colors.statusbar.url.success.http.fg = l_green
c.colors.statusbar.url.success.https.fg = l_green
c.colors.statusbar.url.warn.fg = d_red

c.colors.tabs.bar.bg = d_black
c.colors.tabs.even.bg = d_black
c.colors.tabs.even.fg = l_white
c.colors.tabs.indicator.error = d_red
c.colors.tabs.indicator.start = l_green
c.colors.tabs.indicator.stop = l_yellow
c.colors.tabs.odd.bg = d_black
c.colors.tabs.odd.fg = l_white
c.colors.tabs.pinned.even.bg = d_blue
c.colors.tabs.pinned.even.fg = l_white
c.colors.tabs.pinned.odd.bg = d_blue
c.colors.tabs.pinned.odd.fg = l_white
c.colors.tabs.pinned.selected.even.bg = d_blue
c.colors.tabs.pinned.selected.even.fg = l_white
c.colors.tabs.pinned.selected.odd.bg = d_blue
c.colors.tabs.pinned.selected.odd.fg = l_white
c.colors.tabs.selected.even.bg = d_blue
c.colors.tabs.selected.even.fg = l_white
c.colors.tabs.selected.odd.bg = d_blue
c.colors.tabs.selected.odd.fg = l_white

c.colors.webpage.bg = d_black