class Radio(object):
    
    def __init__(self):
        self.on = False
        self.channel = 1
        self.volume = 1


    def turnOn(self):
        self.on = True


    def turnOff(self):
        if not self.on:
            print('Radio is already off!!')
        else:
            self.on = False
            self.channel = 1
            self.volume = 1


    def setVolume(self, volume):
        if not self.on:
            print('Radio is off!!')
        elif volume > 0 and volume < 5:
            self.volume = volume
        else:
            print('Volume must be in Range[0, 5]')


    def volumeUp(self):
        self.setVolume(self.volume + 1)


    def volumeDown(self):
        self.setVolume(self.volume - 1)


    def setChannel(self, channel):
        if not self.on:
            print('Radio is off!!')
        elif channel > 1 and channel < 10:
            self.channel = channel
        else:
            print('Channel must be in Range[1, 10]')
      

    def channelUp(self):
       self.setChannel(self.channel + 1)


    def channelDown(self):
        self.setChannel(self.channel - 1)


    def getSettings(self):
        return 'Settings: On ' + str(self.on) + ', Channel ' + str(self.channel) + ', Volume ' + str(self.volume)


r1 = Radio()
print(r1.getSettings())
r1.turnOn()
r1.setVolume(3)
r1.channelUp()
r1.channelUp()
r1.channelUp()

print(r1.getSettings())

r1.turnOff();
print(r1.getSettings())