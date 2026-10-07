import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft2, ifft2, fftshift
from skimage.io import imread
from skimage.color import rgb2gray

plt.close('all')

# =============================================================================
# Úkol 1
# Prozkoumejte funkci 'create_harmonic_function'. Jaké jsou její vstupy? Co bude výstupem?
# Zobrazte si vedle sebe libovolnou harmonickou funkci a její amplitudové spektrum
# Měnte vstupní parametry harmonické funkce a pozorujte jejich vliv na výstupní obraz a jeho spektrum.
# =============================================================================

# Prozkoumejte přiloženou funkci 'create_harmonic_function'. Jaké jsou její vstupy? Co bude výstupem?
def create_harmonic_function(sf_u,sf_v,phase,amplitude,img_shape):
    """
    Generates a 2D harmonic function with provided parameters

    :param sf_u: (int, float) spatial frequency in y axis
    :param sf_v: (int, float) spatial frequency in x axis
    :param phase: (int, float) phase
    :param amplitude: (int, float) amplitude
    :param img_shape: (tuple) shape of the image in x and y direction
    :return: (numpy.ndarray) Array of generated 2D harmonic function
    """

    n, m = img_shape
    omega_u = 2 * np.pi * sf_u
    omega_v = 2 * np.pi * sf_v

    [N, M] = np.meshgrid(range(n), range(m))
    harmonic_function = amplitude * np.cos((omega_u * N) / n + (omega_v * M) / m + phase)
    return(harmonic_function)

# Zobrazte si vedle sebe libovolnou harmonickou funkci a její amplitudové spektrum
u = 3
v = 2
phi =0
A = 1
shape = (200,100)
harmonic_function = create_harmonic_function(u, v, phi, A, shape)
spectrum_of_harmonic_function = fft2(harmonic_function)
amplitude_spectrum= fftshift(np.abs(spectrum_of_harmonic_function))

plt.figure()
plt.subplot(1,2,1)
plt.imshow(harmonic_function, cmap = 'gray')
plt.title(f'Harmonicka funkce, u = {u}, v = {v}, phi = {phi}, A = {A}')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.yticks(ticks=np.linspace(start = shape[1], stop = 0, num = 5), labels=np.linspace(0, shape[1], 5).astype(int))

