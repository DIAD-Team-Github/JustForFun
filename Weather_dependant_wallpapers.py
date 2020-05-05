from bs4 import BeautifulSoup
import ctypes
import requests
import random
import glob
import os

canberra_BOM_obs = r"http://www.bom.gov.au/act/forecasts/canberra.shtml"
img_folder = r"LOCATIO OF YOUR BACKGROUDN IMAGES"


def get_forecast():
    page = requests.get(canberra_BOM_obs)

    soup = BeautifulSoup(page.content, 'html.parser')

    forecast = soup.findAll("dd", {"class": "summary"})[0].contents[0].lower()
    forecast_min = float(soup.findAll("em", {"class": "min"})[0].contents[0])
    forecast_max = float(soup.findAll("em", {"class": "max"})[0].contents[0])
       
    return forecast, forecast_min, forecast_max

	
def changeBackground(img):
    
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE   = 3
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img,0)

def set_background():

    forecast, forecast_min, forecast_max = get_forecast()

    if 'rain' in forecast:
        img = os.path.join(img_folder,r'RAIN.jpg')
    
    elif 'fog' in forecast:
        img = os.path.join(img_folder,r'FOG.jpg')
	
    elif 'storm' in forecast:
        img = os.path.join(img_folder,r'STORM.jpg')
     
    elif forecast_min <= 2:
        img = os.path.join(img_folder,r'SNOW.jpg')
        
    else:
        img = random.sample(glob.glob(os.path.join(img_folder,"GENERIC*.jpg")), 1)[0]
        
    
    
    changeBackground(img)
    
    
if __name__ == '__main__':

    set_background()
    