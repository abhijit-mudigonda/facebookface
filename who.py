import subprocess
import os
import requests
import facebook

def main():

            subprocess.call(["fswebcam", "user_photo.jpg"])
            
            cfg = {
                "page_id" : "100001816035196",
                "access_token" : "EAACEdEose0cBAIkKwamZChvkZA3N5lqr1diRpShim1Np8wovdig8ZC1v51U5eaZB3rOZAqAlbfpj5Ci46bqV7cftDHO3ZAr7mjAvZCMOEGZAn510JfZCN4EmbxO5npau1rTyQBlZB5m9DmiBsS5QrNVqgD6I0LTdz0DRSJCCt1bZAZCTVFZBYptWejiUH9Hi7PxznAtQZD"
                }

            api = get_api(cfg)
            status = api.put_photo(image=open('user_photo.jpg','rb'))
            friends = api.get_all_connections(id='me', connection_name='friends')

            print list(friends)

def get_api(cfg):
    graph = facebook.GraphAPI(cfg['access_token'])
    return graph

if __name__ == "__main__":
    main()
            
            #set up user ID thing based on the stackexchange
            
            #submit a facebook post request to privately post 
            #the photo
            
            #somehow access the "suggested tags" from facebook and 
            #do things - maybe play around with all the information
            #you can extract from a photo? 

            

