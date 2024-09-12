#Yes, by default Django signals run in the same database transaction as the caller. This means that if a signal receiver performs any database operations, they are part of the same transaction as the sender, and they will be rolled back if the transaction fails.
#To conclusively prove this, we can:
# 1. Create a Django model and save an object inside the sender.
# 2. In the signal receiver, we will perform another database operation (e.g., updating a field).
# 3. We will simulate a transaction failure in the sender and check if the database changes from the signal receiver are rolled back as well.

from django.db import models, transaction
from django.dispatch import Signal, receiver
import django.db.utils

# Define a Django model
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    updated = models.BooleanField(default=False)

# Define a custom signal
my_signal = Signal()

# Define a receiver function that updates the database
@receiver(my_signal)
def my_signal_receiver(sender, instance, **kwargs):
    print("Receiver started")
    # Update the 'updated' field of the instance
    instance.updated = True
    instance.save()
    print("Receiver finished")

# Code to trigger the signal and simulate a transaction failure
def send_signal_and_fail():
    try:
        with transaction.atomic():
            print("Creating an object")
            instance = MyModel.objects.create(name="Test Object")
            
            # Send the signal
            my_signal.send(sender=None, instance=instance)
            
            # Simulate a transaction failure (e.g., raise an exception)
            print("Simulating transaction failure")
            raise Exception("Transaction failed")
    except Exception as e:
        print(f"Transaction rolled back: {e}")

# Run the test
if __name__ == "__main__":
    send_signal_and_fail()

    # Check if the database has any changes after the transaction failure
    obj = MyModel.objects.filter(name="Test Object").first()
    if obj:
        print(f"Object found in DB: updated={obj.updated}")
    else:
        print("No object found in DB, transaction was rolled back")
