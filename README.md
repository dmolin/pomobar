# Pomobar

---

Pomodoro timer to polybar
![](img/2018-10-09-224812_124x19_scrot.png)
![](img/2018-10-09-224825_79x19_scrot.png)
![](img/2018-10-09-224837_72x20_scrot.png)

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
