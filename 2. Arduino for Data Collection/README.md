# 2. Arduino for Data Collection

[Arduino](https://www.arduino.cc) is a platform of [microcontrollers](https://en.wikipedia.org/wiki/Microcontroller) that has a large user-base, and that is easy to work with. These microcontrollers are programmed in a language developed for the Arduino boards, which is closely related to the programming language called [C](https://en.wikipedia.org/wiki/C_(programming_language)). Learning two programming languages at once is not easy, so we have already uploaded code on the boards so that you can control it by sending it commands from Python.

To communicate with the microcontroller, you will be using a serialized communication protocol simply known as Serial. It encodes the information you want to send into a sequence of bits (zeros and ones) and sends them one by one through a single wire. Two more wires are also required: ground to give the computers a shared reference, and a clock to communicate when a new bit has been sent.
