import pywhatkit as pwk
import datetime
from geopy.geocoders import Nominatim
import geocoder  # New import to get current location

def sendInfoWA(mobilenumber, name):
    # Get current location using IP
    g = geocoder.ip('me')
    lat, longi = g.latlng

    print("Detected Latitude:", lat)
    print("Detected Longitude:", longi)

    # Create Google Maps URL
    urlstr = f"https://www.google.com/maps/dir/{lat},{longi}"
    message = (
        "ALERT ALERT ALERT !!!\n"
        f"Dear {name},\n"
        "A Weed is detected on the Camera in your field at the following location:\n"
        f"{urlstr}\n"
        "Also attached is the Surveillance Image for your reference.\n"
        "PLEASE TAKE ACTION IMMEDIATELY!\n"
        "Regards,\n"
        "Automatic Weed Detection System"
    )

    reference_image_path = "temp.jpg"
    mobilenumber = "+91" + mobilenumber

    # Get time and set to one minute later
    now = datetime.datetime.now()
    send_time = now + datetime.timedelta(minutes=1)
    hr = send_time.hour
    min = send_time.minute

    # Send message with image
    pwk.sendwhats_image(mobilenumber, reference_image_path, message, tab_close=True, close_time=3)

# if __name__ == '__main__':
#     sendInfoWA("9876543210", "Test User")
