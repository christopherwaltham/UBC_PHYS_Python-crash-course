
# Voltage Transients

In an ideal digital system, the voltage can only have two set values: HIGH or LOW. This is not the case in real life though. Electronics will use some finite amount of time transitioning between the two logic states, and this might introduce problems.

Transient is a word used to describe temporary behavior. Here, we use the word to refer to how the voltage behaves when tracking from one equilibrium position to another.

We can visualize some of these effects using an oscilloscope and the square wave produced by the Arduino using `analogWrite`. The setup is described in module 2.

- Zoom in on one of the rising edges by adjusting the time scale.
![](Images/scope_zoom.png)

This oscillatory behavior is surprising. It is caused, in part, by capacitance in the breadboard and inductance in the leads of the oscilloscope probe. The oscillations are, in other words, exacerbated by us measuring the system.

- Use the cursors to measure the amplitude of the oscillations
![](Images/scope_cursor.png)

- Bring down the menu (by swiping down from the top of the screen).
- Go to the `Trigger` section and trigger on a falling edge.
![](Images/scope_falling_edge.png)
