# pomobar
Pomodoro timer to polybar

~~~
.config/polybar/config
[module/pomobar]
type=custom/ipc
hook-0 = cat ~/pomobaroutput
initial=1
click-left = ~/box/src/scripts/pomobar.py start &
click-middle= ~/box/src/scripts/pomobar.py kill &
click-right = ~/box/src/scripts/pomobar.py break &
~~~
