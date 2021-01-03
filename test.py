#analyse d'une image
from scipy import misc
face= misc.face(gray=True)
#plt.imshow(face,cmap='gray')
#0 noir et 255 et le blanc
plt.hist(face.ravel(), bins=255)
#print()