plt.subplot(1,2,2)
plt.imshow(amplitude_spectrum, cmap = 'gray')
plt.title(f'Amplitudove spektrum harmonicke funkce')
plt.xlabel('Prostorova frekvence [1/m]')
plt.ylabel('Prostorova frekvence [1/m]')
plt.xticks(ticks=np.linspace(start = 0, stop = shape[0]-1, num = shape[0]//5), labels=np.linspace(-shape[0]/2, shape[0]/2, shape[0]//5).astype(int))
plt.yticks(ticks=np.linspace(start = shape[1]-1, stop = 0, num = shape[1]//5), labels=np.linspace(-shape[1]/2, shape[1]/2, shape[1]//5).astype(int))
plt.plot([0,shape[0]], [shape[1]/2,shape[1]/2], color = 'green')
plt.plot([shape[0]/2,shape[0]/2], [0,shape[1]], color = 'green')
plt.show()

# Měnte vstupní parametry harmonické funkce a pozorujte jejich vliv na výstupní obraz a jeho spektrum.
plt.close('all')
us = [1, 3, 5]
vs = [0, 2, 4]
phi = 0
A = 1
shape = (200,100)


# =============================================================================
# Úkol 2
# Prozkoumejte přiloženou funkci 'generate_rectangle'. Jaké jsou její vstupy? Co bude výstupem?
# Zobrazte si vedle sebe obraz vystupující z funkce s libovolným nastavením parametrů a jeho amplitudové spektrum
# Měnte vstupní parametry A a B funkce a pozorujte jejich vliv na výstupní obraz a jeho spektrum.
# =============================================================================
plt.close('all')

# Prozkoumejte přiloženou funkci 'generate_rectangle'. Jaké jsou její vstupy? Co bude výstupem?

def generate_rectangle(M,N,A,B):
    """
    Generation of the image of zeros with the rectangle of ones in the middle

    :param M: (int) size of the x axis of the image
    :param N: (int) size of the y axis of the image
    :param A: (int) lenght of the x side of the rectangle
    :param B: (int) lenght of the x side of the rectangle
    :return: (numpy.ndarray) image of zeros with the rectangle of ones in the middle
    """

    rectangle_image=np.zeros([M,N])
    center_of_image=[int(np.floor(M/2)),int(np.floor(N/2))]
    vel_obd=[int(np.floor(A/2)),int(np.floor(B/2))]
    if (A !=1 and B !=1):
        rectangle_image[center_of_image[0]-vel_obd[0]:center_of_image[0]+vel_obd[0],center_of_image[1]-vel_obd[1]:center_of_image[1]+vel_obd[1]]=1
    elif (A==1 and B==1):
        rectangle_image[center_of_image[0],center_of_image[1]]=1
    elif(A==1):
        rectangle_image[center_of_image[0],center_of_image[1]-vel_obd[1]:center_of_image[1]+vel_obd[1]]=1
    else:
        rectangle_image[center_of_image[0]-vel_obd[0]:center_of_image[0]+vel_obd[0],center_of_image[1]]=1
    return(rectangle_image)

# Zobrazte si vedle sebe obraz vystupující z funkce s libovolným nastavením parametrů a jeho amplitudové spektrum
x = 100
y = 200
a = 20
b = 20

img = generate_rectangle(x, y, a, b)
ampl_spectrum = fftshift(np.abs(fft2(img)))
shape = np.shape(img)

plt.figure()
plt.subplot(1,2,1)
plt.imshow(img, cmap = 'gray')
plt.title('Generovany obraz')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')

plt.subplot(1,2,2)
plt.imshow(ampl_spectrum, cmap = 'gray')
plt.title('Amplitudove spektrum')
plt.xlabel('Prostorova frekvence [1/m]')
plt.ylabel('Prostorova frekvence [1/m]')
plt.xticks(ticks=np.linspace(start = 0, stop = shape[1], num = shape[1]//2), labels=np.linspace(-shape[1]/2, shape[1]/2, shape[1]//2).astype(int))
plt.yticks(ticks=np.linspace(start = shape[0], stop = 0, num = shape[0]//2), labels=np.linspace(-shape[0]/2, shape[0]/2, shape[0]//2).astype(int))
plt.show()

# # Měnte vstupní parametry A a B funkce a pozorujte jejich vliv na výstupní obraz a jeho spektrum.
a_s = 10
b_s = 10

plt.figure()


# =============================================================================
# Úkol 3
# Načtěte nultý kanál podvzorkovaného obrazu 'kometa_brno_podvzorkovana.png‘
# Zobrazte tento obraz spolu s jeho amplitudovým spektrem
# Ověřte teorii, že každý obraz je tvořený z 2D harmonických složek.
# =============================================================================
plt.close('all')

# Načtěte nultý kanál podvzorkovaného obrazu loga komety 'kometa_brno_podvzorkovana.png'
img = imread('data/kometa_brno_podvzorkovana.png')[:, :,0]
spectrum = fft2(img)

# Zobrazte tento obraz spolu s jeho amplitudovým a fázovým spektrem
shape = np.shape(img)

plt.figure()
plt.subplot(1,3,1)
plt.imshow(img, cmap = 'gray')
plt.title('Puvodni obraz')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')

plt.subplot(1,3,2)
plt.imshow(np.log(fftshift(np.abs(fft2(img)))), cmap = 'gray')
plt.title('Amplitudove spektrum')
plt.xlabel('Prostorova frekvence [1/m]')
plt.ylabel('Prostorova frekvence [1/m]')
plt.xticks(ticks=np.linspace(start = 0, stop = shape[1], num = shape[1]//2), labels=np.linspace(-shape[1]/2, shape[1]/2, shape[1]//2).astype(int))
plt.yticks(ticks=np.linspace(start = shape[0], stop = 0, num = shape[0]//2), labels=np.linspace(-shape[0]/2, shape[0]/2, shape[0]//2).astype(int))

plt.subplot(1,3,3)
plt.imshow(fftshift(np.angle(fft2(img))), cmap = 'gray')
plt.title('Fazove spektrum')
plt.xlabel('Prostorova frekvence [1/m]')
plt.ylabel('Prostorova frekvence [1/m]')
plt.xticks(ticks=np.linspace(start = 0, stop = shape[1], num = shape[1]//2), labels=np.linspace(-shape[1]/2, shape[1]/2, shape[1]//2).astype(int))
plt.yticks(ticks=np.linspace(start = shape[0], stop = 0, num = shape[0]//2), labels=np.linspace(-shape[0]/2, shape[0]/2, shape[0]//2).astype(int))
plt.show()

# Ověřte si teorii, že každý obraz je stvořený z řady 2D harmonických složek.
ampl_spektrum = fftshift(np.abs(spectrum))
fazove_spektrum = fftshift(np.angle(spectrum))
final_image = np.zeros_like(img)

...

plt.figure()
plt.subplot(1,2,1)
plt.imshow(img, cmap = 'gray')
plt.title('Puvodni obraz')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')

plt.subplot(1,2,2)
plt.imshow(np.flipud(final_image), cmap = 'gray')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.title('Obraz poskladany pomoci skladani harmonickych slozek')
plt.show()


# =============================================================================
# Úkol 4
# Načtěte obrazy 'obr1.jpg' a 'obr2.jpg', převeďte na šedotonové a zobrazte.
# Vypočtěte jejich spektra a do jednoho figure zobrazte amplitudovou a fázovou část spektra.
# Prohoďte amplitudová a fázová spektra obou obrazů a zobrazte obrazy po prohození v originální oblasti.
# =============================================================================
plt.close('all')
# Načtěte dvojici obrazů 'obr1.jpg' a 'obr2.jpg', převeďte na šedotonové a zobrazte.

img_1=rgb2gray(imread('data/obr1.jpg'))  #kometa
img_2=rgb2gray(imread('data/obr2.jpg'))  #sparta

plt.figure()
plt.subplot(1,2,1)
plt.imshow(img_1, cmap = 'gray')
plt.title('Kometa')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')

plt.subplot(1,2,2)
plt.imshow(img_2, cmap = 'gray')
plt.title('Sparta')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.show()

# Vypočtěte jejich spektra a do jednoho figure zobrazte amplitudovou a fázovou část spektra.
IMG_1 = fft2(img_1)
IMG_2 = fft2(img_2)

amplitude_kometa=np.abs(IMG_1)
phase_kometa=np.angle(IMG_1)
amplitude_sparta=np.abs(IMG_2)
phase_sparta=np.angle(IMG_2)

shape = np.shape(amplitude_kometa)

plt.figure()
plt.subplot(221)
plt.imshow(fftshift(np.log(amplitude_kometa)),cmap='gray')
plt.title('Amplitudove kometa')
plt.xlabel('Prostorova frekvence [1/m]')
plt.ylabel('Prostorova frekvence [1/m]')
plt.xticks(ticks=np.linspace(start = 0, stop = shape[1], num = 20), labels=np.linspace(-shape[1]/2, shape[1]/2, 20).astype(int))
plt.yticks(ticks=np.linspace(start = shape[0], stop = 0, num = 20), labels=np.linspace(-shape[0]/2, shape[0]/2, 20).astype(int))

plt.subplot(223)
plt.imshow(fftshift(phase_kometa),cmap='gray')
plt.title('Fazove kometa')
plt.xlabel('Prostorova frekvence [1/m]')
plt.ylabel('Prostorova frekvence [1/m]')
plt.xticks(ticks=np.linspace(start = 0, stop = shape[1], num = 20), labels=np.linspace(-shape[1]/2, shape[1]/2, 20).astype(int))
plt.yticks(ticks=np.linspace(start = shape[0], stop = 0, num = 20), labels=np.linspace(-shape[0]/2, shape[0]/2, 20).astype(int))

shape = np.shape(amplitude_sparta)

plt.subplot(222)
plt.imshow(fftshift(np.log(amplitude_sparta)),cmap='gray')
plt.title('Amplitudove sparta')
plt.xlabel('Prostorova frekvence [1/m]')
plt.ylabel('Prostorova frekvence [1/m]')
plt.xticks(ticks=np.linspace(start = 0, stop = shape[1], num = 20), labels=np.linspace(-shape[1]/2, shape[1]/2, 20).astype(int))
plt.yticks(ticks=np.linspace(start = shape[0], stop = 0, num = 20), labels=np.linspace(-shape[0]/2, shape[0]/2, 20).astype(int))

plt.subplot(224)
plt.imshow(fftshift(phase_sparta),cmap='gray')
plt.title('Fazove sparta')
plt.xlabel('Prostorova frekvence [1/m]')
plt.ylabel('Prostorova frekvence [1/m]')
plt.xticks(ticks=np.linspace(start = 0, stop = shape[1], num = 20), labels=np.linspace(-shape[1]/2, shape[1]/2, 20).astype(int))
plt.yticks(ticks=np.linspace(start = shape[0], stop = 0, num = 20), labels=np.linspace(-shape[0]/2, shape[0]/2, 20).astype(int))
plt.show()

# Prohoďte amplitudová a fázová spektra obou obrazů a zobrazte obrazy po prohození v originální oblasti.
IMG1_changed=amplitude_kometa * np.exp(1j * phase_sparta)
IMG2_changed=amplitude_sparta * np.exp(1j * phase_kometa)

img1_mixed=np.real(ifft2(IMG1_changed))
img2_mixed=np.real(ifft2(IMG2_changed))

plt.figure()
plt.subplot(121)
plt.imshow(img1_mixed,cmap='gray')
plt.title('Amplitudove kometa, fazove sparta')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')

plt.subplot(122)
plt.imshow(img2_mixed,cmap='gray')
plt.title('Amplitudove sparta, fazove kometa')
plt.xlabel('Prostorova souradnice [m]')
plt.ylabel('Prostorova souradnice [m]')
plt.show()
