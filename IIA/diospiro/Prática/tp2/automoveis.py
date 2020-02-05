#
# Introducao a Inteligencia Artificial
# DETI / UA
#
# (c) Diogo Gomes, Luís Seabra Lopes, 2014
# 2014/11/04
#


from tpi2 import *

z = MySN()
z.insert(Declaration('bosch',Depends('illumination','battery')))
z.insert(Declaration('bosch',Subtype('turn signal','illumination')))
z.insert(Declaration('bosch',Subtype('driving lights','illumination')))
z.insert(Declaration('bosch',Subtype('fog lights','illumination')))
z.insert(Declaration('bosch',Depends('starter','battery')))
z.insert(Declaration('bosch',Depends('spark plug','battery')))
z.insert(Declaration('bosch',Depends('fuel pump',  'battery')))
z.insert(Declaration('bosch',Association('ignition','starts','starter')))
z.insert(Declaration('bosch',Association('ignition','starts','spark plug')))
z.insert(Declaration('bosch',Association('ignition','starts','fuel pump')))
z.insert(Declaration('bosch',Depends('engine','spark plug')))

z.insert(Declaration('delfi',Association('dashboard','starts', 'illumination')))

z.insert(Declaration('bmw', Depends('combustion engine',  'starter')))
z.insert(Declaration('bmw', Depends('combustion engine',  'fuel pump')))
z.insert(Declaration('mercedes', Depends('diesel engine',  'fuel pump')))

z.insert(Declaration('karl benz', Subtype('starter', 'engine')))
z.insert(Declaration('karl benz', Subtype('combustion engine', 'engine')))
z.insert(Declaration('karl benz', Subtype('diesel engine', 'engine')))

z.insert(Declaration('shell', Subtype('gasoline', 'petrol')))
z.insert(Declaration('bp', Subtype('gasoline', 'petrol')))
z.insert(Declaration('bp', Subtype('diesel fuel', 'petrol')))
z.insert(Declaration('bp', Subtype('lubricant', 'petrol')))
z.insert(Declaration('bp', Subtype('petrol', 'energy')))
z.insert(Declaration('bp', Subtype('battery', 'energy')))
z.insert(Declaration('bp', Subtype('hidrogen', 'energy')))
z.insert(Declaration('castrol', Subtype('lubricant', 'petrol')))

z.insert(Declaration('renault', Depends('gearbox',  'lubricant')))
z.insert(Declaration('renault', Depends('clutch',  'lubricant')))

z.insert(Declaration('hamilton', Depends('driving',  'combustion engine')))
z.insert(Declaration('lamy', Depends('driving',  'diesel engine')))
z.insert(Declaration('hamilton', Depends('driving',  'gearbox')))
z.insert(Declaration('hamilton', Depends('driving',  'clutch')))
z.insert(Declaration('hamilton', Depends('driving',  'steering')))
z.insert(Declaration('hamilton', Depends('driving',  'wheels')))

z.insert(Declaration('peugeot', Association('wheels', 'connect', 'transmission')))
z.insert(Declaration('peugeot', Association('wheels', 'connect', 'steering')))
z.insert(Declaration('peugeot', Association('transmission', 'connect', 'clutch')))
z.insert(Declaration('peugeot', Association('clutch', 'connect', 'gearbox')))
z.insert(Declaration('peugeot', Association('gearbox', 'connect', 'engine')))

z.insert(Declaration('ferrari', Association('throttle', 'connect', 'fuel pump')))

z.insert(Declaration('fiat', Association('dashboard', 'connect', 'illumination')))
z.insert(Declaration('fiat', Association('dashboard', 'connect', 'ignition')))
z.insert(Declaration('fiat', Association('dashboard', 'connect', 'steering')))
z.insert(Declaration('fiat', Association('dashboard', 'connect', 'gearbox')))

z.insert(Declaration('bmw', Association('fuel pump', 'debug_time', 60)))
z.insert(Declaration('bmw', Association('battery', 'debug_time', 10)))
z.insert(Declaration('bmw', Association('clutch', 'debug_time', 180)))
z.insert(Declaration('bmw', Association('transmission', 'debug_time', 30)))
z.insert(Declaration('bmw', Association('combustion engine', 'debug_time', 240)))
z.insert(Declaration('bmw', Association('diesel engine', 'debug_time', 240)))
z.insert(Declaration('bmw', Association('spark plug', 'debug_time', 60)))
z.insert(Declaration('bmw', Association('lubricant', 'debug_time', 10)))
z.insert(Declaration('bmw', Association('wheels', 'debug_time', 1)))
z.insert(Declaration('bmw', Association('gearbox', 'debug_time', 180)))

z.insert(Declaration('seat', Association('clutch', 'debug_time', 200)))
z.insert(Declaration('seat', Association('transmission', 'debug_time', 50)))
z.insert(Declaration('seat', Association('combustion engine', 'debug_time', 250)))
z.insert(Declaration('seat', Association('diesel engine', 'debug_time', 300)))
z.insert(Declaration('seat', Association('spark plug', 'debug_time', 50)))
z.insert(Declaration('seat', Association('lubricant', 'debug_time', 10)))
z.insert(Declaration('seat', Association('wheels', 'debug_time', 1)))
z.insert(Declaration('seat', Association('gearbox', 'debug_time', 200)))
z.insert(Declaration('seat', Association('steering', 'debug_time', 50)))
z.insert(Declaration('seat', Association('starter', 'debug_time', 50)))

z.insert(Declaration('honda', Association('spark plug', 'debug_time', 300)))
z.insert(Declaration('honda', Association('lubricant', 'debug_time', 30)))
z.insert(Declaration('honda', Association('wheels', 'debug_time', 1)))
z.insert(Declaration('honda', Association('gearbox', 'debug_time', 230)))
z.insert(Declaration('honda', Association('steering', 'debug_time', 80)))
z.insert(Declaration('honda', Association('starter', 'debug_time', 80)))


print(z.query_dependents('battery'))
print(z.query_causes('driving'))
print(z.query_causes_sorted('driving'))