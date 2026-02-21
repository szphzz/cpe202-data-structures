def weight_on_planets():
   earth = float(input('What do you weigh on earth? '))
   mars = earth * 0.38
   jupiter = earth * 2.34
   print('\nOn Mars you would weigh', mars, 'pounds.\nOn Jupiter you would weigh', jupiter, 'pounds.')
   
if __name__ == '__main__':
   weight_on_planets()
