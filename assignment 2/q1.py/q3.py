#Convert distant given in feet and inches into meter and centimeter.
feet=float(input("Enter the distance in Feet="))
inches=float(input("Enter the distance in inches="))
meter=(feet*0.3048)+(inches*0.0254)
cm=meter*100
print(f"Distance in meter={meter}.m")
print(f"Distance in centimeter={cm}.cm")