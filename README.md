# Pomobar

---

Pomodoro timer to polybar
![](img/pomobar.gif)

## Requeriments 

* Polybar
* Icons: FontAwesome

## Getting Started

Only need copy pomobar.py in your system and call it in polybar

## Polybar config:
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
