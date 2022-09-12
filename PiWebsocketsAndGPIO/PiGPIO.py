import RPi.GPIO as GPIO

class InsAndOuts:

    @staticmethod
    def setupOutputs():
        # Setup GPIO using BCM numbering
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        # Define IO
        # Set output
        for x in range(2, 26):
            try:
                GPIO.setup(x, GPIO.OUT)
            except:
                pass

    @staticmethod
    def resetOutput(output):
        GPIO.output(output, GPIO.LOW)

    @staticmethod
    def setOutput(output):
        GPIO.output(output, GPIO.HIGH)
