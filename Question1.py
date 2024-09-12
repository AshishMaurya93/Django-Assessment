# By default, Django signals are executed synchronously. This means that when a signal is sent, the receiver function(s) are executed immediately and in the same thread as the sender.

# Here’s a simple example to demonstrate this behavior:
# 1. Create a signal and connect a receiver.
# 2. The receiver will log a message when the signal is received.
# 3. The execution time of the sender and receiver will be measured to demonstrate that they occur in sequence (synchronously).

import time
import django.dispatch

# Define a signal
my_signal = django.dispatch.Signal()

# Define a receiver function for the signal
def my_signal_receiver(sender, **kwargs):
    print("Receiver started.")
    # Simulate a time-consuming task
    time.sleep(2)
    print("Receiver finished.")

# Connect the receiver to the signal
my_signal.connect(my_signal_receiver)

# Code to send the signal
def send_signal():
    print("Signal sent.")
    my_signal.send(sender=None)
    print("Signal finished sending.")

# Measure the time taken for both sending the signal and receiving it
if __name__ == "__main__":
    start_time = time.time()
    send_signal()
    end_time = time.time()
    print(f"Total execution time: {end_time - start_time:.2f} seconds")
